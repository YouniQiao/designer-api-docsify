# FastBuffer

The FastBuffer object is a method of handling buffers dedicated to binary data.

**Since:** 20

<!--Device-fastbuffer-class FastBuffer--><!--Device-fastbuffer-class FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1
```

Compares buf with target and returns a number indicating whether buf comes before, after,or is the same as target in sort order. Comparison is based on the actual sequence of bytes in each FastBuffer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1--><!--Device-FastBuffer-compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |
| targetStart | number | No |
| targetEnd | number | No |
| sourceStart | number | No |
| sourceEnd | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| -1 |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = fastbuffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// Output: 0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// Output: -1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// Output: 1
```

## copy

```TypeScript
copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number
```

Copies data from a region of buf to a region in target, even if the target memory region overlaps with buf.If sourceEnd is greater than the length of the target, the length of the target shall prevail, and the extra part will not be overwritten.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number--><!--Device-FastBuffer-copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |
| targetStart | number | No |
| sourceStart | number | No |
| sourceEnd | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);
let buf2 = fastbuffer.allocUninitializedFromPool(26).fill('!');

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}

buf1.copy(buf2, 8, 16, 20);
console.info(buf2.toString('ascii', 0, 25));
// Output: !!!!!!!!qrst!!!!!!!!!!!!!
```

## entries

```TypeScript
entries(): IterableIterator<[
            number,
            number
        ]>
```

Creates and returns an iterator of [index, byte] pairs from the contents of buf.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-entries(): IterableIterator<[            number,            number        ]>--><!--Device-FastBuffer-entries(): IterableIterator<[            number,            number        ]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;[             number, number         ]&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('buffer');
let pair = buf.entries();
let next: IteratorResult<Object[]> = pair.next();
while (!next.done) {
  console.info("fastbuffer: " + next.value);
  /*
  Output: buffer: 0,98
           fastbuffer: 1,117
           fastbuffer: 2,102
           fastbuffer: 3,102
           fastbuffer: 4,101
           fastbuffer: 5,114
  */
  next = pair.next();
}
```

## equals

```TypeScript
equals(otherBuffer: Uint8Array | FastBuffer): boolean
```

Returns true if both buf and otherBuffer have exactly the same bytes, false otherwise

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-equals(otherBuffer: Uint8Array | FastBuffer): boolean--><!--Device-FastBuffer-equals(otherBuffer: Uint8Array | FastBuffer): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| otherBuffer | Uint8Array \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('ABC');
let buf2 = fastbuffer.from('414243', 'hex');
let buf3 = fastbuffer.from('ABCD');

console.info(buf1.equals(buf2).toString());
// Output: true
console.info(buf1.equals(buf3).toString());
// Output: false
```

## fill

```TypeScript
fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer
```

Fills buf with the specified value. If the offset and end are not given, the entire buf will be filled.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer--><!--Device-FastBuffer-fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| FastBuffer \| Uint8Array \| number | Yes |
| offset | number | No |
| end | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let b = fastbuffer.allocUninitializedFromPool(50).fill('h');
console.info(b.toString());
// Output: hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
```

## includes

```TypeScript
includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean
```

Returns true if value was found in buf, false otherwise

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean--><!--Device-FastBuffer-includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| FastBuffer \| Uint8Array | Yes |
| [byteOffset](#byteoffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this is a buffer');
console.info(buf.includes('this').toString());
// Output: true
console.info(buf.includes('be').toString());
// Output: false
```

## indexOf

```TypeScript
indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

The index of the first occurrence of value in buf

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number--><!--Device-FastBuffer-indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| FastBuffer \| Uint8Array | Yes |
| [byteOffset](#byteoffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this is a buffer');
console.info(buf.indexOf('this').toString());
// Output: 0
console.info(buf.indexOf('is').toString());
// Output: 2
```

## keys

```TypeScript
keys(): IterableIterator<number>
```

Creates and returns an iterator of buf keys (indices).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-keys(): IterableIterator<number>--><!--Device-FastBuffer-keys(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;number&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('buffer');
let keys = buf.keys();
for (const key of keys) {
  console.info(key.toString());
}
/*
Output: 0
        1
        2
        3
        4
        5
*/
```

## lastIndexOf

```TypeScript
lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

The index of the last occurrence of value in buf

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number--><!--Device-FastBuffer-lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| FastBuffer \| Uint8Array | Yes |
| [byteOffset](#byteoffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from('this buffer is a buffer');
console.info(buf.lastIndexOf('this').toString());
// Output: 0
console.info(buf.lastIndexOf('buffer').toString());
// Output: 17
```

## readBigInt64BE

```TypeScript
readBigInt64BE(offset?: number): bigint
```

Reads a signed, big-endian 64-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readBigInt64BE(offset?: number): bigint--><!--Device-FastBuffer-readBigInt64BE(offset?: number): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64BE(0).toString());
// Output: 7161960797921896816
```

## readBigInt64LE

```TypeScript
readBigInt64LE(offset?: number): bigint
```

Reads a signed, little-endian 64-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readBigInt64LE(offset?: number): bigint--><!--Device-FastBuffer-readBigInt64LE(offset?: number): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64LE(0).toString());
// Output: 8100120198111388771
```

## readBigUInt64BE

```TypeScript
readBigUInt64BE(offset?: number): bigint
```

Reads a unsigned, big-endian 64-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readBigUInt64BE(offset?: number): bigint--><!--Device-FastBuffer-readBigUInt64BE(offset?: number): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64BE(0).toString());
// Output: 7161960797921896816
```

## readBigUInt64LE

```TypeScript
readBigUInt64LE(offset?: number): bigint
```

Reads a unsigned, little-endian 64-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readBigUInt64LE(offset?: number): bigint--><!--Device-FastBuffer-readBigUInt64LE(offset?: number): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// Output: 8100120198111388771
```

