# magicavoxel-shaders

__Shaders for [MagicaVoxel](https://ephtracy.github.io/) to simplify common and repetitive tasks.__

- Current release: `0.5.0`
- Tested with MagicaVoxel 0.97.4 for Windows and Mac
- Released under the MIT License

## Installation

Install by copying the files into the `shader` directory inside your MagicaVoxel installation.

## Shaders

<ul>
    <li><a href="#slice_shader">Slice</a> (<code>sx</code>, <code>sy</code>, <code>sz</code>)</li>
    <li><a href="#lines_shader">Lines</a> (<code>lnx</code>, <code>lny</code>, <code>lnz</code>)</li>
    <li><a href="#outline_shader">outline</a></li>
    <li><a href="#outline2_shader">outline2</a></li>
    <li><a href="#grid_shader">grid</a></li>
    <li><a href="#noise_shader">noise</a></li>
    <li><a href="#noise2_shader">noise2</a></li>
    <li><a href="#dots_shader">dots</a></li>
    <li><a href="#dots2_shader">dots2</a></li>
    <li><a href="#flood_shader">flood</a></li>
    <li><a href="#flood2_shader">flood2</a></li>
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

For example, in the first image above, the segments are removed with these two commands:

```
xs sx 16 2
xs sy 20 2
```

In the second image above, the segment is removed with this command.

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

Replaces all voxels which match your selected color with lines set to the color index passed as `index`. Setting the index to `0` will remove the voxels. Lines are spaced based on the `spacing` argument, which defaults to `2`.

<h3 id="outline_shader">outline</h3>

```
xs outline [index]
```

![Shader preview](/img/outline.png?raw=true)

Replaces all voxels which match your selected color which are adjacent to another voxel of a different color. The outline is colored based on the provided `index`. Outline checks adjacent and diagonal neighbors, producing slightly thicker lines.

<h3 id="outline2_shader">outline2</h3>

```
xs outline2 [index]
```

![Shader preview](/img/outline2.png?raw=true)

Similar to the `outline` shader, except only adjacent voxels are checked. Produces slightly thinner lines.

<h3 id="grid_shader">Grid</h3>

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
