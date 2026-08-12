# Duplex

A stream that is both readable and writable. A duplex stream allows data to be transmitted in two directions, that is, data can be read and written.The **Duplex** class inherits from [Readable](arkts-arkts-stream-readableoptions-i.md#ReadableOptions) and supports all the APIs in  
**Readable**.

**Inheritance/Implementation:** Duplex extends [Readable](arkts-arkts-stream-readable-c.md#Readable)

**Since:** 12

<!--Device-stream-export class Duplex extends Readable--><!--Device-stream-export class Duplex extends Readable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { stream } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Duplex** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-constructor()--><!--Device-Duplex-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
let duplex = new stream.Duplex();
```

## cork

```TypeScript
cork(): boolean
```

Forces subsequent writes to be buffered. This API is called to optimize the performance of continuous write operations. After this API is called, the value of **writableCorked** is incremented by one. It is recommended that this API be used in pair with [uncork()](arkts-arkts-stream-writable-c.md#uncork).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-cork(): boolean--><!--Device-Duplex-cork(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let duplexStream = new stream.Duplex();
let result = duplexStream.cork();
console.info("duplexStream cork result", result); // duplexStream cork result true
```

## doWrite

```TypeScript
doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void
```

A data write API. You need to implement this API but do not call it directly. This API is automatically called when data is written. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void--><!--Device-Duplex-doWrite(chunk: string | Uint8Array, encoding: string, callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunk | string \| Uint8Array | Yes |
| encoding | string | Yes |
| callback | Function | Yes |

## Examples

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is data
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.write('data', 'utf8');
```

## doWritev

```TypeScript
doWritev(chunks: string[] | Uint8Array[], callback: Function): void
```

A batch data write API. You need to implement this API but do not call it directly. This API is automatically called when data is written. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-doWritev(chunks: string[] | Uint8Array[], callback: Function): void--><!--Device-Duplex-doWritev(chunks: string[] | Uint8Array[], callback: Function): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chunks | string[] \| Uint8Array[] | Yes |
| callback | Function | Yes |

## Examples

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }

  doWritev(chunks: string[] | Uint8Array[], callback: Function) {
    console.info("duplexStream chunk", chunks[0]); // duplexStream chunk data1
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write('data1', 'utf8');
duplexStream.write('data2', 'utf8');
duplexStream.uncork();
duplexStream.end();
```

## end

```TypeScript
end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable
```

Ends the writing process in a duplex stream. If the value of **writableCorked** is greater than 0, the value is set to **0** and the remaining data in the buffer is output. If the **chunk** parameter is passed, it is treated as the final data chunk and written using either the **write** or **doWrite** API, based on the current execution context. If **doWrite** is used for writing, the validity check of the **encoding** parameter depends on  
**doWrite**. If **end** is used alone (without **write**) and the **chunk** parameter is passed, the data is written through **doWrite**. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable--><!--Device-Duplex-end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable-End-->

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
| [10200039](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200039-dotransform-is-not-implemented) |

## Examples

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
  console.info("Duplex chunk is", chunk); // Duplex chunk is test
  callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.end('test', 'utf8', () => {
  console.info("Duplex is end"); // Duplex is end
});
```

## setDefaultEncoding

```TypeScript
setDefaultEncoding(encoding?: string): boolean
```

Sets the default encoding format for the writable stream.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-setDefaultEncoding(encoding?: string): boolean--><!--Device-Duplex-setDefaultEncoding(encoding?: string): boolean-End-->

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
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.setDefaultEncoding('utf8');
console.info("duplexStream is result", result); // duplexStream is result true
```

## uncork

```TypeScript
uncork(): boolean
```

Releases the cork state, flushing the buffered data and writing it to the target location. After this API is called, the value of **writableCorked** is decremented by one. If the value reaches **0**, the stream is no longer in the cork state. Otherwise, the stream is still in the cork state. It is recommended that this API be used in pair with [cork()](arkts-arkts-stream-writable-c.md#cork).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-uncork(): boolean--><!--Device-Duplex-uncork(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let dataWritten = '';
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    dataWritten += chunk;
    callback();
  }
}

let duplexStream = new TestDuplex();
duplexStream.cork();
duplexStream.write('a');
duplexStream.write('b');
duplexStream.uncork();
console.info("Duplex test uncork", dataWritten); // Duplex test uncork ab
```

## write

```TypeScript
write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean
```

Writes data to the buffer of the stream. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean--><!--Device-Duplex-write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean-End-->

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
| [10200039](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200039-dotransform-is-not-implemented) |
| [10200037](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200037-callback-is-invoked-multiple-times) |
| [10200036](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200036-write-operation-is-still-performed-after-the-stream-ends) |

## Examples

```TypeScript
class TestDuplex extends stream.Duplex {
  constructor() {
    super();
  }

  doRead(size: number) {
  }

  doWrite(chunk: string | Uint8Array, encoding: string, callback: Function) {
    console.info("duplexStream chunk is", chunk); // duplexStream chunk is test
    callback();
  }
}

let duplexStream = new TestDuplex();
let result = duplexStream.write('test', 'utf8');
console.info("duplexStream result", result); // duplexStream result true
```

## writable

```TypeScript
get writable(): boolean
```

Is true if it is safe to call writable.write(), which means the stream has not been destroyed, error or end.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writable(): boolean--><!--Device-Duplex-get writable(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableCorked

```TypeScript
get writableCorked(): number
```

Number of times writable.uncork() needs to be called in order to fully uncork the stream.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableCorked(): int--><!--Device-Duplex-get writableCorked(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableEnded

```TypeScript
get writableEnded(): boolean
```

Whether Writable.end has been called.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableEnded(): boolean--><!--Device-Duplex-get writableEnded(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableFinished

```TypeScript
get writableFinished(): boolean
```

Whether Writable.end has been called and all buffers have been flushed.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableFinished(): boolean--><!--Device-Duplex-get writableFinished(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## writableHighWatermark

```TypeScript
get writableHighWatermark(): number
```

Value of highWatermark.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableHighWatermark(): int--><!--Device-Duplex-get writableHighWatermark(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableLength

```TypeScript
get writableLength(): number
```

Size of data that can be flushed, in bytes or objects.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableLength(): int--><!--Device-Duplex-get writableLength(): int-End-->

**System capability:** SystemCapability.Utils.Lang

## writableObjectMode

```TypeScript
get writableObjectMode(): boolean
```

Returns boolean indicating whether it is in ObjectMode.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Duplex-get writableObjectMode(): boolean--><!--Device-Duplex-get writableObjectMode(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang
