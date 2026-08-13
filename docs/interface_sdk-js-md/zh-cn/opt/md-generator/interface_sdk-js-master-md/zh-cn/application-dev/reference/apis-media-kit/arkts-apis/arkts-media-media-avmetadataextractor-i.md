# AVMetadataExtractor

元数据获取类，用于从媒体资源中获取元数据、缩略图。在调用AVMetadataExtractor的方法前，需要先通过 [media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md#createAVMetadataExtractor) 构建一个AVMetadataExtractor实例。 获取音频或视频元数据、视频缩略图的demo可参考：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](../../../media/media/avmetadataextractor.md)。 > **说明：** > > - 本Interface首批接口从API version 11开始支持。

**起始版本：** 23

**废弃版本：** -1

<!--Device-media-interface AVMetadataExtractor--><!--Device-media-interface AVMetadataExtractor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

## cancelAllFetchFrames

```TypeScript
cancelAllFetchFrames(): void
```

取消正在进行的批量获取缩略图任务（已完成部分不受影响）。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMetadataExtractor-cancelAllFetchFrames(): void--><!--Device-AVMetadataExtractor-cancelAllFetchFrames(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

## fetchAlbumCover

```TypeScript
fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void
```

获取音频专辑封面。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void--><!--Device-AVMetadataExtractor-fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchAlbumCover

```TypeScript
fetchAlbumCover(callback: AsyncCallback<image.PixelMap | undefined>): void
```

Obtains the cover of the audio album. This API uses an asynchronous callback to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchAlbumCover(callback: AsyncCallback<image.PixelMap | undefined>): void--><!--Device-AVMetadataExtractor-fetchAlbumCover(callback: AsyncCallback<image.PixelMap | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap \| undefined & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchAlbumCover

```TypeScript
fetchAlbumCover(): Promise<image.PixelMap>
```

获取专辑封面。使用Promise异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchAlbumCover(): Promise<image.PixelMap>--><!--Device-AVMetadataExtractor-fetchAlbumCover(): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchAlbumCover

```TypeScript
fetchAlbumCover(): Promise<image.PixelMap | undefined>
```

Obtains the cover of the audio album. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchAlbumCover(): Promise<image.PixelMap | undefined>--><!--Device-AVMetadataExtractor-fetchAlbumCover(): Promise<image.PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>
```

获取视频缩略图。使用Promise异步回调。

**起始版本：** 20

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>--><!--Device-AVMetadataExtractor-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeUs | number | 是 |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | 是 |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>
```

It will decode the given video resource. Then fetch a picture at @timeUs according the given @options and @param .

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>--><!--Device-AVMetadataExtractor-fetchFrameByTime(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeUs | number | 是 |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | 是 |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## fetchFrameByTimeWithTimeout

```TypeScript
fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,
      timeoutMs: number): Promise<image.PixelMap | undefined>
```

获取视频缩略图，支持设置缩略图获取最大耗时timeoutMs。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMetadataExtractor-fetchFrameByTimeWithTimeout(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      timeoutMs: long): Promise<image.PixelMap | undefined>--><!--Device-AVMetadataExtractor-fetchFrameByTimeWithTimeout(timeUs: long, options: AVImageQueryOptions, param: PixelMapParams,      timeoutMs: long): Promise<image.PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeUs | number | 是 |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | 是 |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | 是 |
| [timeoutMs](../../apis-ability-kit/arkts-apis/arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## fetchFramesByTimes

```TypeScript
fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams,
        callback: OnFrameFetched): void
```

批量获取视频缩略图。使用Callback异步回调。 > **说明：** > > - 先对给定的视频资源进行解码，随后依据提供的参数options和param，从timesUs数组中的每个时间点提取图像帧。 > > - 当每一次图像提取完成时，系统将调用回调函数并传递提取结果。请注意，回调函数的执行顺序会与timesUs数组中时间点的先后顺序不一致。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMetadataExtractor-fetchFramesByTimes(timesUs: long[], queryOption: AVImageQueryOptions, param: PixelMapParams,        callback: OnFrameFetched): void--><!--Device-AVMetadataExtractor-fetchFramesByTimes(timesUs: long[], queryOption: AVImageQueryOptions, param: PixelMapParams,        callback: OnFrameFetched): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timesUs | number[] | 是 |
| queryOption | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | 是 |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | 是 |
| callback | [OnFrameFetched](arkts-media-media-onframefetched-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## fetchFramesByTimesWithTimeout

```TypeScript
fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams,
      timeoutMs: number, callback: OnFrameFetched): void
```

批量获取视频缩略图，支持设置每一帧缩略图获取最大耗时timeoutMs。使用Callback异步回调。 > **说明：** > > - 先对给定的视频资源进行解码，随后依据提供的参数options和param，从timesUs数组中的每个时间点提取图像帧。 > > - 当每一次图像提取完成时，系统将调用回调函数并传递提取结果。请注意，回调函数的执行顺序会与timesUs数组中时间点的先后顺序不一致。 > > - 超时时间timeoutMs是针对每一帧的获取时间，而非整个批量抽帧流程。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMetadataExtractor-fetchFramesByTimesWithTimeout(timesUs: long[], queryOption: AVImageQueryOptions, param: PixelMapParams,      timeoutMs: long, callback: OnFrameFetched): void--><!--Device-AVMetadataExtractor-fetchFramesByTimesWithTimeout(timesUs: long[], queryOption: AVImageQueryOptions, param: PixelMapParams,      timeoutMs: long, callback: OnFrameFetched): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timesUs | number[] | 是 |
| queryOption | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | 是 |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | 是 |
| [timeoutMs](../../apis-ability-kit/arkts-apis/arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | number | 是 |
| callback | [OnFrameFetched](arkts-media-media-onframefetched-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## fetchMetadata

```TypeScript
fetchMetadata(callback: AsyncCallback<AVMetadata>): void
```

获取媒体元数据。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchMetadata(callback: AsyncCallback<AVMetadata>): void--><!--Device-AVMetadataExtractor-fetchMetadata(callback: AsyncCallback<AVMetadata>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadata&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchMetadata

```TypeScript
fetchMetadata(callback: AsyncCallback<AVMetadata | undefined>): void
```

Obtains media metadata. This API uses an asynchronous callback to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchMetadata(callback: AsyncCallback<AVMetadata | undefined>): void--><!--Device-AVMetadataExtractor-fetchMetadata(callback: AsyncCallback<AVMetadata | undefined>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadata \| undefined & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchMetadata

```TypeScript
fetchMetadata(): Promise<AVMetadata>
```

获取媒体元数据。使用Promise异步回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchMetadata(): Promise<AVMetadata>--><!--Device-AVMetadataExtractor-fetchMetadata(): Promise<AVMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise & lt;AVMetadata & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchMetadata

```TypeScript
fetchMetadata(): Promise<AVMetadata | undefined>
```

Obtains media metadata. This API uses a promise to return the result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fetchMetadata(): Promise<AVMetadata | undefined>--><!--Device-AVMetadataExtractor-fetchMetadata(): Promise<AVMetadata | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise & lt;AVMetadata \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

## fetchMetadataWithTimeout

```TypeScript
fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata | undefined>
```

获取媒体元数据，支持设置获取最大耗时timeoutMs。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVMetadataExtractor-fetchMetadataWithTimeout(timeoutMs: long): Promise<AVMetadata | undefined>--><!--Device-AVMetadataExtractor-fetchMetadataWithTimeout(timeoutMs: long): Promise<AVMetadata | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [timeoutMs](../../apis-ability-kit/arkts-apis/arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;AVMetadata \ | undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5411012](../errorcode-media.md#5411012-http明文拦截导致请求不受支持) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放资源。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-release(callback: AsyncCallback<void>): void--><!--Device-AVMetadataExtractor-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |

## release

```TypeScript
release(): Promise<void>
```

释放资源。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-release(): Promise<void>--><!--Device-AVMetadataExtractor-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |

## setUrlSource

```TypeScript
setUrlSource(url: string, headers?: Record<string, string>): void
```

网络点播资源地址描述，通过该接口设置数据源。只支持获取网络 [fetchMetadata](#fetchMetadata)（元数据）和 [fetchFrameByTime](#fetchFrameByTime) （缩略图），在获取之前，必须设置媒体资源URL。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-setUrlSource(url: string, headers?: Record<string, string>): void--><!--Device-AVMetadataExtractor-setUrlSource(url: string, headers?: Record<string, string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| headers | Record & lt;string, string & gt; | 否 |

## dataSrc

```TypeScript
dataSrc ?: AVDataSrcDescriptor
```

流式媒体资源描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。 当应用从远端获取音视频媒体文件，在应用未下载完整音视频资源时，可以设置dataSrc提前获取该资源的元数据。

**类型：** [AVDataSrcDescriptor](arkts-media-multimedia-media-avdatasrcdescriptor-i.md)

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-dataSrc ?: AVDataSrcDescriptor--><!--Device-AVMetadataExtractor-dataSrc ?: AVDataSrcDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

## fdSrc

```TypeScript
fdSrc ?: AVFileDescriptor
```

媒体文件描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。 **使用示例**： 假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。 **说明：** 将资源句柄（fd）传递给AVMetadataExtractor实例之后，不允许通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/ AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致音视频元数据获取异常。

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVMetadataExtractor-fdSrc ?: AVFileDescriptor--><!--Device-AVMetadataExtractor-fdSrc ?: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor
