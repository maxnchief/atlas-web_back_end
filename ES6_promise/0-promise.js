function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        const success = true;

        if (success) {
            resolve("API call succeeded");
        } else {
            reject("API call failed");
        }
    });
}