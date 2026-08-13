# ImageBitmap

ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建 [Worker线程](../../../arkts-utils/worker-introduction.md)，支持使用postMessage将ImageBitmap实例传到 Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare class ImageBitmap--><!--Device-unnamed-declare class ImageBitmap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。 > **说明：** > > - 必须与[constructor()](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-imagebitmap.md#constructor)方法配对 > 使用，创建ImageBitmap对象后，应在使用完毕时调用close()释放资源。未调用close()可能导致图形资源泄漏，影响应用性能。 > > - 建议在Canvas绘制完成后调用，如在onReady回调的最后调用close()。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-close(): void--><!--Device-ImageBitmap-close(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(src: string)
```

通过ImageSrc创建ImageBitmap对象。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-constructor(src: string)--><!--Device-ImageBitmap-constructor(src: string)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |

## constructor

```TypeScript
constructor(src: string, unit: LengthMetricsUnit)
```

通过ImageSrc创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-constructor(src: string, unit: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(src: string, unit: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | 是 |

## constructor

```TypeScript
constructor(data: PixelMap)
```

通过PixelMap创建ImageBitmap对象。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ImageBitmap-constructor(data: PixelMap)--><!--Device-ImageBitmap-constructor(data: PixelMap)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |

## constructor

```TypeScript
constructor(data: PixelMap, unit: LengthMetricsUnit)
```

通过PixelMap创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ImageBitmap-constructor(data: PixelMap, unit: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(data: PixelMap, unit: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) | 是 |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | 是 |

## constructor

```TypeScript
constructor(data: Resource, unit?: LengthMetricsUnit)
```

通过Resource创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**起始版本：** 26.0.0

**废弃版本：** -1

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-constructor(data: Resource, unit?: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(data: Resource, unit?: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | 否 |

## height

```TypeScript
readonly height: number
```

ImageBitmap的像素高度。 &lt;br&gt;默认单位为vp。

**类型：** number

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-readonly height: number--><!--Device-ImageBitmap-readonly height: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

ImageBitmap的像素宽度。 &lt;br&gt;默认单位为vp。

**类型：** number

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ImageBitmap-readonly width: number--><!--Device-ImageBitmap-readonly width: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
