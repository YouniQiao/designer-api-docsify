# CanvasRenderer

Canvas渲染器，用于绘制形状、文本、图片等对象。@extends CanvasPath

**继承/实现关系：** CanvasRenderer extends [CanvasPath](arkts-arkui-canvas-canvaspath-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## beginPath

```TypeScript
beginPath(): void
```

创建一个新的绘制路径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clearRect

```TypeScript
clearRect(x: double, y: double, w: double, h: double): void
```

删除指定区域内的绘制内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| w | double | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | 是 |

## clip

```TypeScript
clip(fillRule?: CanvasFillRule): void
```

设置当前路径为剪切路径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | 否 |

## clip

```TypeScript
clip(path: Path2D, fillRule?: CanvasFillRule): void
```

设置指定路径为剪切路径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | 是 |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | 否 |

## createConicGradient

```TypeScript
createConicGradient(startAngle: double, x: double, y: double): CanvasGradient
```

创建一个圆锥渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startAngle | double | 是 |
| x | double | 是 |
| y | double | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## createImageData

```TypeScript
createImageData(sw: double, sh: double): ImageData
```

创建新的、空白的、指定大小的ImageData对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sw | double | 是 |
| sh | double | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## createLinearGradient

```TypeScript
createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient
```

创建一个线性渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x0 | double | 是 |
| y0 | double | 是 |
| x1 | double | 是 |
| y1 | double | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## createPattern

```TypeScript
createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null
```

通过指定图像和重复方式创建图片填充的模板。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 是 |
| repetition | string \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasPattern](arkts-arkui-canvas-canvaspattern-i.md) \| null |

## createRadialGradient

```TypeScript
createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient
```

创建一个径向渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x0 | double | 是 |
| y0 | double | 是 |
| r0 | double | 是 |
| x1 | double | 是 |
| y1 | double | 是 |
| r1 | double | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void
```

进行图像绘制。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |
| dx | double | 是 |
| dy | double | 是 |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void
```

将图像拉伸或压缩绘制。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |
| dx | double | 是 |
| dy | double | 是 |
| dw | double | 是 |
| dh | double | 是 |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,
    dw: double, dh: double): void
```

将图像裁剪后拉伸或压缩绘制。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |
| sx | double | 是 |
| sy | double | 是 |
| sw | double | 是 |
| sh | double | 是 |
| dx | double | 是 |
| dy | double | 是 |
| dw | double | 是 |
| dh | double | 是 |

## fill

```TypeScript
fill(fillRule?: CanvasFillRule): void
```

对当前路径进行填充。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | 否 |

## fill

```TypeScript
fill(path: Path2D, fillRule?: CanvasFillRule): void
```

对指定路径进行填充。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | 是 |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | 否 |

## fillRect

```TypeScript
fillRect(x: double, y: double, w: double, h: double): void
```

填充一个矩形。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| w | double | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | 是 |

## fillText

```TypeScript
fillText(text: string, x: double, y: double, maxWidth?: double): void
```

绘制填充类文本。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| x | double | 是 |
| y | double | 是 |
| maxWidth | double | 否 |

## getImageData

```TypeScript
getImageData(sx: double, sy: double, sw: double, sh: double): ImageData
```

以当前canvas指定区域内的像素创建ImageData对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | double | 是 |
| sy | double | 是 |
| sw | double | 是 |
| sh | double | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## getLineDash

```TypeScript
getLineDash(): double[]
```

获得当前画布的虚线样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| double[] |

## getPixelMap

```TypeScript
getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined
```

以当前canvas指定区域内的像素创建PixelMap对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | double | 是 |
| sy | double | 是 |
| sw | double | 是 |
| sh | double | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| undefined |

## getTransform

```TypeScript
getTransform(): Matrix2D
```

获取当前被应用到上下文的转换矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TextMetrics](arkts-arkui-canvas-textmetrics-i.md) |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string): void
```

使用ImageData数据填充新的矩形区域。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | 是 |
| dx | double \| string | 是 |
| dy | double \| string | 是 |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,
    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void
