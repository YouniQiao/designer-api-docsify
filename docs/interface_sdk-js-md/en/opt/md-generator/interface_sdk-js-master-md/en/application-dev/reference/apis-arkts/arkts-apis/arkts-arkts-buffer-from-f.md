# from

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## from

```TypeScript
function from(array: number[]): Buffer
```

Creates a **Buffer** object with the specified array.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function from(array: double[]): Buffer--><!--Device-buffer-function from(array: double[]): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | number[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
console.info(buf.toString('hex'));
// Output: 627566666572
```


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer
```

Creates a **Buffer** object of the specified length that shares memory with ArrayBuffer.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer--><!--Device-buffer-function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer-End-->

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
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { buffer, JSON } from '@kit.ArkTS';

let ab = new ArrayBuffer(10);
let buf = buffer.from(ab, 0, 2);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[0,0]}
```


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer, byteOffset?: number, length?: number): Buffer
```

This creates a view of the ArrayBuffer without copying the underlying memory.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function from(arrayBuffer: ArrayBuffer, byteOffset?: int, length?: int): Buffer--><!--Device-buffer-function from(arrayBuffer: ArrayBuffer, byteOffset?: int, length?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [arrayBuffer](arkts-arkts-buffer-blob-c.md) | ArrayBuffer | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |


## from

```TypeScript
function from(buffer: Buffer | Uint8Array): Buffer
```

Copies the data of a passed **Buffer** object to create a new **Buffer** object and returns the new one. Creates a **Buffer** object based on the memory of a passed **Uint8Array** object and returns the new object, maintaining the memory association of the data.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function from(buffer: Buffer | Uint8Array): Buffer--><!--Device-buffer-function from(buffer: Buffer | Uint8Array): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [buffer](arkts-buffer.md) | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

// Create a Buffer object of the Buffer type.
let buf1 = buffer.from('buffer');
let buf2 = buffer.from(buf1);

// Create a Buffer object of the Uint8Array type to ensure memory sharing between objects.
let uint8Array = new Uint8Array(10);
let buf3 = buffer.from(uint8Array);
buf3.fill(1);
console.info("uint8Array:", uint8Array);
// Output: 1,1,1,1,1,1,1,1,1,1
```


## from

```TypeScript
function from(object: Object, offsetOrEncoding: number | string, length: number): Buffer
```

Creates a **Buffer** object based on the specified object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function from(object: Object, offsetOrEncoding: int | string, length: int): Buffer--><!--Device-buffer-function from(object: Object, offsetOrEncoding: int | string, length: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | Object | Yes |
| offsetOrEncoding | number \| string | Yes |
| length | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

## Examples

```TypeScript
import { buffer, JSON } from '@kit.ArkTS';

let buf = buffer.from(new String('this is a test'), 'utf8', 14);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[116,104,105,115,32,105,115,32,97,32,116,101,115,116]}
```


## from

```TypeScript
function from(string: String, encoding?: BufferEncoding): Buffer
```

Creates a **Buffer** object based on a string in the given encoding format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function from(string: String, encoding?: BufferEncoding): Buffer--><!--Device-buffer-function from(string: String, encoding?: BufferEncoding): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | String | Yes |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('this is a test');
let buf2 = buffer.from('7468697320697320612074c3a97374', 'hex');

console.info(buf1.toString());
// Output: this is a test
console.info(buf2.toString());
// Output: this is a tést
```
