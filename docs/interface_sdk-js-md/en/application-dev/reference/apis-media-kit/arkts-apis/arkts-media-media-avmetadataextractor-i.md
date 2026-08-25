# AVMetadataExtractor

AVMetadataExtractor is a class for metadata retrieval. It provides APIs to obtain metadata and thumbnails from media assets. Before calling any API of AVMetadataExtractor, you must use [media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md) to create an AVMetadataExtractor instance.For details about the demo of obtaining audio or video metadata and video thumbnails, see [Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](../../../media/media/avmetadataextractor.md).

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## cancelAllFetchFrames

```TypeScript
cancelAllFetchFrames(): void
```

Cancels the ongoing task of obtaining thumbnails in batches. (The thumbnails that have been obtained are not affected.)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## fetchAlbumCover

```TypeScript
fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void
```

Obtains the cover of the audio album. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |

## fetchAlbumCover

```TypeScript
fetchAlbumCover(): Promise<image.PixelMap>
```

Obtains the cover of the audio album. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchFrameByTimeWithTimeout

```TypeScript
fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,
      timeoutMs: number): Promise<image.PixelMap | undefined>
```

Obtains a video thumbnail. You can set the maximum timeout interval (**timeoutMs**) for obtaining the thumbnail. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |
| timeoutMs | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchFramesByTimes

```TypeScript
fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams,
        callback: OnFrameFetched): void
```

Obtains video thumbnails in batches. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The given video resource is decoded first, and then image frames are extracted from each time point in the
> **timesUs** array based on the provided **options** and **param**.&gt;
> - When each image extraction is complete, the system calls the callback function and passes the extraction
> result. Note that the execution order of the callback function may be inconsistent with the time points in the
> **timesUs** array.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timesUs | number[] | Yes |
| queryOption | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |
| callback | [OnFrameFetched](arkts-media-media-onframefetched-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchFramesByTimesWithTimeout

```TypeScript
fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams,
      timeoutMs: number, callback: OnFrameFetched): void
```

Obtains video thumbnails in batches. You can set the maximum timeout interval (**timeoutMs**) for obtaining each thumbnail. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The given video resource is decoded first, and then image frames are extracted from each time point in the
> **timesUs** array based on the provided **options** and **param**.&gt;
> - When each image extraction is complete, the system calls the callback function and passes the extraction
> result. Note that the execution order of the callback function may be inconsistent with the time points in the
> **timesUs** array.&gt;
> - The **timeoutMs** parameter indicates the maximum timeout interval for obtaining each thumbnail frame, not
> the entire batch thumbnail extraction process.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timesUs | number[] | Yes |
| queryOption | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |
| timeoutMs | number | Yes |
| callback | [OnFrameFetched](arkts-media-media-onframefetched-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchMetadata

```TypeScript
fetchMetadata(callback: AsyncCallback<AVMetadata>): void
```

Obtains the media metadata. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadata&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchMetadata

```TypeScript
fetchMetadata(): Promise<AVMetadata>
```

Obtains the media metadata. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AVMetadata & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## fetchMetadataWithTimeout

```TypeScript
fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata | undefined>
```

Obtains the media metadata. You can set the maximum timeout interval (**timeoutMs**) for obtaining the metadata. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeoutMs | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AVMetadata \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |
| [5411012](../errorcode-media.md#5411012-request-not-supported-due-to-http-plaintext-interception) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |

## release

```TypeScript
release(): Promise<void>
```

Releases this AVMetadataExtractor instance. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |

## setUrlSource

```TypeScript
setUrlSource(url: string, headers?: Record<string, string>): void
```

Sets the data source for a network on-demand resource. Only network metadata ([fetchMetadata](#fetchmetadata)) and thumbnails ([fetchFrameByTime](#fetchframebytime)) can be obtained. The media resource URL must be set before the retrieval.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| headers | Record & lt;string, string & gt; | No |

## dataSrc

```TypeScript
dataSrc ?: AVDataSrcDescriptor
```

Streaming media resource descriptor, which specifies the data source. Before obtaining metadata, you must set the data source through either **fdSrc** or **dataSrc**.When an application obtains a media file from the remote, you can set **dataSrc** to obtain the metadata before the application finishes the downloading.

**Type:** [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md)

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

## fdSrc

```TypeScript
fdSrc ?: AVFileDescriptor
```

Media file descriptor, which specifies the data source. Before obtaining metadata, you must set the data source through either **fdSrc** or **dataSrc**.There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.  
**NOTE：**After the resource handle (FD) is transferred to an AVMetadataExtractor instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVMetadataExtractor use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 11

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor
