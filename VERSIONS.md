# 0.11.0

- **stairs**
	- Moved under _primitives_
- **tiles**
	- Updated to used the first and last selected colors from the palette when generating tiles.
- **noise**
	- Updated to use the selected colors from the palette when generating noise.
	- User must now specify the color index to replace
- **random**
	- Updated to use the selected colors from the palette when selecting voxels to replace, allowing **random** to be used on an already noisey area.
- **sand** / **sand2**
	- Introduce new modes for picking voxel colors whilst generating the sand
	- Updated to use the selected colors from the palette when generating noise.
