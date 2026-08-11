# ImageBitmap

An **ImageBitmap** object stores pixel data rendered on a canvas. Since API version 11,when an application creates a  
[worker thread](../../../arkts-utils/worker-introduction.md), it can use **postMessage**to transfer the **ImageBitmap** instance to the worker thread for drawing, and use  
**onmessage** to receive the drawing results sent by the worker thread for display.

**Since:** 8

<!--Device-unnamed-declare class ImageBitmap--><!--Device-unnamed-declare class ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

Releases all graphics resources associated with this **ImageBitmap** object and sets its width and height to **0**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageBitmap-close(): void--><!--Device-ImageBitmap-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(src: string)
```

Creates an **ImageBitmap** object using an **ImageSrc** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageBitmap-constructor(src: string)--><!--Device-ImageBitmap-constructor(src: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |

## constructor

```TypeScript
constructor(src: string, unit: LengthMetricsUnit)
```

Creates an **ImageBitmap** object using an **ImageSrc** object. The unit mode of the Path2D object can be configured using **unit**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageBitmap-constructor(src: string, unit: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(src: string, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-graphics-lengthmetricsunit-e.md) | Yes |

## constructor

```TypeScript
constructor(data: PixelMap)
```

Creates an **ImageBitmap** object using a **PixelMap** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageBitmap-constructor(data: PixelMap)--><!--Device-ImageBitmap-constructor(data: PixelMap)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |

## constructor

```TypeScript
constructor(data: PixelMap, unit: LengthMetricsUnit)
```

Creates an **ImageBitmap** object using a **PixelMap** object. The unit mode of the Path2D object can be configured using **unit**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageBitmap-constructor(data: PixelMap, unit: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(data: PixelMap, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-graphics-lengthmetricsunit-e.md) | Yes |

## constructor

```TypeScript
constructor(data: Resource, unit?: LengthMetricsUnit)
```

Transfer a Resource object to construct an ImageBitmap object.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ImageBitmap-constructor(data: Resource, unit?: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(data: Resource, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-graphics-lengthmetricsunit-e.md) | No |

## height

```TypeScript
readonly height: number
```

Pixel height of the **ImageBitmap** object.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageBitmap-readonly height: number--><!--Device-ImageBitmap-readonly height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

Pixel width of the **ImageBitmap** object.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageBitmap-readonly width: number--><!--Device-ImageBitmap-readonly width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
