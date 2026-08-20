# ImageBitmap

Bitmap image object that can be drawn onto the current Canvas

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ImageBitmap--><!--Device-unnamed-export declare class ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

Releases all graphics resources associated with an ImageBitmap.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBitmap-close(): void--><!--Device-ImageBitmap-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(src: PixelMap | string, unit?: LengthMetricsUnit)
```

Create an ImageBitmap object based on the transferred image path or PixelMap object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBitmap-constructor(src: PixelMap | string, unit?: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(src: PixelMap | string, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](arkts-arkui-pixelmap-t.md) \| string | Yes | image path or PixelMap object |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-lengthmetricsunit-t.md) | No | the unit mode |

## constructor

```TypeScript
constructor(src: Resource | PixelMap | string, unit?: LengthMetricsUnit)
```

Create an ImageBitmap object based on the transferred image path or PixelMap object or Resource object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageBitmap-constructor(src: Resource | PixelMap | string, unit?: LengthMetricsUnit)--><!--Device-ImageBitmap-constructor(src: Resource | PixelMap | string, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) \| string | Yes | image path or PixelMap object or Resource object |
| unit | [LengthMetricsUnit](../arkts-apis/arkts-arkui-lengthmetricsunit-t.md) | No | the unit mode |

