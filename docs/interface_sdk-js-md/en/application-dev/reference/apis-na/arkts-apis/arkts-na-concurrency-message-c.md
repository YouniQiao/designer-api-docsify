# Message

Represents a message that can be sent to a MessageHandler for processing

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-concurrency-export class Message--><!--Device-concurrency-export class Message-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(handler: concurrency.MessageHandler)
```

Constructs a new Message with a handler

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-constructor(handler: concurrency.MessageHandler)--><!--Device-Message-constructor(handler: concurrency.MessageHandler)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | concurrency.MessageHandler | Yes | the handler to process this message. |

## constructor

```TypeScript
constructor(what: int, handler: concurrency.MessageHandler)
```

Constructs a new Message with a what code and handler

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-constructor(what: int, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(what: int, handler: concurrency.MessageHandler)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code. &lt;br&gt;The value should be an integer. |
| handler | concurrency.MessageHandler | Yes | the handler to process this message. |

## constructor

```TypeScript
constructor(what: int, obj: Any, handler: concurrency.MessageHandler)
```

Constructs a new Message with a what code, object, and handler

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-constructor(what: int, obj: Any, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(what: int, obj: Any, handler: concurrency.MessageHandler)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code. &lt;br&gt;The value should be an integer. |
| obj | Any | Yes | the object attached to this message. |
| handler | concurrency.MessageHandler | Yes | the handler to process this message. |

## constructor

```TypeScript
constructor(callback: () => void, handler: concurrency.MessageHandler)
```

Constructs a new Message with a callback and handler

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-constructor(callback: () => void, handler: concurrency.MessageHandler)--><!--Device-Message-constructor(callback: () => void, handler: concurrency.MessageHandler)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | the callback to execute when this message is processed. |
| handler | concurrency.MessageHandler | Yes | the handler to process this message. |

## equals

```TypeScript
equals(other: concurrency.Message): boolean
```

Compares this message with another for equality

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-equals(other: concurrency.Message): boolean--><!--Device-Message-equals(other: concurrency.Message): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [concurrency.Message](arkts-na-concurrency-message-c.md) | Yes | the other message to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the messages are equal, false otherwise |

## getCallback

```TypeScript
getCallback(): (() => void) | undefined
```

Returns the callback of this message

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-getCallback(): (() => void) | undefined--><!--Device-Message-getCallback(): (() => void) | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| (() =&gt; void) | the callback, or undefined if not set |

## getObject

```TypeScript
getObject(): Any
```

Returns the object attached to this message

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-getObject(): Any--><!--Device-Message-getObject(): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Any | the object |

## getTarget

```TypeScript
getTarget(): concurrency.MessageHandler
```

Returns the target handler of this message

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-getTarget(): concurrency.MessageHandler--><!--Device-Message-getTarget(): concurrency.MessageHandler-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| concurrency.MessageHandler | the target handler |

## getWhat

```TypeScript
getWhat(): int
```

Returns the what code of this message

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-getWhat(): int--><!--Device-Message-getWhat(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the what code |

## sendToTarget

```TypeScript
sendToTarget(): void
```

Sends this message to its target handler

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Message-sendToTarget(): void--><!--Device-Message-sendToTarget(): void-End-->

**System capability:** SystemCapability.Utils.Lang

