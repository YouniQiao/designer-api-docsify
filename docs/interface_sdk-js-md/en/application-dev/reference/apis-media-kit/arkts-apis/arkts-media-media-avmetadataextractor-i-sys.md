# AVMetadataExtractor

AVMetadataExtractor is a class for metadata retrieval. It provides APIs to obtain metadata and thumbnails from media assets. Before calling any API of AVMetadataExtractor, you must use [media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md) to create an AVMetadataExtractor instance.For details about the demo of obtaining audio or video metadata and video thumbnails, see [Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](../../../media/media/avmetadataextractor.md).

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getFrameIndexByTime

```TypeScript
getFrameIndexByTime(timeUs: number): Promise<number>
```

Obtains the video frame number corresponding to a video timestamp. Only MP4 video files are supported.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |

## getTimeByFrameIndex

```TypeScript
getTimeByFrameIndex(index: number): Promise<number>
```

Obtains the video timestamp corresponding to a video frame number. Only MP4 video files are supported.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
