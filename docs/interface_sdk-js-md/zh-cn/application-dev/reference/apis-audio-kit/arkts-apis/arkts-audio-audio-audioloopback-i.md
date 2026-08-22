# AudioLoopback

提供音频返听的相关接口。

在使用AudioLoopback的接口之前，需先通过[audio.createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md)获取AudioLoopback实例。

当启用音频返听时，系统会创建低时延渲染器与低时延采集器，实现低时延耳返功能。采集的音频直接通过内部路由返回到渲染器。对于渲染器，其音频焦点策略与 [STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md)相匹配。对于采集器，其音频焦点策略与[SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md)相匹配。

输入\输出设备由系统自动选择。如果当前输入\输出不支持低时延，则音频返听无法启用。在运行过程中，如果音频焦点被另一个音频流抢占，输入\输出设备切换到不支持低时延的设备，系统会自动禁用音频返听。

> **说明：**
> 
> - 本Interface首批接口从API version 20开始支持。

**起始版本：** 23

<!--Device-audio-interface AudioLoopback--><!--Device-audio-interface AudioLoopback-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## enable

```TypeScript
enable(enable: boolean): Promise<boolean>
```

启用或禁用音频返听器。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MICROPHONE

<!--Device-AudioLoopback-enable(enable: boolean): Promise<boolean>--><!--Device-AudioLoopback-enable(enable: boolean): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否启用音频返听器。true表示启用，false表示不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示功能执行成功；返回false表示功能执行失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getEqualizerPreset

```TypeScript
getEqualizerPreset(): AudioLoopbackEqualizerPreset
```

获取当前音频返听器的均衡器类型。

**起始版本：** 24

<!--Device-AudioLoopback-getEqualizerPreset(): AudioLoopbackEqualizerPreset--><!--Device-AudioLoopback-getEqualizerPreset(): AudioLoopbackEqualizerPreset-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | 返回当前音频返听器的均衡器类型。 <br>在没有被修改的情况下，默认的均衡器类型是FULL。 |

## getPreferredDevicePair

```TypeScript
getPreferredDevicePair(): AudioDevicePair | null
```

获取当前设备连接状态下系统推荐的返听音频输入输出设备组合。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioLoopback-getPreferredDevicePair(): AudioDevicePair | null--><!--Device-AudioLoopback-getPreferredDevicePair(): AudioDevicePair | null-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md) \| null | 返回系统推荐的音频输入输出设备组合。 <br>如果没有可用的输入输出设备组合，则返回null。 |

## getReverbPreset

```TypeScript
getReverbPreset(): AudioLoopbackReverbPreset
```

获取当前音频返听器的混响模式。

**起始版本：** 24

<!--Device-AudioLoopback-getReverbPreset(): AudioLoopbackReverbPreset--><!--Device-AudioLoopback-getReverbPreset(): AudioLoopbackReverbPreset-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | 返回当前音频返听器的混响模式。 <br>在没有被修改的情况下，默认的混响模式是THEATER。 |

## getStatus

```TypeScript
getStatus(): Promise<AudioLoopbackStatus>
```

获取音频返听状态。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioLoopback-getStatus(): Promise<AudioLoopbackStatus>--><!--Device-AudioLoopback-getStatus(): Promise<AudioLoopbackStatus>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | Promise对象，返回音频返听状态。 |

## getSupportedDevicePairs

```TypeScript
getSupportedDevicePairs(): Array<AudioDevicePair>
```

获取当前设备连接状态下支持返听的音频输入输出设备组合。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioLoopback-getSupportedDevicePairs(): Array<AudioDevicePair>--><!--Device-AudioLoopback-getSupportedDevicePairs(): Array<AudioDevicePair>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md)&gt; | 返回支持返听的音频输入输出设备数组。 <br>如果没有可用的输入输出设备组合，则返回空数组。 |

## getVolume

```TypeScript
getVolume(): double
```

获取音频返听输出音量。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioLoopback-getVolume(): double--><!--Device-AudioLoopback-getVolume(): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 返回当前音频返听输出音量，范围为[0.0, 1.0]。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = audioRenderer.getVolume();
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, volume) => {
  if (err) {
    console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the volume, volume: ${volume}.`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((volume) => {
  console.info(`Succeeded in obtaining the volume, volume: ${volume}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
});
```

## off('statusChange')

```TypeScript
off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void
```

取消监听音频状态事件。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioLoopback-off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'statusChange' | 是 | 事件回调类型，支持的事件为'statusChange'，当取消监听音频状态事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | 否 | 回调函数，返回当前音频返听的状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## offStatusChange

```TypeScript
offStatusChange(callback?: Callback<AudioLoopbackStatus>): void
```

Unsubscribes audio loopback status change event callback.

**起始版本：** 23

<!--Device-AudioLoopback-offStatusChange(callback?: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-offStatusChange(callback?: Callback<AudioLoopbackStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | 否 | Callback used to listen for the audio loopback status change event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## on('statusChange')

```TypeScript
on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void
```

监听返听状态变化事件（当AudioLoopback的状态发生变化时触发）。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioLoopback-on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'statusChange' | 是 | 事件回调类型，支持的事件为'statusChange'，当AudioLoopback的状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | 是 | 回调函数，返回当前音频返听的状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## onStatusChange

```TypeScript
onStatusChange(callback: Callback<AudioLoopbackStatus>): void
```

Subscribes to audio loopback status changes.

**起始版本：** 23

<!--Device-AudioLoopback-onStatusChange(callback: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-onStatusChange(callback: Callback<AudioLoopbackStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioLoopbackStatus](arkts-audio-audio-audioloopbackstatus-e.md)&gt; | 是 | Callback used to return the audio loopback status change event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## setEqualizerPreset

```TypeScript
setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean
```

设置音频返听器的均衡器类型。

**起始版本：** 24

<!--Device-AudioLoopback-setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean--><!--Device-AudioLoopback-setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preset | [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | 是 | 均衡器类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回均衡器类型是否设置成功。true表示成功，false表示不成功。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## setReverbPreset

```TypeScript
setReverbPreset(preset: AudioLoopbackReverbPreset): boolean
```

设置音频返听器的混响模式。

**起始版本：** 24

<!--Device-AudioLoopback-setReverbPreset(preset: AudioLoopbackReverbPreset): boolean--><!--Device-AudioLoopback-setReverbPreset(preset: AudioLoopbackReverbPreset): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preset | [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | 是 | 混响模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回混响模式是否设置成功。true表示成功，false表示不成功。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## setVolume

```TypeScript
setVolume(volume: double): Promise<void>
```

设置音频返听的音量。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioLoopback-setVolume(volume: double): Promise<void>--><!--Device-AudioLoopback-setVolume(volume: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | double | 是 | 音量值范围为[0.0, 1.0]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed, form 0.0 to 1.0. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});
```

```TypeScript
audioVolumeGroupManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the volume.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Succeeded in setting the volume.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(`setVolume Fail: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5, (err: BusinessError) => {
  if(err){
    console.error(`setVolume Fail: ${err}`);
    return;
  }
  console.info('setVolume Success!');
});
```