## readDoubleBE

```TypeScript
readDoubleBE(offset?: number): number
```

Reads a 64-bit, big-endian double from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readDoubleBE(offset?: number): number--><!--Device-FastBuffer-readDoubleBE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleBE(0).toString());
// Output: 8.20788039913184e-304
```

## readDoubleLE

```TypeScript
readDoubleLE(offset?: number): number
```

Reads a 64-bit, little-endian double from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readDoubleLE(offset?: number): number--><!--Device-FastBuffer-readDoubleLE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleLE(0).toString());
// Output: 5.447603722011605e-270
```

## readFloatBE

```TypeScript
readFloatBE(offset?: number): number
```

Reads a 32-bit, big-endian float from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readFloatBE(offset?: number): number--><!--Device-FastBuffer-readFloatBE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatBE(0).toString());
// Output: 2.387939260590663e-38
```

## readFloatLE

```TypeScript
readFloatLE(offset?: number): number
```

Reads a 32-bit, little-endian float from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readFloatLE(offset?: number): number--><!--Device-FastBuffer-readFloatLE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatLE(0).toString());
// Output: 1.539989614439558e-36
```

## readInt16BE

```TypeScript
readInt16BE(offset?: number): number
```

Reads a signed, big-endian 16-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readInt16BE(offset?: number): number--><!--Device-FastBuffer-readInt16BE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 5]);
console.info(buf.readInt16BE(0).toString());
// Output: 5
```

## readInt16LE

```TypeScript
readInt16LE(offset?: number): number
```

Reads a signed, little-endian 16-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readInt16LE(offset?: number): number--><!--Device-FastBuffer-readInt16LE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 5]);
console.info(buf.readInt16LE(0).toString());
// Output: 1280
```

## readInt32BE

```TypeScript
readInt32BE(offset?: number): number
```

Reads a signed, big-endian 32-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readInt32BE(offset?: number): number--><!--Device-FastBuffer-readInt32BE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 0, 0, 5]);
console.info(buf.readInt32BE(0).toString());
// Output: 5
```

## readInt32LE

```TypeScript
readInt32LE(offset?: number): number
```

Reads a signed, little-endian 32-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readInt32LE(offset?: number): number--><!--Device-FastBuffer-readInt32LE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0, 0, 0, 5]);
console.info(buf.readInt32LE(0).toString());
// Output: 83886080
```

## readInt8

```TypeScript
readInt8(offset?: number): number
```

