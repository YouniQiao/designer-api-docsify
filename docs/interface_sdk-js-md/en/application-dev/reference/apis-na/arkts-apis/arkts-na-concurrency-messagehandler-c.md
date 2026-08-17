# MessageHandler

Handles messages and provides message scheduling capabilities

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-concurrency-export class MessageHandler--><!--Device-concurrency-export class MessageHandler-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())
```

Constructs a new MessageHandler with a handler function

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())--><!--Device-MessageHandler-constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | (message: concurrency.Message) =&gt; void | Yes | the handler function to process messages. |
| worker | [EAWorker](arkts-na-eaworker-c.md) \| undefined | Yes | the worker to associate with this handler. |

## getWorker

```TypeScript
getWorker(): EAWorker
```

Returns the worker associated with this handler

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-getWorker(): EAWorker--><!--Device-MessageHandler-getWorker(): EAWorker-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [EAWorker](arkts-na-eaworker-c.md) | the associated worker |

## hasCallbacks

```TypeScript
hasCallbacks(callback: () => void): boolean
```

Checks whether the handler has the specified callback pending

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-hasCallbacks(callback: () => void): boolean--><!--Device-MessageHandler-hasCallbacks(callback: () => void): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | the callback to check for. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the callback is pending, false otherwise |

## hasMessages

```TypeScript
hasMessages(what: int): boolean
```

Checks whether the handler has messages with the specified what code

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-hasMessages(what: int): boolean--><!--Device-MessageHandler-hasMessages(what: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code to check for. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if such messages exist, false otherwise |

## hasMessages

```TypeScript
hasMessages(what: int, obj: Any): boolean
```

Checks whether the handler has messages with the specified what code and object

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-hasMessages(what: int, obj: Any): boolean--><!--Device-MessageHandler-hasMessages(what: int, obj: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code to check for. <br>The value should be an integer. |
| obj | Any | Yes | the object to check for. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if such messages exist, false otherwise |

## post

```TypeScript
post(callback: () => void): boolean
```

Posts a callback to the handler

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-post(callback: () => void): boolean--><!--Device-MessageHandler-post(callback: () => void): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | the callback to post. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the callback was successfully posted, false otherwise |

## removeCallbacks

```TypeScript
removeCallbacks(callback: () => void): boolean
```

Removes pending callbacks matching the specified callback

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-removeCallbacks(callback: () => void): boolean--><!--Device-MessageHandler-removeCallbacks(callback: () => void): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | the callback to remove. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the callback was removed, false otherwise |

## removeMessages

```TypeScript
removeMessages(what: int): boolean
```

Removes pending messages with the specified what code

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-removeMessages(what: int): boolean--><!--Device-MessageHandler-removeMessages(what: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code to remove. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if messages were removed, false otherwise |

## removeMessages

```TypeScript
removeMessages(what: int, obj: Any): boolean
```

Removes pending messages with the specified what code and object

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-removeMessages(what: int, obj: Any): boolean--><!--Device-MessageHandler-removeMessages(what: int, obj: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code to remove. <br>The value should be an integer. |
| obj | Any | Yes | the object to match. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if messages were removed, false otherwise |

## sendEmptyMessage

```TypeScript
sendEmptyMessage(what: int): boolean
```

Sends an empty message with the specified what code

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-sendEmptyMessage(what: int): boolean--><!--Device-MessageHandler-sendEmptyMessage(what: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| what | int | Yes | the message code to send. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the message was successfully sent, false otherwise |

## sendMessage

```TypeScript
sendMessage(message: concurrency.Message): boolean
```

Sends a message to this handler

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MessageHandler-sendMessage(message: concurrency.Message): boolean--><!--Device-MessageHandler-sendMessage(message: concurrency.Message): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | concurrency.Message | Yes | the message to send. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the message was successfully sent, false otherwise |

