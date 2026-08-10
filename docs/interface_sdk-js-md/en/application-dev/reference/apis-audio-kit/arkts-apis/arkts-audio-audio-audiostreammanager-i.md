# AudioStreamManager

音频流管理。

在使用AudioStreamManager的接口之前，需先通过[getStreamManager](arkts-audio-audio-audiomanager-i.md#getstreammanager)获取AudioStreamManager实例。

> **说明：**
> 
> - 本Interface首批接口从API version 9开始支持。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioStreamManager--><!--Device-audio-interface AudioStreamManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void
```

获取当前音效模式的信息。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioEffectInfoArray&gt; | Yes | 回调函数。当获取当前音效模式的信息成功，err为undefined，data为获取到的当前音效模式的信息；否则 为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>
```

获取当前音效模式的信息。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioEffectInfoArray&gt; | Promise对象，返回当前音效模式的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

## getAudioEffectInfoArraySync

```TypeScript
getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray
```

获取当前音效模式的信息。同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray--><!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) | 返回当前音效模式的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void
```

获取当前音频采集器的信息。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioCapturerChangeInfoArray&gt; | Yes | 回调函数。当获取当前音频采集器的信息成功，err为undefined，data为获取到的当前音 频采集器的信息；否则为错误对象。 |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>
```

获取当前音频采集器的信息。使用Promise异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioCapturerChangeInfoArray&gt; | Promise对象，返回当前音频采集器信息。 |

## getCurrentAudioCapturerInfoArraySync

```TypeScript
getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray
```

获取当前音频采集器的信息。同步返回结果。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) | 返回当前音频采集器信息。 |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void
```

获取当前音频渲染器的信息。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AudioRendererChangeInfoArray&gt; | Yes | 回调函数。当获取当前音频渲染器的信息成功，err为undefined，data为获取到的当前音 频渲染器的信息；否则为错误对象。 |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>
```

获取当前音频渲染器的信息。使用Promise异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioRendererChangeInfoArray&gt; | Promise对象，返回当前音频渲染器信息。 |

## getCurrentAudioRendererInfoArraySync

```TypeScript
getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray
```

获取当前音频渲染器的信息。同步返回结果。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) | 返回当前音频渲染器信息。 |

## isAcousticEchoCancelerSupported

```TypeScript
isAcousticEchoCancelerSupported(sourceType: SourceType): boolean
```

查询指定的音源类型是否支持回声消除。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes | 音源类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持回声消除。true表示支持回声消除，false表示不支持回声消除。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

获取指定音频流活跃状态。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Deprecated since:** 20

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isStreamActive

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频流类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当获取指定音频流活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

获取指定音频流是否为活跃状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Deprecated since:** 20

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isStreamActive

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频流类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |

## isActiveSync

```TypeScript
isActiveSync(volumeType: AudioVolumeType): boolean
```

获取指定音频流是否为活跃状态。同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Deprecated since:** 20

**Substitutes:** ohos.multimedia.audio.AudioStreamManager#isStreamActive

<!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes | 音频流类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 流的活跃状态。返回true表示活跃，返回false表示不活跃。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## isAudioLoopbackSupported

```TypeScript
isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean
```

查询当前系统是否支持指定的音频返听模式。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean--><!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | Yes | 音频返听模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持指定的音频返听模式。true表示支持，false表示不支持。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## isDirectPlaybackSupported

```TypeScript
isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持直通播放。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes | 音频流信息，用于描述基础音频格式。 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用场景，用于决定音频设备和通路类型的选择结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持直通播放。true表示支持，false表示不支持。 |

## isFastPlaybackSupported

```TypeScript
isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持低时延播放。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes | 音频流信息，用于描述基础音频格式。 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用场景，用于决定音频设备和通路类型的选择结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持低时延播放。true表示支持，false表示不支持。 |

## isFastRecordingSupported

```TypeScript
isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean
```

