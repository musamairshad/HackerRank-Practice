

function dataFinder(data) {
    return function find (minRange, maxRange, value) {
        var newData = [];
        if (minRange < 0 || maxRange < 0 || minRange >= data.length || maxRange >= data.length) {
            throw Error("Invalid range")
        }
        for (var i = minRange; i <= maxRange; i++) {
            newData.push(data[i]);
        }

        if(newData.includes(value)) {
            return true;
        } else {
            return false;
        }
    }
}