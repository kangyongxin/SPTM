#!/usr/bin/env python
import os
import os.path

import resnet
from register_test_setups import (register_test_setups, DATA_PATH)

def get_from_env(name, type, default):
  value = os.environ.get(name)
  if value:
    if type in [str, int, float]:
      returned_value = type(value)
    elif type == bool:
      returned_value = eval(value)
    else:
      raise Exception('Unknown constant type!')
  else:
    returned_value = default
  print name, '=', returned_value
  return returned_value

# test setups
TEST_SETUPS = register_test_setups()  

# loaded from environment
SMOOTHED_LOCALIZATION = get_from_env('SMOOTHED_LOCALIZATION', bool, True)
MEMORY_SUBSAMPLING = get_from_env('MEMORY_SUBSAMPLING', int, 4)
MIN_SHORTCUT_DISTANCE = get_from_env('MIN_SHORTCUT_DISTANCE', int, 5)
MEMORY_MAX_FRAMES = get_from_env('MEMORY_MAX_FRAMES', int, None)
ACTION_EXPERIMENT_ID = get_from_env('ACTION_EXPERIMENT_ID', str, '0102_L')
EDGE_EXPERIMENT_ID = get_from_env('EDGE_EXPERIMENT_ID', str, '0103_R')
EXPERIMENT_OUTPUT_FOLDER = get_from_env('EXPERIMENT_OUTPUT_FOLDER', str, 'default_experiment')
WEAK_INTERMEDIATE_REACHABLE_GOAL_THRESHOLD = get_from_env('WEAK_INTERMEDIATE_REACHABLE_GOAL_THRESHOLD', float, 0.7)
INTERMEDIATE_REACHABLE_GOAL_THRESHOLD = get_from_env('INTERMEDIATE_REACHABLE_GOAL_THRESHOLD', float, 0.95)
SMALL_SHORTCUTS_NUMBER = get_from_env('SMALL_SHORTCUTS_NUMBER', int, 2000)
SHORTCUT_WINDOW = get_from_env('SHORTCUT_WINDOW', int, 10)
MIN_LOOK_AHEAD = get_from_env('MIN_LOOK_AHEAD', int, 1)
MAX_LOOK_AHEAD = get_from_env('MAX_LOOK_AHEAD', int, 7)
NUMBER_OF_TRIALS = get_from_env('NUMBER_OF_TRIALS', int, 6)
EDGE_ARCHITECTURE = get_from_env('EDGE_ARCHITECTURE', str, 'SIAMESE_NETWORK') # other option is PIXEL_COMPARISON_NETWORK
PIXEL_COMPARISON_LOCAL_NORMALIZATION = get_from_env('PIXEL_COMPARISON_LOCAL_NORMALIZATION', bool, False)
TRAIN_WAD_PATH = get_from_env('TRAIN_WAD_PATH', str, 'Train/D3_battle_navigation_split.wad_manymaps_test.wad')

# vizdoom
MAP_NAME_TEMPLATE = 'map%02d'
MOVE_FORWARD = [0, 0, 0, 1, 0, 0, 0]
MOVE_BACKWARD = [0, 0, 0, 0, 1, 0, 0]
MOVE_LEFT = [1, 0, 0, 0, 0, 0, 0]
MOVE_RIGHT = [0, 1, 0, 0, 0, 0, 0]
STAY_IDLE = [0, 0, 0, 0, 0, 0, 0]
TURN_LEFT = [0, 0, 0, 0, 0, 1, 0]
TURN_RIGHT = [0, 0, 0, 0, 0, 0, 1]
ACTIONS_LIST = [MOVE_FORWARD, MOVE_BACKWARD, MOVE_LEFT, MOVE_RIGHT, STAY_IDLE, TURN_LEFT, TURN_RIGHT]
ACTION_NAMES = ['MOVE_FORWARD', 'MOVE_BACKWARD', 'MOVE_LEFT', 'MOVE_RIGHT', 'STAY_IDLE', 'TURN_LEFT', 'TURN_RIGHT']
INVERSE_ACTION_NAMES_INDEX = {}
for index, value in enumerate(ACTION_NAMES):
  INVERSE_ACTION_NAMES_INDEX[value] = index
