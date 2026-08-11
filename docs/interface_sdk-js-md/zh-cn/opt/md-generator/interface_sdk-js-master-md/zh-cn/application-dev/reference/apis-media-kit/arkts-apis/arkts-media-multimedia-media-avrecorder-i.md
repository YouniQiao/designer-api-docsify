# AVRecorder

音视频录制管理类，用于音视频媒体录制。在调用AVRecorder的方法前，需要先调用  
[createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder)接口构建一个AVRecorder实例。

音视频录制demo可参考：[音频录制开发指导](../../../media/media/using-avrecorder-for-recording.md)、  
[视频录制开发指导](../../../media/media/video-recording.md)。

> **说明：**
> 
> - 本Interface首批API从API version 9开始支持。
> 
> - 相机视频录制功能需配合相机模块使用，相机模块接口的使用详情请参考[相机管理](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md/arkts-multimedia-camera.md)。

**起始版本：** 9

<!--Device-unnamed-interface AVRecorder--><!--Device-unnamed-interface AVRecorder-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>
```

为AVRecorder添加水印。使用Promise异步回调。应用最多可添加5个水印。只能在prepared状态之前调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVRecorder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVRecorder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watermark | image.PixelMap | 是 |
| config | [WatermarkConfiguration](arkts-media-multimedia-media-watermarkconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void
```

获取实时的配置参数。使用callback异步回调。

只能在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口调用成功后调用。

**起始版本：** 11

<!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void--><!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVRecorderConfig&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(): Promise<AVRecorderConfig>
```

获取实时的配置参数。使用Promise异步回调。

只能在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口调用成功后调用。

**起始版本：** 11

<!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig>--><!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;AVRecorderConfig&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void
```

获取当前音频最大振幅。使用callback异步回调。

在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用此接口。在[stop](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**起始版本：** 11

<!--Device-AVRecorder-getAudioCapturerMaxAmplitude(callback: AsyncCallback<int>): void--><!--Device-AVRecorder-getAudioCapturerMaxAmplitude(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(): Promise<number>
```

获取当前音频最大振幅。使用Promise异步回调。

在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用此接口。在[stop](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))接口成功调用后，调用此接口会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间里面的最大值。

**起始版本：** 11

<!--Device-AVRecorder-getAudioCapturerMaxAmplitude(): Promise<int>--><!--Device-AVRecorder-getAudioCapturerMaxAmplitude(): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void
```

获取可用的编码器参数。使用callback异步回调。

**起始版本：** 11

<!--Device-AVRecorder-getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void--><!--Device-AVRecorder-getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;EncoderInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(): Promise<Array<EncoderInfo>>
```

获取可用的编码器参数。使用Promise异步回调。

**起始版本：** 11

<!--Device-AVRecorder-getAvailableEncoder(): Promise<Array<EncoderInfo>>--><!--Device-AVRecorder-getAvailableEncoder(): Promise<Array<EncoderInfo>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;EncoderInfo&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void
```

获取当前音频采集参数。使用callback异步回调。

在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用此接口。在[stop](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))接口成功调用后，调用此接口会报错。

**起始版本：** 11

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>
```

获取当前音频采集参数。使用Promise异步回调。

在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用此接口。在[stop](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))接口成功调用后，调用此接口会报错。

**起始版本：** 11

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;audio.AudioCapturerChangeInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string>): void
```

获取录制需要的surface。使用callback异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用getInputSurface接口。

**起始版本：** 9

<!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string>): void--><!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string>
```

获取录制需要的surface。使用Promise异步回调。

开发者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口成功调用后，才能调用getInputSurface接口。

**起始版本：** 9

<!--Device-AVRecorder-getInputSurface(): Promise<string>--><!--Device-AVRecorder-getInputSurface(): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void
```

