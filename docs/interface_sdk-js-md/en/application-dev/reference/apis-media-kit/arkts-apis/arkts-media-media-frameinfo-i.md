# FrameInfo

Defines the frame info when fetch picture form a video.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-media-interface FrameInfo--><!--Device-media-interface FrameInfo-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## actualTimeUs

```TypeScript
actualTimeUs?: long
```

The actual frame time.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameInfo-actualTimeUs?: long--><!--Device-FrameInfo-actualTimeUs?: long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## image

```TypeScript
image?: image.PixelMap
```

The image extracted from video.

**Type:** image.PixelMap

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameInfo-image?: image.PixelMap--><!--Device-FrameInfo-image?: image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## requestedTimeUs

```TypeScript
requestedTimeUs: long
```

The requested frame time.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameInfo-requestedTimeUs: long--><!--Device-FrameInfo-requestedTimeUs: long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## result

```TypeScript
result: FetchResult
```

The fetch result code - succeed, failed or cancelled.

**Type:** FetchResult

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameInfo-result: FetchResult--><!--Device-FrameInfo-result: FetchResult-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

