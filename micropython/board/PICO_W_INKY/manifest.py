include("$(PORT_DIR)/boards/manifest.py")

# https://github.com/micropython/micropython-lib/blob/master/micropython/bundles/bundle-networking/manifest.py
require("bundle-networking")
require("urllib.urequest")
require("umqtt.simple")