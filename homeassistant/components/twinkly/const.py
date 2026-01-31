"""Const for Twinkly."""

DOMAIN = "twinkly"

# Strongly named HA attributes keys
ATTR_HOST = "host"
ATTR_VERSION = "version"

# Keys of attributes read from the get_device_info
DEV_ID = "uuid"
DEV_NAME = "device_name"
DEV_MODEL = "product_code"
DEV_LED_PROFILE = "led_profile"

DEV_PROFILE_RGB = "RGB"
DEV_PROFILE_RGBW = "RGBW"

DEV_PERMANENT_LIGHTS_PRODUCT_CODES = ["TWPL072STP", "TWPL072STW"]

TWINKLY_MAX_KELVIN = 7900
TWINKLY_MIN_KELVIN = 3900

# Minimum version required to support cold white
MIN_COLD_WHITE_VERSION = "2.10.0"
# Minimum version required to support effects
MIN_EFFECT_VERSION = "2.7.1"
