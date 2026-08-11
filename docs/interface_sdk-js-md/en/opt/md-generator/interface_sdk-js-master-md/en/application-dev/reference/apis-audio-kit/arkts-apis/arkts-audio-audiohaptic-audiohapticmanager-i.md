# AudioHapticManager

Manages the audio-haptic feature. Before calling any API in AudioHapticManager, you must use   
[getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md#getaudiohapticmanager) to create an AudioHapticManager instance.

**Since:** 11

<!--Device-audioHaptic-interface AudioHapticManager--><!--Device-audioHaptic-interface AudioHapticManager-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## createPlayer

```TypeScript
createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>
```

Create an audio haptic player. This method uses a promise to return the result. If haptics is needed, caller should have the permission of ohos.permission.VIBRATE.

**Since:** 11

**Required permissions:** ohos.permission.VIBRATE

<!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>--><!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AudioHapticPlayer&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
let audioHapticPlayerInstance: audioHaptic.AudioHapticPlayer | undefined = undefined;

audioHapticManagerInstance.createPlayer(id, options).then((value: audioHaptic.AudioHapticPlayer) => {
  audioHapticPlayerInstance = value;
  console.info('Succeeded in doing createPlayer.');
}).catch((err: BusinessError) => {
  console.error(`Failed to createPlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## registerSource

```TypeScript
registerSource(audioUri: string, hapticUri: string): Promise<number>
```

Registers audio and haptic resources via URIs. This API uses a promise to return the result.

> **NOTE：**
> 
> A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
> beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
> of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
> manner.

**Since:** 11

<!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>--><!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| audioUri | string | Yes |
| hapticUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let audioUri = 'data/audioTest.wav'; // Change it to the URI of the target audio source.
let hapticUri = 'data/hapticTest.json'; // Change it to the URI of the target haptic source.
let id = 0;
// A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.
audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
  console.info(`Promise returned to indicate that the source id of the registered source ${value}.`);
  id = value;
}).catch((err: BusinessError) => {
  console.error(`Failed to register source ${err}`);
});
```

## registerSourceFromFd

```TypeScript
registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>
```

Registers audio and haptic resources via file descriptors. This API uses a promise to return the result.

> **NOTE：**
> 
> A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
> beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
> of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
> manner.

**Since:** 20

<!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>--><!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| audioFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes |
| hapticFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg'); // Use the corresponding file in the rawfile directory.
let audioFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: audioFile.fd,
  offset: audioFile.offset,
  length: audioFile.length,
};

let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json'); // Use the corresponding file in the rawfile directory.
let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: hapticFile.fd,
  offset: hapticFile.offset,
  length: hapticFile.length,
};
let id = 0;
// A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.
audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
  console.info('Succeeded in doing registerSourceFromFd.');
  id = value;
}).catch((err: BusinessError) => {
  console.error(`Failed to registerSourceFromFd. Code: ${err.code}, message: ${err.message}`);
});
```

## setAudioLatencyMode

```TypeScript
setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void
```

Sets the latency mode for an audio-haptic source.

**Since:** 11

<!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void--><!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| latencyMode | [AudioLatencyMode](arkts-audio-audiohaptic-audiolatencymode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_FAST;

audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode);
```

## setStreamUsage

```TypeScript
setStreamUsage(id: number, usage: audio.StreamUsage): void
```

Sets the stream usage for an audio-haptic source.

**Since:** 11

<!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void--><!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| usage | audio.StreamUsage | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;

audioHapticManagerInstance.setStreamUsage(id, usage);
```

## unregisterSource

```TypeScript
unregisterSource(id: number): Promise<void>
```

Unregisters an audio-haptic source. This API uses a promise to return the result.

> **NOTE：**
> 
> For resources that are no longer used, you are advised to unregister them in a timely manner to avoid issues
> such as resource leaks or the number of resources exceeding the upper limit.

**Since:** 11

<!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>--><!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

audioHapticManagerInstance.unregisterSource(id).then(() => {
  console.info('Succeeded in doing unregisterSource.');
}).catch((err: BusinessError) => {
  console.error(`Failed to unregisterSource. Code: ${err.code}, message: ${err.message}`);
});
```
