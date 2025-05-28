#!/usr/bin/env python3

import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message."""
    pattern = rf'({"|".join(fields)})=([^{separator}]*)'
    return re.sub(pattern, rf'\1={redaction}', message)


def get_logger() -> logging.Logger:
    """Returns a configured logger for user data with PII filtering."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.handlers = [stream_handler]
    return logger


def get_db() -> MySQLConnection:
    """Connects to the Holberton database using env variables."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main():
    """Retrieve and log user data with PII filtering."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [desc[0] for desc in cursor.description]
    logger = get_logger()
    for row in cursor:
        row_dict = dict(zip(fields, row))
        # Format each field as key=value;
        msg = []
        for k, v in row_dict.items():
            msg.append(f"{k}={v}")
        message = "; ".join(msg) + ";"
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