WAIT_IDLE_TICS = 0
WAIT_BEFORE_START_TICS = 140
VIZDOOM_TO_TF = [1, 2, 0]
NET_WIDTH = 160
NET_HEIGHT = 120
NET_CHANNELS = 3
SHOW_WIDTH = NET_WIDTH * 4
SHOW_HEIGHT = NET_HEIGHT * 4
SHOW_BORDER = 10
SHOW_CHANNELS = NET_CHANNELS
GYM_TO_OUR_ACTION = [STAY_IDLE, MOVE_FORWARD, TURN_RIGHT, TURN_LEFT]
ACTION_STATE_ENCODING_FRAMES = 2
EDGE_STATE_ENCODING_FRAMES = 1

#training
DEFAULT_RANDOM_SEED = 100
LEARNING_RATE = 1e-04
MODEL_CHECKPOINT_PERIOD = 100
MIN_RANDOM_TEXTURE_MAP_INDEX = 2
MAX_RANDOM_TEXTURE_MAP_INDEX = 401
TRAIN_REPEAT = 4
MAX_ACTION_DISTANCE = 5
MAX_CONTINUOUS_PLAY = 10000
BATCH_SIZE = 64
DUMP_AFTER_BATCHES = 1000
INF_EPOCHS = 1000000000
EDGE_MAX_EPOCHS = 1000
ACTION_MAX_EPOCHS = 1900
EDGE_EPISODES = 10
ACTION_EPISODES = 1
EDGE_CLASSES = 2
ACTION_CLASSES = len(ACTIONS_LIST)
NEGATIVE_SAMPLE_MULTIPLIER = 5
TRAIN_MEMORY_FRACTION = 0.4

#testing
TEST_REPEAT = TRAIN_REPEAT
JOINT_NETWORK = resnet.ResnetBuilder.build_resnet_18
SIAMESE_NETWORK = resnet.ResnetBuilder.build_siamese_resnet_18
PIXEL_COMPARISON_NETWORK = resnet.ResnetBuilder.build_pixel_comparison_network
EDGE_NETWORK = eval(EDGE_ARCHITECTURE)
ACTION_NETWORK = resnet.ResnetBuilder.build_resnet_18
DEEP_NET_ACTIONS = 1
GOAL_DISTANCE_ALLOWANCE = 63
TESTING_BATCH_SIZE = 1024
MAX_NUMBER_OF_STEPS_EXPLORATION = 10000
MAX_NUMBER_OF_STEPS_NAVIGATION = 5000
NUMBER_OF_NEAREST_NEIGHBOURS = 5
LARGE_SHORTCUTS_NUMBER = 100000
assert SMALL_SHORTCUTS_NUMBER <= LARGE_SHORTCUTS_NUMBER
TEST_RANDOM_SEED = DEFAULT_RANDOM_SEED + 1
TEST_MEMORY_FRACTION = 0.15

