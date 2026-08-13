# Buffer

The Buffer object is a method of handling buffers dedicated to binary data.

**Since:** 23

**Deprecated since:** -1

<!--Device-buffer-class Buffer--><!--Device-buffer-class Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## compare

```TypeScript
compare(
      target: Buffer | Uint8Array,
      targetStart?: number,
      targetEnd?: number,
      sourceStart?: number,
      sourceEnd?: number
    ): -1 | 0 | 1
```

Compares this **Buffer** object with another object.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: number,      targetEnd?: number,      sourceStart?: number,      sourceEnd?: number    ): -1 | 0 | 1--><!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: number,      targetEnd?: number,      sourceStart?: number,      sourceEnd?: number    ): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
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

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// Output: 0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// Output: -1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// Output: 1
```

## compare

```TypeScript
compare(
      target: Buffer | Uint8Array,
      targetStart?: number,
      targetEnd?: number,
      sourceStart?: number,
      sourceEnd?: number
    ): number
```

Compares buf with target and returns a number indicating whether buf comes before, after, or is the same as target in sort order. Comparison is based on the actual sequence of bytes in each Buffer.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: int,      targetEnd?: int,      sourceStart?: int,      sourceEnd?: int    ): int--><!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: int,      targetEnd?: int,      sourceStart?: int,      sourceEnd?: int    ): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| targetStart | number | No |
| targetEnd | number | No |
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

## copy

```TypeScript
copy(target: Buffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number
```

Copies data at the specified position in this **Buffer** object to the specified position in another **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-copy(target: Buffer | Uint8Array, targetStart?: int, sourceStart?: int, sourceEnd?: int): int--><!--Device-Buffer-copy(target: Buffer | Uint8Array, targetStart?: int, sourceStart?: int, sourceEnd?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
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

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);
let buf2 = buffer.allocUninitializedFromPool(26).fill('!');

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}

buf1.copy(buf2, 8, 16, 20);
console.info(buf2.toString('ascii', 0, 25));
// Output: !!!!!!!!qrst!!!!!!!!!!!!!
```

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

Creates and returns an iterator that contains key-value pairs of this **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-entries(): IterableIterator<[int, long]>--><!--Device-Buffer-entries(): IterableIterator<[int, long]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[number, number]&gt; |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[number, number]&gt; |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('buffer');
let pair = buf.entries();
let next: IteratorResult<Object[]> = pair.next();
while (!next.done) {
  console.info("buffer: " + next.value);
  /*
  Output: buffer: 0,98
           buffer: 1,117
           buffer: 2,102
           buffer: 3,102
           buffer: 4,101
           buffer: 5,114
   */
  next = pair.next();
}
```

## equals

```TypeScript
equals(otherBuffer: Uint8Array | Buffer): boolean
```

Checks whether this **Buffer** object is the same as another **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-equals(otherBuffer: Uint8Array | Buffer): boolean--><!--Device-Buffer-equals(otherBuffer: Uint8Array | Buffer): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| otherBuffer | Uint8Array \| [Buffer](arkts-arkts-buffer-buffer-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('ABC');
let buf2 = buffer.from('414243', 'hex');
let buf3 = buffer.from('ABCD');

console.info(buf1.equals(buf2).toString());
// Output: true
console.info(buf1.equals(buf3).toString());
// Output: false
```

## fill

```TypeScript
fill(
      value: string | Buffer | Uint8Array | number | number | number,
      offset?: number,
      end?: number,
      encoding?: BufferEncoding
    ): Buffer
```

Fills this **Buffer** object at the specified position. By default, data is filled cyclically.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-fill(      value: string | Buffer | Uint8Array | int | double | long,      offset?: int,      end?: int,      encoding?: BufferEncoding    ): Buffer--><!--Device-Buffer-fill(      value: string | Buffer | Uint8Array | int | double | long,      offset?: int,      end?: int,      encoding?: BufferEncoding    ): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array \| number \| number \| number | Yes |
| offset | number | No |
| end | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## includes

```TypeScript
includes(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean
```

Checks whether this **Buffer** object contains the specified value.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-includes(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): boolean--><!--Device-Buffer-includes(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| number \| number \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| [byteOffset](#byteOffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## indexOf

```TypeScript
indexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

Obtains the index of the first occurrence of the specified value in this **Buffer** object. If no match is found, **-1** is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-indexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int--><!--Device-Buffer-indexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| number \| number \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| [byteOffset](#byteOffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## keys

```TypeScript
keys(): IterableIterator<number>
```

Creates and returns an iterator that contains the keys of this **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-keys(): IterableIterator<int>--><!--Device-Buffer-keys(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('buffer');
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
lastIndexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

Obtains the index of the last occurrence of the specified value in this **Buffer** object. If no match is found, **-1** is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-lastIndexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int--><!--Device-Buffer-lastIndexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| number \| number \| number \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| [byteOffset](#byteOffset) | number | No |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## readBigInt64BE

```TypeScript
readBigInt64BE(offset?: number): bigint
```

Reads a 64-bit, big-endian, signed big integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigInt64BE(offset?: int): bigint--><!--Device-Buffer-readBigInt64BE(offset?: int): bigint-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64BE(0).toString());
// Output: 7161960797921896816

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## readBigInt64LE

```TypeScript
readBigInt64LE(offset?: number): bigint
```

Reads a 64-bit, little-endian, signed big integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigInt64LE(offset?: int): bigint--><!--Device-Buffer-readBigInt64LE(offset?: int): bigint-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// Output: 8100120198111388771

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## readBigUInt64BE

```TypeScript
readBigUInt64BE(offset?: number): bigint
```

Reads a 64-bit, big-endian, unsigned big integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigUInt64BE(offset?: int): bigint--><!--Device-Buffer-readBigUInt64BE(offset?: int): bigint-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64BE(0).toString());
// Output: 7161960797921896816
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## readBigUInt64LE

```TypeScript
readBigUInt64LE(offset?: number): bigint
```

Reads a 64-bit, little-endian, unsigned big integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigUInt64LE(offset?: int): bigint--><!--Device-Buffer-readBigUInt64LE(offset?: int): bigint-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// Output: 8100120198111388771

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## readDoubleBE

```TypeScript
readDoubleBE(offset?: number): number
```

Reads a 64-bit, big-endian, double-precision floating-point number from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readDoubleBE(offset?: int): double--><!--Device-Buffer-readDoubleBE(offset?: int): double-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleBE(0).toString());
// Output: 8.20788039913184e-304
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## readDoubleLE

```TypeScript
readDoubleLE(offset?: number): number
```

Reads a 64-bit, little-endian, double-precision floating-point number from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readDoubleLE(offset?: int): double--><!--Device-Buffer-readDoubleLE(offset?: int): double-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleLE(0).toString());
// Output: 5.447603722011605e-270
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## readFloatBE

```TypeScript
readFloatBE(offset?: number): number
```

Reads a 32-bit, big-endian, single-precision floating-point number from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readFloatBE(offset?: int): double--><!--Device-Buffer-readFloatBE(offset?: int): double-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatBE(0).toString());
// Output: 2.387939260590663e-38
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeFloatBE(0xcabcbcbc, 0);
console.info("result = " + result);
// Output: result = 4
```

## readFloatLE

```TypeScript
readFloatLE(offset?: number): number
```

Reads a 32-bit, little-endian, single-precision floating-point number from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readFloatLE(offset?: int): double--><!--Device-Buffer-readFloatLE(offset?: int): double-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatLE(0).toString());
// Output: 1.539989614439558e-36
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeFloatLE(0xcabcbcbc, 0);
console.info("result = " + result);
// Output: result = 4
```

## readInt16BE

```TypeScript
readInt16BE(offset?: number): number
```

Reads a 16-bit, big-endian, signed integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt16BE(offset?: int): long--><!--Device-Buffer-readInt16BE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 5]);
console.info(buf.readInt16BE(0).toString());
// Output: 5
let buf1 = buffer.alloc(2);
let result = buf1.writeInt16BE(0x1234, 0);
console.info("result = " + result);
// Output: result = 2
```

## readInt16LE

```TypeScript
readInt16LE(offset?: number): number
```

Reads a 16-bit, little-endian, signed integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt16LE(offset?: int): long--><!--Device-Buffer-readInt16LE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 5]);
console.info(buf.readInt16LE(0).toString());
// Output: 1280
let buf1 = buffer.alloc(2);
let result = buf1.writeInt16BE(0x1234, 0);
console.info("result = " + result);
// Output: result = 2
```

## readInt32BE

```TypeScript
readInt32BE(offset?: number): number
```

Reads a 32-bit, big-endian, signed integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt32BE(offset?: int): long--><!--Device-Buffer-readInt32BE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 0, 0, 5]);
console.info(buf.readInt32BE(0).toString());
// Output: 5
let buf1 = buffer.alloc(4);
let result = buf1.writeInt32BE(0x12345678, 0);
console.info("result = " + result);
// Output: result = 4
```

