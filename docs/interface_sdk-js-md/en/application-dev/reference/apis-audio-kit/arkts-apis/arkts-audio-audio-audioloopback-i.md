# AudioLoopback

提供音频返听的相关接口。

在使用AudioLoopback的接口之前，需先通过[audio.createAudioLoopback](arkts-audio-audio-createaudioloopback-f.md#createaudioloopback)获取AudioLoopback实例。

当启用音频返听时，系统会创建低时延渲染器与低时延采集器，实现低时延耳返功能。采集的音频直接通过内部路由返回到渲染器。对于渲染器，其音频焦点策略与  
[STREAM_USAGE_MUSIC](arkts-audio-audio-streamusage-e.md)相匹配。对于采集器，其音频焦点策略与[SOURCE_TYPE_MIC](arkts-audio-audio-sourcetype-e.md)相匹配。

输入\输出设备由系统自动选择。如果当前输入\输出不支持低时延，则音频返听无法启用。在运行过程中，如果音频焦点被另一个音频流抢占，输入\输出设备切换到不支持低时延的设备，系统会自动禁用音频返听。

> **说明：**
> 
> - 本Interface首批接口从API version 20开始支持。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioLoopback--><!--Device-audio-interface AudioLoopback-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## enable

```TypeScript
enable(enable: boolean): Promise<boolean>
```

启用或禁用音频返听器。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioLoopback-enable(enable: boolean): Promise<boolean>--><!--Device-AudioLoopback-enable(enable: boolean): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 表示是否启用音频返听器。true表示启用，false表示不启用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示功能执行成功；返回false表示功能执行失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied. |

## getEqualizerPreset

```TypeScript
getEqualizerPreset(): AudioLoopbackEqualizerPreset
```

获取当前音频返听器的均衡器类型。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioLoopback-getEqualizerPreset(): AudioLoopbackEqualizerPreset--><!--Device-AudioLoopback-getEqualizerPreset(): AudioLoopbackEqualizerPreset-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | 返回当前音频返听器的均衡器类型。 &lt;br&gt;在没有被修改的情况下，默认的均衡器类型是FULL。 |

## getPreferredDevicePair

```TypeScript
getPreferredDevicePair(): AudioDevicePair | null
```

获取当前设备连接状态下系统推荐的返听音频输入输出设备组合。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLoopback-getPreferredDevicePair(): AudioDevicePair | null--><!--Device-AudioLoopback-getPreferredDevicePair(): AudioDevicePair | null-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDevicePair](arkts-audio-audio-audiodevicepair-i.md) | 返回系统推荐的音频输入输出设备组合。 &lt;br&gt;如果没有可用的输入输出设备组合，则返回null。 |

## getReverbPreset

```TypeScript
getReverbPreset(): AudioLoopbackReverbPreset
```

获取当前音频返听器的混响模式。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioLoopback-getReverbPreset(): AudioLoopbackReverbPreset--><!--Device-AudioLoopback-getReverbPreset(): AudioLoopbackReverbPreset-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | 返回当前音频返听器的混响模式。 &lt;br&gt;在没有被修改的情况下，默认的混响模式是THEATER。 |

## getStatus

```TypeScript
getStatus(): Promise<AudioLoopbackStatus>
```

获取音频返听状态。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioLoopback-getStatus(): Promise<AudioLoopbackStatus>--><!--Device-AudioLoopback-getStatus(): Promise<AudioLoopbackStatus>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioLoopbackStatus&gt; | Promise对象，返回音频返听状态。 |

## getSupportedDevicePairs

```TypeScript
getSupportedDevicePairs(): Array<AudioDevicePair>
```

获取当前设备连接状态下支持返听的音频输入输出设备组合。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLoopback-getSupportedDevicePairs(): Array<AudioDevicePair>--><!--Device-AudioLoopback-getSupportedDevicePairs(): Array<AudioDevicePair>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;AudioDevicePair&gt; | 返回支持返听的音频输入输出设备数组。 &lt;br&gt;如果没有可用的输入输出设备组合，则返回空数组。 |

## getVolume

ArkTS-Dyn:
```TypeScript
getVolume(): number
```

ArkTS-Sta:
```TypeScript
getVolume(): double
```

获取音频返听输出音量。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioLoopback-getVolume(): double--><!--Device-AudioLoopback-getVolume(): double-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 返回当前音频返听输出音量，范围为[0.0, 1.0]。 |

## off('statusChange')

```TypeScript
off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void
```

取消监听音频状态事件。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioLoopback-off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'statusChange' | Yes | 事件回调类型，支持的事件为'statusChange'，当取消监听音频状态事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioLoopbackStatus&gt; | No | 回调函数，返回当前音频返听的状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## offStatusChange

```TypeScript
offStatusChange(callback?: Callback<AudioLoopbackStatus>): void
```

Unsubscribes audio loopback status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioLoopback-offStatusChange(callback?: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-offStatusChange(callback?: Callback<AudioLoopbackStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioLoopbackStatus&gt; | No | Callback used to listen for the audio loopback status change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## on('statusChange')

```TypeScript
on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void
```

监听返听状态变化事件（当AudioLoopback的状态发生变化时触发）。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AudioLoopback-on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'statusChange' | Yes | 事件回调类型，支持的事件为'statusChange'，当AudioLoopback的状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioLoopbackStatus&gt; | Yes | 回调函数，返回当前音频返听的状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## onStatusChange

```TypeScript
onStatusChange(callback: Callback<AudioLoopbackStatus>): void
```

Subscribes to audio loopback status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioLoopback-onStatusChange(callback: Callback<AudioLoopbackStatus>): void--><!--Device-AudioLoopback-onStatusChange(callback: Callback<AudioLoopbackStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioLoopbackStatus&gt; | Yes | Callback used to return the audio loopback status change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## setEqualizerPreset

```TypeScript
setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean
```

设置音频返听器的均衡器类型。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioLoopback-setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean--><!--Device-AudioLoopback-setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preset | [AudioLoopbackEqualizerPreset](arkts-audio-audio-audioloopbackequalizerpreset-e.md) | Yes | 均衡器类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回均衡器类型是否设置成功。true表示成功，false表示不成功。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## setReverbPreset

```TypeScript
setReverbPreset(preset: AudioLoopbackReverbPreset): boolean
```

设置音频返听器的混响模式。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioLoopback-setReverbPreset(preset: AudioLoopbackReverbPreset): boolean--><!--Device-AudioLoopback-setReverbPreset(preset: AudioLoopbackReverbPreset): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preset | [AudioLoopbackReverbPreset](arkts-audio-audio-audioloopbackreverbpreset-e.md) | Yes | 混响模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回混响模式是否设置成功。true表示成功，false表示不成功。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |

## setVolume

ArkTS-Dyn:
```TypeScript
setVolume(volume: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setVolume(volume: double): Promise<void>
```

设置音频返听的音量。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioLoopback-setVolume(volume: double): Promise<void>--><!--Device-AudioLoopback-setVolume(volume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 音量值范围为[0.0, 1.0]。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed, form 0.0 to 1.0. |