取消订阅录制状态机[AVRecorderState](@ohos.multimedia.media:media.AVRecorderState)切换的事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-onavrecorderstatechangehandler-t.md) | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅录制错误事件，取消后不再接收到AVRecorder的错误事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-off(type: 'error', callback?: ErrorCallback): void--><!--Device-AVRecorder-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void
```

取消订阅录音变化的回调事件。使用callback异步回调。

**起始版本：** 11

<!--Device-AVRecorder-off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 否 |

## off('photoAssetAvailable')

```TypeScript
off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void
```

取消订阅媒体资源的回调类型。使用callback异步回调。

**起始版本：** 12

<!--Device-AVRecorder-off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 否 |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void
```

订阅录音配置变化的回调，任意录音配置的变化会触发变化后的录音配置全量信息回调。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 11

<!--Device-AVRecorder-on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## on('photoAssetAvailable')

```TypeScript
on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void
```

订阅媒体资源回调事件，当[FileGenerationMode](@ohos.multimedia.media:media.FileGenerationMode)枚举设置为系统创建媒体文件时，会在  
[stop](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))操作结束后把  
[PhotoAsset](@ohos.file.photoAccessHelper:photoAccessHelper)对象回调给应用。使用callback异步回调。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

<!--Device-AVRecorder-on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void
```

订阅录制状态机AVRecorderState切换的事件，当AVRecorderState状态机发生变化时，会通过订阅的回调方法通知用户。用户只能订阅一个录制状态机切换事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-onavrecorderstatechangehandler-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅AVRecorder的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时  
[AVRecorderState](@ohos.multimedia.media:media.AVRecorderState)也切换至error状态，用户需要通过  
[reset](media.AVRecorder.reset(callback: AsyncCallback&lt;void&gt;))或者  
[release](media.AVRecorder.release(callback: AsyncCallback&lt;void&gt;))接口退出录制操作。使用callback异步回调。

用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [5400107](../errorcode-media.md#5400107-音频焦点冲突) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停视频录制。使用callback异步回调。

需要[start](media.AVRecorder.start(callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用pause接口，可以通过调用  
[resume](media.AVRecorder.resume(callback: AsyncCallback&lt;void&gt;))接口来恢复录制。

**起始版本：** 9

<!--Device-AVRecorder-pause(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## pause

```TypeScript
pause(): Promise<void>
```

暂停视频录制。使用Promise异步回调。

需要[start](media.AVRecorder.start())接口成功调用后，才能调用pause接口，可以通过调用[resume](media.AVRecorder.resume())接口来恢复录制。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-pause(): Promise<void>--><!--Device-AVRecorder-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## prepare

```TypeScript
prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void
```

音视频录制的参数设置。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AVRecorder-prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void--><!--Device-AVRecorder-prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-multimedia-media-avrecorderconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## prepare

```TypeScript
prepare(config: AVRecorderConfig): Promise<void>
```

音视频录制的参数设置。使用Promise异步回调。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.MICROPHONE This permission is required only if audio recording is involved.
- API版本9 - 11：ohos.permission.MICROPHONE

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-prepare(config: AVRecorderConfig): Promise<void>--><!--Device-AVRecorder-prepare(config: AVRecorderConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-multimedia-media-avrecorderconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音视频录制资源。使用callback异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**起始版本：** 9

<!--Device-AVRecorder-release(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(): Promise<void>
```

释放音视频录制资源。使用Promise异步回调。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-release(): Promise<void>--><!--Device-AVRecorder-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

重置音视频录制。使用callback异步回调。

纯音频录制时，需要重新调用[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口才能重新录制。纯视频录制，音视频录制时，需要重新调用  
[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))和  
[getInputSurface](media.AVRecorder.getInputSurface(callback: AsyncCallback&lt;string&gt;))接口才能重新录制。

**起始版本：** 9

