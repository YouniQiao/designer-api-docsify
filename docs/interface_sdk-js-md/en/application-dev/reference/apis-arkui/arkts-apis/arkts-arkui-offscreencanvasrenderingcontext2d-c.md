# OffscreenCanvasRenderingContext2D

**Inheritance/Implementation:** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvasrenderer-c.md)

**ArkTS mode:** ArkTS-Dyn only

<!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer--><!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer-End-->

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings)
```

构造离屏Canvas画布对象，支持配置画布宽高和OffscreenCanvasRenderingContext2D对象的参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 离屏画布的宽度，默认单位：vp。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 |
| height | number | Yes | 离屏画布的高度，默认单位：vp。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | 用来配置OffscreenCanvasRenderingContext2D对象的参数， 见RenderingContextSettings接口描述。 &lt;br&gt;异常值undefined按RenderingContextSettings的默认值处理。 &lt;br&gt;默认值：null。 |

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 离屏画布的宽度，默认单位：vp。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 |
| height | number | Yes | 离屏画布的高度，默认单位：vp。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | 用来配置OffscreenCanvasRenderingContext2D对象的参数， 见RenderingContextSettings接口描述。 &lt;br&gt;异常值undefined按RenderingContextSettings的默认值处理。 &lt;br&gt;默认值：null。 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式， 配置后无法动态更改，配置方法同 [CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值undefined、NaN和Infinity按默认值处理。 &lt;br&gt;默认值：DEFAULT。 |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: any): string
```

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string--><!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | No | 用于指定图像格式。 &lt;br&gt;可选参数为："image/png"（无损压缩，适合需要精确像素的场景）、"image/jpeg"（有损压缩，适合照片类图像）、"image/webp"（高效压缩，适合网络传输场景）。 &lt;br&gt;异常值undefined或null按默认值处理。 &lt;br&gt;默认值：image/png |
| quality | any | No | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量，0-0.5适合快速传输或低带宽场景，0.6-0.8适合普通场景，0.9-1. 0适合高质量需求。如果超出取值范围，将会使用默认值0.92。 &lt;br&gt;异常值undefined、null、NaN和Infinity按默认值处理。 &lt;br&gt;默认值：0.92 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 图像的URL地址。 |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 存储离屏画布上渲染的像素数据。 |

