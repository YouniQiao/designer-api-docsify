# CanvasRenderer

Canvas渲染器，用于绘制形状、文本、图片等对象。

**Inheritance/Implementation:** CanvasRenderer extends [CanvasPath](arkts-arkui-canvaspath-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CanvasRenderer extends CanvasPath--><!--Device-unnamed-export declare class CanvasRenderer extends CanvasPath-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## beginPath

```TypeScript
beginPath(): void
```

创建一个新的绘制路径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-beginPath(): void--><!--Device-CanvasRenderer-beginPath(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearRect

```TypeScript
clearRect(x: double, y: double, w: double, h: double): void
```

删除指定区域内的绘制内容。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clearRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-clearRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | 指定矩形上的左上角x坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| y | double | Yes | 指定矩形上的左上角y坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| w | double | Yes | 指定矩形的宽度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| h | double | Yes | 指定矩形的高度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |

## clip

```TypeScript
clip(fillRule?: CanvasFillRule): void
```

设置当前路径为剪切路径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | 指定要剪切对象的规则。可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。默认值："nonzero" |

## clip

```TypeScript
clip(path: Path2D, fillRule?: CanvasFillRule): void
```

设置指定路径为剪切路径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes | Path2D剪切路径。异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | 指定要剪切对象的规则。可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。默认值："nonzero" |

## createConicGradient

```TypeScript
createConicGradient(startAngle: double, x: double, y: double): CanvasGradient
```

创建一个圆锥渐变色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createConicGradient(startAngle: double, x: double, y: double): CanvasGradient--><!--Device-CanvasRenderer-createConicGradient(startAngle: double, x: double, y: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startAngle | double | Yes | 开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。 异常值undefined和null按0处理，NaN和Infinity按无效值处理。单位：弧度 |
| x | double | Yes | 圆锥渐变的中心x轴坐标。异常值undefined和null按0处理， NaN和Infinity按无效值处理。默认单位：vp |
| y | double | Yes | 圆锥渐变的中心y轴坐标。异常值undefined和null按0处理， NaN和Infinity按无效值处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

## createImageData

```TypeScript
createImageData(sw: double, sh: double): ImageData
```

创建新的、空白的、指定大小的ImageData对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createImageData(sw: double, sh: double): ImageData--><!--Device-CanvasRenderer-createImageData(sw: double, sh: double): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sw | double | Yes | ImageData的宽度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| sh | double | Yes | ImageData的高度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-imagedata-c.md) | 新的ImageData对象。 |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData--><!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes | 现有的ImageData对象。异常值undefined和null按width和height为0的ImageData处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-imagedata-c.md) | 新的ImageData对象。 |

## createLinearGradient

```TypeScript
createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient
```

创建一个线性渐变色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient--><!--Device-CanvasRenderer-createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x0 | double | Yes | 起点的x轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| y0 | double | Yes | 起点的y轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| x1 | double | Yes | 终点的x轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| y1 | double | Yes | 终点的y轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

## createPattern

```TypeScript
createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null
```

通过指定图像和重复方式创建图片填充的模板。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null--><!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes | 图源对象。异常值undefined或null按无效值处理。 |
| repetition | string \| null | Yes | 设置图像重复的方式： 'repeat'：沿x轴和y轴重复绘制图像； 'repeat-x'：沿x轴重复绘制图像； 'repeat-y'：沿y轴重复绘制图像； 'no-repeat'：不重复绘制图像； 'clamp'：在原始边界外绘制时，超出部分使用边缘的颜色绘制； 'mirror'：沿x轴和y轴重复翻转绘制图像。 异常值undefined或null按无效值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md) | 通过指定图像和重复方式创建图片填充的模板对象。 |

## createRadialGradient

```TypeScript
createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient
```

