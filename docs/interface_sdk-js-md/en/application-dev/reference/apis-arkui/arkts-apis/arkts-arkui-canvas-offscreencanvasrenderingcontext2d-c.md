# OffscreenCanvasRenderingContext2D

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

**Inheritance/Implementation:** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvasrenderer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer--><!--Device-unnamed-export declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | 离屏画布的宽度，默认单位：vp。 异常值NaN和Infinity按无效值处理。 |
| height | double | Yes | 离屏画布的高度，默认单位：vp。 异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | 用来配置OffscreenCanvasRenderingContext2D 对象的参数，见RenderingContextSettings。 异常值undefined按RenderingContextSettings的默认值处理。默认值：null。 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式， 配置后无法动态更改。异常值undefined、NaN和Infinity按默认值处理。默认值：DEFAULT。 |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: double): string
```

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string--><!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | No | 用于指定图像格式。可选参数为："image/png"，"image/jpeg"， "image/webp"。异常值undefined或null按默认值处理。默认值：image/png。 |
| quality | double | No | 在指定图片格式为image/jpeg或image/webp的情况下， 可以从0到1的区间内选择图片的质量。如果超出取值范围， 将会使用默认值0.92。异常值undefined、null、NaN和Infinity按默认值处理。 默认值：0.92。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 图像的URL地址。 |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap | undefined
```

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap | undefined--><!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 存储离屏画布上渲染的像素数据。 |