## readInt32LE

```TypeScript
readInt32LE(offset?: number): number
```

Reads a 32-bit, little-endian, signed integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt32LE(offset?: int): long--><!--Device-Buffer-readInt32LE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 0, 0, 5]);
console.info(buf.readInt32LE(0).toString());
// Output: 83886080
let buf1 = buffer.alloc(4);
let result = buf1.writeInt32BE(0x12345678, 0);
console.info("result = " + result);
// Output: result = 4
```

## readInt8

```TypeScript
readInt8(offset?: number): number
```

Reads an 8-bit signed integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt8(offset?: int): long--><!--Device-Buffer-readInt8(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([-1, 5]);
console.info(buf.readInt8(0).toString());
// Output: 0
console.info(buf.readInt8(1).toString());
// Output: 5
let buf1 = buffer.allocUninitializedFromPool(2);
let result = buf1.writeInt8(0x12);
console.info("result = " + result);
// Output: result = 1
```

## readIntBE

```TypeScript
readIntBE(offset: number, byteLength: number): number
```

Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the result as a big-endian, two's complement signed value that supports up to 48 bits of precision.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readIntBE(offset: int, byteLength: int): long--><!--Device-Buffer-readIntBE(offset: int, byteLength: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from("ab");
let num = buf.readIntBE(0, 1);
console.info(num.toString());
// Output: 97
let buf1 = buffer.allocUninitializedFromPool(6);
let result = buf1.writeIntBE(0x123456789011, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## readIntLE

```TypeScript
readIntLE(offset: number, byteLength: number): number
```

Reads the specified number of bytes from this **Buffer** object at the specified offset and interprets the result as a little-endian, two's complement signed value that supports up to 48 bits of precision.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readIntLE(offset: int, byteLength: int): long--><!--Device-Buffer-readIntLE(offset: int, byteLength: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readIntLE(0, 6).toString(16));
// Output: -546f87a9cbee
let buf1 = buffer.allocUninitializedFromPool(6);
let result = buf1.writeIntLE(0x123456789011, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## readUInt16BE

```TypeScript
readUInt16BE(offset?: number): number
```

Reads a 16-bit, big-endian, unsigned integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt16BE(offset?: int): long--><!--Device-Buffer-readUInt16BE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16BE(0).toString(16));
// Output: 1234
console.info(buf.readUInt16BE(1).toString(16));
// Output: 3456
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt16BE(0x1234, 0);
console.info("result = " + result);
// Output: result = 2
```

## readUInt16LE

```TypeScript
readUInt16LE(offset?: number): number
```

Reads a 16-bit, little-endian, unsigned integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt16LE(offset?: int): long--><!--Device-Buffer-readUInt16LE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16LE(0).toString(16));
// Output: 3412
console.info(buf.readUInt16LE(1).toString(16));
// Output: 5634
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt16LE(0x1234, 0);
console.info("result = " + result);
// Output: result = 2
```

## readUInt32BE

```TypeScript
readUInt32BE(offset?: number): number
```

Reads a 32-bit, big-endian, unsigned integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt32BE(offset?: int): long--><!--Device-Buffer-readUInt32BE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32BE(0).toString(16));
// Output: 12345678
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt32BE(0x12345678, 0);
console.info("result = " + result);
// Output: result = 4
```

## readUInt32LE

```TypeScript
readUInt32LE(offset?: number): number
```

Reads a 32-bit, little-endian, unsigned integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt32LE(offset?: int): long--><!--Device-Buffer-readUInt32LE(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32LE(0).toString(16));
// Output: 78563412
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt32LE(0x12345678, 0);
console.info("result = " + result);
// Output: result = 4
```