创建一个径向渐变色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient--><!--Device-CanvasRenderer-createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x0 | double | Yes | 起始圆的x轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| y0 | double | Yes | 起始圆的y轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| r0 | double | Yes | 起始圆的半径。必须是非负且有限的。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。默认单位：vp |
| x1 | double | Yes | 终点圆的x轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| y1 | double | Yes | 终点圆的y轴坐标。异常值undefined和null会导致此接口返回undefined， NaN和Infinity按无效值处理。默认单位：vp |
| r1 | double | Yes | 终点圆的半径。必须为非负且有限的。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void
```

进行图像绘制。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| PixelMap | Yes | 图片资源。异常值undefined或null按无效值处理，不进行绘制。 |
| dx | double | Yes | 绘制区域左上角在x轴的位置。异常值undefined或null按0处理，NaN和Infinity按无效值处理， 不进行绘制。默认单位：vp |
| dy | double | Yes | 绘制区域左上角在y轴的位置。异常值undefined或null按0处理，NaN和Infinity按无效值处理， 不进行绘制。默认单位：vp |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void
```

将图像拉伸或压缩绘制。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| PixelMap | Yes | 图片资源。异常值undefined或null按无效值处理，不进行绘制。 |
| dx | double | Yes | 绘制区域左上角在x轴的位置。异常值undefined或null按0处理，NaN和Infinity按无效值处理， 不进行绘制。默认单位：vp |
| dy | double | Yes | 绘制区域左上角在y轴的位置。异常值undefined或null按0处理，NaN和Infinity按无效值处理， 不进行绘制。默认单位：vp |
| dw | double | Yes | 绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时， 将图像宽度拉伸或压缩为绘制区域的宽度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| dh | double | Yes | 绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时， 将图像高度拉伸或压缩为绘制区域的高度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,
    dw: double, dh: double): void
```

将图像裁剪后拉伸或压缩绘制。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,    dw: double, dh: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,    dw: double, dh: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| PixelMap | Yes | 图片资源。异常值undefined或null按无效值处理，不进行绘制。 |
| sx | double | Yes | 裁切源图像时距离源图像左上角的x坐标值。异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| sy | double | Yes | 裁切源图像时距离源图像左上角的y坐标值。异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| sw | double | Yes | 裁切源图像时需要裁切的宽度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| sh | double | Yes | 裁切源图像时需要裁切的高度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| dx | double | Yes | 绘制区域左上角在x轴的位置。异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| dy | double | Yes | 绘制区域左上角在y轴的位置。异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。默认单位：vp |
| dw | double | Yes | 绘制区域的宽度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。当绘制区域的宽度和裁剪图像的宽度不一致时， 将图像宽度拉伸或压缩为绘制区域的宽度。默认单位：vp |
| dh | double | Yes | 绘制区域的高度。负数、异常值undefined或null按0处理， NaN和Infinity按无效值处理，不进行绘制。当绘制区域的高度和裁剪图像的高度不一致时， 将图像高度拉伸或压缩为绘制区域的高度。默认单位：vp |

## fill

```TypeScript
fill(fillRule?: CanvasFillRule): void
```

对当前路径进行填充。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | 指定要填充对象的规则。可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。默认值："nonzero" |

## fill

```TypeScript
fill(path: Path2D, fillRule?: CanvasFillRule): void
```

对指定路径进行填充。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes | Path2D填充路径。异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | 指定要填充对象的规则。可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。默认值："nonzero" |

## fillRect

```TypeScript
fillRect(x: double, y: double, w: double, h: double): void
```

填充一个矩形。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fillRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-fillRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | 指定矩形左上角点的x坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| y | double | Yes | 指定矩形左上角点的y坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| w | double | Yes | 指定矩形的宽度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| h | double | Yes | 指定矩形的高度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |

## fillText

```TypeScript
fillText(text: string, x: double, y: double, maxWidth?: double): void
```

绘制填充类文本。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fillText(text: string, x: double, y: double, maxWidth?: double): void--><!--Device-CanvasRenderer-fillText(text: string, x: double, y: double, maxWidth?: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 需要绘制的文本内容。异常值undefined或null按无效值处理，不进行绘制。 |
| x | double | Yes | 文本绘制起点的x轴坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| y | double | Yes | 文本绘制起点的y轴坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| maxWidth | double | No | 指定文本允许的最大宽度。异常值null按无效值处理，不进行绘制， undefined、NaN或Infinity按默认值处理。默认值：不限制宽度。默认单位：vp |

## getImageData

```TypeScript
getImageData(sx: double, sy: double, sw: double, sh: double): ImageData
```

以当前canvas指定区域内的像素创建ImageData对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getImageData(sx: double, sy: double, sw: double, sh: double): ImageData--><!--Device-CanvasRenderer-getImageData(sx: double, sy: double, sw: double, sh: double): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | 需要输出的区域的左上角x坐标。异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sy | double | Yes | 需要输出的区域的左上角y坐标。异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sw | double | Yes | 需要输出的区域的宽度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| sh | double | Yes | 需要输出的区域的高度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-imagedata-c.md) | 新的ImageData对象。 |

## getLineDash

```TypeScript
getLineDash(): double[]
```

获得当前画布的虚线样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getLineDash(): double[]--><!--Device-CanvasRenderer-getLineDash(): double[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double[] | 返回数组，该数组用来描述线段如何交替和间距长度。默认单位：vp |

## getPixelMap

```TypeScript
getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined
```

以当前canvas指定区域内的像素创建PixelMap对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined--><!--Device-CanvasRenderer-getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | 需要输出的区域的左上角x坐标。异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sy | double | Yes | 需要输出的区域的左上角y坐标。异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sw | double | Yes | 需要输出的区域的宽度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| sh | double | Yes | 需要输出的区域的高度。异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 新的PixelMap对象。 |

## getTransform

```TypeScript
getTransform(): Matrix2D
```

获取当前被应用到上下文的转换矩阵。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getTransform(): Matrix2D--><!--Device-CanvasRenderer-getTransform(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) | 当前被应用到上下文的转换矩阵。 |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-measureText(text: string): TextMetrics--><!--Device-CanvasRenderer-measureText(text: string): TextMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 需要进行测量的文本。传入异常值undefined或null时按"undefined"或"null"计算。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextMetrics](arkts-arkui-canvas-textmetrics-i.md) | 文本的尺寸信息。 |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string): void
```

