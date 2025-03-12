function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {  
        const success = true

        if (success) {
            const data = ("API call succeeded");
            resolve(data);
        } else {
            const data = ("API call failed");
            reject(error);
        }
    });
}