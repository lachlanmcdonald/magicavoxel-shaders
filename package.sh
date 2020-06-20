TAG=$(git describe --abbrev=0)
zip "magicavoxel-shaders-${TAG}.zip" shader/*.txt shader/**/*.txt
