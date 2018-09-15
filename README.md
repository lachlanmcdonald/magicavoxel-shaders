# magicavoxel-shaders

__Shaders for [MagicaVoxel](https://ephtracy.github.io/) to simplify common and repetitive tasks.__

- Current release: `0.7.0`
- Tested with MagicaVoxel 0.99.1 for Windows and Mac
- Released under the MIT License

**Note v0.99.1:** Shaders work with v0.99.1, but the tooltip which shows the color index is not present. It [should be present](https://twitter.com/ephtracy/status/997672870452002816) in a later version.

## Installation

Install these shaders by copying the files from the `shader` directory in this project into the `shader` directory of your MagicaVoxel installation.

## Shaders

<ul>
    <li><a href="#slice_shader">Slice</a> &mdash; <code>sx</code> <code>sy</code> <code>sz</code></li>
    <li><a href="#pyramid_shader">Pyramid</a> &mdash; <code>py</code> <code>py2</code></li>
    <li><a href="#sand_shader">Sand</a> &mdash; <code>sand</code> <code>sand2</code></li>
    <li><a href="#soil_shader">Soil</a> &mdash; <code>soil</code> <code>soil2</code></li>
    <li><a href="#case_shader">Case</a> &mdash; <code>case</code> <code>outline2</code></li>
    <li><a href="#outline_shader">Outline</a> &mdash; <code>outline</code> <code>outline2</code></li>
    <li><a href="#noise_shader">Noise</a> &mdash; <code>noise</code></li>
    <li><a href="#rand_shader">Random</a> &mdash; <code>rand</code></li>
    <li><a href="#flood_shader">Flood</a> &mdash; <code>flood</code> <code>flood2</code></li>
    <li><a href="#grid_shader">Grid</a> &mdash; <code>grid</code></li>
    <li><a href="#lines_shader">Lines</a> &mdash; <code>lnx</code> <code>lny</code> <code>lnz</code></li>
</ul>

<h3 id="slice_shader">Slice</h3>

```
xs sx [c] [count]
xs sy [c] [count]
xs sz [c] [count]
```

<img src="/img/slice.png?raw=true" alt="" width="238"><img src="/img/slice_sx_19_1.png?raw=true" alt="" width="238"><img src="/img/slice_sy_15_1.png?raw=true" alt="" width="238">

The slice shaders removes one or more segments from the x, y or z axis. All other rows are shuffled to full the available space. The first parameter `c` is the coordinate of the segment you wish to remove and `count` is the number of rows. Note that `count` is optional and defaults to `1`.

For example, in the first image, segments are removed with these commands:

```
xs sx 19 1
xs sy 15 1
```

<h3 id="pyramid_shader">Pyramid</h3>

```
xs py [index]
xs py2 [index]
```

<img src="/img/py1.png?raw=true" alt="" width="238"><img src="/img/py2.png?raw=true" alt="" width="238">

<img src="/img/py3.png?raw=true" alt="" width="238"><img src="/img/py4.png?raw=true" alt="" width="238">

<img src="/img/py5.png?raw=true" alt="" width="238"><img src="/img/py6.png?raw=true" alt="" width="238">

The `py` and `py2` shaders add a layer of voxel on top of voxels matching the selected colour. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.

`py` will only add voxels when the adjacent voxels match the selected color. Whereas, `py2` will add voxels if there are adjacent voxels of any color.

If provided, `index` will be the color index of the added voxels. This parameter is optional. If ommitted (or set to `0`) the selected color index is used instead. 

Each time the shader is executed, a single layer is added. To add multiple layers at once, you can run the command in a loop as shown below:

```
xs -n 50 py
xs -n 50 py2
```

<img src="/img/py1.png?raw=true" alt="" width="238"><img src="/img/py7.png?raw=true" alt="" width="238">

If neither axis modes (or both X and Y) are set, the shader will form a square pyramid. If either X or Y modes are set, the shader will form a triangle pyramid instead, with the slope facing the X or Y axes respectively.

<h3 id="sand_shader">Sand</h3>

```
xs sand [index] [add]
xs sand2 [index] [add]
```

<img src="/img/sand1.png?raw=true" alt="" width="238"><img src="/img/sand2.png?raw=true" alt="" width="238"><img src="/img/sand3.png?raw=true" alt="" width="238">

The `sand` and `sand2` shaders add a layer voxels on top of voxels matching the selected colour. Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough sand pile. The number of adjacent neighbours affects the randomness, with a higher number of neighbours increasing the odds a voxel will be added.

If provided, `index` will be the color index of the added voxels. This parameter is optional. If ommitted (or set to `0`) the selected color index is used instead.

`add` can be used to increase the odds of adding voxels. Numbers between `0.01` and `0.4` have the best effect. Because `add` is the second parameter, you can set `index` to `0` if using `add` in a loop.

Each time the shader is executed, a single layer is added. To add multiple layers at once, you can run the command in a loop as shown below:

```
xs -n 50 sand
xs -n 50 sand2
```

<h3 id="lines_shader">Lines</h3>

```
xs line [index] [spacing] [offset]
```

<img src="/img/line.png?raw=true" alt="" width="238"><img src="/img/line_2.png?raw=true" alt="" width="238">

Replaces all voxels which match your selected color with lines set to the color passed as `index`. Setting the index to `0` will remove the voxels. Lines are spaced based on the `spacing` parameter, which defaults to `2`. Lines can be offset with the `offset` parameter. You should use axis modes to limit the lines to a particular axis.

<small>(This shader combines the <code>lnx</code>, <code>lny</code> and <code>lnz</code> shaders from the earlier versions.)</small>

<h3 id="soil_shader">Soil</h3>

```
xs soil [index] [n]
xs soil2 [index] [n]
```

<img src="/img/soil.png?raw=true" alt="" width="238"><img src="/img/soil_2.png?raw=true" alt="" width="238">

The `soil` and `soil2` shaders adds voxels, set to the color passed as `index`, on top of voxels matching your selected colour.

- Voxels are only added if there empty space. By default, voxels are added if there is at least one empty space above, however you can adjust the number of voxels that are checked with `n`.
- `soil2` is similar to `soil`, except voxels are replaced instead of added on top.

<h3 id="case_shader">Case</h3>

```
xs case [index]
```

<img src="/img/case.png?raw=true" alt="" width="175"><img src="/img/case_1.png?raw=true" alt="" width="175"><img src="/img/case_x.png?raw=true" alt="" width="175"><img src="/img/case_y.png?raw=true" alt="" width="175"><img src="/img/case_z.png?raw=true" alt="" width="175"><img src="/img/case_xy.png?raw=true" alt="" width="175">

Surrounds (encases) the all voxels which match your selected color. Axis modes can use used to only add voxels on certain axes. The outline color will be the provided index.
 
<h3 id="outline_shader">Outline</h3>

```
xs outline [index]
xs outline2 [index]
```

<img src="/img/outline1.png?raw=true" alt="" width="238"><img src="/img/outline2.png?raw=true" alt="" width="238"><img src="/img/outline3.png?raw=true" alt="" width="238">

Replaces all voxels which match your selected color which are adjacent to another voxel of a different color. The outline color will be the provided `index`. Setting the index to `0` will remove the voxels.

`outline2` is similar to `outline`, except fewer adjacent voxels are checked, producing slightly thinner lines.

<h3 id="grid_shader">Grid</h3>

```
xs grid [index] [x] [y] [xoffset] [yoffset]
```

<img src="/img/grid.png?raw=true" alt="" width="238"><img src="/img/grid1x5.png?raw=true" alt="" width="238"><img src="/img/grid5x5.png?raw=true" alt="" width="238">

Replaces all voxels which match your selected color with a grid with a cell size determined by `x` and `y`. Grid cells are colored based on the provided `index`. Setting the index to `0` will remove the voxels. Grids can be square or rectangular. You can offset the position of the grid with `xoffset` and `yoffset` parameters, which default to `0`.

<h3 id="noise_shader">Noise</h3>

```
xs noise [a] [b]
```

<img src="/img/noise1.png?raw=true" alt="" width="238"><img src="/img/noise2.png?raw=true" alt="" width="238">

Replaces all voxels which match your selected color with a randomly chosen color within a range of colors (`a` and `b`, inclusive).

<img src="/img/noise3.png?raw=true" alt="" width="238"><img src="/img/noise4.png?raw=true" alt="" width="238">

Voxels are replaced across all axes. You can randomize the X, Y, or Z axis (or a combination) with the axis mode.

<h3 id="rand_shader">Random</h3>

```
xs rand [f] [index]
```

<img src="/img/rand_025.png?raw=true" alt="" width="238"><img src="/img/rand_050.png?raw=true" alt="" width="238"><img src="/img/rand_075.png?raw=true" alt="" width="238">

Replaces all voxels which match your selected color with a randomly chosen index. If `index` is 0, voxels are randomly removed instead. You can control the threshold by adjusting the `f` value. Values closer to `0.0` will replace more voxels. Values closer to `1.0` will replace less.

<img src="/img/rand_050_xy.png?raw=true" alt="" width="238"><img src="/img/rand_050_xz.png?raw=true" alt="" width="238"><img src="/img/rand_050_y.png?raw=true" alt="" width="238">

Voxels are replaced across all axes. You can randomize the X, Y, or Z axis (or a combination) with the axis mode.

<h3 id="flood_shader">Flood</h3>

```
xs flood [n]
xs flood2 [n]
```

<img src="/img/flood.png?raw=true" alt="" width="180"><img src="/img/flood_1.png?raw=true" alt="" width="238"><img src="/img/flood2.png?raw=true" alt="" width="238">

Adds `n` number of layers of voxels with your selected color from the bottom of your model upwards. Voxels are only added to empty space and won't replace existing voxels. Defaults to a single layer.

`flood2` is similar to `flood`, except flooding stops when a voxel is encountered so that exclosed spaces aren't filled.
