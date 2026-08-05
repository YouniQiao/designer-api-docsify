# AVImageGenerator

AVImageGenerator is a class for video thumbnail retrieval. It provides APIs to obtain a thumbnail from a video. Before calling any API in AVImageGenerator, you must use [createAVImageGenerator()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to create an AVImageGenerator instance. For details about the demo for obtaining video thumbnails, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-media-interface AVImageGenerator--><!--Device-media-interface AVImageGenerator-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,
      callback: AsyncCallback<image.PixelMap>): void
```

Obtains a video thumbnail. This API uses an asynchronous callback to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Format parameters of the thumbnail to be obtained. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;image.PixelMap&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the PixelMap instance obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by callback. |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,
      callback: AsyncCallback<image.PixelMap | undefined>): void
```

Obtains a video thumbnail. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap | undefined>): void--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Relationship between the time passed in and the video frame. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Format parameters of the thumbnail to be obtained. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;image.PixelMap \| undefined&gt; | Yes | Callback used to return the result.If the operation is successful, **err** is **undefined** and **data** is the **PixelMap** instance obtained;otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by callback. |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Format parameters of the thumbnail to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | Time of the video for which a thumbnail is to be obtained, in μs. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Relationship between the time passed in and the video frame. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Format parameters of the thumbnail to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap \| undefined&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |

## fetchScaledFrameByTime

```TypeScript
fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):
      Promise<image.PixelMap>
```

Fetches a scaled thumbnail from the video at a particular timestamp. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | number | Yes | Timestamp, in microseconds (μs), at which the thumbnail is to be fetched from the video. |
| queryMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Relationship between the thumbnail timestamp in and the video frame. |
| outputSize | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Output size of the thumbnail. By default, the original image size is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise used to return the video thumbnail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |  |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |  |

## fetchScaledFrameByTime

```TypeScript
fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):
      Promise<image.PixelMap | undefined>
```

Supports extracting video thumbnails by proportional scaling

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap | undefined>--><!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: long, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeUs | long | Yes | The time expected to fetch picture from the video resource.The unit is microsecond(us). |
| queryMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Specify how to position the video frame |
| outputSize | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | This field is used to define the output size of frame. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap \| undefined&gt; | Returns the output image object |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |  |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |  |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this AVImageGenerator instance. This API uses an asynchronous callback to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void--><!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful,**err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by callback. |

## release

```TypeScript
release(): Promise<void>
```

Releases this AVImageGenerator instance. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVImageGenerator-release(): Promise<void>--><!--Device-AVImageGenerator-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Returned by promise. |

## fdSrc

```TypeScript
fdSrc ?: AVFileDescriptor
```

Media file descriptor, which specifies the data source. There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**. **NOTE** After the resource handle (FD) is transferred to an AVImageGenerator instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVImageGenerator use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** AVFileDescriptor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor--><!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

