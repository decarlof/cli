import os
import sys
import shutil
from pathlib import Path
from multiprocessing import cpu_count
import threading
import numpy as np
import tomopy
import dxchange

from cli import log

def task(params):
    log.info('task')