```

使用ImageData数据裁剪后填充至新的矩形区域。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | 是 |
| dx | double \| string | 是 |
| dy | double \| string | 是 |
| dirtyX | double \| string | 是 |
| dirtyY | double \| string | 是 |
| dirtyWidth | double \| string | 是 |
| dirtyHeight | double \| string | 是 |

## reset

```TypeScript
reset(): void
```

将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## resetTransform

```TypeScript
resetTransform(): void
```

使用单位矩阵重新设置当前矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

恢复保存的绘图上下文。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## restoreLayer

```TypeScript
restoreLayer(): void
```

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: double): void
```

针对当前坐标轴进行顺时针旋转。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | double | 是 |

## save

```TypeScript
save(): void
```

将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## saveLayer

```TypeScript
saveLayer(): void
```

创建一个图层。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: double, y: double): void
```

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

## setLineDash

```TypeScript
setLineDash(segments: double[]): void
```

设置画布的虚线样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| segments | double[] | 是 |

## setPixelMap

```TypeScript
setPixelMap(value?: PixelMap): void
```

将当前传入PixelMap对象绘制在画布上。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 否 |

## setTransform

```TypeScript
setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵 并创建新的变换矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| a | double | 是 |
| b | double | 是 |
| c | double | 是 |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | 是 |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | 是 |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | double | 是 |

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transform](#transform) | [Matrix2D](arkts-arkui-matrix2d-c.md) | 否 |

## stroke

```TypeScript
stroke(path?: Path2D): void
```

根据指定的路径，进行边框绘制操作。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | 否 |

## strokeRect

```TypeScript
strokeRect(x: double, y: double, w: double, h: double): void
```

绘制具有边框的矩形，矩形内部不填充。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| w | double | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | 是 |

## strokeText

```TypeScript
strokeText(text: string, x: double, y: double, maxWidth?: double): void
```

绘制描边类文本。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| x | double | 是 |
| y | double | 是 |
| maxWidth | double | 否 |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

显示给定的ImageBitmap对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 是 |

## transform

```TypeScript
transform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数， 对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| a | double | 是 |
| b | double | 是 |
| c | double | 是 |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | 是 |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | 是 |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | double | 是 |

## translate

```TypeScript
translate(x: double, y: double): void
```

移动当前坐标系的原点。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

## antialias

```TypeScript
set antialias(antialias: boolean | undefined)
```

用于设置绘制图形和文本时是否开启抗锯齿。设置此接口会覆盖RenderingContextSettings中的抗锯齿效果， 未通过该接口设置时，默认值为undefined，与RenderingContextSettings中的抗锯齿效果保持一致。

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
set direction(direction: CanvasDirection)
```

用于设置绘制文字时使用的文字方向。

**类型：** [CanvasDirection](arkts-arkui-canvasdirection-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fillStyle

```TypeScript
set fillStyle(fillStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

指定绘制的填充色，支持的颜色格式参考ResourceColor中string类型说明。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## filter

```TypeScript
set filter(filter: string)
```

用于设置图像的滤镜，可以组合任意数量的滤镜。支持的滤镜效果如下：'none': 无滤镜效果。'blur(&lt;length&gt;)'：给图像设置高斯模糊，取值范围&gt;=0，支持单位px、vp、rem，默认值：blur(0px)。'brightness([&lt;number&gt;|&lt;percentage&gt;])'：给图片应用一种线性乘法，使其看起来更亮或更暗， 支持数字和百分比参数，取值范围&gt;=0，默认值：brightness(1)。'contrast([&lt;number&gt;|&lt;percentage&gt;])'：调整图像的对比度，支持数字和百分比参数， 取值范围&gt;=0，默认值：contrast(1)。'grayscale([&lt;number&gt;|&lt;percentage&gt;])'：将图像转换为灰度图像，支持数字和百分比参数， 取值范围[0, 1]，默认值：grayscale(0)。'hue-rotate(&lt;angle&gt;)'：给图像应用色相旋转，取值范围0deg-360deg，默认值：hue-rotate(0deg)。'invert([&lt;number&gt;|&lt;percentage&gt;])'：反转输入图像，支持数字和百分比参数， 取值范围[0, 1]，默认值：invert(0)。'opacity([&lt;number&gt;|&lt;percentage&gt;])'：调整图像的透明程度，支持数字和百分比参数， 取值范围[0, 1]，默认值：opacity(1)。'saturate([&lt;number&gt;|&lt;percentage&gt;])'：转换图像饱和度，支持数字和百分比参数， 取值范围&gt;=0，默认值：saturate(1)。'sepia([&lt;number&gt;|&lt;percentage&gt;])'：将图像转换为深褐色，支持数字和百分比参数， 取值范围[0, 1]，默认值：sepia(0)。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
set font(font: string)
```

设置文本绘制中的字体样式。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## globalAlpha

```TypeScript
set globalAlpha(globalAlpha: double)
```

设置透明度，范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## globalCompositeOperation

```TypeScript
set globalCompositeOperation(globalCompositeOperation: string)
```

设置合成操作的方式。支持的类型如下： source-over：在现有绘制内容上显示新绘制内容，属于默认值。 source-atop：在现有绘制内容顶部显示新绘制内容。 source-in：在现有绘制内容中显示新绘制内容。 source-out：在现有绘制内容之外显示新绘制内容。 destination-over：在新绘制内容上方显示现有绘制内容。 destination-atop：在新绘制内容顶部显示现有绘制内容。 destination-in：在新绘制内容中显示现有绘制内容。 destination-out：在新绘制内容外显示现有绘制内容。 lighter：显示新绘制内容和现有绘制内容。 copy：显示新绘制内容而忽略现有绘制内容。 xor：使用异或操作对新绘制内容与现有绘制内容进行融合。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingEnabled

```TypeScript
set imageSmoothingEnabled(imageSmoothingEnabled: boolean)
```

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingQuality

```TypeScript
set imageSmoothingQuality(imageSmoothingQuality: ImageSmoothingQuality)
```

imageSmoothingEnabled为true时，用于设置图像平滑度。

**类型：** [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
set letterSpacing(letterSpacing: LengthMetrics | string)
```

用于指定绘制文本时字母之间的间距。

**类型：** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineCap

```TypeScript
set lineCap(lineCap: CanvasLineCap)
```

指定线端点的样式。

**类型：** [CanvasLineCap](arkts-arkui-canvaslinecap-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineDashOffset

```TypeScript
set lineDashOffset(lineDashOffset: double)
```

设置画布的虚线偏移量。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineJoin

```TypeScript
set lineJoin(lineJoin: CanvasLineJoin)
```

指定线段间相交的交点样式。

**类型：** [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineWidth

```TypeScript
set lineWidth(lineWidth: double)
```

设置绘制线条的宽度。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## miterLimit

```TypeScript
set miterLimit(miterLimit: double)
```

设置斜接面限制值。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowBlur

```TypeScript
set shadowBlur(shadowBlur: double)
```

设置绘制阴影时的模糊级别。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
set shadowColor(shadowColor: string)
```

设置绘制阴影时的阴影颜色。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetX

```TypeScript
set shadowOffsetX(shadowOffsetX: double)
```

设置绘制阴影时和原有对象的水平偏移值。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetY

```TypeScript
set shadowOffsetY(shadowOffsetY: double)
```

设置绘制阴影时和原有对象的垂直偏移值。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
set strokeStyle(strokeStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

设置线条的颜色，支持的颜色格式参考ResourceColor中string类型说明。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
set textAlign(textAlign: CanvasTextAlign)
```

设置文本绘制中的文本对齐方式。

**类型：** [CanvasTextAlign](arkts-arkui-canvastextalign-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textBaseline

```TypeScript
set textBaseline(textBaseline: CanvasTextBaseline)
```

设置文本绘制中的水平对齐方式。

**类型：** [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
