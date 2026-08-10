# ImageData

ImageData对象可以存储canvas渲染的像素数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ImageData--><!--Device-unnamed-export declare class ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组，支持使用unit配置ImageData对象的单位模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)--><!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | 矩形区域宽度，默认单位为vp。&lt;br&gt;异常值NaN和Infinity按0处理。 |
| height | double | Yes | 矩形区域高度，默认单位为vp。&lt;br&gt;异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) | No | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 &lt;br&gt;传入异常值undefined时，data为undefined。&lt;br&gt;默认值：值全为0的一维数组 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | 用来配置ImageData对象的单位模式，配置后无法动态更改， 配置方法同[CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值undefined、NaN和Infinity按默认值处理。&lt;br&gt;默认值：DEFAULT |

## data

```TypeScript
get data(): Uint8ClampedArray | undefined
```

一维数组，保存了相应的颜色数据，数据值范围为0到255。

**Type:** [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-get data(): Uint8ClampedArray | undefined--><!--Device-ImageData-get data(): Uint8ClampedArray | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
get height(): int
```

矩形区域实际像素高度。&lt;br&gt;单位为px。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-get height(): int--><!--Device-ImageData-get height(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
get width(): int
```

矩形区域实际像素宽度。&lt;br&gt;单位为px。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-get width(): int--><!--Device-ImageData-get width(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

