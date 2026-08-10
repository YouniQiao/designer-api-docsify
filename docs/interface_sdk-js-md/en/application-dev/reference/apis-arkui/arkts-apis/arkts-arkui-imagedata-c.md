# ImageData

ImageData对象可以存储canvas渲染的像素数据。

> **说明：**
> 
> 创建ImageData时，宽高不超过16384px，最大面积不超过16000px*16000px，超过最大面积则无法正常绘制。
> 当创建面积超过536870911px时，返回值的width和height均为0px，data为undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class ImageData--><!--Device-unnamed-declare class ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray)
```

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray)--><!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 矩形区域宽度，默认单位为vp。 &lt;br&gt;异常值NaN和Infinity按0处理。 |
| height | number | Yes | 矩形区域高度，默认单位为vp。 &lt;br&gt;异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) | No | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 &lt;br&gt;传入异常值undefined时，data为undefined。 &lt;br/&gt;默认值：值全为0的一维数组。 |

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组，支持使用unit配置ImageData对象的单位模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)--><!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | 矩形区域宽度，默认单位为vp。 &lt;br&gt;异常值NaN和Infinity按0处理。 |
| height | number | Yes | 矩形区域高度，默认单位为vp。 &lt;br&gt;异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) | No | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 &lt;br&gt;传入异常值undefined时，data为undefined。 &lt;br/&gt;默认值：值全为0的一维数组。 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | 用来配置ImageData对象的单位模式，配置后无法动态更改， 配置方法同 [CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值undefined、NaN和Infinity按默认值处理。 &lt;br&gt;默认值：DEFAULT。 |

## data

```TypeScript
readonly data: Uint8ClampedArray
```

一维数组，保存了相应的颜色数据，数据值范围为0到255。

**Type:** [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly data: Uint8ClampedArray--><!--Device-ImageData-readonly data: Uint8ClampedArray-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
readonly height: number
```

矩形区域实际像素高度。&lt;br&gt;单位为px。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly height: number--><!--Device-ImageData-readonly height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

矩形区域实际像素宽度。&lt;br&gt;单位为px。

> **说明：**
> 
> 可使用[px2vp](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#px2vp12)
> 接口进行单位转换。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly width: number--><!--Device-ImageData-readonly width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

