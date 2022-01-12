# Copyright (c) 2022 Lachlan McDonald
# This work is licensed under the MIT License (MIT)
# https://github.com/lachlanmcdonald/magicavoxel-shaders
TAG=$(git describe --tags)
zip "magicavoxel-shaders-${TAG}.zip" shader/*.txt shader/**/*.txt
