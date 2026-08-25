# CommonEventSubscriber

表示公共事件的订阅者。CommonEventSubscriber提供了对有序公共事件的 处理能力，包括获取和设置事件传递的Code和Data数据、查询当前公共事件 是否为有序或粘性公共事件、中止或清理有序公共事件的中止状态、结束对 当前有序公共事件的处理，以及获取订阅者的订阅信息等，适用于订阅者需要 对接收到的公共事件进行数据处理和流程控制的场景。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

## abortCommonEvent

```TypeScript
abortCommonEvent(callback: AsyncCallback<void>): void
```

添加有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以中止当前的有序公共事 件，使该公共事件不再向下一个订阅者传递。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## abortCommonEvent

```TypeScript
abortCommonEvent(): Promise<void>
```

添加有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以中止当前的有序公共事 件，使该公共事件不再向下一个订阅者传递。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## abortCommonEventSync

```TypeScript
abortCommonEventSync(): void
```

同步添加有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以中止当前的有序公共事 件，使该公共事件不再向下一个订阅者传递。

**起始版本：** 10

**系统能力：** SystemCapability.Notification.CommonEvent

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(callback: AsyncCallback<void>): void
```

清理有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以使该公共事件继续向下 一个订阅者传递。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(): Promise<void>
```

清理有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以使该公共事件继续向下 一个订阅者传递。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## clearAbortCommonEventSync

```TypeScript
clearAbortCommonEventSync(): void
```

同步清理有序公共事件的中止状态。当该接口与 [finishCommonEvent](#finishcommonevent)配合使用时，可以使该公共事件继续向下 一个订阅者传递。

**起始版本：** 10

**系统能力：** SystemCapability.Notification.CommonEvent

## finishCommonEvent

```TypeScript
finishCommonEvent(callback: AsyncCallback<void>): void
```

用于订阅者结束对当前有序公共事件的处理。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## finishCommonEvent

```TypeScript
finishCommonEvent(): Promise<void>
```

用于订阅者结束对当前有序公共事件的处理。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(callback: AsyncCallback<boolean>): void
```

获取当前有序公共事件是否处于中止状态。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(): Promise<boolean>
```

获取当前有序公共事件是否处于中止状态。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## getAbortCommonEventSync

```TypeScript
getAbortCommonEventSync(): boolean
```

同步获取当前有序公共事件是否处于中止状态。

**起始版本：** 10

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getCode

```TypeScript
getCode(): Promise<number>
```

获取有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getCodeSync

```TypeScript
getCodeSync(): number
```

同步获取有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getData

```TypeScript
getData(): Promise<string>
```

获取有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getDataSync

```TypeScript
getDataSync(): string
```

同步获取有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getSubscribeInfo

```TypeScript
getSubscribeInfo(): Promise<CommonEventSubscribeInfo>
```

获取订阅者的订阅信息。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isOrderedCommonEvent

```TypeScript
isOrderedCommonEvent(): Promise<boolean>
```

查询当前公共事件是否为有序公共事件。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isOrderedCommonEventSync

```TypeScript
isOrderedCommonEventSync(): boolean
```

同步查询当前公共事件是否为有序公共事件。

**起始版本：** 10

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isStickyCommonEvent

```TypeScript
isStickyCommonEvent(): Promise<boolean>
```

查询当前公共事件是否为一个粘性公共事件。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isStickyCommonEventSync

```TypeScript
isStickyCommonEventSync(): boolean
```

同步检查当前公共事件是否为一个粘性公共事件。

**起始版本：** 10

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

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCode

```TypeScript
setCode(code: number): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string, callback: AsyncCallback<void>): void
```

设置有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCodeAndDataSync

```TypeScript
setCodeAndDataSync(code: number, data: string): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| data | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCodeSync

```TypeScript
setCodeSync(code: number): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setData

```TypeScript
setData(data: string, callback: AsyncCallback<void>): void
```

设置有序公共事件传递的数据。使用callback异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setData

```TypeScript
setData(data: string): Promise<void>
```

设置有序公共事件传递的数据。使用Promise异步回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setDataSync

```TypeScript
setDataSync(data: string): void
```

同步设置有序公共事件传递的数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
