Set-Variable -Name "TAG" -Value (git describe --tags) -Scope Private
Compress-Archive -Force -Path "shader" -DestinationPath "magicavoxel-shaders-${TAG}.zip"
