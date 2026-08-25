# Writable

Stream to which data can be written. A writable stream allows data to be written to a target, which can be a file, an HTTP response, a standard output, another stream, or the like.

**Since:** 12

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { stream } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Writable** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## cork

```TypeScript
cork(): boolean
```

Forces subsequent writes to be buffered. This API is called to optimize the performance of continuous write operations. After this API is called, the value of **writableCorked** is incremented by one. It is recommended that this API be used in pair with [uncork()](#uncork).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

You need to implement this API but do not call it directly. It is automatically called during the initialization of the writable stream. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Function | Yes |

## doWrite

```TypeScript
doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void
```

A data write API. You need to implement this API but do not call it directly. This API is automatically called when data is written. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | string \| Uint8Array | Yes |
| encoding | string | Yes |
| callback | Function | Yes |

## doWritev

```TypeScript
doWritev(chunks: string[] | Uint8Array[], callback: Function): void
```

A batch data write API. You need to implement this API but do not call it directly. This API is automatically called when data is written. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunks | string[] \| Uint8Array[] | Yes |
| callback | Function | Yes |

## end

```TypeScript
end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable
```

Ends the writing process in a writable stream. If the value of **writableCorked** is greater than 0, the value is set to **0** and the remaining data in the buffer is output. If the **chunk** parameter is passed, it is treated as the final data chunk and written using either the **write** or **doWrite** API, based on the current execution context. If **doWrite** is used for writing, the validity check of the **encoding** parameter depends on **doWrite**. If **end** is used alone (without **write**) and the **chunk** parameter is passed, the data is written through **doWrite**. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | string \| Uint8Array | No |
| encoding | string | No |
| callback | Function | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Writable](arkts-arkts-stream-writable-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200035](../errorcode-utils.md#10200035-dowrite-is-not-implemented) |

## off

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

Unregisters an event processing callback used to listen for different events on the writable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | No |

## on

```TypeScript
on(event: string, callback: Callback<emitter.EventData>): void
```

Registers an event processing callback to listen for different events on the writable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | Yes |

## setDefaultEncoding

```TypeScript
setDefaultEncoding(encoding?: string): boolean
```

Sets the default encoding format for the writable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## uncork

```TypeScript
uncork(): boolean
```

Releases the cork state, flushing the buffered data and writing it to the target location. After this API is called, the value of **writableCorked** is decremented by one. If the value reaches **0**, the stream is no longer in the cork state. Otherwise, the stream is still in the cork state. It is recommended that this API be used in pair with [cork()](#cork).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## write

```TypeScript
write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean
```

Writes data to the buffer of the stream. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | string \| Uint8Array | No |
| encoding | string | No |
| callback | Function | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200035](../errorcode-utils.md#10200035-dowrite-is-not-implemented) |
| [10200036](../errorcode-utils.md#10200036-write-operation-is-still-performed-after-the-stream-ends) |
| [10200037](../errorcode-utils.md#10200037-callback-is-invoked-multiple-times) |

## writable

```TypeScript
get writable(): boolean
```

Is true if it is safe to call writable.write(), which means the stream has not been destroyed, error or end.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableCorked

```TypeScript
get writableCorked(): number
```

Number of times writable.uncork() needs to be called in order to fully uncork the stream.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableEnded

```TypeScript
get writableEnded(): boolean
```

Whether Writable.end has been called.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableFinished

```TypeScript
get writableFinished(): boolean
```

Whether Writable.end has been called and all buffers have been flushed.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableHighWatermark

```TypeScript
get writableHighWatermark(): number
```

Value of highWatermark.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableLength

```TypeScript
get writableLength(): number
```

Size of data that can be flushed, in bytes or objects.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## writableObjectMode

```TypeScript
get writableObjectMode(): boolean
```

Returns boolean indicating whether it is in ObjectMode.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
