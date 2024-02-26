class User {
    
    constructor(userName) {
        this.userName = userName;
    }
    
    getUsername() {
        return this.userName;
    }
    
    setUsername(username) {
        this.userName = username;
    }
}

class ChatUser extends User {
    constructor (userName, initialWarningCount) {
        super(userName);
        this.initialWarningCount = 0;
    }
    
    giveWarning() {
        this.initialWarningCount += 1;
    }
    
    getWarningCount() {
        return this.initialWarningCount;
    }
}
