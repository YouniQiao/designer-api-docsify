# AVSessionController

AVSessionController控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

> **说明：**
> 
> - 本Interface首批接口从API version 10开始支持。

**起始版本：** 10

<!--Device-avSession-interface AVSessionController--><!--Device-avSession-interface AVSessionController-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

销毁当前控制器，销毁后当前控制器不可再用。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-destroy(callback: AsyncCallback<void>): void--><!--Device-AVSessionController-destroy(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁当前控制器，销毁后当前控制器不可再用。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-destroy(): Promise<void>--><!--Device-AVSessionController-destroy(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVCallState

```TypeScript
getAVCallState(callback: AsyncCallback<AVCallState>): void
```

获取通话状态数据。结果通过callback异步回调方式返回。

**起始版本：** 11

<!--Device-AVSessionController-getAVCallState(callback: AsyncCallback<AVCallState>): void--><!--Device-AVSessionController-getAVCallState(callback: AsyncCallback<AVCallState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVCallState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVCallState

```TypeScript
getAVCallState(): Promise<AVCallState>
```

获取通话状态数据。结果通过Promise异步回调方式返回。

**起始版本：** 11

<!--Device-AVSessionController-getAVCallState(): Promise<AVCallState>--><!--Device-AVSessionController-getAVCallState(): Promise<AVCallState>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;AVCallState&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVMetadata

```TypeScript
getAVMetadata(callback: AsyncCallback<AVMetadata>): void
```

获取会话元数据。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getAVMetadata(callback: AsyncCallback<AVMetadata>): void--><!--Device-AVSessionController-getAVMetadata(callback: AsyncCallback<AVMetadata>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadata&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVMetadata

```TypeScript
getAVMetadata(): Promise<AVMetadata>
```

获取会话元数据。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVMetadata(): Promise<AVMetadata>--><!--Device-AVSessionController-getAVMetadata(): Promise<AVMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;AVMetadata&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVMetadataSync

```TypeScript
getAVMetadataSync(): AVMetadata
```

使用同步方法获取会话元数据。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVMetadataSync(): AVMetadata--><!--Device-AVSessionController-getAVMetadataSync(): AVMetadata-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| [AVMetadata](arkts-avsession-avsession-avmetadata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void
```

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void--><!--Device-AVSessionController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVPlaybackState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(): Promise<AVPlaybackState>
```

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVPlaybackState(): Promise<AVPlaybackState>--><!--Device-AVSessionController-getAVPlaybackState(): Promise<AVPlaybackState>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;AVPlaybackState&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVPlaybackStateSync

```TypeScript
getAVPlaybackStateSync(): AVPlaybackState
```

使用同步方法获取当前会话的播放状态。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVPlaybackStateSync(): AVPlaybackState--><!--Device-AVSessionController-getAVPlaybackStateSync(): AVPlaybackState-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueItems

```TypeScript
getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void
```

获取当前播放列表相关信息。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void--><!--Device-AVSessionController-getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AVQueueItem&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueItems

```TypeScript
getAVQueueItems(): Promise<Array<AVQueueItem>>
```

获取当前会话播放列表相关信息。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVQueueItems(): Promise<Array<AVQueueItem>>--><!--Device-AVSessionController-getAVQueueItems(): Promise<Array<AVQueueItem>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;AVQueueItem&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueItemsSync

```TypeScript
getAVQueueItemsSync(): Array<AVQueueItem>
```

使用同步方法获取当前会话播放列表相关信息。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVQueueItemsSync(): Array<AVQueueItem>--><!--Device-AVSessionController-getAVQueueItemsSync(): Array<AVQueueItem>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;AVQueueItem&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueTitle

```TypeScript
getAVQueueTitle(callback: AsyncCallback<string>): void
```

获取当前播放列表的名称。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getAVQueueTitle(callback: AsyncCallback<string>): void--><!--Device-AVSessionController-getAVQueueTitle(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueTitle

```TypeScript
getAVQueueTitle(): Promise<string>
```

获取当前会话播放列表的名称。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVQueueTitle(): Promise<string>--><!--Device-AVSessionController-getAVQueueTitle(): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getAVQueueTitleSync

```TypeScript
getAVQueueTitleSync(): string
```

使用同步方法获取当前会话播放列表的名称。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getAVQueueTitleSync(): string--><!--Device-AVSessionController-getAVQueueTitleSync(): string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getCallMetadata

```TypeScript
getCallMetadata(callback: AsyncCallback<CallMetadata>): void
```

获取通话会话的元数据。结果通过callback异步回调方式返回。

**起始版本：** 11

<!--Device-AVSessionController-getCallMetadata(callback: AsyncCallback<CallMetadata>): void--><!--Device-AVSessionController-getCallMetadata(callback: AsyncCallback<CallMetadata>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CallMetadata&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getCallMetadata

```TypeScript
getCallMetadata(): Promise<CallMetadata>
```

获取通话会话的元数据。结果通过Promise异步回调方式返回。

**起始版本：** 11

<!--Device-AVSessionController-getCallMetadata(): Promise<CallMetadata>--><!--Device-AVSessionController-getCallMetadata(): Promise<CallMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;CallMetadata&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getDesktopLyricState

```TypeScript
getDesktopLyricState(): Promise<DesktopLyricState>
```

获取当前会话桌面歌词状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-getDesktopLyricState(): Promise<DesktopLyricState>--><!--Device-AVSessionController-getDesktopLyricState(): Promise<DesktopLyricState>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;DesktopLyricState&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) |

## getExtras

```TypeScript
getExtras(callback: AsyncCallback<{[key: string]: Object}>): void
```

获取媒体提供方设置的自定义媒体数据包。使用callback异步回调。

**起始版本：** 10

<!--Device-AVSessionController-getExtras(callback: AsyncCallback<{[key: string]: Object}>): void--><!--Device-AVSessionController-getExtras(callback: AsyncCallback<{[key: string]: Object}>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{[key: string]: Object}&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## getExtras

```TypeScript
getExtras(): Promise<{[key: string]: Object}>
```

获取媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getExtras(): Promise<{[key: string]: Object}>--><!--Device-AVSessionController-getExtras(): Promise<{[key: string]: Object}>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;{[key: string]: Object}&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## getExtrasWithEvent

```TypeScript
getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>
```

根据远端分布式事件类型，获取远端分布式媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**起始版本：** 18

<!--Device-AVSessionController-getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>--><!--Device-AVSessionController-getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extraEvent | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;ExtraInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |

## getLaunchAbility

```TypeScript
getLaunchAbility(callback: AsyncCallback<WantAgent>): void
```

获取应用在会话中保存的WantAgent对象。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getLaunchAbility(callback: AsyncCallback<WantAgent>): void--><!--Device-AVSessionController-getLaunchAbility(callback: AsyncCallback<WantAgent>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getLaunchAbility

```TypeScript
getLaunchAbility(): Promise<WantAgent>
```

获取应用在会话中保存的WantAgent对象。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getLaunchAbility(): Promise<WantAgent>--><!--Device-AVSessionController-getLaunchAbility(): Promise<WantAgent>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getMediaCenterControlType

```TypeScript
getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>
```

获取应用通过[setMediaCenterControlType](arkts-avsession-avsession-avsession-i.md#setmediacentercontroltype)接口设置优先显示的控制类型列表。使用Promise异步回调。

如果应用未设置或者设置为空列表，则返回空列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>--><!--Device-AVSessionController-getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;AVMediaCenterControlType&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getOutputDevice

```TypeScript
getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void
```

获取播放设备信息。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void--><!--Device-AVSessionController-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;OutputDeviceInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 600101 |
| 600103 |

## getOutputDevice

```TypeScript
getOutputDevice(): Promise<OutputDeviceInfo>
```

获取播放设备信息。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getOutputDevice(): Promise<OutputDeviceInfo>--><!--Device-AVSessionController-getOutputDevice(): Promise<OutputDeviceInfo>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;OutputDeviceInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| 600101 |
| 600103 |

## getOutputDeviceSync

```TypeScript
getOutputDeviceSync(): OutputDeviceInfo
```

使用同步方法获取当前输出设备信息。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getOutputDeviceSync(): OutputDeviceInfo--><!--Device-AVSessionController-getOutputDeviceSync(): OutputDeviceInfo-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getRealPlaybackPositionSync

```TypeScript
getRealPlaybackPositionSync(): number
```

使用同步方法获取当前播放位置。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getRealPlaybackPositionSync(): long--><!--Device-AVSessionController-getRealPlaybackPositionSync(): long-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getSupportedLoopModes

```TypeScript
getSupportedLoopModes(): Promise<Array<LoopMode>>
```

获取应用支持的循环模式列表。使用Promise异步回调。

该列表通过[setSupportedLoopModes](arkts-avsession-avsession-avsession-i.md#setsupportedloopmodes)接口设置。如果应用未设置或者设置为空列表，则返回空列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getSupportedLoopModes(): Promise<Array<LoopMode>>--><!--Device-AVSessionController-getSupportedLoopModes(): Promise<Array<LoopMode>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;LoopMode&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getSupportedPlaySpeeds

```TypeScript
getSupportedPlaySpeeds(): Promise<Array<number>>
```

获取应用支持的播放倍速列表。使用Promise异步回调。

该列表通过[setSupportedPlaySpeeds](arkts-avsession-avsession-avsession-i.md#setsupportedplayspeeds)接口设置。如果应用未设置或者设置为空列表，则返回空列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getSupportedPlaySpeeds(): Promise<Array<double>>--><!--Device-AVSessionController-getSupportedPlaySpeeds(): Promise<Array<double>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;number&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getValidCommands

```TypeScript
getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void
```

获取会话支持的有效命令。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void--><!--Device-AVSessionController-getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AVControlCommandType&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getValidCommands

```TypeScript
getValidCommands(): Promise<Array<AVControlCommandType>>
```

获取会话支持的有效命令。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getValidCommands(): Promise<Array<AVControlCommandType>>--><!--Device-AVSessionController-getValidCommands(): Promise<Array<AVControlCommandType>>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;AVControlCommandType&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## getValidCommandsSync

```TypeScript
getValidCommandsSync(): Array<AVControlCommandType>
```

使用同步方法获取会话支持的有效命令。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-getValidCommandsSync(): Array<AVControlCommandType>--><!--Device-AVSessionController-getValidCommandsSync(): Array<AVControlCommandType>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;AVControlCommandType&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## isActive

```TypeScript
isActive(callback: AsyncCallback<boolean>): void
```

判断会话是否被激活。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-isActive(callback: AsyncCallback<boolean>): void--><!--Device-AVSessionController-isActive(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## isActive

```TypeScript
isActive(): Promise<boolean>
```

获取会话是否被激活。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-isActive(): Promise<boolean>--><!--Device-AVSessionController-isActive(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## isActiveSync

```TypeScript
isActiveSync(): boolean
```

使用同步方法判断会话是否被激活。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-isActiveSync(): boolean--><!--Device-AVSessionController-isActiveSync(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## isDesktopLyricEnabled

```TypeScript
isDesktopLyricEnabled(): Promise<boolean>
```

查询是否启用桌面歌词功能。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-isDesktopLyricEnabled(): Promise<boolean>--><!--Device-AVSessionController-isDesktopLyricEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) |

## isDesktopLyricVisible

```TypeScript
isDesktopLyricVisible(): Promise<boolean>
```

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-isDesktopLyricVisible(): Promise<boolean>--><!--Device-AVSessionController-isDesktopLyricVisible(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) |

## off('metadataChange')

```TypeScript
off(type: 'metadataChange', callback?: (data: AVMetadata) => void)
```

取消元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'metadataChange', callback?: (data: AVMetadata) => void)--><!--Device-AVSessionController-off(type: 'metadataChange', callback?: (data: AVMetadata) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'metadataChange' | 是 |
| callback | (data: AVMetadata) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('playbackStateChange')

```TypeScript
off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)
```

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)--><!--Device-AVSessionController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playbackStateChange' | 是 |
| callback | (state: AVPlaybackState) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('callMetadataChange')

```TypeScript
off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void
```

取消设置通话元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void--><!--Device-AVSessionController-off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callMetadataChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallMetadata&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('callStateChange')

```TypeScript
off(type: 'callStateChange', callback?: Callback<AVCallState>): void
```

取消设置通话状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'callStateChange', callback?: Callback<AVCallState>): void--><!--Device-AVSessionController-off(type: 'callStateChange', callback?: Callback<AVCallState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVCallState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('sessionDestroy')

```TypeScript
off(type: 'sessionDestroy', callback?: () => void)
```

取消监听会话的销毁事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'sessionDestroy', callback?: () => void)--><!--Device-AVSessionController-off(type: 'sessionDestroy', callback?: () => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionDestroy' | 是 |
| callback | () =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('activeStateChange')

```TypeScript
off(type: 'activeStateChange', callback?: (isActive: boolean) => void)
```

取消监听会话激活状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'activeStateChange', callback?: (isActive: boolean) => void)--><!--Device-AVSessionController-off(type: 'activeStateChange', callback?: (isActive: boolean) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activeStateChange' | 是 |
| callback | (isActive: boolean) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('validCommandChange')

```TypeScript
off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)
```

取消监听会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)--><!--Device-AVSessionController-off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'validCommandChange' | 是 |
| callback | (commands: Array&lt;AVControlCommandType&gt;) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('outputDeviceChange')

```TypeScript
off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

取消监听分布式设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSessionController-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChange' | 是 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('sessionEvent')

```TypeScript
off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void
```

取消会话事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionEvent' | 是 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('queueItemsChange')

```TypeScript
off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void
```

取消播放列表变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void--><!--Device-AVSessionController-off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'queueItemsChange' | 是 |
| callback | (items: Array&lt;AVQueueItem&gt;) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('queueTitleChange')

```TypeScript
off(type: 'queueTitleChange', callback?: (title: string) => void): void
```

取消播放列表名称变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'queueTitleChange', callback?: (title: string) => void): void--><!--Device-AVSessionController-off(type: 'queueTitleChange', callback?: (title: string) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'queueTitleChange' | 是 |
| callback | (title: string) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('extrasChange')

```TypeScript
off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void
```

取消自定义媒体数据包变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'extrasChange' | 是 |
| callback | (extras: {[key: string]: Object}) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('customDataChange')

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

取消自定义数据监听。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'customDataChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offDesktopLyricEnabled

```TypeScript
offDesktopLyricEnabled(callback?: Callback<boolean>): void
```

取消桌面歌词启用状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-offDesktopLyricEnabled(callback?: Callback<boolean>): void--><!--Device-AVSessionController-offDesktopLyricEnabled(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offDesktopLyricStateChanged

```TypeScript
offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void
```

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void--><!--Device-AVSessionController-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DesktopLyricState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offDesktopLyricVisibilityChanged

```TypeScript
offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void
```

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void--><!--Device-AVSessionController-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offMediaCenterControlTypeChanged

```TypeScript
offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void
```

取消控制类型列表变化的监听事件。

取消后将不再对该事件进行监听。其中控制类型列表由应用通过[setMediaCenterControlType](arkts-avsession-avsession-avsession-i.md#setmediacentercontroltype)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void--><!--Device-AVSessionController-offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVMediaCenterControlType&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offSupportedLoopModesChange

```TypeScript
offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void
```

取消支持的循环模式列表变化事件监听。

取消后将不再对该事件进行监听。其中循环模式列表由应用通过[setSupportedLoopModes](arkts-avsession-avsession-avsession-i.md#setsupportedloopmodes)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void--><!--Device-AVSessionController-offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;LoopMode&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## offSupportedPlaySpeedsChange

```TypeScript
offSupportedPlaySpeedsChange(callback?: Callback<Array<number>>): void
```

取消支持的播放倍速列表变化事件监听。

取消后将不再对该事件进行监听。其中播放倍速列表由应用通过[setSupportedPlaySpeeds](arkts-avsession-avsession-avsession-i.md#setsupportedplayspeeds)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-offSupportedPlaySpeedsChange(callback?: Callback<Array<double>>): void--><!--Device-AVSessionController-offSupportedPlaySpeedsChange(callback?: Callback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('metadataChange')

```TypeScript
on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)
```

设置元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)--><!--Device-AVSessionController-on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'metadataChange' | 是 |
| filter | Array&lt;keyof AVMetadata&gt; \| 'all' | 是 |
| callback | (data: AVMetadata) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('playbackStateChange')

```TypeScript
on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)
```

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)--><!--Device-AVSessionController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playbackStateChange' | 是 |
| filter | Array&lt;keyof AVPlaybackState&gt; \| 'all' | 是 |
| callback | (state: AVPlaybackState) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('callMetadataChange')

```TypeScript
on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void
```

设置通话元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void--><!--Device-AVSessionController-on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callMetadataChange' | 是 |
| filter | Array&lt;keyof CallMetadata&gt; \| 'all' | 是 | 'all'表示关注通话元数据所有字段变化；Array&lt;keyof CallMetadata&gt; 表示关注Array中的字 段变化。\|
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallMetadata&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('callStateChange')

```TypeScript
on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void
```

设置通话状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void--><!--Device-AVSessionController-on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| filter | Array&lt;keyof AVCallState&gt; \| 'all' | 是 | 'all' 表示关注通话状态所有字段变化；Array&lt;keyof AVCallState&gt;表示关注Array中的字段变 化。\|
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVCallState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('sessionDestroy')

```TypeScript
on(type: 'sessionDestroy', callback: () => void)
```

会话销毁的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'sessionDestroy', callback: () => void)--><!--Device-AVSessionController-on(type: 'sessionDestroy', callback: () => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionDestroy' | 是 |
| callback | () =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('activeStateChange')

```TypeScript
on(type: 'activeStateChange', callback: (isActive: boolean) => void)
```

会话的激活状态的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'activeStateChange', callback: (isActive: boolean) => void)--><!--Device-AVSessionController-on(type: 'activeStateChange', callback: (isActive: boolean) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activeStateChange' | 是 |
| callback | (isActive: boolean) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('validCommandChange')

```TypeScript
on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)
```

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)--><!--Device-AVSessionController-on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'validCommandChange' | 是 |
| callback | (commands: Array&lt;AVControlCommandType&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('outputDeviceChange')

```TypeScript
on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

设置播放设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSessionController-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'outputDeviceChange' | 是 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('sessionEvent')

```TypeScript
on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void
```

媒体控制器设置会话自定义事件变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionEvent' | 是 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('queueItemsChange')

```TypeScript
on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void
```

媒体控制器设置会话自定义播放列表变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void--><!--Device-AVSessionController-on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'queueItemsChange' | 是 |
| callback | (items: Array&lt;AVQueueItem&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('queueTitleChange')

```TypeScript
on(type: 'queueTitleChange', callback: (title: string) => void): void
```

媒体控制器设置会话自定义播放列表的名称变化的监听器。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'queueTitleChange', callback: (title: string) => void): void--><!--Device-AVSessionController-on(type: 'queueTitleChange', callback: (title: string) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'queueTitleChange' | 是 |
| callback | (title: string) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('extrasChange')

```TypeScript
on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void
```

媒体控制器设置自定义媒体数据包事件变化的监听器。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'extrasChange' | 是 |
| callback | (extras: {[key: string]: Object}) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('customDataChange')

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

注册从远程设备发送的自定义数据的监听器。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'customDataChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onDesktopLyricEnabled

```TypeScript
onDesktopLyricEnabled(callback: Callback<boolean>): void
```

桌面歌词功能启用状态变更的监听事件。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-onDesktopLyricEnabled(callback: Callback<boolean>): void--><!--Device-AVSessionController-onDesktopLyricEnabled(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onDesktopLyricStateChanged

```TypeScript
onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void
```

桌面歌词状态变更的监听事件。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void--><!--Device-AVSessionController-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DesktopLyricState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onDesktopLyricVisibilityChanged

```TypeScript
onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void
```

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void--><!--Device-AVSessionController-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onMediaCenterControlTypeChanged

```TypeScript
onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void
```

注册控制类型列表变化的监听事件。使用callback异步回调。

其中控制类型列表由应用通过[setMediaCenterControlType](arkts-avsession-avsession-avsession-i.md#setmediacentercontroltype)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void--><!--Device-AVSessionController-onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVMediaCenterControlType&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onSupportedLoopModesChange

```TypeScript
onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void
```

注册支持的循环模式列表变化的监听事件。使用callback异步回调。

其中循环模式列表由应用通过[setSupportedLoopModes](arkts-avsession-avsession-avsession-i.md#setsupportedloopmodes)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void--><!--Device-AVSessionController-onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;LoopMode&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## onSupportedPlaySpeedsChange

```TypeScript
onSupportedPlaySpeedsChange(callback: Callback<Array<number>>): void
```

注册支持的播放倍速列表变化的监听事件。使用callback异步回调。

其中播放倍速列表由应用通过[setSupportedPlaySpeeds](arkts-avsession-avsession-avsession-i.md#setsupportedplayspeeds)接口设置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-onSupportedPlaySpeedsChange(callback: Callback<Array<double>>): void--><!--Device-AVSessionController-onSupportedPlaySpeedsChange(callback: Callback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## sendAVKeyEvent

```TypeScript
sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void
```

发送按键事件到会话。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 600105 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 600106 |
| 600101 |
| 600103 |
| 600102 |

## sendAVKeyEvent

```TypeScript
sendAVKeyEvent(event: KeyEvent): Promise<void>
```

发送按键事件到控制器对应的会话。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent): Promise<void>--><!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| 600105 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 600106 |
| 600101 |
| 600103 |
| 600102 |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void
```

通过会话控制器发送自定义命令到其对应的会话。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | string | 是 |
| args | {[key: string]: Object} | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600106](../errorcode-avsession.md#6600106-会话未激活) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>
```

通过会话控制器发送自定义控制命令到其对应的会话。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>--><!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | string | 是 |
| args | {[key: string]: Object} | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600106](../errorcode-avsession.md#6600106-会话未激活) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void
```

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

> **说明：**
> 
> 媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口
> [on('play')](avSession.AVSession.on(type: 'play', callback: () => void))、
> [on('pause')](avSession.AVSession.on(type: 'pause', callback: () => void))等。

**起始版本：** 10

<!--Device-AVSessionController-sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600106](../errorcode-avsession.md#6600106-会话未激活) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVControlCommand): Promise<void>
```

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

> **说明：**
> 
> 媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口
> [on('play')](avSession.AVSession.on(type: 'play', callback: () => void))、
> [on('pause')](avSession.AVSession.on(type: 'pause', callback: () => void))等。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-sendControlCommand(command: AVControlCommand): Promise<void>--><!--Device-AVSessionController-sendControlCommand(command: AVControlCommand): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600106](../errorcode-avsession.md#6600106-会话未激活) |
| [6600107](../errorcode-avsession.md#6600107-命令消息过载) |

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

发送私有数据到远端设备。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-sendCustomData(data: Record<string, Object>): Promise<void>--><!--Device-AVSessionController-sendCustomData(data: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record&lt;string, Object&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## setDesktopLyricState

```TypeScript
setDesktopLyricState(state: DesktopLyricState): Promise<void>
```

设置当前会话桌面歌词状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-setDesktopLyricState(state: DesktopLyricState): Promise<void>--><!--Device-AVSessionController-setDesktopLyricState(state: DesktopLyricState): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) |

## setDesktopLyricVisible

```TypeScript
setDesktopLyricVisible(visible: boolean): Promise<void>
```

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVSessionController-setDesktopLyricVisible(visible: boolean): Promise<void>--><!--Device-AVSessionController-setDesktopLyricVisible(visible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| visible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |
| [6600110](../errorcode-avsession.md#6600110-应用程序的桌面歌词功能未开启) |
| [6600111](../errorcode-avsession.md#6600111-当前设备不支持桌面歌词功能) |

## skipToQueueItem

```TypeScript
skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void
```

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过callback异步回调方式返回。

**起始版本：** 10

<!--Device-AVSessionController-skipToQueueItem(itemId: int, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-skipToQueueItem(itemId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## skipToQueueItem

```TypeScript
skipToQueueItem(itemId: number): Promise<void>
```

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-skipToQueueItem(itemId: int): Promise<void>--><!--Device-AVSessionController-skipToQueueItem(itemId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## sessionId

```TypeScript
readonly sessionId: string
```

AVSessionController对象唯一的会话标识。

**类型：** string

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVSessionController-readonly sessionId: string--><!--Device-AVSessionController-readonly sessionId: string-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core
