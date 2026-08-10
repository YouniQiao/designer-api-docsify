# Buffer

Buffer对象是处理二进制数据的缓冲区。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-buffer-class Buffer--><!--Device-buffer-class Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
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

比较当前Buffer对象与目标Buffer对象，并返回Buffer在排序中的结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: number,      targetEnd?: number,      sourceStart?: number,      sourceEnd?: number    ): -1 | 0 | 1--><!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: number,      targetEnd?: number,      sourceStart?: number,      sourceEnd?: number    ): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 要比较的实例对象。 |
| targetStart | number | No | target实例中开始的偏移量。默认值：0。 |
| targetEnd | number | No | target实例中结束的偏移量（不包含结束位置）。默认值：目标对象的字节长度。 |
| sourceStart | number | No | this实例中开始的偏移量。默认值：0。 |
| sourceEnd | number | No | this实例中结束的偏移量（不包含结束位置）。默认值：当前对象的字节长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| -1 | 比较结果。如果两个Buffer对象相同，则返回0；如果当前对象在排序时位于目标对象之后，则返回1； 如果当前对象在排序时位于目标对象之前，则返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[targetStart/targetEnd/sourceStart/sourceEnd]" is out of range. It must be >= 0 and <= [right range]. Received value is: [targetStart/targetEnd/sourceStart/sourceEnd] |

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
      targetStart?: int,
      targetEnd?: int,
      sourceStart?: int,
      sourceEnd?: int
    ): int