使用ImageData数据填充新的矩形区域。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string): void--><!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes | 包含像素值的ImageData对象。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | double \| string | Yes | 填充区域在x轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dy | double \| string | Yes | 填充区域在y轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,
    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void
```

使用ImageData数据裁剪后填充至新的矩形区域。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void--><!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes | 包含像素值的ImageData对象。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | double \| string | Yes | 填充区域在x轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dy | double \| string | Yes | 填充区域在y轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dirtyX | double \| string | Yes | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dirtyY | double \| string | Yes | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dirtyWidth | double \| string | Yes | 源图像数据矩形裁切范围的宽度。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |
| dirtyHeight | double \| string | Yes | 源图像数据矩形裁切范围的高度。 异常值undefined、null、NaN和Infinity按0处理。默认单位：vp |

## reset

```TypeScript
reset(): void
```

将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-reset(): void--><!--Device-CanvasRenderer-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetTransform

```TypeScript
resetTransform(): void
```

使用单位矩阵重新设置当前矩阵。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-resetTransform(): void--><!--Device-CanvasRenderer-resetTransform(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

恢复保存的绘图上下文。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-restore(): void--><!--Device-CanvasRenderer-restore(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restoreLayer

```TypeScript
restoreLayer(): void
```

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-restoreLayer(): void--><!--Device-CanvasRenderer-restoreLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: double): void
```

