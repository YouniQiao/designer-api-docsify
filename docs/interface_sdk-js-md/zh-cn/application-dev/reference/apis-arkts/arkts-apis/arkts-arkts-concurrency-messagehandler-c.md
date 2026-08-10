# MessageHandler

Handles messages and provides message scheduling capabilities

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-concurrency-export class MessageHandler--><!--Device-concurrency-export class MessageHandler-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())
```

Constructs a new MessageHandler with a handler function

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())--><!--Device-MessageHandler-constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | (message: concurrency.Message) =&gt; void | 是 | the handler function to process messages. |
| worker | [EAWorker](arkts-arkts-eaworker-c.md) \| undefined | 是 | the worker to associate with this handler. |

## getWorker

```TypeScript
getWorker(): EAWorker
```

Returns the worker associated with this handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-getWorker(): EAWorker--><!--Device-MessageHandler-getWorker(): EAWorker-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EAWorker](arkts-arkts-eaworker-c.md) | the associated worker |

## hasCallbacks

```TypeScript
hasCallbacks(callback: () => void): boolean
```

Checks whether the handler has the specified callback pending

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-hasCallbacks(callback: () => void): boolean--><!--Device-MessageHandler-hasCallbacks(callback: () => void): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () =&gt; void | 是 | the callback to check for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the callback is pending, false otherwise |

## hasMessages

```TypeScript
hasMessages(what: int): boolean
```

Checks whether the handler has messages with the specified what code

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-hasMessages(what: int): boolean--><!--Device-MessageHandler-hasMessages(what: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code to check for. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if such messages exist, false otherwise |

## hasMessages

```TypeScript
hasMessages(what: int, obj: Any): boolean
```

Checks whether the handler has messages with the specified what code and object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-hasMessages(what: int, obj: Any): boolean--><!--Device-MessageHandler-hasMessages(what: int, obj: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code to check for. &lt;br&gt;The value should be an integer. |
| obj | Any | 是 | the object to check for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if such messages exist, false otherwise |

## post

```TypeScript
post(callback: () => void): boolean
```

Posts a callback to the handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-post(callback: () => void): boolean--><!--Device-MessageHandler-post(callback: () => void): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () =&gt; void | 是 | the callback to post. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the callback was successfully posted, false otherwise |

## removeCallbacks

```TypeScript
removeCallbacks(callback: () => void): boolean
```

Removes pending callbacks matching the specified callback

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-removeCallbacks(callback: () => void): boolean--><!--Device-MessageHandler-removeCallbacks(callback: () => void): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () =&gt; void | 是 | the callback to remove. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the callback was removed, false otherwise |

## removeMessages

```TypeScript
removeMessages(what: int): boolean
```

Removes pending messages with the specified what code

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-removeMessages(what: int): boolean--><!--Device-MessageHandler-removeMessages(what: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if messages were removed, false otherwise |

## removeMessages

```TypeScript
removeMessages(what: int, obj: Any): boolean
```

Removes pending messages with the specified what code and object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-removeMessages(what: int, obj: Any): boolean--><!--Device-MessageHandler-removeMessages(what: int, obj: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code to remove. &lt;br&gt;The value should be an integer. |
| obj | Any | 是 | the object to match. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if messages were removed, false otherwise |

## sendEmptyMessage

```TypeScript
sendEmptyMessage(what: int): boolean
```

Sends an empty message with the specified what code

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-sendEmptyMessage(what: int): boolean--><!--Device-MessageHandler-sendEmptyMessage(what: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code to send. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the message was successfully sent, false otherwise |

## sendMessage

```TypeScript
sendMessage(message: concurrency.Message): boolean
```

Sends a message to this handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MessageHandler-sendMessage(message: concurrency.Message): boolean--><!--Device-MessageHandler-sendMessage(message: concurrency.Message): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | concurrency.Message | 是 | the message to send. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the message was successfully sent, false otherwise |

