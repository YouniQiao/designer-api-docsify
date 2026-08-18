# AudioStreamManager

This interface implements audio stream management. Before calling any API in AudioStreamManager, you must use [getStreamManager](arkts-audio-audio-audiomanager-i.md#getstreammanager) to obtain an AudioStreamManager instance. > **NOTE：**> > - The initial APIs of this interface are supported since API version 9.

**Since:** 23

<!--Device-audio-interface AudioStreamManager--><!--Device-audio-interface AudioStreamManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
```

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void
```

Obtains information about the audio effect mode in use. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getAudioEffectInfoArray

```TypeScript
getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>
```

Obtains information about the audio effect mode in use. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>--><!--Device-AudioStreamManager-getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getAudioEffectInfoArraySync

```TypeScript
getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray
```

Obtains information about the audio effect mode in use. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray--><!--Device-AudioStreamManager-getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioEffectInfoArray](arkts-audio-audio-audioeffectinfoarray-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void
```

Obtains the information about this audio capturer. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio capturer information returned by this API may include internal audio recording streams, such as voice > wakeup and cellular calls.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | Yes |

## getCurrentAudioCapturerInfoArray

```TypeScript
getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>
```

Obtains the information about this audio capturer. This API uses a promise to return the result. > **NOTE：**> > The audio capturer information returned by this API may include internal audio recording streams, such as voice > wakeup and cellular calls.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; |

## getCurrentAudioCapturerInfoArraySync

```TypeScript
getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray
```

Obtains the information about this audio capturer. This API returns the result synchronously. > **NOTE：**> > The audio capturer information returned by this API may include internal audio recording streams, such as voice > wakeup and cellular calls.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md) |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void
```

Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio renderer information returned by this API may include internal audio playback streams, such as > cellular calls and ultrasonic streams.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | Yes |

## getCurrentAudioRendererInfoArray

```TypeScript
getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>
```

Obtains the information about this audio renderer. This API uses a promise to return the result. > **NOTE：**> > The audio renderer information returned by this API may include internal audio playback streams, such as > cellular calls and ultrasonic streams.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; |

## getCurrentAudioRendererInfoArraySync

```TypeScript
getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray
```

Obtains the information about this audio renderer. This API returns the result synchronously. > **NOTE：**> > The audio renderer information returned by this API may include internal audio playback streams, such as > cellular calls and ultrasonic streams.

**Since:** 23

<!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray--><!--Device-AudioStreamManager-getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md) |

## isAcousticEchoCancelerSupported

```TypeScript
isAcousticEchoCancelerSupported(sourceType: SourceType): boolean
```

Checks whether the specified audio source type supports echo cancellation.

**Since:** 23

<!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isAcousticEchoCancelerSupported(sourceType: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceType | [SourceType](../../apis-na/arkts-apis/arkts-na-webview-sourcetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void
```

Checks whether a stream is active. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isStreamActive](#isstreamactive)

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isActive

```TypeScript
isActive(volumeType: AudioVolumeType): Promise<boolean>
```

Checks whether a stream is active. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isStreamActive](#isstreamactive)

<!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>--><!--Device-AudioStreamManager-isActive(volumeType: AudioVolumeType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isActiveSync

```TypeScript
isActiveSync(volumeType: AudioVolumeType): boolean
```

Checks whether a stream is active. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** 20

**Substitutes:** [isStreamActive](#isstreamactive)

<!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean--><!--Device-AudioStreamManager-isActiveSync(volumeType: AudioVolumeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isAudioLoopbackSupported

```TypeScript
isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean
```

Checks whether the current system supports the specified audio loopback mode.

**Since:** 23

<!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean--><!--Device-AudioStreamManager-isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isDirectPlaybackSupported

```TypeScript
isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

Return if direct playback is supported for the specific audio stream info and usage type in current device situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFastPlaybackSupported

```TypeScript
isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

Return if fast playback is supported for the specific audio stream info and usage type in current device situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFastRecordingSupported

```TypeScript
isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean
```

Return if fast recording is supported for the specific audio stream info and usage type in current device situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean--><!--Device-AudioStreamManager-isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes |
| source | [SourceType](../../apis-na/arkts-apis/arkts-na-webview-sourcetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isIntelligentNoiseReductionEnabledForCurrentDevice

```TypeScript
isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean
```

Checks whether the intelligent noise reduction feature is enabled for the audio stream of the specified source type.

**Since:** 24

<!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean--><!--Device-AudioStreamManager-isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceType | [SourceType](../../apis-na/arkts-apis/arkts-na-webview-sourcetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isMultichannelPlaybackSupported

```TypeScript
isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

Return if multichannel playback is supported for the specific audio stream info and usage type in current device situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isOffloadPlaybackSupported

```TypeScript
isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean
```

Return if offload playback is supported for the specific audio stream info and usage type in current device situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean--><!--Device-AudioStreamManager-isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md) | Yes |
| usage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRecordingAvailable

```TypeScript
isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean
```

Checks whether recording can be started based on the audio source type in the audio capturer information.

**Since:** 23

<!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean--><!--Device-AudioStreamManager-isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## isStreamActive

```TypeScript
isStreamActive(streamUsage: StreamUsage): boolean
```

Checks whether a stream is active. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean--><!--Device-AudioStreamManager-isStreamActive(streamUsage: StreamUsage): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## offAudioCapturerChange

```TypeScript
offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void
```

Unsubscribes to audio capturer change events.

**Since:** 23

<!--Device-AudioStreamManager-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-offAudioCapturerChange(callback?: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## offAudioRendererChange

```TypeScript
offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void
```

Unsubscribes to audio renderer change events.

**Since:** 23

<!--Device-AudioStreamManager-offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-offAudioRendererChange(callback?: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off_audioCapturerChange

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void
```

Unsubscribes from the audio capturer change event. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio capturer information returned by this API may include internal audio recording streams, such as voice > wakeup and cellular calls.

**Since:** 9

<!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off_audioRendererChange

```TypeScript
off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void
```

Unsubscribes from the audio renderer change event. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio renderer information returned by this API may include internal audio playback streams, such as > cellular calls and ultrasonic streams.

**Since:** 9

<!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioRendererChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## onAudioCapturerChange

```TypeScript
onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void
```

Listens for audio capturer change events. When there is any audio capturer change, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioStreamManager-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-onAudioCapturerChange(callback: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## onAudioRendererChange

```TypeScript
onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void
```

Listens for audio renderer change events. When there is any audio renderer change, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioStreamManager-onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-onAudioRendererChange(callback: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on_audioCapturerChange

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void
```

Subscribes to the audio capturer change event, which is triggered when the audio recording stream status or device is changed. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio capturer information returned by this API may include internal audio recording streams, such as voice > wakeup and cellular calls.

**Since:** 9

<!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerChangeInfoArray](arkts-audio-audio-audiocapturerchangeinfoarray-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on_audioRendererChange

```TypeScript
on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void
```

Subscribes to the audio renderer change event, which is triggered when the audio playback stream status or device is changed. This API uses an asynchronous callback to return the result. > **NOTE：**> > The audio renderer information returned by this API may include internal audio playback streams, such as > cellular calls and ultrasonic streams.

**Since:** 9

<!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void--><!--Device-AudioStreamManager-on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioRendererChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioRendererChangeInfoArray](arkts-audio-audio-audiorendererchangeinfoarray-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
