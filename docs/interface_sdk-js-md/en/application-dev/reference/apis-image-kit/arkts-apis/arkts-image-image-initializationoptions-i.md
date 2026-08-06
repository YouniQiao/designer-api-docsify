# InitializationOptions

Defines PixelMap initialization options.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-image-interface InitializationOptions--><!--Device-image-interface InitializationOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## alphaType

```TypeScript
alphaType?: AlphaType
```

Alpha type. The default value is **IMAGE\_ALPHA\_TYPE\_PREMUL**.

**Type:** AlphaType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-alphaType?: AlphaType--><!--Device-InitializationOptions-alphaType?: AlphaType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## editable

```TypeScript
editable?: boolean
```

Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance. The default value is **false**.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-editable?: boolean--><!--Device-InitializationOptions-editable?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelFormat

```TypeScript
pixelFormat?: PixelMapFormat
```

Pixel format of the generated PixelMap. The default value is **RGBA\_8888**.

**Type:** PixelMapFormat

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-pixelFormat?: PixelMapFormat--><!--Device-InitializationOptions-pixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## scaleMode

```TypeScript
scaleMode?: ScaleMode
```

Scale mode. The default value is **0**.

**Type:** ScaleMode

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-scaleMode?: ScaleMode--><!--Device-InitializationOptions-scaleMode?: ScaleMode-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
size: Size
```

Image size.

**Type:** Size

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-InitializationOptions-size: Size--><!--Device-InitializationOptions-size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## srcPixelFormat

```TypeScript
srcPixelFormat?: PixelMapFormat
```

Pixel format of the passed-in buffer data. The default value is **BGRA\_8888**.

**Type:** PixelMapFormat

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InitializationOptions-srcPixelFormat?: PixelMapFormat--><!--Device-InitializationOptions-srcPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

