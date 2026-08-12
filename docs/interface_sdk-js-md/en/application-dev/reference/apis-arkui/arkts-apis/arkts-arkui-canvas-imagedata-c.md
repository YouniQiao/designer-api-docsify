# ImageData

Image data object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ImageData--><!--Device-unnamed-export declare class ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

Create an ImageData object based on the input parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)--><!--Device-ImageData-constructor(width: double, height: double, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | Width of the image. |
| height | double | Yes | Height of the image. |
| data | Uint8ClampedArray | No | Data of the image. If this parameter is not specified, the default value is a black rectangular image. |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | the unit mode |

## data

```TypeScript
get data(): Uint8ClampedArray | undefined
```

Array containing image pixel data

**Type:** Uint8ClampedArray

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-get data(): Uint8ClampedArray | undefined--><!--Device-ImageData-get data(): Uint8ClampedArray | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
get height(): int
```

Height of the image.

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

Width of the image.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageData-get width(): int--><!--Device-ImageData-get width(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

