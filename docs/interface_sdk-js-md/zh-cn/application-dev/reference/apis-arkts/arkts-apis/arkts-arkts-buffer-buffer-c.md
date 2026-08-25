# Buffer

Buffer对象是处理二进制数据的缓冲区。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

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

比较当前Buffer对象与目标Buffer或Uint8Array对象，并返回在排序中的结果。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | Buffer \| Uint8Array | 是 |
| targetStart | number | 否 |
| targetEnd | number | 否 |
| sourceStart | number | 否 |
| sourceEnd | number | 否 |

**返回值：**

| 类型 |
| --- |
| -1 \| 0 \| 1 |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// 输出结果：1
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// 输出结果：1
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// 输出结果：0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// 输出结果：-1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// 输出结果：1
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// 输出结果：0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// 输出结果：-1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// 输出结果：1
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

比较当前Buffer对象与目标Buffer或Uint8Array对象，并返回在排序中的结果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | Buffer \| Uint8Array | 是 |
| targetStart | int | 否 |
| targetEnd | int | 否 |
| sourceStart | int | 否 |
| sourceEnd | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

参见 [compare](#compare)

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | Buffer \| Uint8Array | 是 |
| targetStart | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| sourceStart | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| sourceEnd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);
let buf2 = buffer.allocUninitializedFromPool(26).fill('!');

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}

buf1.copy(buf2, 8, 16, 20);
console.info(buf2.toString('ascii', 0, 25));
// 输出结果：!!!!!!!!qrst!!!!!!!!!!!!!
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

