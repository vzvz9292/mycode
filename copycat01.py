#!/usr/bin/env python3
# Written By: Abdel Abuyasin (Lab)

import shutil
import os

os.chdir('/TEMP/GitHub/mycode/')

shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

shutil.copytree('5g_research/', '5g_research_backup/')