<!--Device-AVRecorder-reset(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-reset(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## reset

```TypeScript
reset(): Promise<void>
```

重置音视频录制。使用Promise异步回调。

纯音频录制时，需要重新调用[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口才能重新录制。纯视频录制，音视频录制时，需要重新调用  
[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))和  
[getInputSurface](media.AVRecorder.getInputSurface())接口才能重新录制。

**起始版本：** 9

<!--Device-AVRecorder-reset(): Promise<void>--><!--Device-AVRecorder-reset(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

恢复视频录制。使用callback异步回调。

需要在[pause](media.AVRecorder.pause(callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用resume接口。

**起始版本：** 9

<!--Device-AVRecorder-resume(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-resume(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## resume

```TypeScript
resume(): Promise<void>
```

恢复视频录制。使用Promise异步回调。

需要在[pause](media.AVRecorder.pause())接口成功调用后，才能调用resume接口。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-resume(): Promise<void>--><!--Device-AVRecorder-resume(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## setMetadata

```TypeScript
setMetadata(metadata: Record<string, string>): void
```

设置录制的元数据信息。如果这些信息的键相同，会覆盖config.metadata.customInfo（参考  
[prepare()](media.AVRecorder.prepare(config: AVRecorderConfig))和  
[AVRecorderConfig](@ohos.multimedia.media:media.AVRecorderConfig)）中的值。

该方法只能在[prepare()](media.AVRecorder.prepare(config: AVRecorderConfig))事件成功触发后，且必须在  
[stop()](media.AVRecorder.stop(callback: AsyncCallback&lt;void&gt;))之前调用。

**起始版本：** 26.0.0

<!--Device-AVRecorder-setMetadata(metadata: Record<string, string>): void--><!--Device-AVRecorder-setMetadata(metadata: Record<string, string>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadata | Record&lt;string, string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

设置当前录制音频流是否启用静音打断模式。使用Promise异步回调。

**起始版本：** 20

<!--Device-AVRecorder-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>--><!--Device-AVRecorder-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| muteWhenInterrupted | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始视频录制。使用callback异步回调。

纯音频录制需在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在  
[getInputSurface](media.AVRecorder.getInputSurface(callback: AsyncCallback&lt;string&gt;))接口成功调用后，才能调用start接口。

**起始版本：** 9

<!--Device-AVRecorder-start(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

开始视频录制。使用Promise异步回调。

纯音频录制需在[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口成功调用后，才能调用start接口。纯视频录制，音视频录制需在  
[getInputSurface](media.AVRecorder.getInputSurface())接口成功调用后，才能调用start接口。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-start(): Promise<void>--><!--Device-AVRecorder-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止视频录制。使用callback异步回调。

需要在[start](media.AVRecorder.start(callback: AsyncCallback&lt;void&gt;))或  
[pause](media.AVRecorder.pause(callback: AsyncCallback&lt;void&gt;))接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))接口才能重新录制。纯视频录制，音视频录制时，需要重新调用  
[prepare](media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;))和  
[getInputSurface](media.AVRecorder.getInputSurface(callback: AsyncCallback&lt;string&gt;))接口才能重新录制。

**起始版本：** 9

<!--Device-AVRecorder-stop(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## stop

```TypeScript
stop(): Promise<void>
```

停止视频录制。使用Promise异步回调。

需要在[start](media.AVRecorder.start())或[pause](media.AVRecorder.pause())接口成功调用后，才能调用stop接口。

纯音频录制时，需要重新调用[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口才能重新录制。纯视频录制，音视频录制时，需要重新调用  
[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))和  
[getInputSurface](media.AVRecorder.getInputSurface())接口才能重新录制。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-stop(): Promise<void>--><!--Device-AVRecorder-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## updateRotation

```TypeScript
updateRotation(rotation: number): Promise<void>
```

更新视频旋转角度。使用Promise异步回调。

当且仅当[prepare](media.AVRecorder.prepare(config: AVRecorderConfig))接口成功调用后，且在  
[start](media.AVRecorder.start(callback: AsyncCallback&lt;void&gt;))接口之前，才能调用updateRotation接口。

**起始版本：** 12

<!--Device-AVRecorder-updateRotation(rotation: int): Promise<void>--><!--Device-AVRecorder-updateRotation(rotation: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotation | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## state

```TypeScript
readonly state: AVRecorderState
```

音视频录制的状态。

**原子化服务API：** 从API version 12 开始，该接口支持在原子化服务中使用。

**类型：** [AVRecorderState](arkts-media-avrecorderstate-t.md)

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVRecorder-readonly state: AVRecorderState--><!--Device-AVRecorder-readonly state: AVRecorderState-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
