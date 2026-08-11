# RingtonePlayer（系统接口）

系统铃声播放器，提供系统铃声的参数设置、参数获取、播放、停止等功能。在调用RingtonePlayer的接口前，需要先通过  
[getRingtonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneplayer)创建实例。

**起始版本：** 10

<!--Device-unnamed-export interface RingtonePlayer--><!--Device-unnamed-export interface RingtonePlayer-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## configure

```TypeScript
configure(options: RingtoneOptions, callback: AsyncCallback<void>): void
```

配置铃声播放参数。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-configure(options: RingtoneOptions, callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-configure(options: RingtoneOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## configure

```TypeScript
configure(options: RingtoneOptions): Promise<void>
```

配置铃声播放参数。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-configure(options: RingtoneOptions): Promise<void>--><!--Device-RingtonePlayer-configure(options: RingtoneOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## getAudioRendererInfo

```TypeScript
getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void
```

获取铃声使用的AudioRendererInfo。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void--><!--Device-RingtonePlayer-getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioRendererInfo&gt; | 是 |

## getAudioRendererInfo

```TypeScript
getAudioRendererInfo(): Promise<audio.AudioRendererInfo>
```

获取铃声使用的AudioRendererInfo。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-getAudioRendererInfo(): Promise<audio.AudioRendererInfo>--><!--Device-RingtonePlayer-getAudioRendererInfo(): Promise<audio.AudioRendererInfo>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;audio.AudioRendererInfo&gt; |

## getTitle

```TypeScript
getTitle(callback: AsyncCallback<string>): void
```

获取铃声标题。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-getTitle(callback: AsyncCallback<string>): void--><!--Device-RingtonePlayer-getTitle(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

获取铃声标题。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-getTitle(): Promise<string>--><!--Device-RingtonePlayer-getTitle(): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt'): void
```

取消监听音频中断事件。

**起始版本：** 10

<!--Device-RingtonePlayer-off(type: 'audioInterrupt'): void--><!--Device-RingtonePlayer-off(type: 'audioInterrupt'): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void--><!--Device-RingtonePlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioInterrupt' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放铃声播放器。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-release(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放铃声播放器。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-release(): Promise<void>--><!--Device-RingtonePlayer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

开始播放铃声。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-start(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## start

```TypeScript
start(): Promise<void>
```

开始播放铃声。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-start(): Promise<void>--><!--Device-RingtonePlayer-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止播放铃声。使用callback异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-stop(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## stop

```TypeScript
stop(): Promise<void>
```

停止播放铃声。使用Promise异步回调。

**起始版本：** 10

<!--Device-RingtonePlayer-stop(): Promise<void>--><!--Device-RingtonePlayer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## state

```TypeScript
readonly state: media.AVPlayerState
```

音频渲染器的状态。

**类型：** media.AVPlayerState

**起始版本：** 10

<!--Device-RingtonePlayer-readonly state: media.AVPlayerState--><!--Device-RingtonePlayer-readonly state: media.AVPlayerState-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。