返回一个包含字节索引（key）和字节值（value）的迭代器。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, number]&gt; |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, number]&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[int, long]&gt; |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('buffer');
let pair = buf.entries();
let next: IteratorResult<Object[]> = pair.next();
while (!next.done) {
  console.info("buffer: " + next.value);
  /*
  输出结果：buffer: 0,98
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| otherBuffer | Uint8Array \| Buffer | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('ABC');
let buf2 = buffer.from('414243', 'hex');
let buf3 = buffer.from('ABCD');

console.info(buf1.equals(buf2).toString());
// 输出结果：true
console.info(buf1.equals(buf3).toString());
// 输出结果：false
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

使用value填充当前对象指定位置的数据，当value的长度小于需要填充的范围时会重复value进行填充，并返回填充后的Buffer对象。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: string \| Buffer \| Uint8Array \| number \| number \| number<br>ArkTS-Sta：string \ | Buffer \| Uint8Array \| int \| double \| long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let b = buffer.allocUninitializedFromPool(50).fill('h');
console.info(b.toString());
// 输出结果：hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array<br>ArkTS-Sta：string \ | int \| double \| long \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('this is a buffer');
console.info(buf.includes('this').toString());
// 输出结果：true
console.info(buf.includes('be').toString());
// 输出结果：false
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array<br>ArkTS-Sta：string \ | int \| double \| long \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('this is a buffer');
console.info(buf.indexOf('this').toString());
// 输出结果：0
console.info(buf.indexOf('is').toString());
// 输出结果：2
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;int&gt; |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('buffer');
let keys = buf.keys();
for (const key of keys) {
  console.info(key.toString());
}
/*
输出结果：0
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: string \| number \| number \| number \| Buffer \| Uint8Array<br>ArkTS-Sta：string \ | int \| double \| long \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from('this buffer is a buffer');
console.info(buf.lastIndexOf('this').toString());
// 输出结果：0
console.info(buf.lastIndexOf('buffer').toString());
// 输出结果：17
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigInt64BE(0).toString());
// 输出结果：7161960797921896816

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// 输出结果：8100120198111388771

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64BE(0).toString());
// 输出结果：7161960797921896816
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x70,
  0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78]);
console.info(buf.readBigUInt64LE(0).toString());
// 输出结果：8100120198111388771

let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleBE(0).toString());
// 输出结果：8.20788039913184e-304
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readDoubleLE(0).toString());
// 输出结果：5.447603722011605e-270
let buf1 = buffer.allocUninitializedFromPool(8);
let result = buf1.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatBE(0).toString());
// 输出结果：2.387939260590663e-38
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeFloatBE(0xcabcbcbc, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);
console.info(buf.readFloatLE(0).toString());
// 输出结果：1.539989614439558e-36
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeFloatLE(0xcabcbcbc, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 5]);
console.info(buf.readInt16BE(0).toString());
// 输出结果：5
let buf1 = buffer.alloc(2);
let result = buf1.writeInt16BE(0x1234, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 5]);
console.info(buf.readInt16LE(0).toString());
// 输出结果：1280
let buf1 = buffer.alloc(2);
let result = buf1.writeInt16BE(0x1234, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 0, 0, 5]);
console.info(buf.readInt32BE(0).toString());
// 输出结果：5
let buf1 = buffer.alloc(4);
let result = buf1.writeInt32BE(0x12345678, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0, 0, 0, 5]);
console.info(buf.readInt32LE(0).toString());
// 输出结果：83886080
let buf1 = buffer.alloc(4);
let result = buf1.writeInt32BE(0x12345678, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([-1, 5]);
console.info(buf.readInt8(0).toString());
// 输出结果：0
console.info(buf.readInt8(1).toString());
// 输出结果：5
let buf1 = buffer.allocUninitializedFromPool(2);
let result = buf1.writeInt8(0x12);
console.info("result = " + result);
// 输出结果：result = 1
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from("ab");
let num = buf.readIntBE(0, 1);
console.info(num.toString());
// 输出结果：97
let buf1 = buffer.allocUninitializedFromPool(6);
let result = buf1.writeIntBE(0x123456789011, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readIntLE(0, 6).toString(16));
// 输出结果：-546f87a9cbee
let buf1 = buffer.allocUninitializedFromPool(6);
let result = buf1.writeIntLE(0x123456789011, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16BE(0).toString(16));
// 输出结果：1234
console.info(buf.readUInt16BE(1).toString(16));
// 输出结果：3456
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt16BE(0x1234, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

从指定的`offset`处读取无符号的小端序16位整数。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56]);
console.info(buf.readUInt16LE(0).toString(16));
// 输出结果：3412
console.info(buf.readUInt16LE(1).toString(16));
// 输出结果：5634
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt16LE(0x1234, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32BE(0).toString(16));
// 输出结果：12345678
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt32BE(0x12345678, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78]);
console.info(buf.readUInt32LE(0).toString(16));
// 输出结果：78563412
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt32LE(0x12345678, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

从指定的`offset`处读取8位无符号整型数。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([1, -2]);
console.info(buf.readUInt8(0).toString());
// 输出结果：1
console.info(buf.readUInt8(1).toString());
// 输出结果：0
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUInt8(0x42);
console.info("result = " + result);
// 输出结果：result = 1
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntBE(0, 6).toString(16));
// 输出结果：1234567890ab
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUIntBE(0x13141516, 0, 4);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);
console.info(buf.readUIntLE(0, 6).toString(16));
// 输出结果：ab9078563412
let buf1 = buffer.allocUninitializedFromPool(4);
let result = buf1.writeUIntLE(0x13141516, 0, 4);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);

for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
const buf2 = buf1.subarray(0, 3);
console.info(buf2.toString('ascii', 0, buf2.length));
// 输出结果: abc
```

## swap16

```TypeScript
swap16(): Buffer
```

将当前对象转换为无符号的16位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换16位数据的场景。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer的长度错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap16();
console.info(buf1.toString('hex'));
// 输出结果：0201040306050807
```

## swap32

```TypeScript
swap32(): Buffer
```

将当前对象转换为无符号的32位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换32位数据的场景。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer的长度错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap32();
console.info(buf1.toString('hex'));
// 输出结果：0403020108070605
```

## swap64

```TypeScript
swap64(): Buffer
```

将当前对象转换为无符号的64位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换64位数据的场景。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200009](../errorcode-utils.md#10200009-buffer的长度错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);
console.info(buf1.toString('hex'));
// 输出结果：0102030405060708
buf1.swap64();
console.info(buf1.toString('hex'));
// 输出结果：0807060504030201
```

## toJSON

```TypeScript
toJSON(): Object
```

将Buffer转为JSON对象并返回，该对象包含type属性（值为'Buffer'）和data属性（值为按字节顺序排列的数组）。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Object |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
let obj = buf1.toJSON();
console.info(JSON.stringify(obj));
// 输出结果: {"type":"Buffer","data":[1,2,3,4,5]}
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
let obj = buf1.toJSON();
console.info(JSON.stringify(obj));
// 输出结果: {"type":"Buffer","data":[1,2,3,4,5]}
```

## toJSON

```TypeScript
toJSON(): jsonx.JsonElement
```

将此Buffer实例转换为JsonElement。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| jsonx.JsonElement |

**示例**

参见 [toJSON](#tojson)

## toString

```TypeScript
toString(encoding?: string, start?: number, end?: number): string
```

将当前对象中指定位置的数据转成指定编码格式的字符串并返回。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 否 |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);
for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
console.info(buf1.toString('utf-8'));
// 输出结果: abcdefghijklmnopqrstuvwxyz
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.allocUninitializedFromPool(26);
for (let i = 0; i < 26; i++) {
  buf1.writeInt8(i + 97, i);
}
console.info(buf1.toString('utf-8'));
// 输出结果: abcdefghijklmnopqrstuvwxyz
```

## toString

```TypeScript
toString(): string
```

按照encoding指定的字符编码将buf解码为字符串。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

**示例**

参见 [toString](#tostring)

## toString

```TypeScript
toString(encoding?: BufferEncoding, start?: int, end?: int): string
```

按照encoding指定的字符编码将buf解码为字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | BufferEncoding | 否 |
| start | int | 否 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

参见 [toString](#tostring)

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt;  <br>ArkTS-Sta：[IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;long&gt; |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('buffer');
let pair = buf1.values();
let next:IteratorResult<number> = pair.next();
while (!next.done) {
  console.info(next.value.toString());
  /*
  输出结果：98
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| [length](#length) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.alloc(256);
let len = buf.write('\u00bd + \u00bc = \u00be', 0);
console.info(`${len} bytes: ${buf.toString('utf-8', 0, len)}`);
// 输出结果: 12 bytes: ½ + ¼ = ¾

let buffer1 = buffer.alloc(10);
let length = buffer1.write('abcd', 8);
console.info("length = " + length);
// 输出结果：length = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64BE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigInt64LE(BigInt(0x0102030405060708), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64BE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeBigUInt64LE(BigInt(0xdecafafecacefade), 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleBE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeDoubleLE(123.456, 0);
console.info("result = " + result);
// 输出结果：result = 8
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatBE(0xcafebabe, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(8);
let result = buf.writeFloatLE(0xcafebabe, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16BE(0x0102, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt16LE(0x0304, 0);
console.info("result = " + result);
// 输出结果：result = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32BE(0x01020304, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeInt32LE(0x05060708, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(2);
let result = buf.writeInt8(2, 0);
console.info("result = " + result);
// 输出结果：result = 1
let result1 = buf.writeInt8(-2, 1);
console.info("result1 = " + result1);
// 输出结果：result1 = 2
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16BE(0xdead, 0);
console.info("result = " + result);
// 输出结果：result = 2
let result1 = buf.writeUInt16BE(0xbeef, 2);
console.info("result1 = " + result1);
// 输出结果：result1 = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt16LE(0xdead, 0);
console.info("result = " + result);
// 输出结果：result = 2
let result1 = buf.writeUInt16LE(0xbeef, 2);
console.info("result1 = " + result1);
// 输出结果：result1 = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32BE(0xfeedface, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt32LE(0xfeedface, 0);
console.info("result = " + result);
// 输出结果：result = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(4);
let result = buf.writeUInt8(0x3, 0);
console.info("result = " + result);
// 输出结果：result = 1
let result1 = buf.writeUInt8(0x4, 1);
console.info("result1 = " + result1);
// 输出结果：result1 = 2
let result2 = buf.writeUInt8(0x23, 2);
console.info("result2 = " + result2);
// 输出结果：result2 = 3
let result3 = buf.writeUInt8(0x42, 3);
console.info("result3 = " + result3);
// 输出结果：result3 = 4
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntBE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| byteLength | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(6);
let result = buf.writeUIntLE(0x1234567890ab, 0, 6);
console.info("result = " + result);
// 输出结果：result = 6
```

## [index: int]

```TypeScript
[index: int]: long
```

返回指定索引处的元素。

**类型：** long

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
buffer: ArrayBuffer
```

ArrayBuffer对象。

**类型：** ArrayBuffer

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
byteOffset: number
```

当前Buffer所在内存池的偏移量。<br>- 当Buffer通过内存池创建时（如使用[allocUninitializedFromPool](arkts-arkts-buffer-allocuninitializedfrompool-f.md)创 建Buffer，或使用buffer.from()传入字符串，且字符串长度加当前内存池偏移量小于4kb），返回相对于内存池的偏移量。<br>- 当Buffer直接分配内存时（如使用 [alloc](arkts-arkts-buffer-alloc-f.md)），返回值为0。

**类型：** number

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Buffer对象的字节长度。

**类型：** number

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
