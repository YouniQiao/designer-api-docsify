# AudioEffectManager（系统接口）

Implements audio effect management.

**起始版本：** 18

<!--Device-audio-interface AudioEffectManager--><!--Device-audio-interface AudioEffectManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

## getAudioEffectProperty

```TypeScript
getAudioEffectProperty(): Array<AudioEffectProperty>
```

Gets current audio effect properties.

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;AudioEffectProperty&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## 示例

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

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>--><!--Device-AudioEffectManager-getSupportedAudioEffectProperty(): Array<AudioEffectProperty>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;AudioEffectProperty&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## 示例

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

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean--><!--Device-AudioEffectManager-isAudioSeparationEffectSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

let isSupported: boolean = audioEffectManager.isAudioSeparationEffectSupported();
console.info(`Audio separation effect is supported: ${isSupported}`);
```

## offAudioSeparationEffectEnabledChange

```TypeScript
offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void
```

去订阅系统音频分离效果使能状态变更事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void--><!--Device-AudioEffectManager-offAudioSeparationEffectEnabledChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

audioEffectManager.offAudioSeparationEffectEnabledChange();
```

## onAudioSeparationEffectEnabledChange

```TypeScript
onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void
```

订阅系统音频分离效果使能状态变更事件。系统中的音频分离效果状态可由系统播放控制器应用设定，其他应用程序可以使用此函数来监听change事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void--><!--Device-AudioEffectManager-onAudioSeparationEffectEnabledChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

audioEffectManager.onAudioSeparationEffectEnabledChange((isEnabled: boolean) => {
  console.info(`Audio separation effect enabled state changed: ${isEnabled}`);
});
```

## setAudioEffectProperty

```TypeScript
setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void
```

Sets current audio effect properties.

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

<!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void--><!--Device-AudioEffectManager-setAudioEffectProperty(propertyArray: Array<AudioEffectProperty>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propertyArray | Array&lt;AudioEffectProperty&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## 示例

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

设置特定应用进程的音频分离效果开关。或用于特定的音频播放流。该接口使用promise返回结果。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectEnabled(enabled: boolean, uid: int, streamId?: long): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| uid | number | 是 |
| streamId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

audioEffectManager.setAudioSeparationEffectEnabled(true, 10001).then(() => {
  console.info('Succeeded in setting audio separation effect enabled.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set audio separation effect enabled. Code: ${err.code}, message: ${err.message}`);
});
```

## setAudioSeparationEffectVolume

```TypeScript
setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: number): Promise<void>
```

设置特定音量类型的音频分离效果音量。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_SYSTEM_AUDIO_EFFECTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>--><!--Device-AudioEffectManager-setAudioSeparationEffectVolume(type: AudioSeparationVolumeType, volume: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AudioSeparationVolumeType](arkts-audio-audio-audioseparationvolumetype-e-sys.md) | 是 |
| volume | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

audioEffectManager.setAudioSeparationEffectVolume(audio.AudioSeparationVolumeType.VOLUME_TYPE_VOCAL, 0.5).then(() => {
  console.info('Succeeded in setting audio separation effect volume.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set audio separation effect volume. Code: ${err.code}, message: ${err.message}`);
});
```
