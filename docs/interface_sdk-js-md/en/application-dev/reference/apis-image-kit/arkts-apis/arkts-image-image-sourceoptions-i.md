# SourceOptions

Defines image source initialization options.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-image-interface SourceOptions--><!--Device-image-interface SourceOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourceDensity

```TypeScript
sourceDensity: int
```

Pixel density of the image resource, in ppi.

If **desiredSize** is not set in [DecodingOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and  
**SourceOptions.sourceDensity** and **DecodingOptions.fitDensity** are not 0, the PixelMap output after decoding will be scaled.

The formula for calculating the width after scaling is as follows (the same applies to the height): (width *  
fitDensity + (sourceDensity >  
    1)) / sourceDensity.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourceDensity: int--><!--Device-SourceOptions-sourceDensity: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourcePixelFormat

```TypeScript
sourcePixelFormat?: PixelMapFormat
```

Image pixel format. The default value is **UNKNOWN**.

**Type:** PixelMapFormat

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourcePixelFormat?: PixelMapFormat--><!--Device-SourceOptions-sourcePixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourceSize

```TypeScript
sourceSize?: Size
```

Image pixel size. The default value is null.

**Type:** Size

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourceSize?: Size--><!--Device-SourceOptions-sourceSize?: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

