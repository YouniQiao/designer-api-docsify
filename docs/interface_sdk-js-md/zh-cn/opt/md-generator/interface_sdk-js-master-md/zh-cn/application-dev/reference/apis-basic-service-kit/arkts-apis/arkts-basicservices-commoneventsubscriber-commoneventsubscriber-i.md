# CommonEventSubscriber

表示公共事件的订阅者。CommonEventSubscriber提供了对有序公共事件的处理能力，包括获取和设置事件传递的Code和Data数据、查询当前公共事件是否为有序或粘性公共事件、中止或清理有序公共事件的中止状态、结束对当前有序公共事件的处理，以及获取订阅者的订阅信息等，适用于订阅者需要对接收到的公共事件进行数据处理和流程控制的场景。

**起始版本：** 7

<!--Device-unnamed-export interface CommonEventSubscriber--><!--Device-unnamed-export interface CommonEventSubscriber-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

## abortCommonEvent

```TypeScript
abortCommonEvent(callback: AsyncCallback<void>): void
```

添加有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用callback异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-abortCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-abortCommonEvent(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## abortCommonEvent

```TypeScript
abortCommonEvent(): Promise<void>
```

添加有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用Promise异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-abortCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-abortCommonEvent(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## abortCommonEventSync

```TypeScript
abortCommonEventSync(): void
```

同步添加有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**起始版本：** 10

<!--Device-CommonEventSubscriber-abortCommonEventSync(): void--><!--Device-CommonEventSubscriber-abortCommonEventSync(): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(callback: AsyncCallback<void>): void
```

清理有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用callback异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-clearAbortCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-clearAbortCommonEvent(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(): Promise<void>
```

清理有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用Promise异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-clearAbortCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-clearAbortCommonEvent(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## clearAbortCommonEventSync

```TypeScript
clearAbortCommonEventSync(): void
```

同步清理有序公共事件的中止状态。当该接口与  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent)配合使用时，可以使该公共事件继续向下一个订阅者传递。

**起始版本：** 10

<!--Device-CommonEventSubscriber-clearAbortCommonEventSync(): void--><!--Device-CommonEventSubscriber-clearAbortCommonEventSync(): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

## finishCommonEvent

```TypeScript
finishCommonEvent(callback: AsyncCallback<void>): void
```

用于订阅者结束对当前有序公共事件的处理。使用callback异步回调。

**起始版本：** 9

<!--Device-CommonEventSubscriber-finishCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-finishCommonEvent(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## finishCommonEvent

```TypeScript
finishCommonEvent(): Promise<void>
```

用于订阅者结束对当前有序公共事件的处理。使用Promise异步回调。

**起始版本：** 9

<!--Device-CommonEventSubscriber-finishCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-finishCommonEvent(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(callback: AsyncCallback<boolean>): void
```

获取当前有序公共事件是否处于中止状态。使用callback异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-getAbortCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-getAbortCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(): Promise<boolean>
```

获取当前有序公共事件是否处于中止状态。使用Promise异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-getAbortCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-getAbortCommonEvent(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## getAbortCommonEventSync

```TypeScript
getAbortCommonEventSync(): boolean
```

同步获取当前有序公共事件是否处于中止状态。

**起始版本：** 10

<!--Device-CommonEventSubscriber-getAbortCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-getAbortCommonEventSync(): boolean-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| boolean |

## getCode

```TypeScript
getCode(callback: AsyncCallback<number>): void
```

获取有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getCode(callback: AsyncCallback<int>): void--><!--Device-CommonEventSubscriber-getCode(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getCode

```TypeScript
getCode(): Promise<number>
```

获取有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getCode(): Promise<int>--><!--Device-CommonEventSubscriber-getCode(): Promise<int>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

## getCodeSync

```TypeScript
getCodeSync(): number
```

同步获取有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getCodeSync(): int--><!--Device-CommonEventSubscriber-getCodeSync(): int-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| number |

## getData

```TypeScript
getData(callback: AsyncCallback<string>): void
```

获取有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getData(callback: AsyncCallback<string>): void--><!--Device-CommonEventSubscriber-getData(callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getData

```TypeScript
getData(): Promise<string>
```

获取有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getData(): Promise<string>--><!--Device-CommonEventSubscriber-getData(): Promise<string>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## getDataSync

```TypeScript
getDataSync(): string
```

同步获取有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getDataSync(): string--><!--Device-CommonEventSubscriber-getDataSync(): string-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| string |

## getSubscribeInfo

```TypeScript
getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void
```

获取订阅者的订阅信息。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void--><!--Device-CommonEventSubscriber-getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getSubscribeInfo

```TypeScript
getSubscribeInfo(): Promise<CommonEventSubscribeInfo>
```

获取订阅者的订阅信息。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getSubscribeInfo(): Promise<CommonEventSubscribeInfo>--><!--Device-CommonEventSubscriber-getSubscribeInfo(): Promise<CommonEventSubscribeInfo>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md)&gt; |

## getSubscribeInfoSync

```TypeScript
getSubscribeInfoSync(): CommonEventSubscribeInfo
```

同步获取订阅者的订阅信息。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-getSubscribeInfoSync(): CommonEventSubscribeInfo--><!--Device-CommonEventSubscriber-getSubscribeInfoSync(): CommonEventSubscribeInfo-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| [CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md) |

## isOrderedCommonEvent

```TypeScript
isOrderedCommonEvent(callback: AsyncCallback<boolean>): void
```

查询当前公共事件是否为有序公共事件。使用callback异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-isOrderedCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-isOrderedCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## isOrderedCommonEvent

```TypeScript
isOrderedCommonEvent(): Promise<boolean>
```

查询当前公共事件是否为有序公共事件。使用Promise异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-isOrderedCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-isOrderedCommonEvent(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## isOrderedCommonEventSync

```TypeScript
isOrderedCommonEventSync(): boolean
```

同步查询当前公共事件是否为有序公共事件。

**起始版本：** 10

<!--Device-CommonEventSubscriber-isOrderedCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-isOrderedCommonEventSync(): boolean-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| boolean |

## isStickyCommonEvent

```TypeScript
isStickyCommonEvent(callback: AsyncCallback<boolean>): void
```

查询当前公共事件是否为一个粘性公共事件。使用callback异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-isStickyCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-isStickyCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## isStickyCommonEvent

```TypeScript
isStickyCommonEvent(): Promise<boolean>
```

查询当前公共事件是否为一个粘性公共事件。使用Promise异步回调。

**起始版本：** 7

<!--Device-CommonEventSubscriber-isStickyCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-isStickyCommonEvent(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## isStickyCommonEventSync

```TypeScript
isStickyCommonEventSync(): boolean
```

同步检查当前公共事件是否为一个粘性公共事件。

**起始版本：** 10

<!--Device-CommonEventSubscriber-isStickyCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-isStickyCommonEventSync(): boolean-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| boolean |

## setCode

```TypeScript
setCode(code: number, callback: AsyncCallback<void>): void
```

设置有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCode(code: int, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setCode(code: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setCode

```TypeScript
setCode(code: number): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCode(code: int): Promise<void>--><!--Device-CommonEventSubscriber-setCode(code: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string, callback: AsyncCallback<void>): void
```

设置有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string): Promise<void>--><!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setCodeAndDataSync

```TypeScript
setCodeAndDataSync(code: number, data: string): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCodeAndDataSync(code: int, data: string): void--><!--Device-CommonEventSubscriber-setCodeAndDataSync(code: int, data: string): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setCodeSync

```TypeScript
setCodeSync(code: number): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setCodeSync(code: int): void--><!--Device-CommonEventSubscriber-setCodeSync(code: int): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setData

```TypeScript
setData(data: string, callback: AsyncCallback<void>): void
```

设置有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setData(data: string, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setData(data: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setData

```TypeScript
setData(data: string): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setData(data: string): Promise<void>--><!--Device-CommonEventSubscriber-setData(data: string): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setDataSync

```TypeScript
setDataSync(data: string): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonEventSubscriber-setDataSync(data: string): void--><!--Device-CommonEventSubscriber-setDataSync(data: string): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
