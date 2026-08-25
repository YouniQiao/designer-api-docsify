# Readable

Stream from which data can be read. A readable stream is used to read data from a source, such as a file or a network socket.

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

A constructor used to create a **Readable** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(options: ReadableOptions)
```

A constructor used to create a **Readable** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ReadableOptions](arkts-arkts-stream-readableoptions-i.md) | Yes |

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

You need to implement this API. It is called when the readable stream calls on for the first time. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Function | Yes |

## doRead

```TypeScript
doRead(size: number): void
```

A data read API that needs to be implemented in child classes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## isPaused

```TypeScript
isPaused(): boolean
```

Checks whether the readable stream is paused. The stream is paused after [pause()](#pause) is called and resumes from the paused state after [resume()](#resume) is called.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## off

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

Unregisters an event processing callback used to listen for different events on the readable stream.

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

Registers an event processing callback to listen for different events on the readable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | Yes |

## pause

```TypeScript
pause(): Readable
```

Pauses the readable stream in flowing mode. You can use **isPaused** to check whether the stream is paused.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## pipe

```TypeScript
pipe(destination: Writable, options?: Object): Writable
```

Attaches a writable stream to the readable stream to implement automatic data transmission.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Writable](arkts-arkts-stream-writable-c.md) | Yes |
| options | Object | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Writable](arkts-arkts-stream-writable-c.md) |

## push

```TypeScript
push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean
```

Pushes data into the buffer of the readable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | Uint8Array \| string \| undefined \| null | Yes | Data to read.There has been a compatibility change since API version 22. In API version 21 and earlier versions, the type is `Uint8Array \| string \|
| encoding | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## read

```TypeScript
read(size?: number): string | null
```

Reads data from the buffer of the readable stream and returns the read data. If no data is read, **null** is returned.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string \| null |

**Error codes:**

| Error Code ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread-is-not-implemented) |

## resume

```TypeScript
resume(): Readable
```

Resumes an explicitly paused readable stream. You can use **isPaused** to check whether the stream is paused.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## setEncoding

```TypeScript
setEncoding(encoding?: string): boolean
```

Sets an encoding format for the readable stream. If the buffer contains data, setting the encoding format is not allowed, and **false** is returned.

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

## unpipe

```TypeScript
unpipe(destination?: Writable): Readable
```

Detaches a writable stream previously attached to the readable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Writable](arkts-arkts-stream-writable-c.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## readable

```TypeScript
get readable(): boolean
```

Is true if it is safe to call readable.read(), which means the stream has not been destroyed or emitted 'error' or 'end'.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableEncoding

```TypeScript
get readableEncoding(): string | null
```

Getter for the property encoding of a given Readable stream. The encoding property can be set using the readable.setEncoding() method.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableEnded

```TypeScript
get readableEnded(): boolean
```

Whether all data has been generated.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableFlowing

```TypeScript
get readableFlowing(): boolean | null
```

This property reflects the current state of the readable stream null/true/false.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableHighWatermark

```TypeScript
get readableHighWatermark(): number
```

Returns the value of highWatermark passed when creating this Readable.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableLength

```TypeScript
get readableLength(): number
```

Size of the data that can be read, in bytes or objects.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## readableObjectMode

```TypeScript
get readableObjectMode(): boolean
```

Returns boolean indicating whether it is in ObjectMode.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