```

比较当前Buffer对象与目标Buffer对象，并返回Buffer在排序中的结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: int,      targetEnd?: int,      sourceStart?: int,      sourceEnd?: int    ): int--><!--Device-Buffer-compare(      target: Buffer | Uint8Array,      targetStart?: int,      targetEnd?: int,      sourceStart?: int,      sourceEnd?: int    ): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 要比较的实例对象。 |
| targetStart | int | No | `target`实例中开始的偏移量。默认值：0。 |
| targetEnd | int | No | `target`实例中结束的偏移量（不包含结束位置）。默认值：目标对象的字节长度。 |
| sourceStart | int | No | `this`实例中开始的偏移量。默认值：0。 |
| sourceEnd | int | No | `this`实例中结束的偏移量（不包含结束位置）。默认值：当前对象的字节长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回比较结果。-1：当前排列在目标前，0：当前与目标相同，1：当前排列在目标后。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[targetStart/targetEnd/sourceStart/sourceEnd]" is out of range. It must be >= 0 and <= [right range]. Received value is: [targetStart/targetEnd/sourceStart/sourceEnd] |

## copy

ArkTS-Dyn:
```TypeScript
copy(target: Buffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number
```

ArkTS-Sta:
```TypeScript
copy(target: Buffer | Uint8Array, targetStart?: int, sourceStart?: int, sourceEnd?: int): int
```

将`this`实例中指定位置的数据复制到`target`的指定位置上，并返回复制的字节总长度。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-copy(target: Buffer | Uint8Array, targetStart?: int, sourceStart?: int, sourceEnd?: int): int--><!--Device-Buffer-copy(target: Buffer | Uint8Array, targetStart?: int, sourceStart?: int, sourceEnd?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 要复制到的Buffer或Uint8Array实例。 |
| targetStart | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | `target`实例中开始写入的偏移量。默认值：0。 |
| sourceStart | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | `this`实例中开始复制的偏移量。默认值: 0。 |
| sourceEnd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | `this`实例中结束复制的偏移量（不包含结束位置）。默认值：当前对象的字节长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 复制的字节总长度。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[targetStart/sourceStart/sourceEnd]" is out of range. It must be >= 0. Received value is: [targetStart/sourceStart/sourceEnd] |

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

ArkTS-Dyn:
```TypeScript
entries(): IterableIterator<[number, number]>
```

ArkTS-Sta:
```TypeScript
entries(): IterableIterator<[int, long]>
```

返回一个包含key和value的迭代器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-entries(): IterableIterator<[int, long]>--><!--Device-Buffer-entries(): IterableIterator<[int, long]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, number]&gt; | 包含key和value的迭代器，同时两者皆为number类型。<br>**Applicable version:** 9 - 10 |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, number]&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, long]&gt; | <br>**Applicable version:** 11 and later |

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

比较`this`实例和otherBuffer实例是否相等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-equals(otherBuffer: Uint8Array | Buffer): boolean--><!--Device-Buffer-equals(otherBuffer: Uint8Array | Buffer): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| otherBuffer | Uint8Array \| Buffer | Yes | 比较的目标对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 相等则返回true，否则返回false。 |

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

ArkTS-Dyn:
```TypeScript
fill(
      value: string | Buffer | Uint8Array | number | number | number,
      offset?: number,
      end?: number,
      encoding?: BufferEncoding
    ): Buffer
```

ArkTS-Sta:
```TypeScript
fill(
      value: string | Buffer | Uint8Array | int | double | long,
      offset?: int,
      end?: int,
      encoding?: BufferEncoding
    ): Buffer
```

使用value填充当前对象指定位置的数据，默认为循环填充，并返回填充后的Buffer对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-fill(      value: string | Buffer | Uint8Array | int | double | long,      offset?: int,      end?: int,      encoding?: BufferEncoding    ): Buffer--><!--Device-Buffer-fill(      value: string | Buffer | Uint8Array | int | double | long,      offset?: int,      end?: int,      encoding?: BufferEncoding    ): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: string \| Buffer \| Uint8Array \| number \| number \| number  <br>ArkTS-Sta：string \| Buffer \| Uint8Array \| int \| double \| long | Yes | 用于填充的值。<br>**Since:** 11 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 起始偏移量。默认值：0。 |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 结束偏移量（不包含结束位置）。默认值：当前对象的字节长度。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 字符编码格式（value为string才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 返回填充后的Buffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[offset/end]" is out of range. It must be >= 0 and <= [right range]. Received value is: [offset/end] |

## includes

ArkTS-Dyn:
```TypeScript
includes(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean
```

ArkTS-Sta:
```TypeScript
includes(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): boolean
```

检查Buffer对象是否包含value值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-includes(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): boolean--><!--Device-Buffer-includes(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array  <br>ArkTS-Sta：string \| int \| double \| long \| Buffer \| Uint8Array | Yes | 要搜索的内容。<br>**Since:** 11 |
| byteOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 字节偏移量。如果为负数，则从末尾开始计算偏移量。默认值：0。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 字符编码格式（value为string才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 存在返回true，否则返回false。 |

## indexOf

ArkTS-Dyn:
```TypeScript
indexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

ArkTS-Sta:
```TypeScript
indexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int
```

返回当前对象中首次出现value的索引，如果不包含value，则返回-1。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-indexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int--><!--Device-Buffer-indexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array  <br>ArkTS-Sta：string \| int \| double \| long \| Buffer \| Uint8Array | Yes | 要查找的内容。<br>**Since:** 11 |
| byteOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 字节偏移量。如果为负数，则从末尾开始计算偏移量。默认值：0。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 字符编码格式（value为string才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 第一次出现位置。 |

## keys

ArkTS-Dyn:
```TypeScript
keys(): IterableIterator<number>
```

ArkTS-Sta:
```TypeScript
keys(): IterableIterator<int>
```

返回包含key值的迭代器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-keys(): IterableIterator<int>--><!--Device-Buffer-keys(): IterableIterator<int>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; | 返回一个包含key值的迭代器。 |

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

ArkTS-Dyn:
```TypeScript
lastIndexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

ArkTS-Sta:
```TypeScript
lastIndexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int
```

返回this实例中最后一次出现value的索引，如果对象不包含value，则返回-1。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-lastIndexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int--><!--Device-Buffer-lastIndexOf(value: string | int | double | long | Buffer | Uint8Array, byteOffset?: int, encoding?: BufferEncoding): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array  <br>ArkTS-Sta：string \| int \| double \| long \| Buffer \| Uint8Array | Yes | 要搜索的内容。<br>**Since:** 11 |
| byteOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 字节偏移量。如果为负数，则从末尾开始计算偏移量。默认值：Buffer.length。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 字符编码格式（value为string才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 最后一次出现value值的索引。 |

## readBigInt64BE

ArkTS-Dyn:
```TypeScript
readBigInt64BE(offset?: number): bigint
```

ArkTS-Sta:
```TypeScript
readBigInt64BE(offset?: int): bigint
```

从指定的`offset`处读取有符号的大端序64位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigInt64BE(offset?: int): bigint--><!--Device-Buffer-readBigInt64BE(offset?: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readBigInt64LE(offset?: number): bigint
```

ArkTS-Sta:
```TypeScript
readBigInt64LE(offset?: int): bigint
```

从指定的`offset`处读取有符号的小端序64位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigInt64LE(offset?: int): bigint--><!--Device-Buffer-readBigInt64LE(offset?: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 8，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readBigUInt64BE(offset?: number): bigint
```

ArkTS-Sta:
```TypeScript
readBigUInt64BE(offset?: int): bigint
```

从指定的`offset`处读取无符号的大端序64位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigUInt64BE(offset?: int): bigint--><!--Device-Buffer-readBigUInt64BE(offset?: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 8，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readBigUInt64LE(offset?: number): bigint
```

ArkTS-Sta:
```TypeScript
readBigUInt64LE(offset?: int): bigint
```

从指定的`offset`处读取无符号的小端序64位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readBigUInt64LE(offset?: int): bigint--><!--Device-Buffer-readBigUInt64LE(offset?: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 8，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readDoubleBE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readDoubleBE(offset?: int): double
```

从指定的`offset`处读取64位大端序双精度值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readDoubleBE(offset?: int): double--><!--Device-Buffer-readDoubleBE(offset?: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 8，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readDoubleLE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readDoubleLE(offset?: int): double
```

从指定的`offset`处读取64位小端序双精度值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readDoubleLE(offset?: int): double--><!--Device-Buffer-readDoubleLE(offset?: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 8，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readFloatBE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readFloatBE(offset?: int): double
```

从指定的`offset`处读取32位大端序浮点数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readFloatBE(offset?: int): double--><!--Device-Buffer-readFloatBE(offset?: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readFloatLE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readFloatLE(offset?: int): double
```

从指定的`offset`处读取32位小端序浮点数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readFloatLE(offset?: int): double--><!--Device-Buffer-readFloatLE(offset?: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readInt16BE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readInt16BE(offset?: int): long
```

从指定的`offset`处读取有符号的大端序16位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt16BE(offset?: int): long--><!--Device-Buffer-readInt16BE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 2，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readInt16LE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readInt16LE(offset?: int): long
```

从指定的`offset`处读取有符号的小端序16位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt16LE(offset?: int): long--><!--Device-Buffer-readInt16LE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 2，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readInt32BE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readInt32BE(offset?: int): long
```

从指定的`offset`处读取有符号的大端序32位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt32BE(offset?: int): long--><!--Device-Buffer-readInt32BE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readInt32LE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readInt32LE(offset?: int): long
```

从指定的`offset`处读取有符号的小端序32位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt32LE(offset?: int): long--><!--Device-Buffer-readInt32LE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readInt8(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readInt8(offset?: int): long
```

从指定的`offset`处读取有符号的8位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readInt8(offset?: int): long--><!--Device-Buffer-readInt8(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 1，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readIntBE(offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
readIntBE(offset: int, byteLength: int): long
```

从指定的`offset`处读取byteLength个字节，并将结果解释为支持最高48位精度的大端序、二进制补码有符号值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readIntBE(offset: int, byteLength: int): long--><!--Device-Buffer-readIntBE(offset: int, byteLength: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。取值范围：0 <= offset <= Buffer.length - byteLength，默认值：0。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取的内容。当offset为小数时，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
readIntLE(offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
readIntLE(offset: int, byteLength: int): long
```

从指定的`offset`处读取`byteLength`个字节，并将结果解释为支持最高48位精度的小端序、二进制补码有符号值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readIntLE(offset: int, byteLength: int): long--><!--Device-Buffer-readIntLE(offset: int, byteLength: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。取值范围：0 <= offset <= Buffer.length - byteLength，默认值：0。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。当offset为小数时，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
readUInt16BE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readUInt16BE(offset?: int): long
```

从指定的`offset`处读取无符号的大端序16位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt16BE(offset?: int): long--><!--Device-Buffer-readUInt16BE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 2，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readUInt16LE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readUInt16LE(offset?: int): long
```

从指定的`offset`处的buf读取无符号的小端序16位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt16LE(offset?: int): long--><!--Device-Buffer-readUInt16LE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 2，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readUInt32BE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readUInt32BE(offset?: int): long
```

从指定的`offset`处的buf读取无符号的大端序32位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt32BE(offset?: int): long--><!--Device-Buffer-readUInt32BE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readUInt32LE(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readUInt32LE(offset?: int): long
```

从指定的`offset`处的buf读取无符号的小端序32位整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt32LE(offset?: int): long--><!--Device-Buffer-readUInt32LE(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 4，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readUInt8(offset?: number): number
```

ArkTS-Sta:
```TypeScript
readUInt8(offset?: int): long
```

从`offset`处读取8位无符号整型数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUInt8(offset?: int): long--><!--Device-Buffer-readUInt8(offset?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。取值范围：0 <= offset <= Buffer.length - 1，默认值：0。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1 . Received value is: [offset] |

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

ArkTS-Dyn:
```TypeScript
readUIntBE(offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
readUIntBE(offset: int, byteLength: int): long
```

从指定的`offset`处的buf读取`byteLength`个字节，并将结果解释为支持最高48位精度的无符号大端序整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUIntBE(offset: int, byteLength: int): long--><!--Device-Buffer-readUIntBE(offset: int, byteLength: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。取值范围：0 <= offset <= Buffer.length - byteLength，默认值：0。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要读取的字节数。读取的字节数。取值范围：1 <= byteLength <= 6。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。当offset为小数时，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
readUIntLE(offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
readUIntLE(offset: int, byteLength: int): long
```

从指定的`offset`处的buf读取`byteLength`个字节，并将结果解释为支持最高48位精度的无符号小端序整数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-readUIntLE(offset: int, byteLength: int): long--><!--Device-Buffer-readUIntLE(offset: int, byteLength: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。取值范围：0 <= offset <= Buffer.length - byteLength，默认值：0。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 读取的字节数。取值范围：1 <= byteLength <= 6。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 读取出的内容。当offset为小数时，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
subarray(start?: number, end?: number): Buffer
```

ArkTS-Sta:
```TypeScript
subarray(start?: int, end?: int): Buffer
```

截取当前对象指定位置的数据并返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-subarray(start?: int, end?: int): Buffer--><!--Device-Buffer-subarray(start?: int, end?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 截取开始位置。默认值：0。 |
| end | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 截取结束位置（不包含结束位置）。默认值：当前对象的字节长度。在传入null时返回空Buffer。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 返回新的Buffer对象。当start < 0或end < 0时返回空Buffer。 |

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

将当前对象转换为无符号的16位整数数组，并交换字节顺序。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap16(): Buffer--><!--Device-Buffer-swap16(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 交换之后的Buffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200009 | The buffer size must be a multiple of 16-bits |

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

将当前对象转换为无符号的32位整数数组，并交换字节顺序。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap32(): Buffer--><!--Device-Buffer-swap32(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 交换之后的Buffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200009 | The buffer size must be a multiple of 32-bits |

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

将当前对象转换为无符号的64位整数数组，并交换字节顺序。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-swap64(): Buffer--><!--Device-Buffer-swap64(): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 交换之后的Buffer对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200009 | The buffer size must be a multiple of 64-bits |

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

将Buffer转为JSON并返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-toJSON(): Object--><!--Device-Buffer-toJSON(): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Object | JSON对象。 |

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

将此Buffer实例转换为JsonElement。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-toJSON(): jsonx.JsonElement--><!--Device-Buffer-toJSON(): jsonx.JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| jsonx.JsonElement | 新的JsonElement对象，包含此Buffer的内容。 |

## toString

```TypeScript
toString(encoding?: string, start?: number, end?: number): string
```

将当前对象中指定位置的数据转成指定编码格式的字符串并返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-toString(encoding?: string, start?: number, end?: number): string--><!--Device-Buffer-toString(encoding?: string, start?: number, end?: number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | 字符编码格式。默认值：'utf8'。 |
| start | number | No | 开始位置。默认值：0。 |
| end | number | No | 结束位置。默认值：Buffer.length。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 字符串。当start >= Buffer.length或start > end时返回空字符串。 |

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

按照encoding指定的字符编码将buf解码为字符串。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Buffer-toString(): string--><!--Device-Buffer-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 解码后的字符串。 |

## toString

```TypeScript
toString(encoding?: BufferEncoding, start?: int, end?: int): string
```

按照encoding指定的字符编码将buf解码为字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-toString(encoding?: BufferEncoding, start?: int, end?: int): string--><!--Device-Buffer-toString(encoding?: BufferEncoding, start?: int, end?: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | encoding [encoding='utf8'] 使用的字符编码。 |
| start | int | No | start [start = 0] 开始解码的字节偏移量。 该值应为整数。 |
| end | int | No | end [end = buf.length] 结束解码的字节偏移量（不包含结束位置）。 该值应为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 解码后的字符串。 |

## values

ArkTS-Dyn:
```TypeScript
values(): IterableIterator<number>
```

ArkTS-Sta:
```TypeScript
values(): IterableIterator<long>
```

返回一个包含value的迭代器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-values(): IterableIterator<long>--><!--Device-Buffer-values(): IterableIterator<long>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;long&gt; | 迭代器。 |

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

ArkTS-Dyn:
```TypeScript
write(str: string, offset?: number, length?: number, encoding?: string): number
```

ArkTS-Sta:
```TypeScript
write(str: string, offset?: int, length?: int, encoding?: string): int
```

在Buffer对象的offset偏移处写入指定编码的字符串，写入的字节长度为length。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-write(str: string, offset?: int, length?: int, encoding?: string): int--><!--Device-Buffer-write(str: string, offset?: int, length?: int, encoding?: string): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | 要写入Buffer的字符串。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。 |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 最大字节长度。默认值：（Buffer.length - offset）。 |
| encoding | string | No | 字符编码。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[offset/length]" is out of range. It must be >= 0 and <= buf.length. Received value is: [offset/length] |

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

ArkTS-Dyn:
```TypeScript
writeBigInt64BE(value: bigint, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeBigInt64BE(value: bigint, offset?: int): int
```

在Buffer对象的offset偏移处写入有符号的大端序64位BigInt型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigInt64BE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigInt64BE(value: bigint, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigInt64LE

ArkTS-Dyn:
```TypeScript
writeBigInt64LE(value: bigint, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeBigInt64LE(value: bigint, offset?: int): int
```

在Buffer对象的offset偏移处写入有符号的小端序64位BigInt型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigInt64LE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigInt64LE(value: bigint, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64BE

ArkTS-Dyn:
```TypeScript
writeBigUInt64BE(value: bigint, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeBigUInt64BE(value: bigint, offset?: int): int
```

在Buffer对象的offset偏移处写入无符号的大端序64位BigUInt型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigUInt64BE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigUInt64BE(value: bigint, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeBigUInt64LE

ArkTS-Dyn:
```TypeScript
writeBigUInt64LE(value: bigint, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeBigUInt64LE(value: bigint, offset?: int): int
```

在Buffer对象的offset偏移处写入无符号的小端序64位BigUInt型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeBigUInt64LE(value: bigint, offset?: int): int--><!--Device-Buffer-writeBigUInt64LE(value: bigint, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleBE

ArkTS-Dyn:
```TypeScript
writeDoubleBE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeDoubleBE(value: double, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的64位双浮点型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeDoubleBE(value: double, offset?: int): int--><!--Device-Buffer-writeDoubleBE(value: double, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeDoubleLE

ArkTS-Dyn:
```TypeScript
writeDoubleLE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeDoubleLE(value: double, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的64位双浮点型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeDoubleLE(value: double, offset?: int): int--><!--Device-Buffer-writeDoubleLE(value: double, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 8。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8 . Received value is: [offset] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// Output: result = 8
```

## writeFloatBE

ArkTS-Dyn:
```TypeScript
writeFloatBE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeFloatBE(value: double, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的32位浮点型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeFloatBE(value: double, offset?: int): int--><!--Device-Buffer-writeFloatBE(value: double, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatBE(0xcafebabe, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeFloatLE

ArkTS-Dyn:
```TypeScript
writeFloatLE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeFloatLE(value: double, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的32位浮点型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeFloatLE(value: double, offset?: int): int--><!--Device-Buffer-writeFloatLE(value: double, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4 . Received value is: [offset] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatLE(0xcafebabe, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt16BE

ArkTS-Dyn:
```TypeScript
writeInt16BE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeInt16BE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的16位有符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt16BE(value: long, offset?: int): int--><!--Device-Buffer-writeInt16BE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 2。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16BE(0x0102, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt16LE

ArkTS-Dyn:
```TypeScript
writeInt16LE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeInt16LE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的16位有符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt16LE(value: long, offset?: int): int--><!--Device-Buffer-writeInt16LE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 2。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16LE(0x0304, 0);
console.info("result = " + result);
// Output: result = 2
```

## writeInt32BE

ArkTS-Dyn:
```TypeScript
writeInt32BE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeInt32BE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的32位有符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt32BE(value: long, offset?: int): int--><!--Device-Buffer-writeInt32BE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32BE(0x01020304, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt32LE

ArkTS-Dyn:
```TypeScript
writeInt32LE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeInt32LE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的32位有符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt32LE(value: long, offset?: int): int--><!--Device-Buffer-writeInt32LE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32LE(0x05060708, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeInt8

ArkTS-Dyn:
```TypeScript
writeInt8(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeInt8(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入8位有符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeInt8(value: long, offset?: int): int--><!--Device-Buffer-writeInt8(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 1。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
writeIntBE(value: number, offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
writeIntBE(value: long, offset: int, byteLength: int): int
```

在Buffer对象的offset偏移处写入大端序的有符号数据，字节长度为byteLength。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeIntBE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeIntBE(value: long, offset: int, byteLength: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - byteLength。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要写入的字节数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeIntLE

ArkTS-Dyn:
```TypeScript
writeIntLE(value: number, offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
writeIntLE(value: long, offset: int, byteLength: int): int
```

在Buffer对象的offset偏移处写入小端序的有符号数据，字节长度为byteLength。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeIntLE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeIntLE(value: long, offset: int, byteLength: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - byteLength。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要写入的字节数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUInt16BE

ArkTS-Dyn:
```TypeScript
writeUInt16BE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeUInt16BE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的16位无符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt16BE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt16BE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值为0。取值范围：0 <= offset <= Buffer.length - 2。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
writeUInt16LE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeUInt16LE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的16位无符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt16LE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt16LE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 2。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
writeUInt32BE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeUInt32BE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入大端序的32位无符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt32BE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt32BE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32BE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt32LE

ArkTS-Dyn:
```TypeScript
writeUInt32LE(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeUInt32LE(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入小端序的32位无符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt32LE(value: long, offset?: int): int--><!--Device-Buffer-writeUInt32LE(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer对象的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 4。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32LE(0xfeedface, 0);
console.info("result = " + result);
// Output: result = 4
```

## writeUInt8

ArkTS-Dyn:
```TypeScript
writeUInt8(value: number, offset?: number): number
```

ArkTS-Sta:
```TypeScript
writeUInt8(value: long, offset?: int): int
```

在Buffer对象的offset偏移处写入8位无符号整型数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUInt8(value: long, offset?: int): int--><!--Device-Buffer-writeUInt8(value: long, offset?: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - 1。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

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

ArkTS-Dyn:
```TypeScript
writeUIntBE(value: number, offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
writeUIntBE(value: long, offset: int, byteLength: int): int
```

在Buffer对象的offset偏移处写入大端序的无符号数据，字节长度为byteLength。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUIntBE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeUIntBE(value: long, offset: int, byteLength: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - byteLength。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要写入的字节数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## writeUIntLE

ArkTS-Dyn:
```TypeScript
writeUIntLE(value: number, offset: number, byteLength: number): number
```

ArkTS-Sta:
```TypeScript
writeUIntLE(value: long, offset: int, byteLength: int): int
```

在Buffer对象的offset偏移处写入小端序的无符号数据，字节长度为byteLength。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-writeUIntLE(value: long, offset: int, byteLength: int): int--><!--Device-Buffer-writeUIntLE(value: long, offset: int, byteLength: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 写入Buffer的数据。 |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 偏移量。默认值：0。取值范围：0 <= offset <= Buffer.length - byteLength。 |
| byteLength | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要写入的字节数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 偏移量offset加上写入的字节数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200001 | The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param] |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// Output: result = 6
```

## [index: int]

```TypeScript
[index: int]: long
```

返回指定索引处的元素。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Buffer-[index: int]: long--><!--Device-Buffer-[index: int]: long-End-->

**System capability:** SystemCapability.Utils.Lang

## buffer

```TypeScript
buffer: ArrayBuffer
```

ArrayBuffer对象。

**Type:** ArrayBuffer

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-buffer: ArrayBuffer--><!--Device-Buffer-buffer: ArrayBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
byteOffset: number
```

当前Buffer所在内存池的偏移量。&lt;br&gt;- 当Buffer通过内存池创建时（如使用[allocUninitializedFromPool](arkts-arkts-buffer-allocuninitializedfrompool-f.md#allocuninitializedfrompool)创建Buffer，或使用buffer.from()传入字符串，且字符串长度加当前内存池偏移量小于4kb），返回相对于内存池的偏移量。&lt;br&gt;- 当Buffer直接分配内存时（如使用  
[alloc](arkts-arkts-buffer-alloc-f.md#alloc)），返回值为0。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-byteOffset: number--><!--Device-Buffer-byteOffset: number-End-->

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Buffer对象的字节长度。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Buffer-length: number--><!--Device-Buffer-length: number-End-->

**System capability:** SystemCapability.Utils.Lang

