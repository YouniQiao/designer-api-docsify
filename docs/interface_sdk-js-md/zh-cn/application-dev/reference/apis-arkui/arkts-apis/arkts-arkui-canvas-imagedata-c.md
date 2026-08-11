# ImageData

ImageData对象可以存储canvas渲染的像素数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ImageData--><!--Device-unnamed-export declare class ImageData-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组，支持使用unit配置ImageData对象的单位模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)--><!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | double | 是 | 矩形区域宽度，默认单位为vp。&lt;br&gt;异常值NaN和Infinity按0处理。 |
| height | double | 是 | 矩形区域高度，默认单位为vp。&lt;br&gt;异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-collections-uint8clampedarray-c.md) | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 &lt;br&gt;传入异常值undefined时，data为undefined。&lt;br&gt;默认值：值全为0的一维数组 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | 否 | 用来配置ImageData对象的单位模式，配置后无法动态更改， 配置方法同[CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值undefined、NaN和Infinity按默认值处理。&lt;br&gt;默认值：DEFAULT |

## data

```TypeScript
get data(): Uint8ClampedArray | undefined
```

一维数组，保存了相应的颜色数据，数据值范围为0到255。

**类型：** [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-collections-uint8clampedarray-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageData-get data(): Uint8ClampedArray | undefined--><!--Device-ImageData-get data(): Uint8ClampedArray | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
get height(): int
```

矩形区域实际像素高度。&lt;br&gt;单位为px。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageData-get height(): int--><!--Device-ImageData-get height(): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
get width(): int
```

矩形区域实际像素宽度。&lt;br&gt;单位为px。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageData-get width(): int--><!--Device-ImageData-get width(): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

