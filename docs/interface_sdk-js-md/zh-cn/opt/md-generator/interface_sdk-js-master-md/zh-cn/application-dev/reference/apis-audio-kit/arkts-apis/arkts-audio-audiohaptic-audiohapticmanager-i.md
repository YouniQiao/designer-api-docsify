# AudioHapticManager

管理音振协同功能。在调用AudioHapticManager的接口前，需要先通过[getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md#getaudiohapticmanager)创建实例。

**起始版本：** 23

<!--Device-audioHaptic-interface AudioHapticManager--><!--Device-audioHaptic-interface AudioHapticManager-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

## 导入模块

```TypeScript
```

## createPlayer

```TypeScript
createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>
```

创建音振播放器。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.VIBRATE

<!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>--><!--Device-AudioHapticManager-createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioHapticPlayer](arkts-audio-audiohaptic-audiohapticplayer-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-不支持的规格) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // 需要通过registerSource或registerSourceFromFd方法获取。

let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
let audioHapticPlayerInstance: audioHaptic.AudioHapticPlayer | undefined = undefined;

audioHapticManagerInstance.createPlayer(id, options).then((value: audioHaptic.AudioHapticPlayer) => {
  audioHapticPlayerInstance = value;
  console.info('Succeeded in creating the player.');
}).catch((err: BusinessError) => {
  console.error(`Failed to create the player. Code: ${err.code}, message: ${err.message}`);
});
```

## createPlayer

```TypeScript
createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>
```

Create an audio haptic player. This method uses a promise to return the result. If haptics is needed, caller should have the permission of ohos.permission.VIBRATE.

**起始版本：** 23

**需要权限：** ohos.permission.VIBRATE

<!--Device-AudioHapticManager-createPlayer(id: int, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>--><!--Device-AudioHapticManager-createPlayer(id: int, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer | null>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| options | [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioHapticPlayer](arkts-audio-audiohaptic-audiohapticplayer-i.md) \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-不支持的规格) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## registerSource

```TypeScript
registerSource(audioUri: string, hapticUri: string): Promise<number>
```

通过Uri注册音频和振动资源。使用Promise异步回调。 > **注意：** > > 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**起始版本：** 23

<!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>--><!--Device-AudioHapticManager-registerSource(audioUri: string, hapticUri: string): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| audioUri | string | 是 |
| hapticUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 音频资源的URI，传递给registerSource用于注册。
let audioUri = 'data/audioTest.wav'; // 需更改为目标音频资源的URI。
// 振动资源的URI，传递给registerSource用于注册。
let hapticUri = 'data/hapticTest.json'; // 需更改为目标振动资源的URI。
let id = 0;
// 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。
audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
  id = value;
  console.info(`Succeeded in registering the source, sourceId: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to register the source. Code: ${err.code}, message: ${err.message}`);
});
```

## registerSourceFromFd

```TypeScript
registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>
```

通过文件描述符注册音频和振动资源。使用Promise异步回调。 > **注意：** > > 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**起始版本：** 23

<!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>--><!--Device-AudioHapticManager-registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| audioFd | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | 是 |
| [hapticFd](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefromfile-i.md) | [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg'); // 需要改成rawfile目录下的对应文件。
let audioFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: audioFile.fd,
  offset: audioFile.offset,
  length: audioFile.length,
};

let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json'); // 需要改成rawfile目录下的对应文件。
let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
  fd: hapticFile.fd,
  offset: hapticFile.offset,
  length: hapticFile.length,
};
let id = 0;
// 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。
audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
  id = value;
  console.info(`Succeeded in registering the source from fd, sourceId: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to register the source from fd. Code: ${err.code}, message: ${err.message}`);
});
```

## setAudioLatencyMode

```TypeScript
setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void
```

设置音频时延模式。

**起始版本：** 23

<!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void--><!--Device-AudioHapticManager-setAudioLatencyMode(id:int, latencyMode: AudioLatencyMode): void-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| latencyMode | [AudioLatencyMode](arkts-audio-audiohaptic-audiolatencymode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // 需要通过registerSource或registerSourceFromFd方法获取。

let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_FAST;

audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode);
```

## setStreamUsage

```TypeScript
setStreamUsage(id: number, usage: audio.StreamUsage): void
```

设置音频流使用类型。

**起始版本：** 23

<!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void--><!--Device-AudioHapticManager-setStreamUsage(id: int, usage: audio.StreamUsage): void-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| usage | audio.StreamUsage | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // 需要通过registerSource或registerSourceFromFd方法获取。

let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;

audioHapticManagerInstance.setStreamUsage(id, usage);
```

## unregisterSource

```TypeScript
unregisterSource(id: number): Promise<void>
```

取消注册音频和振动资源。使用Promise异步回调。 > **注意：** > > 对于不再需要使用的资源，建议应用及时取消注册，避免出现资源泄漏或资源数量超上限等问题。

**起始版本：** 23

<!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>--><!--Device-AudioHapticManager-unregisterSource(id: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id = 0; // 需要通过registerSource或registerSourceFromFd方法获取。

audioHapticManagerInstance.unregisterSource(id).then(() => {
  console.info('Succeeded in unregistering the source.');
}).catch((err: BusinessError) => {
  console.error(`Failed to unregister the source. Code: ${err.code}, message: ${err.message}`);
});
```
