function cleanSet(set, startString) {
    if (typeof startString !== 'string' || startString.length === 0) {
        return '';
    }

    let result = '';

    set.forEach(value => {
        if (value.startsWith(startString)) {
            if (result.length > 0) {
                result += '-';
            }
            result += value.slice(startString.length);
        }
    });

    return result;
}