Reads a signed 8-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readInt8(offset?: number): number--><!--Device-FastBuffer-readInt8(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([-1, 5]);
console.info(buf.readInt8(0).toString());
// Output: -1
console.info(buf.readInt8(1).toString());
// Output: 5
```

## readIntBE

```TypeScript
readIntBE(offset: number, byteLength: number): number
```

Reads byteLength number of bytes from buf at the specified offset and interprets the result as a big-endian,two's complement signed value supporting up to 48 bits of accuracy

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readIntBE(offset: number, byteLength: number): number--><!--Device-FastBuffer-readIntBE(offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from("ab");
let num = buf.readIntBE(0, 1);
console.info(num.toString());
// Output: 97
```

## readIntLE

```TypeScript
readIntLE(offset: number, byteLength: number): number
```

Reads byteLength number of bytes from buf at the specified offset and interprets the result as a little-endian,two's complement signed value supporting up to 48 bits of accuracy.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readIntLE(offset: number, byteLength: number): number--><!--Device-FastBuffer-readIntLE(offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readIntLE(0, 6).toString(16));
// Output: -546f87a9cbee
```

## readUInt16BE

```TypeScript
readUInt16BE(offset?: number): number
```

Reads an unsigned, big-endian 16-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUInt16BE(offset?: number): number--><!--Device-FastBuffer-readUInt16BE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16BE(0).toString(16));
// Output: 1234
console.info(buf.readUInt16BE(1).toString(16));
// Output: 3456
```

## readUInt16LE

```TypeScript
readUInt16LE(offset?: number): number
```

Reads an unsigned, little-endian 16-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUInt16LE(offset?: number): number--><!--Device-FastBuffer-readUInt16LE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16LE(0).toString(16));
// Output: 3412
console.info(buf.readUInt16LE(1).toString(16));
// Output: 5634
```

## readUInt32BE

```TypeScript
readUInt32BE(offset?: number): number
```

Reads an unsigned, big-endian 32-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUInt32BE(offset?: number): number--><!--Device-FastBuffer-readUInt32BE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32BE(0).toString(16));
// Output: 12345678
```

## readUInt32LE

```TypeScript
readUInt32LE(offset?: number): number
```

Reads an unsigned, little-endian 32-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUInt32LE(offset?: number): number--><!--Device-FastBuffer-readUInt32LE(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32LE(0).toString(16));
// Output: 78563412
```

## readUInt8

```TypeScript
readUInt8(offset?: number): number
```

Reads an unsigned 8-bit integer from buf at the specified offset

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUInt8(offset?: number): number--><!--Device-FastBuffer-readUInt8(offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([1, -2]);
console.info(buf.readUInt8(0).toString());
// Output: 1
console.info(buf.readUInt8(1).toString());
// Output: 254
```

## readUIntBE

```TypeScript
readUIntBE(offset: number, byteLength: number): number
```

Reads byteLength number of bytes from buf at the specified offset and interprets the result as an unsigned big-endian integer supporting up to 48 bits of accuracy.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUIntBE(offset: number, byteLength: number): number--><!--Device-FastBuffer-readUIntBE(offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntBE(0, 6).toString(16));
// Output: 1234567890ab
```

## readUIntLE

```TypeScript
readUIntLE(offset: number, byteLength: number): number
```

Reads byteLength number of bytes from buf at the specified offset and interprets the result as an unsigned,little-endian integer supporting up to 48 bits of accuracy.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-readUIntLE(offset: number, byteLength: number): number--><!--Device-FastBuffer-readUIntLE(offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntLE(0, 6).toString(16));
// Output: ab9078563412
```

## subarray

```TypeScript
subarray(start?: number, end?: number): FastBuffer
```

