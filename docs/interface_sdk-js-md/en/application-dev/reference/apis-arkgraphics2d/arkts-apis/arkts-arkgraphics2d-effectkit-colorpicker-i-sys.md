# ColorPicker

取色类，用于从一张图像数据中获取它的主要颜色，适用于UI主题色提取、图片配色分析、智能配色推荐等场景，可帮助开发者基于图片内容动态生成和谐的配色方案。在调用ColorPicker的方法前，需要先通过  
[createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker)创建一个ColorPicker实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-effectKit-interface ColorPicker--><!--Device-effectKit-interface ColorPicker-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## discriminatePictureLightDegree

```TypeScript
discriminatePictureLightDegree(): PictureLightDegree
```

获取图片的明亮程度。当无法判别图片明亮程度时，返回UNKNOWN_LIGHT_COLOR_DEGREE_PICTURE。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-discriminatePictureLightDegree(): PictureLightDegree--><!--Device-ColorPicker-discriminatePictureLightDegree(): PictureLightDegree-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [PictureLightDegree](arkts-arkgraphics2d-effectkit-picturelightdegree-e-sys.md) | 图像颜色明亮程度。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let pictureLightDegree: effectKit.PictureLightDegree = colorPicker.discriminatePictureLightDegree();
      console.info('The color light degree of the image is ' + pictureLightDegree);
    }
  })
});
```

## getAlphaZeroTransparentProportion

ArkTS-Dyn:
```TypeScript
getAlphaZeroTransparentProportion(): number
```

ArkTS-Sta:
```TypeScript
getAlphaZeroTransparentProportion(): double
```

获取图像中完全透明的像素占比。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ColorPicker-getAlphaZeroTransparentProportion(): double--><!--Device-ColorPicker-getAlphaZeroTransparentProportion(): double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 完全透明的像素占比，比例的取值范围为[0, 1]。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 权限校验失败，非系统应用调用系统接口。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
        let percentage: number = colorPicker.getAlphaZeroTransparentProportion();
      console.info('Get proportion of fully transparent pixels: ' + percentage);
    }
  })
});
```

## getComplexityDegree

```TypeScript
getComplexityDegree(): PictureComplexityDegree
```

获取图像内容复杂度。当无法判别图像内容复杂度时，返回默认值UNKNOWN_COMPLEXITY_DEGREE_PICTURE。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-ColorPicker-getComplexityDegree(): PictureComplexityDegree--><!--Device-ColorPicker-getComplexityDegree(): PictureComplexityDegree-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [PictureComplexityDegree](arkts-arkgraphics2d-effectkit-picturecomplexitydegree-e-sys.md) | 图像内容复杂度。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 权限校验失败，非系统应用调用系统接口。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let complexityDegree: effectKit.PictureComplexityDegree = colorPicker.getComplexityDegree();
      console.info('The complexity degree of the image is ' + complexityDegree);
    }
  })
});
```

## getDeepenImmersionColor

```TypeScript
getDeepenImmersionColor(): Color
```

生成与背景色融合且比背景色更深的强沉浸感颜色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口通过颜色混合算法，创建一种既与背景色协调又具有更强沉浸感的颜色效果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-getDeepenImmersionColor(): Color--><!--Device-ColorPicker-getDeepenImmersionColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Color实例，即图像强沉浸色对应的颜色值。当图像处理失败或无法生成沉浸色时返回null。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getDeepenImmersionColor();
      console.info('get deepen immersion color =' + color);
    }
  })
});
```

## getImmersiveBackgroundColor

```TypeScript
getImmersiveBackgroundColor(): Color
```

生成能够创造沉浸式视觉效果的沉浸式背景色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口基于主色生成适合作为沉浸式背景的颜色值。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-getImmersiveBackgroundColor(): Color--><!--Device-ColorPicker-getImmersiveBackgroundColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Color实例，即图像沉浸式背景色对应的颜色值。当图像处理失败或无法生成沉浸式背景色时返回null。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getImmersiveBackgroundColor();
      console.info('get immersive background color =' + color);
    }
  })
});
```

## getImmersiveForegroundColor

```TypeScript
getImmersiveForegroundColor(): Color
```

生成能够创造沉浸式视觉效果的沉浸式前景色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口基于主色生成适合作为沉浸式前景的颜色值。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-getImmersiveForegroundColor(): Color--><!--Device-ColorPicker-getImmersiveForegroundColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Color实例，即图像沉浸式前景色对应的颜色值。当图像处理失败或无法生成沉浸式前景色时返回null。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getImmersiveForegroundColor();
      console.info('get immersive foreground color =' + color);
    }
  })
});
```

