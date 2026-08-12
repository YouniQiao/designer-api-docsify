# AudioStreamManager

音频流管理。

在使用AudioStreamManager的接口之前，需先通过[getStreamManager](arkts-audio-audio-audiomanager-i.md#getStreamManager)获取AudioStreamManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 9

<!--Device-audio-interface AudioStreamManager--><!--Device-audio-interface AudioStreamManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void
```

获取当前音效模式的信息。使用callback异步回调。

**起始版本：** 10

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>
```

获取当前音效模式的信息。使用Promise异步回调。

**起始版本：** 10

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## getAudioEffectInfoArraySync

```TypeScript
getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray
```

获取当前音效模式的信息。同步返回结果。

**起始版本：** 10

<!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray--><!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void
```

获取当前音频采集器的信息。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**起始版本：** 9

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | 是 |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>
```

获取当前音频采集器的信息。使用Promise异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**起始版本：** 9

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; |

## getCurrentAudioCapturerInfoArraySync

```TypeScript
getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray
```

获取当前音频采集器的信息。同步返回结果。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**起始版本：** 10

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 |
| --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void
```

获取当前音频渲染器的信息。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**起始版本：** 9

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | 是 |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>
```

获取当前音频渲染器的信息。使用Promise异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**起始版本：** 9

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; |

## getCurrentAudioRendererInfoArraySync

```TypeScript
getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray
```

获取当前音频渲染器的信息。同步返回结果。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**起始版本：** 10

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 |
| --- |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) |

## isAcousticEchoCancelerSupported

```TypeScript
isAcousticEchoCancelerSupported(sourceType: SourceType): boolean
```

查询指定的音源类型是否支持回声消除。

**起始版本：** 20

<!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音频流活跃状态。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [isStreamActive](#isStreamActive)

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音频流是否为活跃状态。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**替代接口：** [isStreamActive](#isStreamActive)

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isActiveSync

```TypeScript
isActiveSync(volumeType: AudioVolumeType): boolean
```

获取指定音频流是否为活跃状态。同步返回结果。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [isStreamActive](#isStreamActive)

<!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## isAudioLoopbackSupported

```TypeScript
isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean
```

查询当前系统是否支持指定的音频返听模式。

**起始版本：** 20

<!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean--><!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## isDirectPlaybackSupported

```TypeScript
isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持直通播放。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 是 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isFastPlaybackSupported

```TypeScript
isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持低时延播放。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 是 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isFastRecordingSupported

```TypeScript
isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean
```

查询指定音频流信息和音源类型下是否支持低时延录制。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean--><!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 是 |
| source | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isIntelligentNoiseReductionEnabledForCurrentDevice

```TypeScript
isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean
```

查询指定的音源类型智能降噪开关是否打开。

**起始版本：** 21

<!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## isMultichannelPlaybackSupported

```TypeScript
isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持多声道播放。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 是 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isOffloadPlaybackSupported

```TypeScript
isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持低功耗通路播放。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | 是 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isRecordingAvailable

```TypeScript
isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean
```

检查传入的音频采集器信息中音源类型的录制是否可以启动成功。

**起始版本：** 20

<!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean--><!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## isStreamActive

```TypeScript
isStreamActive(streamUsage: StreamUsage): boolean
```

获取指定音频流是否为活跃状态。同步返回结果。

**起始版本：** 20

<!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean--><!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## off('audioRendererChange')

```TypeScript
off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void
```

取消监听音频渲染器更改事件。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**起始版本：** 9

<!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioRendererChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void
```

取消监听音频采集器更改事件。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**起始版本：** 9

<!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## on('audioRendererChange')

```TypeScript
on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void
```

监听音频渲染器更改事件（当音频播放流状态变化或设备变化时触发）。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**起始版本：** 9

<!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioRendererChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void
```

监听音频采集器更改事件（当音频录制流状态变化或设备变化时触发）。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**起始版本：** 9

<!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioCapturerChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-无效入参) |
