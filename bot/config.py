import json
import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

TELEGRAM = os.getenv('TELEGRAM')
DATABASE_URL = os.getenv('DATABASE_URL')
ADMINS = json.loads(os.getenv('ADMINS'))

NX_MEME = -1001482614635
NX_MAIN = -1001839268196

LOG_GROUP = -1001739784948
ADMIN_GROUP = -1001723195485

UG_LZ = -1001263239083
UG_ADMIN = -802186561

GROUP_SOURCE = -1001694922864

CHANNEL_UA_RU = -1001640548153

MSG_REMOVAL_PERIOD = 1200

ADMIN_GROUPS = {
    -1001845172955: ADMIN_GROUP,  # NN_UA
    -1001888944217: ADMIN_GROUP,  # NN_AFRIKA - still present?
    UG_LZ: UG_ADMIN,  # UKR_GER
    -1001618190222: -1001895565760,  # UA_Krieg
    -1002104916595: ADMIN_GROUP,  # Israel
}

CONTAINER: Final[bool] = bool(os.getenv('CONTAINER', False), )