## readUInt8

```TypeScript
readUInt8(offset?: number): number
```

Reads an 8-bit unsigned integer from this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt8(offset?: int): long--><!--Device-Buffer-readUInt8(offset?: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, -2]);
console.info(buf.readUInt8(0).toString());
// Output: 1
console.info(buf.readUInt8(1).toString());
// Output: 0
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt8(0x42);
console.info("result = " + result);
// Output: result = 1
```

## readUIntBE

```TypeScript
readUIntBE(offset: number, byteLength: number): number
```

Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the result as an unsigned, big-endian integer that supports up to 48 bits of precision.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUIntBE(offset: int, byteLength: int): long--><!--Device-Buffer-readUIntBE(offset: int, byteLength: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntBE(0, 6).toString(16));
// Output: 1234567890ab
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUIntBE(0x13141516, 0, 4);
console.info("result = " + result);
// Output: result = 4
```

## readUIntLE

```TypeScript
readUIntLE(offset: number, byteLength: number): number
```

Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the result as an unsigned, little-endian integer that supports up to 48 bits of precision.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUIntLE(offset: int, byteLength: int): long--><!--Device-Buffer-readUIntLE(offset: int, byteLength: int): long-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntLE(0, 6).toString(16));
// Output: ab9078563412
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUIntLE(0x13141516, 0, 4);
console.info("result = " + result);
// Output: result = 4
```

## subarray

```TypeScript
subarray(start?: number, end?: number): Buffer
```

Truncates this **Buffer** object from the specified position to create a new **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-subarray(start?: int, end?: int): Buffer--><!--Device-Buffer-subarray(start?: int, end?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
const buf2 = buf1.subarray(0, 3);
console.info(buf2.toString('ascii', 0, buf2.length));
// Output: abc
```

