# magicavoxel-shaders

A number of shaders for [MagicaVoxel](https://ephtracy.github.io/) to simplify common or repetitive tasks.

## Installation

These can be installed by copying the files into the `shader` directory inside your MagicaVoxel installation.

## Shaders

### del
```xs del```

![Shader preview](/img/del.png?raw=true)

Removes all voxels which match your selected color.

### repl
```xs repl [index]```

![Shader preview](/img/repl.png?raw=true)

Replaces all voxels which match your selected color with the color index passed as `index`.

### noise
```xs noise [a] [b]```

![Shader preview](/img/noise.png?raw=true)

Replaces all voxels which match your selected color with a randomly chosen color within a range of colors (`a` and `b`, inclusive). The noise will be the same across the z-axis.

### noise2
```xs noise2 [a] [b]```

![Shader preview](/img/noise2.png?raw=true)

Similar to `noise`, except the z-axis is randomized as well.

### dots
```xs dots [f] [index]```

![Shader preview](/img/dots_a.png?raw=true)
![Shader preview](/img/dots_b.png?raw=true)

Replaces all voxels which match your selected color with a randomly chosen index. If `index` is 0, voxels are randomly removed instead. You can control the threshold by adjusting the `f` value. Values closer to `0.0` will replace more voxels. Values closer to `1.0` will replace less. Like with `noise`, dots are not removed randomly on the z-axis.

### flood
```xs flood [n]```

![Shader preview](/img/flood.png?raw=true)

Adds `n` number of layers of voxels with your selected color from the bottom of your model upwards. Voxels are only added to empty space and won't replace existing voxels.
