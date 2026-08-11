# AudioEffectManager (System API)

Implements audio effect management.

**Since:** 18

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

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;AudioEffectProperty&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

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

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;AudioEffectProperty&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

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

Checks whether the current device supports audio separation effect in system.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean--><!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offAudioSeparationEffectEnabledChange

```TypeScript
offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void
```

Unsubscribes from the system audio separation effect enabled state change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void--><!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onAudioSeparationEffectEnabledChange

```TypeScript
onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void
```

Subscribes to system audio separation effect enabled state change event.The audio separation effect state in system can be set by system playback controller application,other applications can use this function to listen the change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void--><!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setAudioEffectProperty

```TypeScript
setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void
```

Sets current audio effect properties.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void--><!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propertyArray | Array&lt;AudioEffectProperty&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

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

```TypeScript
setAudioSeparationEffectEnabled(enabled: boolean, uid: number, streamId?: number): Promise<void>
```

Sets audio separation effect enable or disable for specific application process,or for specific audio playback stream.This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |
| uid | number | Yes |
| streamId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |

## setAudioSeparationEffectVolume

```TypeScript
setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: number): Promise<void>
```

Sets audio separation effect volume for specific volume type.This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) | Yes |
| volume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) |
