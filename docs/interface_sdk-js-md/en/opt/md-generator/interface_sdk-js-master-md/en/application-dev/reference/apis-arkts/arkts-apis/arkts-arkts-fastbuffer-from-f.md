# from

## Modules to Import

```TypeScript
```

## from

```TypeScript
function from(array: number[]): FastBuffer
```

Allocates a new FastBuffer using an array of bytes in the range 0 – 255. Array entries outside that range will be truncated to fit into it.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function from(array: number[]): FastBuffer--><!--Device-fastbuffer-function from(array: number[]): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Examples**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
console.info(buf.toString('hex'));
// Output: 627566666572
```


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer
```

This creates a view of the ArrayBuffer without copying the underlying memory.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer--><!--Device-fastbuffer-function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [arrayBuffer](arkts-arkts-buffer-blob-c.md) | ArrayBuffer \| [SharedArrayBuffer](../../apis-na/arkts-apis/arkts-na-lib-es2017-sharedmemory-sharedarraybuffer-i.md) | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

**Examples**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let ab = new ArrayBuffer(10);
let buf = fastbuffer.from(ab, 0, 2);
console.info(buf.length.toString());
// Output: 2
```


## from

```TypeScript
function from(buffer: FastBuffer | Uint8Array): FastBuffer
```

Copies the passed buffer data onto a new FastBuffer instance.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function from(buffer: FastBuffer | Uint8Array): FastBuffer--><!--Device-fastbuffer-function from(buffer: FastBuffer | Uint8Array): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

**Examples**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

// Create a FastBuffer object of the FastBuffer type.
let buf1 = fastbuffer.from('buffer');
let buf2 = fastbuffer.from(buf1);
console.info(buf2.toString());
// Output: buffer

// Create a FastBuffer object of the Uint8Array type to ensure memory sharing between objects.
let uint8Array = new Uint8Array(10);
let buf3 = fastbuffer.from(uint8Array);
buf3.fill(1)
console.info("uint8Array:", uint8Array)
// Output: 1,1,1,1,1,1,1,1,1,1
```


## from

```TypeScript
function from(value: string, encoding?: BufferEncoding): FastBuffer
```

Creates a new FastBuffer containing string. The encoding parameter identifies the character encoding to be used when converting string into bytes.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function from(value: string, encoding?: BufferEncoding): FastBuffer--><!--Device-fastbuffer-function from(value: string, encoding?: BufferEncoding): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Examples**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('this is a test');
let buf2 = fastbuffer.from('7468697320697320612074c3a97374', 'hex');

console.info(buf1.toString());
// Output: this is a test
console.info(buf2.toString());
// Output: this is a tést
```
