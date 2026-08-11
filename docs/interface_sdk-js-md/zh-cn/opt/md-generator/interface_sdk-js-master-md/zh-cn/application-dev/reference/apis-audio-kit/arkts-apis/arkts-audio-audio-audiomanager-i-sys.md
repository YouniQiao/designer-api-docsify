# AudioManager

音频音量和设备管理。

在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager)获取AudioManager实例。

**起始版本：** 7

<!--Device-audio-interface AudioManager--><!--Device-audio-interface AudioManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

## disableSafeMediaVolume

```TypeScript
disableSafeMediaVolume(): Promise<void>
```

user disable the safe media volume state.

**起始版本：** 12

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-disableSafeMediaVolume(): Promise<void>--><!--Device-AudioManager-disableSafeMediaVolume(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.disableSafeMediaVolume().then(() => {
  console.info('disableSafeMediaVolume success.');
}).catch((err: BusinessError) => {
  console.error(`disableSafeMediaVolume fail: ${err.code},${err.message}`);
});
```

## getCollaborativeManager

```TypeScript
getCollaborativeManager(): AudioCollaborativeManager
```

获取协同播放管理实例

**起始版本：** 20

<!--Device-AudioManager-getCollaborativeManager(): AudioCollaborativeManager--><!--Device-AudioManager-getCollaborativeManager(): AudioCollaborativeManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioCollaborativeManager](arkts-audio-audio-audiocollaborativemanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getEffectManager

```TypeScript
getEffectManager(): AudioEffectManager
```

Obtains an {@link AudioEffectManager} instance.

**起始版本：** 18

<!--Device-AudioManager-getEffectManager(): AudioEffectManager--><!--Device-AudioManager-getEffectManager(): AudioEffectManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioEffectManager](arkts-audio-audio-audioeffectmanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

let audioEffectManager: audio.AudioEffectManager = audioManager.getEffectManager();
```

## getExtraParameters

```TypeScript
getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>
```

Obtains the values of a certain key. This method uses a promise to return the query result.

**起始版本：** 11

<!--Device-AudioManager-getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>--><!--Device-AudioManager-getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainKey | string | 是 |
| subKeys | Array&lt;string&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, string&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subKeys: Array<String> = ['key_example'];
audioManager.getExtraParameters('key_example', subKeys).then((value: Record<string, string>) => {
  console.info(`Promise returned to indicate that the value of the audio extra parameters is obtained ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get the audio extra parameters ${err}`);
});
```

## getRecordingManager

```TypeScript
getRecordingManager(): AudioRecordingManager
```

获取录音管理器实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioManager-getRecordingManager(): AudioRecordingManager--><!--Device-AudioManager-getRecordingManager(): AudioRecordingManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<VolumeEvent>): void
```

Listens for system volume change events. This method uses a callback to get volume change events.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** ohos.multimedia.audio.AudioVolumeManager#event:volumeChange

<!--Device-AudioManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'volumeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | 是 |

## 示例

```TypeScript
audioManager.on('volumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

## on('ringerModeChange')

```TypeScript
on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void
```

Listens for ringer mode change events. This method uses a callback to get ringer mode changes.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** ohos.multimedia.audio.AudioVolumeGroupManager#event:ringerModeChange

<!--Device-AudioManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void--><!--Device-AudioManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'ringerModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRingMode&gt; | 是 |

## 示例

```TypeScript
audioManager.on('ringerModeChange', (ringerMode: audio.AudioRingMode) => {
  console.info(`Updated ringermode: ${ringerMode}`);
});
```

## setAudioScene

```TypeScript
setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void
```

Sets the audio scene mode to change audio strategies. This method uses an asynchronous callback to return the result.

**起始版本：** 8

<!--Device-AudioManager-setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void--><!--Device-AudioManager-setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioScene(audio.AudioScene.AUDIO_SCENE_PHONE_CALL, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the audio scene mode. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the audio scene mode.');
});
```

## setAudioScene

```TypeScript
setAudioScene(scene: AudioScene): Promise<void>
```

Sets the audio scene mode to change audio strategies. This method uses a promise to return the result.

**起始版本：** 8

<!--Device-AudioManager-setAudioScene(scene: AudioScene): Promise<void>--><!--Device-AudioManager-setAudioScene(scene: AudioScene): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioScene(audio.AudioScene.AUDIO_SCENE_PHONE_CALL).then(() => {
  console.info('Promise returned to indicate a successful setting of the audio scene mode.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the audio scene mode ${err}`);
});
```

## setExtraParameters

```TypeScript
setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>
```

Sets extra audio parameters. This method uses a promise to return the result.

**起始版本：** 11

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>--><!--Device-AudioManager-setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainKey | string | 是 |
| kvpairs | Record&lt;string, string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let kvpairs = {} as Record<string, string>;
kvpairs = {
  'key_example': 'value_example'
};

audioManager.setExtraParameters('key_example', kvpairs).then(() => {
  console.info('Promise returned to indicate a successful setting of the extra parameters.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the audio extra parameters ${err}`);
});
```
