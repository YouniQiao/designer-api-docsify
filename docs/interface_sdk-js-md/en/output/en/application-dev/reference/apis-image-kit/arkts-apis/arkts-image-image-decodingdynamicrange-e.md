# DecodingDynamicRange

Enumerates the desired dynamic range of an image during decoding.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-image-enum DecodingDynamicRange--><!--Device-image-enum DecodingDynamicRange-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AUTO

```TypeScript
AUTO = 0
```

The image is decoded based on the format. If the image is in HDR format, it is decoded based on the HDR content; otherwise, it is decoded based on the SDR content. The image source created by calling [CreateIncrementalSource]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is decoded into SDR content.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DecodingDynamicRange-AUTO = 0--><!--Device-DecodingDynamicRange-AUTO = 0-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SDR

```TypeScript
SDR = 1
```

The image is decoded according to the standard dynamic range.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DecodingDynamicRange-SDR = 1--><!--Device-DecodingDynamicRange-SDR = 1-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## HDR

```TypeScript
HDR = 2
```

The image is decoded according to the high dynamic range. The image source created by calling [CreateIncrementalSource]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is decoded into SDR content.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DecodingDynamicRange-HDR = 2--><!--Device-DecodingDynamicRange-HDR = 2-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

