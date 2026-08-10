# Message

Represents a message that can be sent to a MessageHandler for processing

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-concurrency-export class Message--><!--Device-concurrency-export class Message-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(handler: concurrency.MessageHandler)
```

Constructs a new Message with a handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-constructor(handler: concurrency.MessageHandler)--><!--Device-Message-constructor(handler: concurrency.MessageHandler)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | concurrency.MessageHandler | 是 | the handler to process this message. |

## constructor

```TypeScript
constructor(what: int, handler: concurrency.MessageHandler)
```

Constructs a new Message with a what code and handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-constructor(what: int, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(what: int, handler: concurrency.MessageHandler)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code. &lt;br&gt;The value should be an integer. |
| handler | concurrency.MessageHandler | 是 | the handler to process this message. |

## constructor

```TypeScript
constructor(what: int, obj: Any, handler: concurrency.MessageHandler)
```

Constructs a new Message with a what code, object, and handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-constructor(what: int, obj: Any, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(what: int, obj: Any, handler: concurrency.MessageHandler)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| what | int | 是 | the message code. &lt;br&gt;The value should be an integer. |
| obj | Any | 是 | the object attached to this message. |
| handler | concurrency.MessageHandler | 是 | the handler to process this message. |

## constructor

```TypeScript
constructor(callback: () => void, handler: concurrency.MessageHandler)
```

Constructs a new Message with a callback and handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-constructor(callback: () => void, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(callback: () => void, handler: concurrency.MessageHandler)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () =&gt; void | 是 | the callback to execute when this message is processed. |
| handler | concurrency.MessageHandler | 是 | the handler to process this message. |

## equals

```TypeScript
equals(other: concurrency.Message): boolean
```

Compares this message with another for equality

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-equals(other: concurrency.Message): boolean--><!--Device-Message-equals(other: concurrency.Message): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | concurrency.Message | 是 | the other message to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the messages are equal, false otherwise |

## getCallback

```TypeScript
getCallback(): (() => void) | undefined
```

Returns the callback of this message

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-getCallback(): (() => void) | undefined--><!--Device-Message-getCallback(): (() => void) | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (() =&gt; void) | the callback, or undefined if not set |

## getObject

```TypeScript
getObject(): Any
```

Returns the object attached to this message

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-getObject(): Any--><!--Device-Message-getObject(): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | the object |

## getTarget

```TypeScript
getTarget(): concurrency.MessageHandler
```

Returns the target handler of this message

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-getTarget(): concurrency.MessageHandler--><!--Device-Message-getTarget(): concurrency.MessageHandler-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| concurrency.MessageHandler | the target handler |

## getWhat

```TypeScript
getWhat(): int
```

Returns the what code of this message

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-getWhat(): int--><!--Device-Message-getWhat(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the what code |

## sendToTarget

```TypeScript
sendToTarget(): void
```

Sends this message to its target handler

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Message-sendToTarget(): void--><!--Device-Message-sendToTarget(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

