# AudioHapticManager

管理音振协同功能。在调用AudioHapticManager的接口前，需要先通过[getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md#getaudiohapticmanager)创建实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

创建音振播放器。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Required permissions:** ohos.permission.VIBRATE

<!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>--><!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | 已注册资源的source id。 |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | No | 音振播放器选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioHapticPlayer&gt; | Promise对象，返回创建的音振播放器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400106 | Unsupport format. |
| 201 | Permission denied. |

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

## createPlayer

```TypeScript
createPlayer(id: int, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>
```

Create an audio haptic player. This method uses a promise to return the result. If haptics is needed, caller should have the permission of ohos.permission.VIBRATE.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.VIBRATE

<!--Device-AudioHapticManager-createPlayer(id: int, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>--><!--Device-AudioHapticManager-createPlayer(id: int, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | Source id. |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | No | Options when creating audio haptic player. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioHapticPlayer \| null&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400106 | Unsupport format. |
| 201 | Permission denied. |

## registerSource

ArkTS-Dyn:
```TypeScript
registerSource(audioUri: string, hapticUri: string): Promise<number>
```

ArkTS-Sta:
```TypeScript
registerSource(audioUri: string, hapticUri: string): Promise<int>
```

通过Uri注册音频和振动资源。使用Promise异步回调。

> **注意：**
> 
> 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>--><!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| audioUri | string | Yes | 音频资源的Uri。 &lt;br&gt;- 对普通时延模式，音频资源格式和路径格式的支持可参考[AVPlayer](../../apis-media-kit/arkts-apis/arkts-media-media-avplayer-i.md/arkts-media-media-avplayer-i.md)。 &lt;br&gt;- 对低时延模式，音频资源格式支持可参考[SoundPool](../../apis-media-kit/arkts-apis/arkts-media-soundpool-soundpool-i.md/arkts-media-soundpool-soundpool-i.md)，路径格式需满足 [fileIo.open](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-open-f.md/arkts-corefile-file-fs-open-f.md#open)的要求。 &lt;br&gt;- 对两种时延模式，均建议传入文件的绝对路径。 |
| hapticUri | string | Yes | 振动资源的Uri。 &lt;br&gt;振动资源格式支持可参考[HapticFileDescriptor](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-hapticfiledescriptor-i.md/arkts-sensorservice-vibrator-hapticfiledescriptor-i.md)，路径格式需满足 [fileIo.open](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-open-f.md/arkts-corefile-file-fs-open-f.md#open)的要求。 &lt;br&gt;建议传入文件的绝对路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回注册的资源ID。 &lt;br&gt;正常情况下返回注册的资源ID为非负数。若返回注册的资源ID为负数，则表示注册失败，需检查注册资源数量是否超过上限。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

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

ArkTS-Dyn:
```TypeScript
registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>
```

ArkTS-Sta:
```TypeScript
registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>
```

通过文件描述符注册音频和振动资源。使用Promise异步回调。

> **注意：**
> 
> 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>--><!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| audioFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes | 已打开的有效文件描述符对象，用于描述音频文件。配套的offset和length需符合实际文件长度。 |
| hapticFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | Yes | 已打开的有效文件描述符对象，用于描述振动文件。配套的offset和length必须符合实际文件长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回注册的资源ID。 &lt;br&gt;正常情况下返回注册的资源ID为非负数。若返回注册的资源ID为负数，则表示注册失败，需检查注册资源数量是否超过上限。 |

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

ArkTS-Dyn:
```TypeScript
setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void
```

ArkTS-Sta:
```TypeScript
setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void
```

设置音频时延模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void--><!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 已注册资源的source id。 |
| latencyMode | [AudioLatencyMode](arkts-audio-audiohaptic-audiolatencymode-e.md) | Yes | 音频时延模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_FAST;

audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode);
```

## setStreamUsage

ArkTS-Dyn:
```TypeScript
setStreamUsage(id: number, usage: audio.StreamUsage): void
```

ArkTS-Sta:
```TypeScript
setStreamUsage(id: int, usage: audio.StreamUsage): void
```

设置音频流使用类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void--><!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 已注册资源的source id。 |
| usage | audio.StreamUsage | Yes | 音频流使用类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 5400102 | Operation not allowed. |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // The ID is obtained using registerSource.

let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;

audioHapticManagerInstance.setStreamUsage(id, usage);
```

## unregisterSource

ArkTS-Dyn:
```TypeScript
unregisterSource(id: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
unregisterSource(id: int): Promise<void>
```

取消注册音频和振动资源。使用Promise异步回调。

> **注意：**
> 
> 对于不再需要使用的资源，建议应用及时取消注册，避免出现资源泄漏或资源数量超上限等问题。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>--><!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 已注册资源的source id。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

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

