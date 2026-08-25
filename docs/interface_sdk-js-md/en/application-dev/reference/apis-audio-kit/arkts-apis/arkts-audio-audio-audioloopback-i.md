# AudioLoopback

This interface provides APIs for audio monitoring.Before calling any API in AudioLoopback, you must use [audio.createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md) to create an AudioLoopback instance.When audio loopback is enabled, the system creates a low-latency renderer and capturer to implement low-latency in- ear monitoring. The audio captured is routed back to the renderer through an internal path. The renderer follows the audio focus strategy for [STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md), whereas the capturer follows the strategy for [SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md).The system automatically chooses the input and output devices. If these devices do not support low latency, audio loopback does not work. If another audio stream takes over the audio focus or if the input or output device changes to the one that does not support low latency, the system disables audio loopback automatically.

> **NOTE：**&gt;
> - The initial APIs of this interface are supported since API version 20.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## enable

```TypeScript
enable(enable: boolean): Promise<boolean>
```

Enable or disable audio loopback. When audio loopback is enabled, the system automatically creates fast playback and recording streams to implement low-latency in-ear monitoring. When audio loopback is disabled, the audio stream is destroyed. If enabling audio loopback fails, you can use [getStatus](#getstatus) to query the cause. After audio loopback is enabled, you can subscribe to the statusChange event to listen for audio loopback status changes.

**Since:** 20

**Required permissions:** ohos.permission.MICROPHONE

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [enable](#enable) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getEqualizerPreset

```TypeScript
getEqualizerPreset(): AudioLoopbackEqualizerPreset
```

Gets the current equalizer preset. The default equalizer preset of audio loopback is [FULL](arkts-audio-audio-audioloopbackequalizerpreset-e.md#full) if users do not modify the preset.

**Since:** 21

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) |

## getPreferredDevicePair

```TypeScript
getPreferredDevicePair(): AudioDevicePair | null
```

Gets the preferred audio device pair in current device connection situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md) \| null |

## getReverbPreset

```TypeScript
getReverbPreset(): AudioLoopbackReverbPreset
```

Get the current reverberation. The default reverberation preset of audio loopback is [THEATER](arkts-audio-audio-audioloopbackreverbpreset-e.md#theater) if users do not modify the preset.

**Since:** 21

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) |

## getStatus

```TypeScript
getStatus(): Promise<AudioLoopbackStatus>
```

Obtains the audio loopback status. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; |

## getSupportedDevicePairs

```TypeScript
getSupportedDevicePairs(): Array<AudioDevicePair>
```

Gets supported audio device pairs in current device connection situation.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md)&gt; |

## getVolume

```TypeScript
getVolume(): number
```

Gets the output volume for audio loopback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## off('statusChange')

```TypeScript
off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void
```

Unsubscribes from the audio loopback status event. This API uses an asynchronous callback to return the result.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'statusChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('statusChange')

```TypeScript
on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void
```

Subscribes to the audio loopback status change event, which is triggered when the status of the audio loopback is changed. This API uses an asynchronous callback to return the result.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'statusChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setEqualizerPreset

```TypeScript
setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean
```

Sets the equalizer preset of the audio loopback.

**Since:** 21

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [preset](../../apis-media-kit/arkts-apis/arkts-media-media-avscreencapturerecordconfig-i.md) | [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setReverbPreset

```TypeScript
setReverbPreset(preset: AudioLoopbackReverbPreset): boolean
```

Sets the reverberation of the audio loopback.

**Since:** 21

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [preset](../../apis-media-kit/arkts-apis/arkts-media-media-avscreencapturerecordconfig-i.md) | [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setVolume

```TypeScript
setVolume(volume: number): Promise<void>
```

Sets the volume for audio loopback. This volume does not affect other audio streams or the system volume.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
