# ImageData

An **ImageData** object stores pixel data rendered on a canvas.

> **NOTE：**
> 
> A constructor used to create an **ImageData** object. To ensure successful drawing,
> make sure the object's area does not exceed 16000 x 16000, with its width and height
> not greater than 16384 px. If the created area exceeds 536870911 px, the returned
> width and height are both 0 px, and **data** is **undefined**.

**Since:** 8

<!--Device-unnamed-declare class ImageData--><!--Device-unnamed-declare class ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray)
```

Creates an **ImageData** object with the specified width, height, and color.If data is not defined, it is populated with a one-dimensional array of 0s.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray)--><!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | number | Yes |
| [height](#height) | number | Yes |
| [data](#data) | [Uint8ClampedArray](../../apis-default/arkts-apis/arkts-lib-es5-uint8clampedarray-i.md) | No |

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

Creates an **ImageData** object with the specified width, height, and color.If data is not defined, it is populated with a one-dimensional array of 0s.The unit of the **ImageData** object can be configured using **unit**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)--><!--Device-ImageData-constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | number | Yes |
| [height](#height) | number | Yes |
| [data](#data) | [Uint8ClampedArray](../../apis-default/arkts-apis/arkts-lib-es5-uint8clampedarray-i.md) | No |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-graphics-lengthmetricsunit-e.md) | No |

## data

```TypeScript
readonly data: Uint8ClampedArray
```

A one-dimensional array of color values. The values range from 0 to 255.

**Type:** [Uint8ClampedArray](../../apis-default/arkts-apis/arkts-lib-es5-uint8clampedarray-i.md)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly data: Uint8ClampedArray--><!--Device-ImageData-readonly data: Uint8ClampedArray-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
readonly height: number
```

Actual height of the rectangle on the canvas.

The unit is px.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly height: number--><!--Device-ImageData-readonly height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

Actual width of the rectangle on the canvas.

The unit is px.

> **NOTE：**
> 
> The [px2vp](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#px2vp)
> API can be used for unit conversion.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageData-readonly width: number--><!--Device-ImageData-readonly width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
