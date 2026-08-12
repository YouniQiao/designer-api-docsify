# AVMetadataExtractor

AVMetadataExtractor is a class for metadata retrieval. It provides APIs to obtain metadata and thumbnails from media assets. Before calling any API of AVMetadataExtractor, you must use   
[media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md#createAVMetadataExtractor)to create an AVMetadataExtractor instance.

For details about the demo of obtaining audio or video metadata and video thumbnails, see   
[Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](../../../media/media/avmetadataextractor.md).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-media-interface AVMetadataExtractor--><!--Device-media-interface AVMetadataExtractor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## getFrameIndexByTime

ArkTS-Dyn:
```TypeScript
getFrameIndexByTime(timeUs: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
getFrameIndexByTime(timeUs: long): Promise<int>
```

Obtains the video frame number corresponding to a video timestamp. Only MP4 video files are supported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVMetadataExtractor-getFrameIndexByTime(timeUs: long): Promise<int>--><!--Device-AVMetadataExtractor-getFrameIndexByTime(timeUs: long): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Video timestamp, in microseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the video frame number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

## Examples

```TypeScript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

avMetadataExtractor.getFrameIndexByTime(0).then((index: number) => {
  console.info(`Succeeded getFrameIndexByTime index: ${index}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getFrameIndexByTime ${err.message}`);
})
```

## getTimeByFrameIndex

ArkTS-Dyn:
```TypeScript
getTimeByFrameIndex(index: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
getTimeByFrameIndex(index: int): Promise<long>
```

Obtains the video timestamp corresponding to a video frame number. Only MP4 video files are supported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVMetadataExtractor-getTimeByFrameIndex(index: int): Promise<long>--><!--Device-AVMetadataExtractor-getTimeByFrameIndex(index: int): Promise<long>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Video frame number. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise used to return the timestamp, in microseconds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Return by promise. |
| [5400102](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

## Examples

```TypeScript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

avMetadataExtractor.getTimeByFrameIndex(0).then((timeUs: number) => {
  console.info(`Succeeded getTimeByFrameIndex timeUs: ${timeUs}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTimeByFrameIndex ${err.message}`);
})
```

