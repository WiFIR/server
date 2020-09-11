import flask
import semver

app = flask.Flask('ESP_updater')

headers = (
    "HTTP_USER_AGENT",
    "HTTP_X_ESP8266_STA_MAC",
    "HTTP_X_ESP8266_AP_MAC",
    "HTTP_X_ESP8266_FREE_SPACE",
    "HTTP_X_ESP8266_SKETCH_SIZE",
    "HTTP_X_ESP8266_SKETCH_MD5",
    "HTTP_X_ESP8266_CHIP_SIZE",
    "HTTP_X_ESP8266_SDK_VERSION",
    "HTTP_X_ESP8266_VERSION"
)


class Node:
    user_agent = "ESP8266-http-Update"

    def __init__(self, headers):
        self.sta_mac = headers['HTTP_X_ESP8266_STA_MAC']
        self.ap_mac = headers['HTTP_X_ESP8266_AP_MAC']
        self.free_space = headers['HTTP_X_ESP8266_FREE_SPACE']
        self.sketch_size = headers['HTTP_X_ESP8266_SKETCH_SIZE']
        self.sketch_md5 = headers['HTTP_X_ESP8266_SKETCH_MD5']
        self.chip_size = headers['HTTP_X_ESP8266_CHIP_SIZE']
        self.sdk_version = headers['HTTP_X_ESP8266_SDK_VERSION']
        self.version = headers['HTTP_X_ESP8266_VERSION']


version = "0.2.0"


@app.route('/api/update')
def updater():
    esp = Node(flask.request.headers.environ)

    if 
    return "test"


if __name__ == '__main__':
    app.run()
