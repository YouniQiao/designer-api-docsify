# AudioHapticPlayer

音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过  
[createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer)创建实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-audioHaptic-interface AudioHapticPlayer--><!--Device-audioHaptic-interface AudioHapticPlayer-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## isMuted

```TypeScript
isMuted(type: AudioHapticType): boolean
```

查询该音振类型是否被静音。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-isMuted(type: AudioHapticType): boolean--><!--Device-AudioHapticPlayer-isMuted(type: AudioHapticType): boolean-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AudioHapticType](arkts-audio-audiohaptic-audiohaptictype-e.md) | Yes | 音振类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示查询的音振类型是否被静音。true表示静音，false表示非静音。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Parameter verification failed. |

## Examples

```TypeScript
let audioHapticType: audioHaptic.AudioHapticType = audioHaptic.AudioHapticType.AUDIO_HAPTIC_TYPE_AUDIO;

let result: boolean = audioHapticPlayerInstance.isMuted(audioHapticType);
```

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

取消监听流结束事件。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AudioHapticPlayer-off(type: 'endOfStream', callback?: Callback<void>): void--><!--Device-AudioHapticPlayer-off(type: 'endOfStream', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | 事件回调类型，支持的事件为'endOfStream'，当取消监听流结束事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 回调函数，无返回结果。 |

## Examples

```TypeScript
// Cancel all subscriptions to the event.
audioHapticPlayerInstance.off('endOfStream');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let endOfStreamCallback = () => {
  console.info(`Receive the callback of endOfStream.`);
};

audioHapticPlayerInstance.on('endOfStream', endOfStreamCallback);

audioHapticPlayerInstance.off('endOfStream', endOfStreamCallback);
```

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void
```

取消监听音频中断事件。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AudioHapticPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void--><!--Device-AudioHapticPlayer-off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | 事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | No | 回调函数，返回中断事件信息。 |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

// Cancel all subscriptions to the event.
audioHapticPlayerInstance.off('audioInterrupt');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let isPlaying: boolean; // An identifier specifying whether rendering is in progress.
let isDucked: boolean; // An identifier specifying whether the audio volume is reduced.
let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the audioHapticPlayerInstance receives the interruptEvent callback and performs processing based on the content in the callback.
  // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
  // Note: In the default focus strategy, INTERRUPT_HINT_RESUME maps to the force type INTERRUPT_SHARE, and others map to INTERRUPT_FORCE. Therefore, the value of forceType does not need to be checked.
  // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // The audio focus event has been forcibly executed by the system. The application needs to update its status and displayed content.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // The audio stream has been paused and temporarily loses the focus. It will receive the interruptEvent corresponding to resume when it is able to regain the focus.
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // The audio stream has been stopped and permanently loses the focus. The user must manually trigger the operation to resume rendering.
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // The audio stream is rendered at a reduced volume.
        console.info('Force ducked. Update volume status');
        isDucked = true; // A simplified processing indicating several operations for updating the volume status.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // The audio stream is rendered at the normal volume.
        console.info('Force unducked. Update volume status');
        isDucked = false; // A simplified processing indicating several operations for updating the volume status.
        break;
      default:
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // The audio focus event needs to be operated by the application, which can choose the processing mode. It is recommended that the application process the event according to the value of InterruptHint.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // It is recommended that the application continue rendering. (The audio stream has been forcibly paused and temporarily lost the focus. It can resume rendering now.)
        // The INTERRUPT_HINT_RESUME operation must be proactively executed by the application and cannot be forcibly executed by the system. Therefore, the INTERRUPT_HINT_RESUME event must map to INTERRUPT_SHARE.
        console.info('Resume force paused renderer or ignore');
        // To continue rendering, the application must perform the required operations.
        break;
      default:
        break;
    }
  }
};

audioHapticPlayerInstance.on('audioInterrupt', audioInterruptCallback);

audioHapticPlayerInstance.off('audioInterrupt', audioInterruptCallback);
```

## offAudioInterrupt

```TypeScript
offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void
```

Unsubscribes audio interrupt event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioHapticPlayer-offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void--><!--Device-AudioHapticPlayer-offAudioInterrupt(callback?: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | No | Callback used to listen for audio interrupt info. |

## offEndOfStream

```TypeScript
offEndOfStream(callback?: Callback<void>): void
```

Unsubscribes end of stream event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioHapticPlayer-offEndOfStream(callback?: Callback<void>): void--><!--Device-AudioHapticPlayer-offEndOfStream(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback used to listen for the playback end of stream. |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

监听流结束事件（音频流播放结束时触发）。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AudioHapticPlayer-on(type: 'endOfStream', callback: Callback<void>): void--><!--Device-AudioHapticPlayer-on(type: 'endOfStream', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | 事件回调类型，支持的事件为'endOfStream'，当音频流播放结束时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数，无返回结果。 |

## Examples

```TypeScript
audioHapticPlayerInstance.on('endOfStream', () => {
  console.info(`Receive the callback of endOfStream.`);
});
```

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AudioHapticPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void--><!--Device-AudioHapticPlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | 事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | Yes | 回调函数，返回中断事件信息。 |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let isPlaying: boolean; // An identifier specifying whether rendering is in progress.
let isDucked: boolean; // An identifier specifying whether the audio volume is reduced.

audioHapticPlayerInstance.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
  // When an audio interruption event occurs, the audioHapticPlayerInstance receives the interruptEvent callback and performs processing based on the content in the callback.
  // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
  // Note: In the default focus strategy, INTERRUPT_HINT_RESUME maps to the force type INTERRUPT_SHARE, and others map to INTERRUPT_FORCE. Therefore, the value of forceType does not need to be checked.
  // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // The audio focus event has been forcibly executed by the system. The application needs to update its status and displayed content.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // The audio stream has been paused and temporarily loses the focus. It will receive the interruptEvent corresponding to resume when it is able to regain the focus.
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // The audio stream has been stopped and permanently loses the focus. The user must manually trigger the operation to resume rendering.
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // A simplified processing indicating several operations for switching the application to the paused state.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // The audio stream is rendered at a reduced volume.
        console.info('Force ducked. Update volume status');
        isDucked = true; // A simplified processing indicating several operations for updating the volume status.
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // The audio stream is rendered at the normal volume.
        console.info('Force unducked. Update volume status');
        isDucked = false; // A simplified processing indicating several operations for updating the volume status.
        break;
      default:
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // The audio focus event needs to be operated by the application, which can choose the processing mode. It is recommended that the application process the event according to the value of InterruptHint.
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // It is recommended that the application continue rendering. (The audio stream has been forcibly paused and temporarily lost the focus. It can resume rendering now.)
        // The INTERRUPT_HINT_RESUME operation must be proactively executed by the application and cannot be forcibly executed by the system. Therefore, the INTERRUPT_HINT_RESUME event must map to INTERRUPT_SHARE.
        console.info('Resume force paused renderer or ignore');
        // To continue rendering, the application must perform the required operations.
        break;
      default:
        break;
    }
  }
});
```

## onAudioInterrupt

```TypeScript
onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void
```

Subscribes audio interrupt event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioHapticPlayer-onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void--><!--Device-AudioHapticPlayer-onAudioInterrupt(callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | Yes | Callback used to listen for audio interrupt info. |

## onEndOfStream

```TypeScript
onEndOfStream(callback: Callback<void>): void
```

Subscribes end of stream event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AudioHapticPlayer-onEndOfStream(callback: Callback<void>): void--><!--Device-AudioHapticPlayer-onEndOfStream(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to listen for the playback end of stream. |

## release

```TypeScript
release(): Promise<void>
```

释放音振播放器。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-release(): Promise<void>--><!--Device-AudioHapticPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400105 | Service died. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.release().then(() => {
  console.info(`Promise returned to indicate that release the audio haptic player successfully.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to release the audio haptic player. ${err}`);
});
```

