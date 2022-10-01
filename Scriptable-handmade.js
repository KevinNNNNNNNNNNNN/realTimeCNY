// This program is going to be used in iOS Scriptable app
// It will greb the data in http://kwang-yloft.ddns.net:8581/ server and display it on the widget
// To grab the data, it will look at the tail command of the log file store in ~/priceHistory.txt


let configurationFileName = 'tailConfig.json'
const usePersistedConfiguration = true; // false would mean to use the visible configuration below; true means the state saved in iCloud (or locally) will be used
const overwritePersistedConfig = true; // if you like your configuration, run the script ONCE with this param to true, then it is saved and can be used via 'USE_CONFIG:yourfilename.json' in widget params

const CONFIGURATION_JSON_VERSION = 2; // never change this! If i need to change the structure of configuration class, i will increase this counter. Your created config files sadly won't be compatible afterwards.


// show the background color of the widget as black
let widget = new ListWidget()
widget.backgroundColor = Color.black()


class Configuration{
    CNYServiceMachineBaseUrl = 'http://kwang-yloft.ddns.net:8581'; // location of your system running the hb-service, e.g. http://192.168.2.101:8581
    username = 'kwang';
    password = 'd4vNooYv0JsYY!99R!#&1S*#h$NAx%&O';
    //send a command "tail -f ~/priceHistory.txt"
    command = 'tail -f  ~/priceHistory.txt';
    fileManagerMode = 'ICLOUD'; // default is ICLOUD. If you don't use iCloud Drive use option LOCAL
    fontColor_light = '#FFFFFF'; // _light the default color if adaptToLightOrDarkMode is false
    fontColor_dark = '#FFFFFF';
    backgroundColor = '#000000'; // default is black
    failIcon = '❌';

    

}
