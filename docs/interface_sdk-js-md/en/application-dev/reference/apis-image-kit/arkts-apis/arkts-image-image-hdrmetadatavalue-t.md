# HdrMetadataValue

```TypeScript
type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata
```

Describes the HDR metadata values used by a PixelMap, which corresponds to the values available for   
[HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md#HdrMetadataKey).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-image-type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata--><!--Device-image-type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

| Type | Description |
| --- | --- |
| HdrMetadataType | Metadata value corresponding to the **HDR_METADATA_TYPE** key in [HdrMetadataKey]{ |
| HdrStaticMetadata | Metadata value corresponding to the **HDR_STATIC_METADATA** key in [HdrMetadataKey]{ |
| ArrayBuffer | Metadata value corresponding to the **HDR_DYNAMIC_METADATA** key in [HdrMetadataKey]{ |
| HdrGainmapMetadata | Metadata value corresponding to the **HDR_GAINMAP_METADATA** key in [HdrMetadataKey]{ |

