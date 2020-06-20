TAG=$(git describe --tags)
zip "magicavoxel-shaders-${TAG}.zip" shader/*.txt shader/**/*.txt
