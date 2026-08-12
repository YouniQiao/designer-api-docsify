# SoundPool

音频池提供了系统声音的加载、播放、音量设置、循环设置、停止播放和资源卸载等功能，在调用SoundPool的接口前，需要先通过  
[media.createSoundPool](../../../reference/apis-media-kit/arkts-apis-media-f.md)创建实例。

> **说明：**
> 
> - 在使用SoundPool实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。
> > - [on('loadComplete')](SoundPool.on(type: 'loadComplete', callback: Callback&lt;int&gt;))：监听资源加载完成。建议开发者监听此回调以确
> 保音频在加载完成后进行播放。
> > -
> [on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))：监听播
> 放完成，同时返回播放结束的音频的streamId。
> > - [on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))：监听播放完成。
> > - [on('error')](SoundPool.on(type: 'error', callback: ErrorCallback))：监听错误事件。
> > - [on('errorOccurred')](SoundPool.on(type:'errorOccurred', callback:Callback&lt;ErrorInfo&gt;))：监听错误事件，同时返回
> [errorInfo](arkts-media-soundpool-errorinfo-i.md#ErrorInfo)。
> 
> - SoundPool目前不支持后台播放、设置音频打断等音频焦点策略和跳过音频头尾的静音帧。SoundPool低时延播放可参考
> [使用SoundPool播放短音频(ArkTS)](../../../media/media/using-soundpool-for-playback.md)。

**起始版本：** 10

<!--Device-unnamed-export declare interface SoundPool--><!--Device-unnamed-export declare interface SoundPool-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

## load

```TypeScript
load(uri: string, callback: AsyncCallback<number>): void
```

加载音频资源。使用callback异步回调。

通过callback异步回调获取资源ID，入参URL通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过  
[load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](#load)或者  
[load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](#load-3)实现。

> **说明：**
> 
> - 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
> 
> - 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**起始版本：** 10

<!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## load

```TypeScript
load(uri: string): Promise<number>
```

加载音频资源。使用Promise异步回调。

通过Promise异步回调获取资源ID，入参URL通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过  
[load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](#load)或者  
[load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](#load-3)实现。

> **说明：**
> 
> - 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
> 
> - 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**起始版本：** 10

<!--Device-SoundPool-load(uri: string): Promise<int>--><!--Device-SoundPool-load(uri: string): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## load

```TypeScript
load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void
```

加载音频资源。使用callback异步回调。

通过callback异步回调获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

> **说明：**
> 
> - 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
> 
> - 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**起始版本：** 10

<!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| offset | number | 是 |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## load

```TypeScript
load(fd: number, offset: number, length: number): Promise<number>
```

加载音频资源。使用Promise异步回调。

通过Promise异步回调获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

> **说明：**
> 
> - 将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。
> 
> - 同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**起始版本：** 10

<!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>--><!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| offset | number | 是 |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## off('loadComplete')

```TypeScript
off(type: 'loadComplete'): void
```

取消监听资源的加载完成。

**起始版本：** 10

<!--Device-SoundPool-off(type: 'loadComplete'): void--><!--Device-SoundPool-off(type: 'loadComplete'): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'loadComplete' | 是 |

## off('playFinished')

```TypeScript
off(type: 'playFinished'): void
```

取消监听音频池资源播放完成。

**起始版本：** 10

<!--Device-SoundPool-off(type: 'playFinished'): void--><!--Device-SoundPool-off(type: 'playFinished'): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |

## off('error')

```TypeScript
off(type: 'error'): void
```

取消监听音频池的错误事件。

**起始版本：** 10

<!--Device-SoundPool-off(type: 'error'): void--><!--Device-SoundPool-off(type: 'error'): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |

## off('playFinishedWithStreamId')

```TypeScript
off(type: 'playFinishedWithStreamId'): void
```

取消监听音频池资源播放完成。

**起始版本：** 18

<!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void--><!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinishedWithStreamId' | 是 |

## off('errorOccurred')

```TypeScript
off(type: 'errorOccurred', callback?:Callback<ErrorInfo>): void
```

取消监听音频池的错误事件。

**起始版本：** 20

<!--Device-SoundPool-off(type: 'errorOccurred', callback?:Callback<ErrorInfo>): void--><!--Device-SoundPool-off(type: 'errorOccurred', callback?:Callback<ErrorInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'errorOccurred' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | 否 |

## on('loadComplete')

```TypeScript
on(type: 'loadComplete', callback: Callback<number>): void
```

音频池资源加载完成监听。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'loadComplete' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on('playFinished')

```TypeScript
on(type: 'playFinished', callback: Callback<void>): void
```

音频池资源播放完成监听。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void--><!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听[SoundPool](../../../reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool)的错误事件，该事件仅用于错误提示。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void--><!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on('playFinishedWithStreamId')

```TypeScript
on(type: 'playFinishedWithStreamId', callback: Callback<number>): void
```

音频池资源播放完成监听，同时返回播放结束的音频的streamId。使用callback异步回调。

当仅单独注册[on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))事件回调或者  
[on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))事件回调时，当音频播放完成的时候，都会触发注册的回调。

当同时注册[on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))事件回调和  
[on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;))事件回调时，当音频播放完成的时候，仅会触发'playFinishedWithStreamId'事件回调，不会触发'playFinished'事件回调。

**起始版本：** 18

<!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinishedWithStreamId' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## on('errorOccurred')

```TypeScript
on(type:'errorOccurred', callback:Callback<ErrorInfo>): void
```

监听[SoundPool](../../../reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool)的错误事件，并返回包含错误码、错误发生阶段、资源ID和音频流ID的[ErrorInfo](arkts-media-soundpool-errorinfo-i.md#ErrorInfo)。使用callback异步回调。

**起始版本：** 20

<!--Device-SoundPool-on(type:'errorOccurred', callback:Callback<ErrorInfo>): void--><!--Device-SoundPool-on(type:'errorOccurred', callback:Callback<ErrorInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'errorOccurred' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | 是 |

## play

```TypeScript
play(soundID: number, params: PlayParameters, callback: AsyncCallback<number>): void
```

播放音频资源，获取音频流streamID。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| soundID | number | 是 |
| params | [PlayParameters](arkts-media-soundpool-playparameters-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## play

```TypeScript
play(soundID: number, callback: AsyncCallback<number>): void
```

使用默认参数播放音频资源，获取音频流streamID。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| soundID | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## play

```TypeScript
play(soundID: number, params?: PlayParameters): Promise<number>
```

播放音频资源，获取音频流streamID。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>--><!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| soundID | number | 是 |
| params | [PlayParameters](arkts-media-soundpool-playparameters-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放音频池实例。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-release(callback: AsyncCallback<void>): void--><!--Device-SoundPool-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## release

```TypeScript
release(): Promise<void>
```

释放音频池实例。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-release(): Promise<void>--><!--Device-SoundPool-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setInterruptMode

```TypeScript
setInterruptMode(interruptMode: media.SoundInterruptMode): void
```

设置同一ID音频在播放时的打断模式。创建soundPool之后，该接口仅在首次调用soundPool的Play函数之前设置有效，期间可多次设置，否则将默认使用  
[SAME_SOUND_INTERRUPT](../../../reference/apis-media-kit/arkts-apis-media-e.md)，即对同一ID的音频，如果前者尚未播放完成，后者在播放前会先打断前者的播放。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void--><!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interruptMode | media.SoundInterruptMode | 是 |

## setLoop

```TypeScript
setLoop(streamID: number, loop: number, callback: AsyncCallback<void>): void
```

设置循环模式。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| loop | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setLoop

```TypeScript
setLoop(streamID: number, loop: number): Promise<void>
```

设置循环模式。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>--><!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| loop | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setPriority

```TypeScript
setPriority(streamID: number, priority: number, callback: AsyncCallback<void>): void
```

设置音频流播放的优先级。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| priority | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setPriority

```TypeScript
setPriority(streamID: number, priority: number): Promise<void>
```

设置音频流优先级。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>--><!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| priority | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setRate

```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void
```

设置音频流播放速率。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| rate | audio.AudioRendererRate | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setRate

```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate): Promise<void>
```

设置音频流的播放速率。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| rate | audio.AudioRendererRate | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setVolume

```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number, callback: AsyncCallback<void>): void
```

设置音频流播放音量。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| [leftVolume](arkts-media-soundpool-playparameters-i.md) | number | 是 |
| [rightVolume](arkts-media-soundpool-playparameters-i.md) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## setVolume

```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number): Promise<void>
```

设置音频流的播放音量。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| [leftVolume](arkts-media-soundpool-playparameters-i.md) | number | 是 |
| [rightVolume](arkts-media-soundpool-playparameters-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## stop

```TypeScript
stop(streamID: number, callback: AsyncCallback<void>): void
```

停止播放音频资源。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## stop

```TypeScript
stop(streamID: number): Promise<void>
```

停止streamID对应的音频播放。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-stop(streamID: int): Promise<void>--><!--Device-SoundPool-stop(streamID: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamID | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## unload

```TypeScript
unload(soundID: number, callback: AsyncCallback<void>): void
```

卸载音频资源。使用callback异步回调。

**起始版本：** 10

<!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| soundID | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |

## unload

```TypeScript
unload(soundID: number): Promise<void>
```

卸载音频资源。使用Promise异步回调。

**起始版本：** 10

<!--Device-SoundPool-unload(soundID: int): Promise<void>--><!--Device-SoundPool-unload(soundID: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| soundID | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |
