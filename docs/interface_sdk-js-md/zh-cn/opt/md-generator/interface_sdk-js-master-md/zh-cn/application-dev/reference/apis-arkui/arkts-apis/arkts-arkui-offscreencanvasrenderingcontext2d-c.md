# OffscreenCanvasRenderingContext2D

**继承/实现关系：** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvasrenderer-c.md#CanvasRenderer)

**起始版本：** -1

**废弃版本：** -1

<!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D--><!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D-End-->

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings)
```

构造离屏Canvas画布对象，支持配置画布宽高和OffscreenCanvasRenderingContext2D对象的参数。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | 否 |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: any): string
```

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string--><!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 否 |
| quality | any | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) |
