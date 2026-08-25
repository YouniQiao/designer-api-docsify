# AVRecorder

AVRecorder是音视频录制管理类，用于音视频录制的全流程管理，支持音频录制、视频录制及音视频混合录制，可灵活配置编码参数、添加水印、设置元数据、监听录制状态和错误事件等。 适用于录制音视频并保存到文件的场景，包括需要在音频流打断期间保持录制连续性、实时监控音频振幅等场景。 在调用AVRecorder的方法前，需要先调用 [createAVRecorder](arkts-media-media-createavrecorder-f.md)接口构建一个AVRecorder实例。 典型录制流程： [createAVRecorder](arkts-media-media-createavrecorder-f.md) → [prepare](#prepare) → [getInputSurface](#getinputsurface)（纯视频/音视频录制时） → [start](#start) → [pause](#pause)/ [resume](#resume) → [stop](#stop) → [release](#release)。音视频录制示例可参考：[音频录制开发指导](../../../media/media/using-avrecorder-for-recording.md)、 [视频录制开发指导](../../../media/media/video-recording.md)。

> **说明：**
> - 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> - 本Interface首批接口从API version 9开始支持。
> - 相机视频录制功能需配合相机模块使用，相机模块接口的使用详情请参考[相机管理](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md)。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>
```

添加自定义水印图像到录制视频中。适用于需要在录制视频中嵌入品牌标识、版权信息或时间戳等水印的场景。使用Promise异步回调。

> **说明：**
> - 应用最多可添加5个水印。
> - 必须在[prepare](#prepare)之前调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watermark | image.PixelMap | 是 |
| config | [WatermarkConfiguration](arkts-media-media-watermarkconfiguration-i.md) | 是 |

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

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void
```

获取当前音频最大振幅。适用于需要实时监控音频振幅的场景，如录音音量可视化显示、音频质量检测等。使用callback异步回调。必须在[prepare](#prepare) 和[stop](#stop)之间调用。调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间内的最大值。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(): Promise<number>
```

获取当前音频最大振幅。适用于需要实时监控音频振幅的场景，如录音音量可视化显示、音频质量检测等。使用Promise异步回调。必须在[prepare](#prepare) 和[stop](#stop)之间调用。调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。例如，在1s时获取了一次最大振幅，到2s时再获取到的最大振幅是1-2s这个区间内的最大值。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void
```

获取可用的编码器参数。适用于需要根据设备能力选择合适编码器的场景。使用callback异步回调。必须在非released/error状态下调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[EncoderInfo](arkts-media-media-encoderinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(): Promise<Array<EncoderInfo>>
```

获取可用的编码器参数。适用于需要根据设备能力选择合适编码器的场景。使用Promise异步回调。必须在非released/error状态下调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[EncoderInfo](arkts-media-media-encoderinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void
```

获取实时的配置参数。适用于需要确认录制配置是否正确应用的场景，如调试录制参数、验证配置生效情况等。使用callback异步回调。

必须在[prepare](#prepare)之后调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md)&gt; | 是 |

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

获取实时的配置参数。适用于需要确认录制配置是否正确应用的场景，如调试录制参数、验证配置生效情况等。使用Promise异步回调。

必须在[prepare](#prepare)之后调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void
```

获取当前音频采集参数。适用于需要确认当前音频采集设备类型或验证音频配置的场景。使用callback异步回调。必须在[prepare](#prepare) 和[stop](#stop)之间调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 是 |

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

获取当前音频采集参数。适用于需要确认当前音频采集设备类型或验证音频配置的场景。使用Promise异步回调。必须在[prepare](#prepare) 和[stop](#stop)之间调用。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise & lt;audio.AudioCapturerChangeInfo & gt; |

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

获得录制需要的surface。适用于纯视频或音视频录制时需要获取surface传递视频数据的场景。 相机视频录制功能需配合相机模块使用，详情请参考[相机管理](../apis-camera-kit/arkts-apis-camera.md)。使用callback异步回调。开发者从此surface中获取surfaceBuffer，填入待录制的视频数据。填入视频数据时需携带时间戳（单位ns）和buffer size。时间戳的起始时间以系统启动时间为基准。必须在[prepare](#prepare)和 [start](#start)之间调用。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

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

获得录制需要的surface。适用于纯视频或音视频录制时需要获取surface传递视频数据的场景。 相机视频录制功能需配合相机模块使用，详情请参考[相机管理](../apis-camera-kit/arkts-apis-camera.md)。使用callback异步回调。开发者从此surface中获取surfaceBuffer，填入待录制的视频数据。填入视频数据时需携带时间戳（单位ns）和buffer size。时间戳的起始时间以系统启动时间为基准。必须在[prepare](#prepare)和 [start](#start)之间调用。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

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

取消订阅录制状态机[AVRecorderState](arkts-media-media-avrecorderstate-t.md)切换的回调事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | 否 |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消订阅录制错误的回调事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void
```

取消订阅录音配置变化的回调事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 否 |

## off('photoAssetAvailable')

```TypeScript
off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void
```

取消订阅媒体资源创建完成的回调事件。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 否 |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void
```

订阅录音配置变化的回调事件。当录音配置发生变化时，会触发回调返回变化后的录音配置全量信息。使用callback异步回调。用户只能订阅一个录音配置变化事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('photoAssetAvailable')

```TypeScript
on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void
```

订阅媒体资源创建完成的回调事件。当[FileGenerationMode](arkts-media-media-filegenerationmode-e.md)枚举设置为系统创建媒体文件时， [stop](#stop)操作结束后会把 [PhotoAsset](../../apis-media-library-kit/arkts-apis/arkts-file-photoaccesshelper.md)对象回调给应用。使用callback异步回调。用户只能订阅一个媒体资源回调事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAssetAvailable' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void
```

订阅录制状态机[AVRecorderState](arkts-media-media-avrecorderstate-t.md)切换的回调事件。 当AVRecorderState发生变化时，会通过回调方法通知用户。用户只能订阅一个回调方法，重复订阅时以最后一次订阅的回调接口为准。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

订阅录制错误的回调事件。该事件仅用于错误提示，用户无需停止录制操作。 如果[AVRecorderState](arkts-media-media-avrecorderstate-t.md)也切换至error状态， 用户需通过[reset](#reset) 或者[release](#release)接口退出录制操作。使用callback异步回调。用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400104](../errorcode-media.md#5400104-操作超时) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |
| [5400107](../errorcode-media.md#5400107-音频焦点冲突) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停录制。使用callback异步回调。必须在[start](#start)之后调用，调用成功后进入paused状态， 之后可以通过调用[resume](#resume)接口来恢复录制。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

暂停录制。使用Promise异步回调。必须在[start](#start)之后调用，调用成功后进入paused状态， 之后可以通过调用[resume](#resume)接口来恢复录制。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

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
prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void
```

准备录制。设置音视频录制的参数，并初始化录制上下文。使用callback异步回调。必须在[start](#start)之前调用，调用成功后进入prepared状态， 此时，纯音频录制可直接调用start接口开始录制； 纯视频或音视频录制需先调用getInputSurface 接口获取surface，再调用start接口开始录制。

**起始版本：** 9

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## prepare

```TypeScript
prepare(config: AVRecorderConfig): Promise<void>
```

准备录制。设置音视频录制的参数，并初始化录制上下文。使用Promise异步回调。必须在start之前调用，调用成功后进入prepared状态，此时，纯音频录制可直接调用start接口开始录制； 纯视频或音视频录制需先调用getInputSurface接口获取surface，再调用start接口开始录制。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.MICROPHONE This permission is required only if audio recording is involved.
- API版本9 - 11：ohos.permission.MICROPHONE

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音视频录制资源。使用callback异步回调。必须在非released状态下调用，调用成功后进入released状态。与[createAVRecorder](arkts-media-media-createavrecorder-f.md)配对使用，录制流程结束后应调用此接口释放资源。 释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(): Promise<void>
```

释放音视频录制资源。使用Promise异步回调。必须在非released状态下调用，调用成功后进入released状态。与[createAVRecorder](arkts-media-media-createavrecorder-f.md)配对使用，录制流程结束后应调用此接口释放资源。 释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

重置音视频录制，将录制器恢复至初始状态以便重新配置参数。使用callback异步回调。必须在非released状态下调用，调用成功后进入idle状态。纯音频录制时，需要重新调用[prepare](#prepare)接口 才能重新录制。纯视频录制、音视频录制时，需要重新调用 [prepare](#prepare)和 [getInputSurface](#getinputsurface)接口才能重新录制。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## reset

```TypeScript
reset(): Promise<void>
```

重置音视频录制，将录制器恢复至初始状态以便重新配置参数。使用Promise异步回调。必须在非released状态下调用，调用成功后进入idle状态。纯音频录制时，需要重新调用[prepare](#prepare)接口才能重新录制。 纯视频录制、音视频录制时，需要重新调用[prepare](#prepare)和 [getInputSurface](#getinputsurface)接口才能重新录制。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

恢复录制。使用callback异步回调。必须在[pause](#pause)之后调用，调用成功后进入started状态， 之后可以再次调用[pause](#pause)接口暂停录制，或调用 [stop](#stop)接口停止录制。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

恢复录制。使用Promise异步回调。必须在[pause](#pause)之后调用，调用成功后进入started状态， 之后可以再次调用[pause](#pause)接口暂停录制，或调用[stop](#stop)接口停止录制。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

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

## setMetadata

```TypeScript
setMetadata(metadata: Record<string, string>): void
```

设置录制的元数据信息。适用于需要在录制文件中嵌入自定义元数据（如作者、标题、标签等）的场景。 如果metadata参数与config.metadata.customInfo（参考[prepare()](#prepare)和 [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md)）中存在相同的键，前者的对应值将覆盖后者。必须在prepare()和stop()之间调用。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadata | Record & lt;string, string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

设置当前录制音频流是否启用静音打断模式。启用后，录制音频流被更高优先级音频打断时将录制静音而非停止录制，适用于需要在打断期间保持录制连续性的场景（如会议录音、语音备忘）。 不启用则保持默认打断模式（音频流被打断时停止录制）。使用Promise异步回调。必须在prepare()之前调用。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| muteWhenInterrupted | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始录制。使用callback异步回调。必须在[prepare](#prepare)之后调用， 调用成功后进入started状态。录制视频时，还需在 [getInputSurface](#getinputsurface)接口调用成功后，才能调用此接口。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

开始录制。使用Promise异步回调。必须在[prepare](#prepare)之后调用，调用成功后进入started状态。录制视频时，还需在 [getInputSurface](#getinputsurface)接口调用成功后，才能调用此接口。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

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

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止录制。使用callback异步回调。必须在[start](#start)或 [pause](#pause)之后调用，调用成功后进入stopped状态。 当prepare配置中将FileGenerationMode设置为系统创建媒体文件模式时，本接口调用结束后会触发on('photoAssetAvailable')回调。 纯音频录制时，需要重新调用[prepare](#prepare) 接口才能重新录制；纯视频录制、音视频录制时，需要重新调用 [prepare](#prepare)和 [getInputSurface](#getinputsurface)接口才能重新录制。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

停止录制。使用Promise异步回调。必须在[start](#start)或[pause](#pause)之后调用，调用成功后进入stopped状态。 当prepare配置中将FileGenerationMode设置为系统创建媒体文件模式时，本接口调用结束后会触发on('photoAssetAvailable')回调。 纯音频录制时，需要重新调用[prepare](#prepare)接口才能重新录制； 纯视频录制、音视频录制时，需要重新调用[prepare](#prepare)和 [getInputSurface](#getinputsurface)接口才能重新录制。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

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

## updateRotation

```TypeScript
updateRotation(rotation: number): Promise<void>
```

更新视频旋转角度。适用于设备方向发生变化（如横竖屏切换）时需要动态调整录制视频旋转角度的场景。使用Promise异步回调。必须在prepare和start之间调用。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotation | number | 是 |

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
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## state

```TypeScript
readonly state: AVRecorderState
```

音视频录制的状态。

**原子化服务API：** 从API version 12 开始，该接口支持在原子化服务中使用。

**类型：** [AVRecorderState](arkts-media-media-avrecorderstate-t.md)

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