针对当前坐标轴进行顺时针旋转。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-rotate(angle: double): void--><!--Device-CanvasRenderer-rotate(angle: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | 设置顺时针旋转的弧度值，可以通过 degree Math.PI / 180 将角度转换为弧度值。 单位：弧度 |

## save

```TypeScript
save(): void
```

将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-save(): void--><!--Device-CanvasRenderer-save(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saveLayer

```TypeScript
saveLayer(): void
```

创建一个图层。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-saveLayer(): void--><!--Device-CanvasRenderer-saveLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: double, y: double): void
```

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-scale(x: double, y: double): void--><!--Device-CanvasRenderer-scale(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | 设置水平方向的缩放值。 |
| y | double | Yes | 设置垂直方向的缩放值。 |

## setLineDash

```TypeScript
setLineDash(segments: double[]): void
```

设置画布的虚线样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setLineDash(segments: double[]): void--><!--Device-CanvasRenderer-setLineDash(segments: double[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segments | double[] | Yes | 描述线段如何交替和线段间距长度的数组。 异常值undefined或null按无效值处理。默认单位：vp |

## setPixelMap

```TypeScript
setPixelMap(value?: PixelMap): void
```

将当前传入PixelMap对象绘制在画布上。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void--><!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | No | 包含像素值的PixelMap对象。 异常值undefined和null按无效值处理，不进行绘制。默认值：null |

## setTransform

```TypeScript
setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void--><!--Device-CanvasRenderer-setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| a | double | Yes | scaleX：指定水平缩放值，支持设置负数。 |
| b | double | Yes | skewY：指定垂直倾斜值，支持设置负数。 |
| c | double | Yes | skewX：指定水平倾斜值，支持设置负数。 |
| d | double | Yes | scaleY：指定垂直缩放值，支持设置负数。 |
| e | double | Yes | translateX：指定水平移动值，支持设置负数。默认单位：vp |
| f | double | Yes | translateY：指定垂直移动值，支持设置负数。默认单位：vp |

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void--><!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | 变换矩阵。异常值undefined或null按无效值处理。默认值：null |

## stroke

```TypeScript
stroke(path?: Path2D): void
```

根据指定的路径，进行边框绘制操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-stroke(path?: Path2D): void--><!--Device-CanvasRenderer-stroke(path?: Path2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | No | 需要绘制的Path2D。异常值undefined或null按无效值处理，不进行绘制。 |

## strokeRect

```TypeScript
strokeRect(x: double, y: double, w: double, h: double): void
```

绘制具有边框的矩形，矩形内部不填充。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-strokeRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-strokeRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | 指定矩形的左上角x坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| y | double | Yes | 指定矩形的左上角y坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| w | double | Yes | 指定矩形的宽度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| h | double | Yes | 指定矩形的高度。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |

## strokeText

```TypeScript
strokeText(text: string, x: double, y: double, maxWidth?: double): void
```

绘制描边类文本。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-strokeText(text: string, x: double, y: double, maxWidth?: double): void--><!--Device-CanvasRenderer-strokeText(text: string, x: double, y: double, maxWidth?: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 需要绘制的文本内容。异常值undefined或null按无效值处理，不进行绘制。 |
| x | double | Yes | 文本绘制起点的x轴坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| y | double | Yes | 文本绘制起点的y轴坐标。异常值undefined、null、NaN或Infinity按无效值处理， 不进行绘制。默认单位：vp |
| maxWidth | double | No | 需要绘制的文本的最大宽度。异常值null按无效值处理，不进行绘制， undefined、NaN或Infinity按默认值处理。默认单位：vp。默认值：不限制宽度。 |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

显示给定的ImageBitmap对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void--><!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes | 待显示的ImageBitmap对象。 |

## transform

```TypeScript
transform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-transform(a: double, b: double, c: double, d: double, e: double, f: double): void--><!--Device-CanvasRenderer-transform(a: double, b: double, c: double, d: double, e: double, f: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| a | double | Yes | 变换矩阵中第一行第一列的单元格。scaleX：指定水平缩放值，支持设置负数。 |
| b | double | Yes | 变换矩阵第二行第一列的单元格。skewY：指定垂直倾斜值，支持设置负数。 |
| c | double | Yes | 变换矩阵第一行第二列的单元格。skewX：指定水平倾斜值，支持设置负数。 |
| d | double | Yes | 变换矩阵第二行第二列的单元格。scaleY：指定垂直缩放值，支持设置负数。 |
| e | double | Yes | 变换矩阵第一行第三列的单元格。translateX：指定水平移动值， 支持设置负数。默认单位：vp |
| f | double | Yes | 变换矩阵第二行第三列的单元格。translateY：指定垂直移动值， 支持设置负数。默认单位：vp |

## translate

```TypeScript
translate(x: double, y: double): void
```

移动当前坐标系的原点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-translate(x: double, y: double): void--><!--Device-CanvasRenderer-translate(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | 设置水平平移量。默认单位：vp |
| y | double | Yes | 设置竖直平移量。默认单位：vp |

## antialias

```TypeScript
set antialias(antialias: boolean | undefined)
```

用于设置绘制图形和文本时是否开启抗锯齿。设置此接口会覆盖RenderingContextSettings中的抗锯齿效果，未通过该接口设置时，默认值为undefined，与RenderingContextSettings中的抗锯齿效果保持一致。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set antialias(antialias: boolean | undefined)--><!--Device-CanvasRenderer-set antialias(antialias: boolean | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
set direction(direction: CanvasDirection)
```

用于设置绘制文字时使用的文字方向。

**Type:** [CanvasDirection](arkts-arkui-canvasdirection-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set direction(direction: CanvasDirection)--><!--Device-CanvasRenderer-set direction(direction: CanvasDirection)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillStyle

```TypeScript
set fillStyle(fillStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

指定绘制的填充色，支持的颜色格式参考ResourceColor中string类型说明。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set fillStyle(fillStyle: string | Color | int | CanvasGradient | CanvasPattern)--><!--Device-CanvasRenderer-set fillStyle(fillStyle: string | Color | int | CanvasGradient | CanvasPattern)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## filter

```TypeScript
set filter(filter: string)
```

用于设置图像的滤镜，可以组合任意数量的滤镜。支持的滤镜效果如下：'none': 无滤镜效果。'blur(&lt;length&gt;)'：给图像设置高斯模糊，取值范围>=0，支持单位px、vp、rem，默认值：blur(0px)。'brightness([&lt;number&gt;|&lt;percentage&gt;])'：给图片应用一种线性乘法，使其看起来更亮或更暗， 支持数字和百分比参数，取值范围>=0，默认值：brightness(1)。'contrast([&lt;number&gt;|&lt;percentage&gt;])'：调整图像的对比度，支持数字和百分比参数， 取值范围>=0，默认值：contrast(1)。'grayscale([&lt;number&gt;|&lt;percentage&gt;])'：将图像转换为灰度图像，支持数字和百分比参数， 取值范围[0, 1]，默认值：grayscale(0)。'hue-rotate(&lt;angle&gt;)'：给图像应用色相旋转，取值范围0deg-360deg，默认值：hue-rotate(0deg)。'invert([&lt;number&gt;|&lt;percentage&gt;])'：反转输入图像，支持数字和百分比参数， 取值范围[0, 1]，默认值：invert(0)。'opacity([&lt;number&gt;|&lt;percentage&gt;])'：调整图像的透明程度，支持数字和百分比参数， 取值范围[0, 1]，默认值：opacity(1)。'saturate([&lt;number&gt;|&lt;percentage&gt;])'：转换图像饱和度，支持数字和百分比参数， 取值范围>=0，默认值：saturate(1)。'sepia([&lt;number&gt;|&lt;percentage&gt;])'：将图像转换为深褐色，支持数字和百分比参数， 取值范围[0, 1]，默认值：sepia(0)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set filter(filter: string)--><!--Device-CanvasRenderer-set filter(filter: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
set font(font: string)
```

设置文本绘制中的字体样式。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set font(font: string)--><!--Device-CanvasRenderer-set font(font: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalAlpha

```TypeScript
set globalAlpha(globalAlpha: double)
```

设置透明度，范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set globalAlpha(globalAlpha: double)--><!--Device-CanvasRenderer-set globalAlpha(globalAlpha: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalCompositeOperation

```TypeScript
set globalCompositeOperation(globalCompositeOperation: string)
```

设置合成操作的方式。支持的类型如下：source-over：在现有绘制内容上显示新绘制内容，属于默认值。source-atop：在现有绘制内容顶部显示新绘制内容。source-in：在现有绘制内容中显示新绘制内容。source-out：在现有绘制内容之外显示新绘制内容。destination-over：在新绘制内容上方显示现有绘制内容。destination-atop：在新绘制内容顶部显示现有绘制内容。destination-in：在新绘制内容中显示现有绘制内容。destination-out：在新绘制内容外显示现有绘制内容。lighter：显示新绘制内容和现有绘制内容。copy：显示新绘制内容而忽略现有绘制内容。xor：使用异或操作对新绘制内容与现有绘制内容进行融合。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set globalCompositeOperation(globalCompositeOperation: string)--><!--Device-CanvasRenderer-set globalCompositeOperation(globalCompositeOperation: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingEnabled

```TypeScript
set imageSmoothingEnabled(imageSmoothingEnabled: boolean)
```

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set imageSmoothingEnabled(imageSmoothingEnabled: boolean)--><!--Device-CanvasRenderer-set imageSmoothingEnabled(imageSmoothingEnabled: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingQuality

```TypeScript
set imageSmoothingQuality(imageSmoothingQuality: ImageSmoothingQuality)
```

imageSmoothingEnabled为true时，用于设置图像平滑度。

**Type:** [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set imageSmoothingQuality(imageSmoothingQuality: ImageSmoothingQuality)--><!--Device-CanvasRenderer-set imageSmoothingQuality(imageSmoothingQuality: ImageSmoothingQuality)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
set letterSpacing(letterSpacing: LengthMetrics | string)
```

用于指定绘制文本时字母之间的间距。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set letterSpacing(letterSpacing: LengthMetrics | string)--><!--Device-CanvasRenderer-set letterSpacing(letterSpacing: LengthMetrics | string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineCap

```TypeScript
set lineCap(lineCap: CanvasLineCap)
```

指定线端点的样式。

**Type:** [CanvasLineCap](arkts-arkui-canvaslinecap-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set lineCap(lineCap: CanvasLineCap)--><!--Device-CanvasRenderer-set lineCap(lineCap: CanvasLineCap)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineDashOffset

```TypeScript
set lineDashOffset(lineDashOffset: double)
```

设置画布的虚线偏移量。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set lineDashOffset(lineDashOffset: double)--><!--Device-CanvasRenderer-set lineDashOffset(lineDashOffset: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineJoin

```TypeScript
set lineJoin(lineJoin: CanvasLineJoin)
```

指定线段间相交的交点样式。

**Type:** [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set lineJoin(lineJoin: CanvasLineJoin)--><!--Device-CanvasRenderer-set lineJoin(lineJoin: CanvasLineJoin)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineWidth

```TypeScript
set lineWidth(lineWidth: double)
```

设置绘制线条的宽度。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set lineWidth(lineWidth: double)--><!--Device-CanvasRenderer-set lineWidth(lineWidth: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## miterLimit

```TypeScript
set miterLimit(miterLimit: double)
```

设置斜接面限制值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set miterLimit(miterLimit: double)--><!--Device-CanvasRenderer-set miterLimit(miterLimit: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowBlur

```TypeScript
set shadowBlur(shadowBlur: double)
```

设置绘制阴影时的模糊级别。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set shadowBlur(shadowBlur: double)--><!--Device-CanvasRenderer-set shadowBlur(shadowBlur: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
set shadowColor(shadowColor: string)
```

设置绘制阴影时的阴影颜色。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set shadowColor(shadowColor: string)--><!--Device-CanvasRenderer-set shadowColor(shadowColor: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetX

```TypeScript
set shadowOffsetX(shadowOffsetX: double)
```

设置绘制阴影时和原有对象的水平偏移值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set shadowOffsetX(shadowOffsetX: double)--><!--Device-CanvasRenderer-set shadowOffsetX(shadowOffsetX: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetY

```TypeScript
set shadowOffsetY(shadowOffsetY: double)
```

设置绘制阴影时和原有对象的垂直偏移值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set shadowOffsetY(shadowOffsetY: double)--><!--Device-CanvasRenderer-set shadowOffsetY(shadowOffsetY: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
set strokeStyle(strokeStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

设置线条的颜色，支持的颜色格式参考ResourceColor中string类型说明。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set strokeStyle(strokeStyle: string | Color | int | CanvasGradient | CanvasPattern)--><!--Device-CanvasRenderer-set strokeStyle(strokeStyle: string | Color | int | CanvasGradient | CanvasPattern)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
set textAlign(textAlign: CanvasTextAlign)
```

设置文本绘制中的文本对齐方式。

**Type:** [CanvasTextAlign](arkts-arkui-canvastextalign-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set textAlign(textAlign: CanvasTextAlign)--><!--Device-CanvasRenderer-set textAlign(textAlign: CanvasTextAlign)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBaseline

```TypeScript
set textBaseline(textBaseline: CanvasTextBaseline)
```

设置文本绘制中的水平对齐方式。

**Type:** [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-set textBaseline(textBaseline: CanvasTextBaseline)--><!--Device-CanvasRenderer-set textBaseline(textBaseline: CanvasTextBaseline)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

