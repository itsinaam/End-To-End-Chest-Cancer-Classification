import os

# Current working directory
current_dir = os.getcwd()

# Relative paths
CONFIG_FILE_PATH_RELATIVE = "../../../config/config.yaml"
PARAMS_FILE_PATH_RELATIVE = "../../../params.yaml"

# Convert to absolute paths
CONFIG_FILE_PATH_ABSOLUTE = os.path.abspath(os.path.join(current_dir, CONFIG_FILE_PATH_RELATIVE))
PARAMS_FILE_PATH_ABSOLUTE = os.path.abspath(os.path.join(current_dir, PARAMS_FILE_PATH_RELATIVE))
