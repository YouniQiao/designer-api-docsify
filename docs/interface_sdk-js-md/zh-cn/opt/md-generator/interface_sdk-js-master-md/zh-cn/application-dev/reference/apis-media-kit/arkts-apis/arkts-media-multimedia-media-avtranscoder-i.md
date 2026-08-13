# AVTranscoder

视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过 [createAVTranscoder()](arkts-media-media-createavtranscoder-f.md#createAVTranscoder)构建一个AVTranscoder实例。 视频转码demo可参考：[视频转码开发指导](../../../media/media/using-avtranscoder-for-transcodering.md) > **说明：** > > - 本Interface首批接口从API version 12开始支持。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-interface AVTranscoder--><!--Device-unnamed-interface AVTranscoder-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>
```

add a watermark for the AVTranscoder. This API uses a promise to return the result. App can add up to 5 watermarks. This API can be called only before the prepared state.

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watermark | image.PixelMap | 是 |
| config | [WatermarkConfiguration](arkts-media-multimedia-media-watermarkconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## cancel

```TypeScript
cancel(): Promise<void>
```

取消视频转码。使用Promise异步回调。 需要在prepare()、start()、 pause()或resume()事件成功触发后，才能调用cancel方法。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-cancel(): Promise<void>--><!--Device-AVTranscoder-cancel(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## offComplete

```TypeScript
offComplete(callback?: Callback<void>):void
```

Unsubscribes from the event indicating that transcoding is complete. This event can be triggered by both user operations and the system.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void--><!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## offError

```TypeScript
offError(callback?: ErrorCallback):void
```

Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive AVTranscoder errors. This event is triggered when an error occurs during transcoding.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-offError(callback?: ErrorCallback):void--><!--Device-AVTranscoder-offError(callback?: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## offProgressUpdate

```TypeScript
offProgressUpdate(callback?: Callback<number>):void
```

Unsubscribes from transcoding progress updates. This event can be triggered by both user operations and the system.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void--><!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## off_complete

```TypeScript
off(type:'complete', callback?: Callback<void>):void
```

取消注册转码完成事件。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void--><!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off_error

```TypeScript
off(type:'error', callback?: ErrorCallback):void
```

取消注册转码错误事件，取消后不再接收到AVTranscoder的错误事件。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void--><!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off_progressUpdate

```TypeScript
off(type:'progressUpdate', callback?: Callback<number>):void
```

取消注册转码进度更新事件。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void--><!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressUpdate' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## onComplete

```TypeScript
onComplete(callback: Callback<void>):void
```

Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one transcoding completion event. When the application initiates multiple subscriptions to this event, the last subscription is applied. When this event is reported, the current transcoding operation is complete. You need to call [release()](#release) to exit the transcoding.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-onComplete(callback: Callback<void>):void--><!--Device-AVTranscoder-onComplete(callback: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## onError

```TypeScript
onError(callback: ErrorCallback):void
```

Subscribes to AVTranscoder errors. If this event is reported, call [release()](#release) to exit the transcoding. An application can subscribe to only one AVTranscoder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-onError(callback: ErrorCallback):void--><!--Device-AVTranscoder-onError(callback: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## onProgressUpdate

```TypeScript
onProgressUpdate(callback: Callback<number>):void
```

Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void--><!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on_complete

```TypeScript
on(type:'complete', callback: Callback<void>):void
```

注册转码完成事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。 当AVTranscoder上报complete事件时，当前转码操作已完成，开发者需要通过release()退出转码操作。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void--><!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on_error

```TypeScript
on(type:'error', callback: ErrorCallback):void
```

注册AVTranscoder的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，开发者需要通过release()退出转码操作 。使用callback异步回调。 开发者只能订阅一个错误事件的回调方法，当开发者重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void--><!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## on_progressUpdate

```TypeScript
on(type:'progressUpdate', callback: Callback<number>):void
```

注册转码进度更新事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。使用callback异步回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void--><!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressUpdate' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## pause

```TypeScript
pause(): Promise<void>
```

暂停视频转码。使用Promise异步回调。 需要start()事件成功触发后，才能调用pause方法，可以通过调用resume()接 口来恢复转码。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-pause(): Promise<void>--><!--Device-AVTranscoder-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## prepare

```TypeScript
prepare(config: AVTranscoderConfig): Promise<void>
```

进行视频转码的参数设置。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>--><!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AVTranscoderConfig](arkts-media-multimedia-media-avtranscoderconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(): Promise<void>
```

释放视频转码资源。使用Promise异步回调。 释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-release(): Promise<void>--><!--Device-AVTranscoder-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## resume

```TypeScript
resume(): Promise<void>
```

恢复视频转码。使用Promise异步回调。 需要在pause()事件成功触发后，才能调用resume方法。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-resume(): Promise<void>--><!--Device-AVTranscoder-resume(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## start

```TypeScript
start(): Promise<void>
```

开始视频转码。使用Promise异步回调。 需要prepare()事件成功触发后，才能调用start方法。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-start(): Promise<void>--><!--Device-AVTranscoder-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## fdDst

```TypeScript
fdDst: number
```

目标媒体文件描述，通过该属性设置数据输出。在创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。 **说明：** - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator /AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** number

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-fdDst: int--><!--Device-AVTranscoder-fdDst: int-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

源媒体文件描述，通过该属性设置数据源。 **使用示例**： 假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。 **说明：** - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator /AVTranscoder。 - 同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-AVTranscoder-fdSrc: AVFileDescriptor--><!--Device-AVTranscoder-fdSrc: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder
