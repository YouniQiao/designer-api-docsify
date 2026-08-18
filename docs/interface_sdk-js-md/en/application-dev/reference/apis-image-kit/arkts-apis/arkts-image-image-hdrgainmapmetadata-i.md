# HdrGainmapMetadata

Describes the metadata keys used by a gain map, that is, the values available for **HDR_GAINMAP_METADATA** in [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md). For details, see ISO 21496-1.

**Since:** 23

<!--Device-image-interface HdrGainmapMetadata--><!--Device-image-interface HdrGainmapMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## alternateHeadroom

```TypeScript
alternateHeadroom: double
```

The alternate hdr headroom.

**Type:** double

**Since:** 23

<!--Device-HdrGainmapMetadata-alternateHeadroom: double--><!--Device-HdrGainmapMetadata-alternateHeadroom: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## baseHeadroom

```TypeScript
baseHeadroom: double
```

The baseline hdr headroom.

**Type:** double

**Since:** 23

<!--Device-HdrGainmapMetadata-baseHeadroom: double--><!--Device-HdrGainmapMetadata-baseHeadroom: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## channels

```TypeScript
channels: Array<GainmapChannel>
```

The per-channel metadata.

**Type:** Array&lt;[GainmapChannel](arkts-image-image-gainmapchannel-i.md)&gt;

**Since:** 23

<!--Device-HdrGainmapMetadata-channels: Array<GainmapChannel>--><!--Device-HdrGainmapMetadata-channels: Array<GainmapChannel>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gainmapChannelCount

```TypeScript
gainmapChannelCount: int
```

The number of gain map channels, with a value of 1 or 3.

**Type:** int

**Since:** 23

<!--Device-HdrGainmapMetadata-gainmapChannelCount: int--><!--Device-HdrGainmapMetadata-gainmapChannelCount: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## miniVersion

```TypeScript
miniVersion: int
```

The minimum version a parser needs to understand.

**Type:** int

**Since:** 23

<!--Device-HdrGainmapMetadata-miniVersion: int--><!--Device-HdrGainmapMetadata-miniVersion: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## useBaseColorFlag

```TypeScript
useBaseColorFlag: boolean
```

Indicate whether to use the color space of the base image.

**Type:** boolean

**Since:** 23

<!--Device-HdrGainmapMetadata-useBaseColorFlag: boolean--><!--Device-HdrGainmapMetadata-useBaseColorFlag: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## writerVersion

```TypeScript
writerVersion: int
```

The version used by the writer.

**Type:** int

**Since:** 23

<!--Device-HdrGainmapMetadata-writerVersion: int--><!--Device-HdrGainmapMetadata-writerVersion: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