# paths
DEFAULT_CONFIG = os.path.join(DATA_PATH, 'default.cfg')
TRAIN_WAD = os.path.join(DATA_PATH, TRAIN_WAD_PATH)
EXPERIMENTS_DIRECTORY = '../../experiments/'
EXPERIMENTS_PATH_TEMPLATE = os.path.join(EXPERIMENTS_DIRECTORY, '%s/')
LOGS_PATH_TEMPLATE = os.path.join(EXPERIMENTS_PATH_TEMPLATE, 'logs/')
MODELS_PATH_TEMPLATE = os.path.join(EXPERIMENTS_PATH_TEMPLATE, 'models/')
LAST_MODEL_PATH_TEMPLATE = os.path.join(MODELS_PATH_TEMPLATE, 'model.h5')
CURRENT_MODEL_PATH_TEMPLATE = os.path.join(MODELS_PATH_TEMPLATE, 'model.{epoch:06d}.h5')
EVALUATION_PATH_TEMPLATE = os.path.join(EXPERIMENTS_PATH_TEMPLATE, 'evaluation/')
TESTED_MODEL_PATH_TEMPLATE = os.path.join(MODELS_PATH_TEMPLATE, 'model.h5')
ACTION_MODEL_ITERATION = ACTION_MAX_EPOCHS - 1
EDGE_MODEL_ITERATION = EDGE_MAX_EPOCHS - 1
ACTION_MODEL_PATH = os.path.join((MODELS_PATH_TEMPLATE % ACTION_EXPERIMENT_ID), 'model.%.6d.h5' % ACTION_MODEL_ITERATION)
ACTION_MODEL_WEIGHTS_PATH = os.path.join((MODELS_PATH_TEMPLATE % ACTION_EXPERIMENT_ID), 'model_weights.h5')
EDGE_MODEL_PATH = os.path.join((MODELS_PATH_TEMPLATE % EDGE_EXPERIMENT_ID), 'model.%.6d.h5' % EDGE_MODEL_ITERATION)
EDGE_MODEL_WEIGHTS_PATH = os.path.join((MODELS_PATH_TEMPLATE % EDGE_EXPERIMENT_ID), 'model_weights.h5')
EVALUATION_PATH = EVALUATION_PATH_TEMPLATE % EXPERIMENT_OUTPUT_FOLDER
SHORTCUTS_OUTPUT_PATH = os.path.join(EVALUATION_PATH, 'graph_shortcuts')
SHORTCUTS_CACHE_FILE_TEMPLATE = os.path.join(SHORTCUTS_OUTPUT_PATH, '%s_skip%d_max%d_shortcuts.npy')

#video visualization
FPS = 24
START_PAUSE_FRAMES = int(2.5 * FPS)
END_PAUSE_FRAMES = int(1.5 * FPS)
DELIMITER_FRAMES = int(FPS / 3)
HIGH_RESOLUTION_VIDEO = False
WRITE_EXPLORATION_VIDEO = False

#logging
FINAL_RESULTS = 'Final results:'
CURRENT_NAVIGATION_ENVIRONMENT = 'Current navigation environment:'
CURRENT_NAVIGATION_MODE = 'Current navigation mode:'
EXPLORATION_MODEL_DIRECTORY = 'Exploration model directory:'

# pixel comparison baseline
PIXEL_COMPARISON_DOWNSAMPLING_FACTOR = 2
DOWNSAMPLING = 2 ** PIXEL_COMPARISON_DOWNSAMPLING_FACTOR
assert NET_HEIGHT % DOWNSAMPLING == 0
assert NET_WIDTH % DOWNSAMPLING == 0
PIXEL_COMPARISON_HEIGHT = NET_HEIGHT / DOWNSAMPLING #28
PIXEL_COMPARISON_WIDTH = NET_WIDTH / DOWNSAMPLING #37
PIXEL_COMPARISON_CHANNELS = 1
PIXEL_COMPARISON_LOCAL_WINDOW = 10
if PIXEL_COMPARISON_LOCAL_NORMALIZATION:
  assert PIXEL_COMPARISON_HEIGHT % PIXEL_COMPARISON_LOCAL_WINDOW == 0
  assert PIXEL_COMPARISON_WIDTH % PIXEL_COMPARISON_LOCAL_WINDOW == 0

# teach and repeat
TEACH_AND_REPEAT_RANDOMIZATION = 0.1
def inverse_action(action):
  if action == MOVE_FORWARD:
    return MOVE_BACKWARD
  elif action == MOVE_BACKWARD:
    return MOVE_FORWARD
  elif action == MOVE_LEFT:
    return MOVE_RIGHT
  elif action == MOVE_RIGHT:
    return MOVE_LEFT
  elif action == STAY_IDLE:
    return STAY_IDLE
  elif TURN_LEFT:
    return TURN_RIGHT
  elif TURN_RIGHT:
    return TURN_LEFT
  else:
    raise Exception('Unknown action')