查询指定音频流信息和音源类型下是否支持低时延录制。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean--><!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes | 音频流信息，用于描述基础音频格式。 |
| source | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes | 音源类型，用于决定音频设备和通路类型的选择结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持低时延录制。true表示支持，false表示不支持。 |

## isIntelligentNoiseReductionEnabledForCurrentDevice

```TypeScript
isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean
```

查询指定的音源类型智能降噪开关是否打开。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes | 表示音源类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 智能降噪开关的状态。true表示打开，false表示关闭。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## isMultichannelPlaybackSupported

```TypeScript
isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持多声道播放。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes | 音频流信息，用于描述基础音频格式。 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用场景，用于决定音频设备和通路类型的选择结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持多声道播放。true表示支持，false表示不支持。 |

## isOffloadPlaybackSupported

```TypeScript
isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

查询指定音频流信息和使用场景下是否支持低功耗通路播放。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes | 音频流信息，用于描述基础音频格式。 |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用场景，用于决定音频设备和通路类型的选择结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持低功耗通路播放。true表示支持，false表示不支持。 |

## isRecordingAvailable

```TypeScript
isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean
```

检查传入的音频采集器信息中音源类型的录制是否可以启动成功。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean--><!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | 音频采集器信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 代表录制是否可以启动成功。true表示成功，false表示失败。 &lt;br&gt;仅检测是否可以获取音频采集器信息中音源类型的焦点。通常在音频录制启动前调用，否则已存在的录制流可能会拒绝其启动。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## isStreamActive

```TypeScript
isStreamActive(streamUsage: StreamUsage): boolean
```

获取指定音频流是否为活跃状态。同步返回结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean--><!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes | 音频流使用类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 流是否处于活跃状态。返回true表示活跃，返回false表示不活跃。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## off('audioRendererChange')

```TypeScript
off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void
```

取消监听音频渲染器更改事件。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioRendererChange' | Yes | 事件回调类型，支持的事件为'audioRendererChange'，当取消监听音频渲染器更改事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRendererChangeInfoArray&gt; | No | 回调函数，返回当前音频渲染器信息。<br>**Since:** 18 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## off('audioCapturerChange')

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void
```

取消监听音频采集器更改事件。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioCapturerChange' | Yes | 事件回调类型，支持的事件为'audioCapturerChange'，当取消监听音频采集器更改事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerChangeInfoArray&gt; | No | 回调函数，返回当前音频采集器信息。<br>**Since:** 18 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## offAudioCapturerChange

```TypeScript
offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void
```

Unsubscribes to audio capturer change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioStreamManager-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerChangeInfoArray&gt; | No | Callback invoked for the audio capturer change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## offAudioRendererChange

```TypeScript
offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void
```

Unsubscribes to audio renderer change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioStreamManager-offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRendererChangeInfoArray&gt; | No | Callback invoked for the audio renderer change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## on('audioRendererChange')

```TypeScript
on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void
```

监听音频渲染器更改事件（当音频播放流状态变化或设备变化时触发）。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioRendererChange' | Yes | 事件回调类型，支持的事件为'audioRendererChange'，当音频播放流状态变化或设备变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRendererChangeInfoArray&gt; | Yes | 回调函数，返回当前音频渲染器信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## on('audioCapturerChange')

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void
```

监听音频采集器更改事件（当音频录制流状态变化或设备变化时触发）。使用callback异步回调。

> **说明：**
> 
> 该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioCapturerChange' | Yes | 事件回调类型，支持的事件为'audioCapturerChange'，当音频录制流状态变化或设备变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerChangeInfoArray&gt; | Yes | 回调函数，返回当前音频采集器信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

## onAudioCapturerChange

```TypeScript
onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void
```

Listens for audio capturer change events. When there is any audio capturer change,registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioStreamManager-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioCapturerChangeInfoArray&gt; | Yes | Callback invoked for the audio capturer change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## onAudioRendererChange

```TypeScript
onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void
```

Listens for audio renderer change events. When there is any audio renderer change,registered clients will receive the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioStreamManager-onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRendererChangeInfoArray&gt; | Yes | Callback invoked for the audio renderer change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