## swap16

```TypeScript
swap16(): Buffer
```

Converts this **Buffer** object into an array of unsigned 16-bit integers and swaps the byte order in place.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap16(): Buffer--><!--Device-Buffer-swap16(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// Output: 0102030405060708
buf1.swap16();
console.info(buf1.toString('hex'));
// Output: 0201040306050807
```

## swap32

```TypeScript
swap32(): Buffer
```

Converts this **Buffer** object into an array of unsigned 32-bit integers and swaps the byte order in place.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap32(): Buffer--><!--Device-Buffer-swap32(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// Output: 0102030405060708
buf1.swap32();
console.info(buf1.toString('hex'));
// Output: 0403020108070605
```

## swap64

```TypeScript
swap64(): Buffer
```

Converts this **Buffer** object into an array of unsigned 64-bit integers and swaps the byte order in place.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap64(): Buffer--><!--Device-Buffer-swap64(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer-size-error) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
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

Converts this **Buffer** object into a JSON object.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-toJSON(): Object--><!--Device-Buffer-toJSON(): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
let obj = buf1.toJSON();
console.info(JSON.stringify(obj));
// Output: {"type":"Buffer","data":[1,2,3,4,5]}
```

## toJSON

```TypeScript
toJSON(): jsonx.JsonElement
```

Converts this Buffer instance into a JsonElement.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-toJSON(): jsonx.JsonElement--><!--Device-Buffer-toJSON(): jsonx.JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| jsonx.JsonElement |

## toString

```TypeScript
toString(encoding?: string, start?: number, end?: number): string
```

Converts the data at the specified position in this **Buffer** object into a string in the specified encoding format.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-toString(encoding?: string, start?: number, end?: number): string--><!--Device-Buffer-toString(encoding?: string, start?: number, end?: number): string-End-->

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

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);
for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
console.info(buf1.toString('utf-8'));
// Output: abcdefghijklmnopqrstuvwxyz
```

## toString

```TypeScript
toString(): string
```

Decodes buf to a string according to the specified character encoding in encoding

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Buffer-toString(): string--><!--Device-Buffer-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
toString(encoding?: BufferEncoding, start?: number, end?: number): string
```

Decodes buf to a string according to the specified character encoding in encoding

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-toString(encoding?: BufferEncoding, start?: int, end?: int): string--><!--Device-Buffer-toString(encoding?: BufferEncoding, start?: int, end?: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## values

```TypeScript
values(): IterableIterator<number>
```

Creates and returns an iterator that contains the values of this **Buffer** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-values(): IterableIterator<long>--><!--Device-Buffer-values(): IterableIterator<long>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;number&gt; |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('buffer');
let pair = buf1.values();
let next:IteratorResult<number> = pair.next();
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

Writes a string of the specified length to this **Buffer** object at the specified position in the given encoding format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-write(str: string, offset?: int, length?: int, encoding?: string): int--><!--Device-Buffer-write(str: string, offset?: int, length?: int, encoding?: string): int-End-->

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

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.alloc(256);
let len = buf.write('\u00bd + \u00bc = \u00be', 0);
console.info(`${len} bytes: ${buf.toString('utf-8', 0, len)}`);
// Output: 12 bytes: ½ + ¼ = ¾

let buffer1 = buffer.alloc(10);
let length = buffer1.write('abcd', 8);
console.info("length = " + length);
// Output: length = 2
```

## writeBigInt64BE

```TypeScript
writeBigInt64BE(value: bigint, offset?: number): number
```

Writes a 64-bit, big-endian, signed big integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigInt64BE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigInt64BE(value: bigint, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigInt64LE

```TypeScript
writeBigInt64LE(value: bigint, offset?: number): number
```

Writes a 64-bit, little-endian, signed big integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigInt64LE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigInt64LE(value: bigint, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64BE

```TypeScript
writeBigUInt64BE(value: bigint, offset?: number): number
```

Writes a 64-bit, big-endian, signed big integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigUInt64BE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigUInt64BE(value: bigint, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64LE

```TypeScript
writeBigUInt64LE(value: bigint, offset?: number): number
```

Writes a 64-bit, little-endian, unsigned big integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigUInt64LE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigUInt64LE(value: bigint, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleBE

```TypeScript
writeDoubleBE(value: number, offset?: number): number
```

Writes a 64-bit, big-endian, double-precision floating-point number to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeDoubleBE(value: double, offset?: int): int--><!--Device-Buffer-writeDoubleBE(value: double, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleLE

```TypeScript
writeDoubleLE(value: number, offset?: number): number
```

Writes a 64-bit, little-endian, double-precision floating-point number to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeDoubleLE(value: double, offset?: int): int--><!--Device-Buffer-writeDoubleLE(value: double, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeFloatBE

```TypeScript
writeFloatBE(value: number, offset?: number): number
```

Writes a 32-bit, big-endian, single-precision floating-point number to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeFloatBE(value: double, offset?: int): int--><!--Device-Buffer-writeFloatBE(value: double, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatBE(0xcafebabe, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeFloatLE

```TypeScript
writeFloatLE(value: number, offset?: number): number
```

Writes a 32-bit, little-endian, single-precision floating-point number to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeFloatLE(value: double, offset?: int): int--><!--Device-Buffer-writeFloatLE(value: double, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatLE(0xcafebabe, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt16BE

```TypeScript
writeInt16BE(value: number, offset?: number): number
```

Writes a 16-bit, big-endian, signed integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt16BE(value: long, offset?: int): int--><!--Device-Buffer-writeInt16BE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16BE(0x0102, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt16LE

```TypeScript
writeInt16LE(value: number, offset?: number): number
```

Writes a 16-bit, little-endian, signed integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt16LE(value: long, offset?: int): int--><!--Device-Buffer-writeInt16LE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16LE(0x0304, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt32BE

```TypeScript
writeInt32BE(value: number, offset?: number): number
```

Writes a 32-bit, big-endian, signed integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt32BE(value: long, offset?: int): int--><!--Device-Buffer-writeInt32BE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32BE(0x01020304, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt32LE

```TypeScript
writeInt32LE(value: number, offset?: number): number
```

Writes a 32-bit, little-endian, signed integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt32LE(value: long, offset?: int): int--><!--Device-Buffer-writeInt32LE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32LE(0x05060708, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt8

```TypeScript
writeInt8(value: number, offset?: number): number
```

Writes an 8-bit signed integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt8(value: long, offset?: int): int--><!--Device-Buffer-writeInt8(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
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

Writes a big-endian signed value of the specified length to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeIntBE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeIntBE(value: long, offset: int, byteLength: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeIntLE

```TypeScript
writeIntLE(value: number, offset: number, byteLength: number): number
```

Writes a little-endian signed value of the specified length to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeIntLE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeIntLE(value: long, offset: int, byteLength: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUInt16BE

```TypeScript
writeUInt16BE(value: number, offset?: number): number
```

Writes a 16-bit, big-endian, unsigned integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt16BE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt16BE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
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

Writes a 16-bit, little-endian, unsigned integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt16LE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt16LE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
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

Writes a 32-bit, big-endian, unsigned integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt32BE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt32BE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32BE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt32LE

```TypeScript
writeUInt32LE(value: number, offset?: number): number
```

Writes a 32-bit, little-endian, unsigned integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt32LE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt32LE(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32LE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt8

```TypeScript
writeUInt8(value: number, offset?: number): number
```

Writes an 8-bit unsigned integer to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt8(value: long, offset?: int): int--><!--Device-Buffer-writeUInt8(value: long, offset?: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
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

Writes an unsigned big-endian value of the specified length to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUIntBE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeUIntBE(value: long, offset: int, byteLength: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUIntLE

```TypeScript
writeUIntLE(value: number, offset: number, byteLength: number): number
```

Writes an unsigned little-endian value of the specified length to this **Buffer** object at the specified offset.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUIntLE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeUIntLE(value: long, offset: int, byteLength: int): int-End-->

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
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## buffer

```TypeScript
buffer: ArrayBuffer
```

**ArrayBuffer** object.

**Type:** ArrayBuffer

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-buffer: ArrayBuffer--><!--Device-Buffer-buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
byteOffset: number
```

Offset of the **Buffer** object in the memory pool.

**Type:** number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-byteOffset: number--><!--Device-Buffer-byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Length of the **Buffer** object, in bytes.

**Type:** number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-length: number--><!--Device-Buffer-length: number-End-->

**System capability:** SystemCapability.Utils.Lang
