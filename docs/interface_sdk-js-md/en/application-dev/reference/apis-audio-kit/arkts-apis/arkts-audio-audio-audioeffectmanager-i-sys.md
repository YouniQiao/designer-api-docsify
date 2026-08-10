# AudioEffectManager (System API)

Implements audio effect management.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioEffectManager--><!--Device-audio-interface AudioEffectManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAudioEffectProperty

```TypeScript
getAudioEffectProperty(): Array<AudioEffectProperty>
```

Gets current audio effect properties.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;AudioEffectProperty&gt; | Array of current audio effect properties. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | System error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let propertyArray: Array<audio.AudioEffectProperty> = audioStreamManager.getAudioEffectProperty();
  console.info(`The effect modes are: ${propertyArray}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAudioEffectProperty ERROR: ${error}`);
}
```

## getSupportedAudioEffectProperty

```TypeScript
getSupportedAudioEffectProperty(): Array<AudioEffectProperty>
```

Gets supported audio effect properties based on current devices.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;AudioEffectProperty&gt; | Array of supported audio effect properties. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | System error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let propertyArray: Array<audio.AudioEffectProperty> = audioStreamManager.getSupportedAudioEffectProperty();
  console.info(`The effect modes are: ${propertyArray}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getSupportedAudioEffectProperty ERROR: ${error}`);
}
```

## isAudioSeparationEffectSupported

```TypeScript
isAudioSeparationEffectSupported(): boolean
```

检查当前设备是否支持系统中的音频分离效果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean--><!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前设备是否支持音频分离效果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## offAudioSeparationEffectEnabledChange

```TypeScript
offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void
```

去订阅系统音频分离效果使能状态变更事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void--><!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | 订阅函数中用于取消订阅的回调。 如果不使用此参数，则之前在当前进程中订阅的所有回调都将被取消订阅 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |

## onAudioSeparationEffectEnabledChange

```TypeScript
onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void
```

订阅系统音频分离效果使能状态变更事件。系统中的音频分离效果状态可由系统播放控制器应用设定，其他应用程序可以使用此函数来监听change事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void--><!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | 监听系统音频分离效果的回调 启用状态更改事件 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## setAudioEffectProperty

```TypeScript
setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void
```

Sets current audio effect properties.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void--><!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propertyArray | Array&lt;AudioEffectProperty&gt; | Yes | array of audio effect property to be set. Notice that only one effect property name in each effect property category should be set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. Possible causes: 1. More than one effect property name of the same effect property category are in the input array. 2. The input audioEffectProperties are not supported by the current device. 3. The name or catergory of the input audioEffectProperties is incorrect. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | System error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let propertyArray: Array<audio.AudioEffectProperty> = audioEffectManager.getAudioEffectProperty();
  console.info(`The effect modes are: ${propertyArray}`);
  audioEffectManager.setAudioEffectProperty(propertyArray);
} catch (err) {
  let error = err as BusinessError;
  console.error(`setAudioEffectProperty ERROR: ${error}`);
}
```

## setAudioSeparationEffectEnabled

ArkTS-Dyn:
```TypeScript
setAudioSeparationEffectEnabled(enabled: boolean, uid: number, streamId?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>
```

设置特定应用进程的音频分离效果开关。或用于特定的音频播放流。该接口使用promise返回结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 所需的效果状态，true表示启用，false表示禁用 |
| uid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要添加效果的目标应用程序进程的uid。 &lt;br&gt;取值限定为整数。 |
| streamId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | No | 要添加效果的目标音频播放流的ID，播放应用程序 可以使用{@link AudioRenderer#getAudioStreamId}来获取 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 不会返回任何值的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |
| 6800104 | Effect is not supported in this device. |

## setAudioSeparationEffectVolume

ArkTS-Dyn:
```TypeScript
setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>
```

设置特定音量类型的音频分离效果音量。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) | Yes | 要设置音量的类型 |
| volume | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标卷值。 &lt;br&gt;取值范围：[0,1]。 &lt;br&gt;Value range: [0,1]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | Audio service error occurs like service died. |
| 6800104 | Effect is not supported in this device. |

