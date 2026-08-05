# HdrMetadataValue

```TypeScript
type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata
```

Describes the HDR metadata values used by a PixelMap, which corresponds to the values available for [HdrMetadataKey]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-image-type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata--><!--Device-image-type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

| Type | Description |
| --- | --- |
| HdrMetadataType | Metadata value corresponding to the **HDR\_METADATA\_TYPE** key in [HdrMetadataKey]{ |
| HdrStaticMetadata | Metadata value corresponding to the **HDR\_STATIC\_METADATA** key in [HdrMetadataKey]{ |
| ArrayBuffer | Metadata value corresponding to the **HDR\_DYNAMIC\_METADATA** key in [HdrMetadataKey]{ |
| HdrGainmapMetadata | Metadata value corresponding to the **HDR\_GAINMAP\_METADATA** key in [HdrMetadataKey]{ |

