# OffscreenCanvasRenderingContext2D

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制， 绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区， 然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制， 绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。@extends CanvasRenderer

**继承/实现关系：** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvas-canvasrenderer-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数 和单位模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | double | 是 |
| height | double | 是 |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | 否 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | 否 |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: double): string
```

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 否 |
| quality | double | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap | undefined
```

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| undefined |
