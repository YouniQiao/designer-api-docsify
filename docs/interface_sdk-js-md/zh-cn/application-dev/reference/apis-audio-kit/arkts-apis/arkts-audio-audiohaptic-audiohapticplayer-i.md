# AudioHapticPlayer

音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过 [createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer)创建 实例。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

## 导入模块

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## isMuted

```TypeScript
isMuted(type: AudioHapticType): boolean
```

查询该音振类型是否被静音。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AudioHapticType](arkts-audio-audiohaptic-audiohaptictype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

取消监听流结束事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'endOfStream' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void
```

取消监听音频中断事件。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | 否 |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

监听流结束事件（音频流播放结束时触发）。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'endOfStream' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放音振播放器。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setLoop

```TypeScript
setLoop(loop: boolean): Promise<void>
```

设置音振播放器循环播放。使用Promise异步回调。

> **注意：**&gt;
> 该方法需在音振播放器销毁前调用。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loop | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |

## setVolume

```TypeScript
setVolume(volume: number): Promise<void>
```

设置音振播放器的音量。使用Promise异步回调。

> **注意：**&gt;
> 该方法需在音振播放器释放前调用。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-参数超过取值范围) |

## start

```TypeScript
start(): Promise<void>
```

开始播放。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## stop

```TypeScript
stop(): Promise<void>
```

停止播放。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |
