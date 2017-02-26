# magicavoxel-shaders

__Shaders for [MagicaVoxel](https://ephtracy.github.io/) to simplify common and repetitive tasks.__

- Current release: `0.6.0`
- Tested with MagicaVoxel 0.98.1 (Beta) for Windows and Mac
- Released under the MIT License

## Installation

Install these shaders by copying the files from the `shader` directory in this project into the `shader` directory of your MagicaVoxel installation.

## Shaders

<ul>
    <li><a href="#slice_shader">Slice</a> &mdash; <code>sx</code> <code>sy</code> <code>sz</code></li>
    <li><a href="#pyramid_shader">Pyramid</a> &mdash; <code>py</code> <code>py2</code></li>
    <li><a href="#sand_shader">Sand</a> &mdash; <code>sand</code> <code>sand2</code></li>
    <li><a href="#soil_shader">Soil</a> &mdash; <code>soil</code> <code>soil2</code></li>
    <li><a href="#outline_shader">Outline</a> &mdash; <code>outline</code> <code>outline2</code></li>
    <li><a href="#noise_shader">Noise</a> &mdash; <code>noise</code></li>
    <li><a href="#rand_shader">Random</a> &mdash; <code>rand</code></li>
    <li><a href="#flood_shader">Flood</a> &mdash; <code>flood</code> <code>flood2</code></li>
    <li><a href="#grid_shader">Grid</a> &mdash; <code>grid</code></li>
    <li><a href="#lines_shader">Lines</a> &mdash; <code>lnx</code> <code>lny</code> <code>lnz</code></li>
</ul>

From version 0.6.0, `dots` and `dots2` are combined into a single shader (`rand`) that can be configured to produce the same output by using "axis modes."

<h3 id="slice_shader">Slice</h3>

```
xs sx [c] [count]
xs sy [c] [count]
xs sz [c] [count]
```

![Shader preview](/img/slice_a.png?raw=true)

![Shader preview](/img/slice_b.png?raw=true)

The slice shaders removes one or more segments from the x, y or z axis. All other rows are shuffled to full the available space. The first argument `c` is the coordinate of the segment you wish to remove and `count` is the number of rows. Note that `count` is optional and defaults to `1`.

For example, in the first image, segments are removed with these commands:

```
xs sx 16 2
xs sy 20 2
```

In the second image, segments are removed with this command:

```
xs sz 2
```

<h3 id="pyramid_shader">Pyramid</h3>

```
xs py [index]
xs py2 [index]
```

The `py` and `py2` shaders add a layer of voxel on top of voxels matching the selected colour. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.

`py` will only add voxels when the adjacent voxels match the selected color. Whereas, `py2` will add voxels if there are adjacent voxels of any color.

If provided, `index` will be the color index of the added voxels. This argument is optional. If ommitted (or set to `0`) the selected color index is used instead. 

Each time the shader is executed, a single layer is added. To add multiple layers at once, you can run the command in a loop.

```
xs -n 50 py
xs -n 50 py2
```

If neither axis modes (or both X and Y) are set, the shader will form a square pyramid. If either X or Y modes are set, the shader will form a triangle pyramid instead, with the slope facing the X or Y axes respectively.

<h3 id="sand_shader">Sand</h3>

```
xs sand [index] [add]
xs sand2 [index] [add]
```

The `sand` and `sand2` shaders add a layer voxels on top of voxels matching the selected colour. Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough sand pile. The number of adjacent neighbours affects the randomness, with a higher number of neighbours increasing the odds a voxel will be added.

If provided, `index` will be the color index of the added voxels. This argument is optional. If ommitted (or set to `0`) the selected color index is used instead.

`add` can be used to increase the odds of adding voxels. Numbers between `0.01` and `0.4` have the best effect. Because `add` is the second argument, you can set `index` to `0` if using `add` in a loop.

Each time the shader is executed, a single layer is added. To add multiple layers at once, you can run the command in a loop as shown below.


```
xs -n 50 sand
xs -n 50 sand2
```

<h3 id="lines_shader">Lines</h3>

```
xs lnx [index] [spacing] [offset]
xs lny [index] [spacing] [offset]
xs lnz [index] [spacing] [offset]
```

![Shader preview](/img/lines.png?raw=true)

Replaces all voxels which match your selected color with lines set to the color passed as `index`. Setting the index to `0` will remove the voxels. Lines are spaced based on the `spacing` argument, which defaults to `2`.

<h3 id="soil_shader">Soil</h3>

```
xs soil [index] [n]
xs soil2 [index] [n]
```

![Shader preview](/img/soil.png?raw=true)

The `soil` and `soil2` shaders adds voxels, set to the color passed as `index`, on top of voxels matching your selected colour. Voxels are only added if there empty space. By default, voxels are added if there is at least one empty space above, however you can adjust the number of voxels that are checked with `n`. For example, in the images above a `n` of `1` and `10` were used respectively.

![Shader preview](/img/soil2.png?raw=true)

`soil2` is similar to `soil`, except voxels are replaced instead of added on top.

<h3 id="outline_shader">outline</h3>

```
xs outline [index]
xs outline2 [index]
```

![Shader preview](/img/outline.png?raw=true)

Replaces all voxels which match your selected color which are adjacent to another voxel of a different color. The outline color will be the provided `index`. Setting the index to `0` will remove the voxels.

![Shader preview](/img/outline2.png?raw=true)

`outline2` is similar to `outline`, except fewer adjacent voxels are checked, producing slightly thinner lines.

<h3 id="grid_shader">grid</h3>

```
xs grid [index] [x] [y] [xoffset] [yoffset]
```

![Shader preview](/img/grid.png?raw=true)

Replaces all voxels which match your selected color with a grid with a cell size determined by `x` and `y`. Grid cells are colored based on the provided `index`. Setting the index to `0` will remove the voxels. Grids can be square or rectangular. You can offset the position of the grid with `xoffset` and `yoffset` arguments, which default to `0`.

<h3 id="noise_shader">Noise</h3>

```
xs noise [a] [b]
```

Replaces all voxels which match your selected color with a randomly chosen color within a range of colors (`a` and `b`, inclusive).

Voxels are replaced across all axes. You can randomize the X, Y, or Z axis (or a combination) with the axis mode.

<h3 id="rand_shader">Random</h3>

```
xs rand [f] [index]
```

Replaces all voxels which match your selected color with a randomly chosen index. If `index` is 0, voxels are randomly removed instead. You can control the threshold by adjusting the `f` value. Values closer to `0.0` will replace more voxels. Values closer to `1.0` will replace less.

Voxels are replaced across all axes. You can randomize the X, Y, or Z axis (or a combination) with the axis mode.


<h3 id="flood_shader">flood</h3>

```
xs flood [n]
```

![Shader preview](/img/flood.png?raw=true)

Adds `n` number of layers of voxels with your selected color from the bottom of your model upwards. Voxels are only added to empty space and won't replace existing voxels. Defaults to 1 layer.

<h3 id="flood2_shader">flood2</h3>

```
xs flood2 [n]
```

Similar to `flood`, except flooding stops when a voxel is encountered so that exclosed spaces aren't filled.
