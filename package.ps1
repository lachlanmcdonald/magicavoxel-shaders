# Copyright (c) 2023 Lachlan McDonald
# This work is licensed under the MIT License (MIT)
# https://github.com/lachlanmcdonald/magicavoxel-shaders
Set-Variable -Name "TAG" -Value (git describe --tags) -Scope Private
Compress-Archive -Force -Path "shader" -DestinationPath "magicavoxel-shaders-${TAG}.zip"
