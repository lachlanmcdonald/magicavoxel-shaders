# magicavoxel-shaders

__Shaders for [MagicaVoxel](https://ephtracy.github.io/) to simplify common and repetitive tasks.__

- Current release: `0.5.0`
- Tested with MagicaVoxel 0.98.1 (Beta) for Windows and Mac
- Released under the MIT License

## Installation

Install these shaders by copying the files from the `shader` directory in this project into the `shader` directory of your MagicaVoxel installation.

## Shaders

<ul>
    <li><a href="#slice_shader">Slice</a> (<code>sx</code>, <code>sy</code>, <code>sz</code>)</li>
    <li><a href="#lines_shader">Lines</a> (<code>lnx</code>, <code>lny</code>, <code>lnz</code>)</li>
    <li><a href="#soil_shader">soil</a> \ <a href="#soil2_shader">soil2</a></li>
    <li><a href="#outline_shader">outline</a> \ <a href="#outline2_shader">outline2</a></li>
    <li><a href="#grid_shader">grid</a></li>
    <li><a href="#noise_shader">noise</a> \ <a href="#noise2_shader">noise2</a></li>
    <li><a href="#dots_shader">dots</a> \ <a href="#dots2_shader">dots2</a></li>
    <li><a href="#flood_shader">flood</a> \ <a href="#flood2_shader">flood2</a></li>
</ul>

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

<h3 id="lines_shader">Lines</h3>

```
xs lnx [index] [spacing] [offset]
xs lny [index] [spacing] [offset]
xs lnz [index] [spacing] [offset]
```

![Shader preview](/img/lines.png?raw=true)

Replaces all voxels which match your selected color with lines set to the color passed as `index`. Setting the index to `0` will remove the voxels. Lines are spaced based on the `spacing` argument, which defaults to `2`.

<h3 id="soil_shader">soil</h3>

```
xs soil [index] [n]
```

![Shader preview](/img/soil.png?raw=true)

The `soil` shader adds voxels, set to the color passed as `index`, on top of voxels matching your selected colour. Voxels are only added if there empty space. By default, voxels are added if there is at least one empty space above, however you can adjust the number of voxels that are checked with `n`. For example, in the images above a `n` of `1` and `10` were used respectively.

<h3 id="soil2_shader">soil2</h3>

```
xs soil2 [index] [n]
```

![Shader preview](/img/soil2.png?raw=true)

Similar to `soil`, except voxels are replaced instead of added on top.

<h3 id="outline_shader">outline</h3>

```
xs outline [index]
```

![Shader preview](/img/outline.png?raw=true)

Replaces all voxels which match your selected color which are adjacent to another voxel of a different color. The outline color will be the provided `index`. Setting the index to `0` will remove the voxels.

`outline` checks adjacent and diagonal neighbors, producing slightly thicker lines when compared to `outline2`.

<h3 id="outline2_shader">outline2</h3>

```
xs outline2 [index]
```

![Shader preview](/img/outline2.png?raw=true)

Similar to `outline`, except only adjacent voxels are checked. Produces slightly thinner lines.

<h3 id="grid_shader">grid</h3>

```
xs grid [index] [x] [y] [xoffset] [yoffset]
```

![Shader preview](/img/grid.png?raw=true)

Replaces all voxels which match your selected color with a grid with a cell size determined by `x` and `y`. Grid cells are colored based on the provided `index`. Setting the index to `0` will remove the voxels. Grids can be square or rectangular. You can offset the position of the grid with `xoffset` and `yoffset` arguments, which default to `0`.

<h3 id="noise_shader">noise</h3>

```
xs noise [a] [b]
```

![Shader preview](/img/noise.png?raw=true)

Replaces all voxels which match your selected color with a randomly chosen color within a range of colors (`a` and `b`, inclusive). The noise will be the same across the z-axis.

<h3 id="noise2_shader">noise2</h3>

```
xs noise2 [a] [b]
```

![Shader preview](/img/noise2.png?raw=true)

Same as `noise`, except the z-axis is also randomized.

<h3 id="dots_shader">dots</h3>

```
xs dots [f] [index]
```

![Shader preview](/img/dots_a.png?raw=true)
![Shader preview](/img/dots_b.png?raw=true)

Replaces all voxels which match your selected color with a randomly chosen index. If `index` is 0, voxels are randomly removed instead. You can control the threshold by adjusting the `f` value. Values closer to `0.0` will replace more voxels. Values closer to `1.0` will replace less. Like with `noise`, dots are not removed randomly on the z-axis.

<h3 id="dots2_shader">dots2</h3>

```
xs dots2 [f] [index]
```

Same as `dots`, except the z-axis is also randomized.

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