Returns a new FastBuffer that references the same memory as the original, but offset and cropped by the start and end indices.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-subarray(start?: number, end?: number): FastBuffer--><!--Device-FastBuffer-subarray(start?: number, end?: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
const buf2 = buf1.subarray(0, 3);
console.info(buf2.toString('ascii', 0, buf2.length));
// Output: abc
```

## swap16

```TypeScript
swap16(): FastBuffer
```

Interprets buf as an array of unsigned 16-bit integers and swaps the byte order in-place.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-swap16(): FastBuffer--><!--Device-FastBuffer-swap16(): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// Output: 0102030405060708
buf1.swap16();
console.info(buf1.toString('hex'));
// Output: 0201040306050807
```

## swap32

```TypeScript
swap32(): FastBuffer
```

Interprets buf as an array of unsigned 32-bit integers and swaps the byte order in-place.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-swap32(): FastBuffer--><!--Device-FastBuffer-swap32(): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// Output: 0102030405060708
buf1.swap32();
console.info(buf1.toString('hex'));
// Output: 0403020108070605
```

## swap64

```TypeScript
swap64(): FastBuffer
```

Interprets buf as an array of unsigned 64-bit integers and swaps the byte order in-place.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-swap64(): FastBuffer--><!--Device-FastBuffer-swap64(): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// Output: 0102030405060708
buf1.swap64();
console.info(buf1.toString('hex'));
// Output: 0807060504030201
```

## toJSON

```TypeScript
toJSON(): Object
```

Returns a JSON representation of buf

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-toJSON(): Object--><!--Device-FastBuffer-toJSON(): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
let obj = buf1.toJSON();
console.info(JSON.stringify(obj));
// Output: {"type":"FastBuffer","data":[1,2,3,4,5]}
```

## toString

```TypeScript
toString(encoding?: string, start?: number, end?: number): string
```

Decodes buf to a string according to the specified character encoding in encoding

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-toString(encoding?: string, start?: number, end?: number): string--><!--Device-FastBuffer-toString(encoding?: string, start?: number, end?: number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | No |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.allocUninitializedFromPool(26);
for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
console.info(buf1.toString('utf-8'));
// Output: abcdefghijklmnopqrstuvwxyz
```

## values

```TypeScript
values(): IterableIterator<number>
```

Creates and returns an iterator for buf values (bytes).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-values(): IterableIterator<number>--><!--Device-FastBuffer-values(): IterableIterator<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator&lt;number&gt;](arkts-arkts-iterator-iterableiterator-i.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('buffer');
let pair = buf1.values()
let next:IteratorResult<number> = pair.next()
while (!next.done) {
  console.info(next.value.toString());
  /*
  Output: 98
           117
           102
           102
           101
           114
  */
  next = pair.next();
}
```

## write

```TypeScript
write(str: string, offset?: number, length?: number, encoding?: string): number
```

Writes string to buf at offset according to the character encoding in encoding

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-write(str: string, offset?: number, length?: number, encoding?: string): number--><!--Device-FastBuffer-write(str: string, offset?: number, length?: number, encoding?: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| str | string | Yes |
| offset | number | No |
| [length](#length) | number | No |
| encoding | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.alloc(256);
let len = buf.write('\u00bd + \u00bc = \u00be', 0);
console.info(`${len} bytes: ${buf.toString('utf-8', 0, len)}`);
// Output: 12 bytes: ½ + ¼ = ¾

let buffer1 = fastbuffer.alloc(10);
let length = buffer1.write('abcd', 8);
console.info("length = " + length);
// Output: length = 2
```

## writeBigInt64BE

```TypeScript
writeBigInt64BE(value: bigint, offset?: number): number
```

Writes value to buf at the specified offset as big-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeBigInt64BE(value: bigint, offset?: number): number--><!--Device-FastBuffer-writeBigInt64BE(value: bigint, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigInt64LE

```TypeScript
writeBigInt64LE(value: bigint, offset?: number): number
```

Writes value to buf at the specified offset as little-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeBigInt64LE(value: bigint, offset?: number): number--><!--Device-FastBuffer-writeBigInt64LE(value: bigint, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64BE

```TypeScript
writeBigUInt64BE(value: bigint, offset?: number): number
```

Writes value to buf at the specified offset as big-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeBigUInt64BE(value: bigint, offset?: number): number--><!--Device-FastBuffer-writeBigUInt64BE(value: bigint, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64LE

```TypeScript
writeBigUInt64LE(value: bigint, offset?: number): number
```

Writes value to buf at the specified offset as little-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeBigUInt64LE(value: bigint, offset?: number): number--><!--Device-FastBuffer-writeBigUInt64LE(value: bigint, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleBE

```TypeScript
writeDoubleBE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeDoubleBE(value: number, offset?: number): number--><!--Device-FastBuffer-writeDoubleBE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleLE

```TypeScript
writeDoubleLE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeDoubleLE(value: number, offset?: number): number--><!--Device-FastBuffer-writeDoubleLE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeFloatBE

```TypeScript
writeFloatBE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeFloatBE(value: number, offset?: number): number--><!--Device-FastBuffer-writeFloatBE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeFloatBE(3.1415, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeFloatLE

```TypeScript
writeFloatLE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeFloatLE(value: number, offset?: number): number--><!--Device-FastBuffer-writeFloatLE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(8);
let result = buf.writeFloatLE(3.1415, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt16BE

```TypeScript
writeInt16BE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian. The value must be a valid signed 16-bit integer

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeInt16BE(value: number, offset?: number): number--><!--Device-FastBuffer-writeInt16BE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt16BE(0x0102, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt16LE

```TypeScript
writeInt16LE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian. The value must be a valid signed 16-bit integer

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeInt16LE(value: number, offset?: number): number--><!--Device-FastBuffer-writeInt16LE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt16LE(0x0304, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt32BE

```TypeScript
writeInt32BE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian. The value must be a valid signed 32-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeInt32BE(value: number, offset?: number): number--><!--Device-FastBuffer-writeInt32BE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeInt32BE(0x01020304, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt32LE

```TypeScript
writeInt32LE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian. The value must be a valid signed 32-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeInt32LE(value: number, offset?: number): number--><!--Device-FastBuffer-writeInt32LE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeInt32LE(0x05060708, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt8

```TypeScript
writeInt8(value: number, offset?: number): number
```

Writes value to buf at the specified offset. value must be a valid signed 8-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeInt8(value: number, offset?: number): number--><!--Device-FastBuffer-writeInt8(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(2);
let result = buf.writeInt8(2, 0);
console.info("result = " + result);
// Output: result = 1
let result1 = buf.writeInt8(-2, 1);
console.info("result1 = " + result1);
// Output: result1 = 2
```

## writeIntBE

```TypeScript
writeIntBE(value: number, offset: number, byteLength: number): number
```

Writes byteLength bytes of value to buf at the specified offset as big-endian

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeIntBE(value: number, offset: number, byteLength: number): number--><!--Device-FastBuffer-writeIntBE(value: number, offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeIntLE

```TypeScript
writeIntLE(value: number, offset: number, byteLength: number): number
```

Writes byteLength bytes of value to buf at the specified offset as little-endian

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeIntLE(value: number, offset: number, byteLength: number): number--><!--Device-FastBuffer-writeIntLE(value: number, offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUInt16BE

```TypeScript
writeUInt16BE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian. The value must be a valid unsigned 16-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUInt16BE(value: number, offset?: number): number--><!--Device-FastBuffer-writeUInt16BE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16BE(0xdead, 0);
console.info("result = " + result);
// Output: result = 2
let result1 = buf.writeUInt16BE(0xbeef, 2);
console.info("result1 = " + result1);
// Output: result1 = 4
```

## writeUInt16LE

```TypeScript
writeUInt16LE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian. The value must be a valid unsigned 16-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUInt16LE(value: number, offset?: number): number--><!--Device-FastBuffer-writeUInt16LE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16LE(0xdead, 0);
console.info("result = " + result);
// Output: result = 2
let result1 = buf.writeUInt16LE(0xbeef, 2);
console.info("result1 = " + result1);
// Output: result1 = 4
```

## writeUInt32BE

```TypeScript
writeUInt32BE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as big-endian. The value must be a valid unsigned 32-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUInt32BE(value: number, offset?: number): number--><!--Device-FastBuffer-writeUInt32BE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32BE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt32LE

```TypeScript
writeUInt32LE(value: number, offset?: number): number
```

Writes value to buf at the specified offset as little-endian. The value must be a valid unsigned 32-bit integer.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUInt32LE(value: number, offset?: number): number--><!--Device-FastBuffer-writeUInt32LE(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32LE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt8

```TypeScript
writeUInt8(value: number, offset?: number): number
```

Writes value to buf at the specified offset. value must be a valid unsigned 8-bit integer

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUInt8(value: number, offset?: number): number--><!--Device-FastBuffer-writeUInt8(value: number, offset?: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(4);
let result = buf.writeUInt8(0x3, 0);
console.info("result = " + result);
// Output: result = 1
let result1 = buf.writeUInt8(0x4, 1);
console.info("result1 = " + result1);
// Output: result1 = 2
let result2 = buf.writeUInt8(0x23, 2);
console.info("result2 = " + result2);
// Output: result2 = 3
let result3 = buf.writeUInt8(0x42, 3);
console.info("result3 = " + result3);
// Output: result3 = 4
```

## writeUIntBE

```TypeScript
writeUIntBE(value: number, offset: number, byteLength: number): number
```

Writes byteLength bytes of value to buf at the specified offset as big-endian

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUIntBE(value: number, offset: number, byteLength: number): number--><!--Device-FastBuffer-writeUIntBE(value: number, offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUIntLE

```TypeScript
writeUIntLE(value: number, offset: number, byteLength: number): number
```

Writes byteLength bytes of value to buf at the specified offset as little-endian

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-writeUIntLE(value: number, offset: number, byteLength: number): number--><!--Device-FastBuffer-writeUIntLE(value: number, offset: number, byteLength: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| offset | number | Yes |
| byteLength | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitializedFromPool(6);
let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## buffer

```TypeScript
buffer: ArrayBuffer
```

The arraybuffer underlying the FastBuffer object

**Type:** ArrayBuffer

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-buffer: ArrayBuffer--><!--Device-FastBuffer-buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
byteOffset: number
```

The byteOffset of the Buffers underlying ArrayBuffer object

**Type:** number

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-byteOffset: number--><!--Device-FastBuffer-byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Returns the number of bytes in buf

**Type:** number

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FastBuffer-length: number--><!--Device-FastBuffer-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
