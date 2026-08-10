# AudioManager

音频音量和设备管理。

在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-audio-audio-getaudiomanager-f.md#getaudiomanager)获取AudioManager实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioManager--><!--Device-audio-interface AudioManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## disableSafeMediaVolume

```TypeScript
disableSafeMediaVolume(): Promise<void>
```

user disable the safe media volume state.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-disableSafeMediaVolume(): Promise<void>--><!--Device-AudioManager-disableSafeMediaVolume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system App. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioManager-getCollaborativeManager(): AudioCollaborativeManager--><!--Device-AudioManager-getCollaborativeManager(): AudioCollaborativeManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [AudioCollaborativeManager](arkts-audio-audio-audiocollaborativemanager-i-sys.md) | 协同播放管理实例 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system App. |

## getEffectManager

```TypeScript
getEffectManager(): AudioEffectManager
```

Obtains an {@link AudioEffectManager} instance.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioManager-getEffectManager(): AudioEffectManager--><!--Device-AudioManager-getEffectManager(): AudioEffectManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [AudioEffectManager](arkts-audio-audio-audioeffectmanager-i-sys.md) | AudioEffectManager instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system App. |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioEffectManager: audio.AudioEffectManager = audioManager.getEffectManager();
```

## getExtraParameters

```TypeScript
getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>
```

Obtains the values of a certain key. This method uses a promise to return the query result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioManager-getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>--><!--Device-AudioManager-getExtraParameters(mainKey: string, subKeys?: Array<string>): Promise<Record<string, string>>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mainKey | string | Yes | Main key of the audio parameters to get. |
| subKeys | Array&lt;string&gt; | No | Sub keys of the audio parameters to get. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, string&gt;&gt; | Promise used to return the key-value pairs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 202 | Not system App. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioManager-getRecordingManager(): AudioRecordingManager--><!--Device-AudioManager-getRecordingManager(): AudioRecordingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRecordingManager](arkts-audio-audio-audiorecordingmanager-i-sys.md) | 返回音频记录管理器的实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## on('volumeChange')

```TypeScript
on(type: 'volumeChange', callback: Callback<VolumeEvent>): void
```

Listens for system volume change events. This method uses a callback to get volume change events.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeManager#event:volumeChange

<!--Device-AudioManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioManager-on(type: 'volumeChange', callback: Callback<VolumeEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'volumeChange' | Yes | Type of the event to listen for. Only the volumeChange event is supported. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VolumeEvent&gt; | Yes | Callback used to get the system volume change event. |

## Examples

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

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioVolumeGroupManager#event:ringerModeChange

<!--Device-AudioManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void--><!--Device-AudioManager-on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'ringerModeChange' | Yes | Type of the event to listen for. Only the ringerModeChange event is supported. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioRingMode&gt; | Yes | Callback used to get the updated ringer mode. |

## Examples

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

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioManager-setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void--><!--Device-AudioManager-setAudioScene(scene: AudioScene, callback: AsyncCallback<void> ): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | Yes | Audio scene mode. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

## Examples

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

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioManager-setAudioScene(scene: AudioScene): Promise<void>--><!--Device-AudioManager-setAudioScene(scene: AudioScene): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | [AudioScene](arkts-audio-audio-audioscene-e.md) | Yes | Audio scene mode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

## Examples

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioManager-setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>--><!--Device-AudioManager-setExtraParameters(mainKey: string, kvpairs: Record<string, string>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mainKey | string | Yes | Main key of the audio parameters to set. |
| kvpairs | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes | Key-value pairs with subkeys and values to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Not system App. |

## Examples

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