## setLoop

```TypeScript
setLoop(loop: boolean): Promise<void>
```

设置音振播放器循环播放。使用Promise异步回调。

> **注意：**
> 
> 该方法需在音振播放器销毁前调用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-setLoop(loop: boolean): Promise<void>--><!--Device-AudioHapticPlayer-setLoop(loop: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loop | boolean | Yes | 是否循环播放。true表示循环播放，false表示不循环播放。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operate not permit in current state. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.setLoop(true).then(() => {
  console.info('Promise returned to indicate that set player loop successfully.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set player loop. ${err}`);
});
```

## setVolume

ArkTS-Dyn:
```TypeScript
setVolume(volume: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setVolume(volume: double): Promise<void>
```

设置音振播放器的音量。使用Promise异步回调。

> **注意：**
> 
> 该方法需在音振播放器释放前调用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-setVolume(volume: double): Promise<void>--><!--Device-AudioHapticPlayer-setVolume(volume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 取值范围为[0.00, 1.00]，其中1.00表示最大音量（100%）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operate not permit in current state. |
| 5400105 | Service died. |
| 5400108 | Parameter out of range. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.setVolume(0.5).then(() => {
  console.info('Promise returned to indicate that set volume successfully.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set volume. ${err}`);
});
```

## start

```TypeScript
start(): Promise<void>
```

开始播放。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-start(): Promise<void>--><!--Device-AudioHapticPlayer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operate not permit. |
| 5400103 | IO error. |
| 5400105 | Service died. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.start().then(() => {
  console.info(`Promise returned to indicate that start playing successfully.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to start playing. ${err}`);
});
```

## stop

```TypeScript
stop(): Promise<void>
```

停止播放。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-stop(): Promise<void>--><!--Device-AudioHapticPlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operate not permit. |
| 5400105 | Service died. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioHapticPlayerInstance.stop().then(() => {
  console.info(`Promise returned to indicate that stop playing successfully.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to stop playing. ${err}`);
});
```

