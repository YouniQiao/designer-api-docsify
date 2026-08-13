# Readable

Stream from which data can be read. A readable stream is used to read data from a source, such as a file or a network socket.

**Since:** 23

**Deprecated since:** -1

<!--Device-stream-export class Readable--><!--Device-stream-export class Readable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { stream } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Readable** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-constructor()--><!--Device-Readable-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
let readableStream = new stream.Readable();
```

## constructor

```TypeScript
constructor(options: ReadableOptions)
```

A constructor used to create a **Readable** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-constructor(options: ReadableOptions)--><!--Device-Readable-constructor(options: ReadableOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ReadableOptions](arkts-arkts-stream-readableoptions-i.md) | Yes |

## Examples

```TypeScript
let option : stream.ReadableOptions = {
  encoding : 'utf-8'
};
let readableStream = new stream.Readable(option);
```

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

You need to implement this API. It is called when the readable stream calls [on](arkts-arkts-stream-writable-c.md#on_string) for the first time. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-doInitialize(callback: Function): void--><!--Device-Readable-doInitialize(callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Function | Yes |

## Examples

```TypeScript
class MyReadable extends stream.Readable {
  doInitialize(callback: Function) {
    super.doInitialize(callback);
    console.info("Readable doInitialize"); // Readable doInitialize
}

  doRead(size: number) {
  }
}

let myReadable = new MyReadable();
myReadable.on('data', () => {
});
```

## doRead

```TypeScript
doRead(size: number): void
```

A data read API that needs to be implemented in child classes.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-doRead(size: int): void--><!--Device-Readable-doRead(size: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    console.info("doRead called"); // doRead called
  }
}

let readable = new TestReadable();
readable.on('data', () => {
});
```

## isPaused

```TypeScript
isPaused(): boolean
```

Checks whether the readable stream is paused. The stream is paused after [pause()](#pause) is called and resumes from the paused state after [resume()](#resume) is called.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-isPaused(): boolean--><!--Device-Readable-isPaused(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused false
readableStream.pause();
console.info("Readable isPaused", readableStream.isPaused()); // Readable isPaused true
```

## off_string

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

Unregisters an event processing callback used to listen for different events on the readable stream.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Readable-off(event: string, callback?: Callback<emitter.EventData>): void--><!--Device-Readable-off(event: string, callback?: Callback<emitter.EventData>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | No |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readable = new TestReadable();

function read() {
  console.info("read() called");
}

readable.setEncoding('utf8');
readable.on('readable', read);
readable.off('readable');
readable.push('test');
// After off is used to unregister the listening of the readable stream events, the read function is not called and "read() called" is not printed.
```

## off_string

```TypeScript
off(event: string, callback?: Function): void
```

Cancel event message.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-off(event: string, callback?: Function): void--><!--Device-Readable-off(event: string, callback?: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | Function | No |

## on_string

```TypeScript
on(event: string, callback: Callback<emitter.EventData>): void
```

Registers an event processing callback to listen for different events on the readable stream.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Readable-on(event: string, callback: Callback<emitter.EventData>): void--><!--Device-Readable-on(event: string, callback: Callback<emitter.EventData>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | Yes |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    throw new Error('Simulated error');
  }
}

let readable = new TestReadable();
readable.push('test');
readable.on('error', () => {
  console.info("error event called"); // error event called
});
```

## on_string

```TypeScript
on(event: string, callback: Function): void
```

Registering Event Messages.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-on(event: string, callback: Function): void--><!--Device-Readable-on(event: string, callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | Function | Yes |

## pause

```TypeScript
pause(): Readable
```

Pauses the readable stream in flowing mode. You can use **isPaused** to check whether the stream is paused.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-pause(): Readable--><!--Device-Readable-pause(): Readable-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.pause();
console.info("Readable test pause", readableStream.isPaused()); // Readable test pause true
```

## pipe

```TypeScript
pipe(destination: Writable, options?: Object): Writable
```

Attaches a writable stream to the readable stream to implement automatic data transmission.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-pipe(destination: Writable, options?: Object): Writable--><!--Device-Readable-pipe(destination: Writable, options?: Object): Writable-End-->

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

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push('test');
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("Readable test pipe", chunk); // Readable test pipe test
    callback();
  }
}

let readable = new TestReadable();
let writable = new TestWritable();
readable.pipe(writable);
```

## push

```TypeScript
push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean
```

Pushes data into the buffer of the readable stream.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean--><!--Device-Readable-push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | Uint8Array \| string \| undefined \| null | Yes | Data to read.&lt;br&gt; There has been a compatibility change since API version 22. In API version 21 and earlier versions, the type is `Uint8Array \| string \|
| encoding | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readable = new TestReadable();
let testData = 'Hello world';
readable.push(testData);
console.info("Readable push test", readable.readableLength); // Readable push test 11
```

## read

```TypeScript
read(size?: number): string | null
```

Reads data from the buffer of the readable stream and returns the read data. If no data is read, **null** is returned.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Readable-read(size?: number): string | null--><!--Device-Readable-read(size?: number): string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread-is-not-implemented) |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.push('test');
readableStream.pause();
let dataChunk = readableStream.read();
console.info('Readable data is', dataChunk); // Readable data is test
```

## read

```TypeScript
read(size?: number): buffer.Buffer | string | null
```

Reads a buffer of a specified size from the buffer. If the available buffer is sufficient, the result of the specified size is returned. Otherwise, if Readable has ended, all remaining buffers are returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-read(size?: int): buffer.Buffer | string | null--><!--Device-Readable-read(size?: int): buffer.Buffer | string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| buffer.Buffer |

**Error codes:**

| Error Code ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread-is-not-implemented) |

## resume

```TypeScript
resume(): Readable
```

Resumes an explicitly paused readable stream. You can use **isPaused** to check whether the stream is paused.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-resume(): Readable--><!--Device-Readable-resume(): Readable-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
readableStream.resume();
console.info("Readable test resume", !readableStream.isPaused()); // After a successful switching, the log "Readable test resume true" is displayed.
```

## setEncoding

```TypeScript
setEncoding(encoding?: string): boolean
```

Sets an encoding format for the readable stream. If the buffer contains data, setting the encoding format is not allowed, and **false** is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-setEncoding(encoding?: string): boolean--><!--Device-Readable-setEncoding(encoding?: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
  }
}

let readableStream = new TestReadable();
let result = readableStream.setEncoding('utf8');
console.info("Readable result", result); // Readable result true
```

## unpipe

```TypeScript
unpipe(destination?: Writable): Readable
```

Detaches a writable stream previously attached to the readable stream.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Readable-unpipe(destination?: Writable): Readable--><!--Device-Readable-unpipe(destination?: Writable): Readable-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Writable](arkts-arkts-stream-writable-c.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## Examples

```TypeScript
class TestReadable extends stream.Readable {
  constructor() {
    super();
  }

  doRead(size: number) {
    this.push('test');
    this.push(null);
  }
}

class TestWritable extends stream.Writable {
  constructor() {
    super();
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let readable = new TestReadable();
let writable = new TestWritable();
readable.pipe(writable);
readable.unpipe(writable);
readable.on('data', () => {
  console.info("Readable test unpipe data event triggered");
});
// After successful detaching, the data event is not triggered and "Readable test unpipe data event triggered" is not printed.
```