## getMorandiShadowColor

```TypeScript
getMorandiShadowColor(): Color
```

从图像的主色中获取莫兰迪阴影色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)。该接口通过特定的颜色转换算法，将主色调转换为具有莫兰迪风格的阴影色调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-getMorandiShadowColor(): Color--><!--Device-ColorPicker-getMorandiShadowColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Color实例，即图像莫兰迪阴影色对应的颜色值。当图像处理失败或无法获取莫兰迪阴影色时返回null。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getMorandiShadowColor();
      console.info('get Morandi shadow color =' + color);
    }
  })
});
```

## getReverseColor

```TypeScript
getReverseColor(): Color
```

基于图像亮度判别结果生成反向颜色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。根据  
[discriminatePictureLightDegree](arkts-arkgraphics2d-effectkit-colorpicker-i-sys.md#discriminatepicturelightdegree)接口获取的图片明亮类型得到一个反色，仅极亮色图片（EXTREMELY_LIGHT_COLOR_PICTURE）类型返回黑色，其他类型返回白色。用于界面主题或对比度计算。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ColorPicker-getReverseColor(): Color--><!--Device-ColorPicker-getReverseColor(): Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Color实例，即图像反向颜色对应的颜色值。当图像处理失败或无法生成反向颜色时返回null。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getReverseColor();
      console.info('get reverse color =' + color);
    }
  })
});
```

## getShadeDegree

```TypeScript
getShadeDegree(): PictureShadeDegree
```

获取图像颜色深浅度。当无法判别图像颜色深浅度时，返回默认值UNKNOWN_SHADE_DEGREE_PICTURE。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-ColorPicker-getShadeDegree(): PictureShadeDegree--><!--Device-ColorPicker-getShadeDegree(): PictureShadeDegree-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [PictureShadeDegree](arkts-arkgraphics2d-effectkit-pictureshadedegree-e-sys.md) | 图像颜色深浅度。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 权限校验失败，非系统应用调用系统接口。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let shadeDegree: effectKit.PictureShadeDegree = colorPicker.getShadeDegree();
      console.info('The shade degree of the image is ' + shadeDegree);
    }
  })
});
```

## getTopProportionColorsAndPercentage

ArkTS-Dyn:
```TypeScript
getTopProportionColorsAndPercentage(colorCount: number): Map<Color | null, number | null>
```

ArkTS-Sta:
```TypeScript
getTopProportionColorsAndPercentage(colorCount: int): Map<Color | null, double | null>
```

同步返回图像占比靠前的颜色值及其对应比例，个数由`colorCount`指定。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-ColorPicker-getTopProportionColorsAndPercentage(colorCount: int): Map<Color | null, double | null>--><!--Device-ColorPicker-getTopProportionColorsAndPercentage(colorCount: int): Map<Color | null, double | null>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 颜色值及对应比例的个数，向下取整。在OpenHarmony 6.1之前，取值范围为[1, 10]， 取色个数大于10视为取前10个；从OpenHarmony 6.1开始，取值范围为[1, 20]，取色个数大于20视为取前20个。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Map&lt;Color \| null, number \| null&gt;  <br>ArkTS-Sta：Map&lt;Color \| null, double \| null&gt; | 图像占比前`colorCount`的颜色值与对应比例的字典，比例的取值范围为[0,1]。 - 当实际读取的特征色个数小于`colorCount`时，字典大小为实际特征色个数。 - 取色失败或取色个数小于1返回`Map()`。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 权限校验失败，非系统应用调用系统接口。 |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let colors: Map<effectKit.Color | null, number | null> = colorPicker.getTopProportionColorsAndPercentage(2);
      colors.forEach((value: number | null, key: effectKit.Color | null) => {
        console.info('get top proportion colors and percentages: color ' + key + ', percentage ' + value);
      })
    }
  })
});
```

