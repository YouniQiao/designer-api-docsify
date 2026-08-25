# Buffer

Buffer对象是处理二进制数据的缓冲区。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

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

比较当前Buffer对象与目标Buffer或Uint8Array对象，并返回在排序中的结果。

**起始版本：** 9

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

## copy

```TypeScript
copy(target: Buffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number
```

将`this`实例中指定位置的数据复制到`target`的指定位置上，并返回复制的字节总长度。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | Buffer \| Uint8Array | 是 |
| targetStart | number | 否 |
| sourceStart | number | 否 |
| sourceEnd | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## entries

```TypeScript
entries(): IterableIterator<[number, number]>
```

返回一个包含字节索引（key）和字节值（value）的迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;[number, number] & gt; |
| IterableIterator & lt;[number, number] & gt; |

## equals

```TypeScript
equals(otherBuffer: Uint8Array | Buffer): boolean
```

比较`this`实例和otherBuffer实例是否相等。

**起始版本：** 9

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

## fill

```TypeScript
fill(
      value: string | Buffer | Uint8Array | number | number | number,
      offset?: number,
      end?: number,
      encoding?: BufferEncoding
    ): Buffer
```

使用value填充当前对象指定位置的数据，当value的长度小于需要填充的范围时会重复value进行填充，并返回填充后的Buffer对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| Buffer \| Uint8Array \| number \| number \| number | 是 |
| offset | number | 否 |
| end | number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## includes

```TypeScript
includes(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean
```

检查Buffer对象是否包含value值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| number \| number \| number \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## indexOf

```TypeScript
indexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

返回当前对象中首次出现value的索引，如果不包含value，则返回-1。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| number \| number \| number \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## keys

```TypeScript
keys(): IterableIterator<number>
```

返回包含key值的迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

## lastIndexOf

```TypeScript
lastIndexOf(value: string | number | number | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number
```

返回this实例中最后一次出现value的索引，如果对象不包含value，则返回-1。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| number \| number \| number \| Buffer \| Uint8Array | 是 |
| [byteOffset](#byteoffset) | number | 否 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## readBigInt64BE

```TypeScript
readBigInt64BE(offset?: number): bigint
```

从指定的`offset`处读取有符号的大端序64位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readBigInt64LE

```TypeScript
readBigInt64LE(offset?: number): bigint
```

从指定的`offset`处读取有符号的小端序64位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readBigUInt64BE

```TypeScript
readBigUInt64BE(offset?: number): bigint
```

从指定的`offset`处读取无符号的大端序64位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readBigUInt64LE

```TypeScript
readBigUInt64LE(offset?: number): bigint
```

从指定的`offset`处读取无符号的小端序64位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readDoubleBE

```TypeScript
readDoubleBE(offset?: number): number
```

从指定的`offset`处读取64位大端序双精度值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readDoubleLE

```TypeScript
readDoubleLE(offset?: number): number
```

从指定的`offset`处读取64位小端序双精度值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readFloatBE

```TypeScript
readFloatBE(offset?: number): number
```

从指定的`offset`处读取32位大端序浮点数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readFloatLE

```TypeScript
readFloatLE(offset?: number): number
```

从指定的`offset`处读取32位小端序浮点数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readInt16BE

```TypeScript
readInt16BE(offset?: number): number
```

从指定的`offset`处读取有符号的大端序16位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readInt16LE

```TypeScript
readInt16LE(offset?: number): number
```

从指定的`offset`处读取有符号的小端序16位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readInt32BE

```TypeScript
readInt32BE(offset?: number): number
```

从指定的`offset`处读取有符号的大端序32位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readInt32LE

```TypeScript
readInt32LE(offset?: number): number
```

从指定的`offset`处读取有符号的小端序32位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readInt8

```TypeScript
readInt8(offset?: number): number
```

从指定的`offset`处读取有符号的8位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readIntBE

```TypeScript
readIntBE(offset: number, byteLength: number): number
```

从指定的`offset`处读取byteLength个字节，并将结果解释为支持最高48位精度的大端序、二进制补码有符号值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readIntLE

```TypeScript
readIntLE(offset: number, byteLength: number): number
```

从指定的`offset`处读取`byteLength`个字节，并将结果解释为支持最高48位精度的小端序、二进制补码有符号值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUInt16BE

```TypeScript
readUInt16BE(offset?: number): number
```

从指定的`offset`处读取无符号的大端序16位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUInt16LE

```TypeScript
readUInt16LE(offset?: number): number
```

从指定的`offset`处读取无符号的小端序16位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUInt32BE

```TypeScript
readUInt32BE(offset?: number): number
```

从指定的`offset`处的buf读取无符号的大端序32位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUInt32LE

```TypeScript
readUInt32LE(offset?: number): number
```

从指定的`offset`处的buf读取无符号的小端序32位整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUInt8

```TypeScript
readUInt8(offset?: number): number
```

从指定的`offset`处读取8位无符号整型数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUIntBE

```TypeScript
readUIntBE(offset: number, byteLength: number): number
```

从指定的`offset`处的buf读取`byteLength`个字节，并将结果解释为支持最高48位精度的无符号大端序整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## readUIntLE

```TypeScript
readUIntLE(offset: number, byteLength: number): number
```

从指定的`offset`处的buf读取`byteLength`个字节，并将结果解释为支持最高48位精度的无符号小端序整数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## subarray

```TypeScript
subarray(start?: number, end?: number): Buffer
```

截取当前对象指定位置的数据并返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 否 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

## swap16

```TypeScript
swap16(): Buffer
```

将当前对象转换为无符号的16位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换16位数据的场景。

**起始版本：** 9

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

## swap32

```TypeScript
swap32(): Buffer
```

将当前对象转换为无符号的32位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换32位数据的场景。

**起始版本：** 9

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

## swap64

```TypeScript
swap64(): Buffer
```

将当前对象转换为无符号的64位整数数组，并交换字节顺序。适用于需要在大端序和小端序之间转换64位数据的场景。

**起始版本：** 9

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

## toJSON

```TypeScript
toJSON(): Object
```

将Buffer转为JSON对象并返回，该对象包含type属性（值为'Buffer'）和data属性（值为按字节顺序排列的数组）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Object |

## toString

```TypeScript
toString(encoding?: string, start?: number, end?: number): string
```

将当前对象中指定位置的数据转成指定编码格式的字符串并返回。

**起始版本：** 9

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

## values

```TypeScript
values(): IterableIterator<number>
```

返回一个包含value的迭代器。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;number & gt; |

## write

```TypeScript
write(str: string, offset?: number, length?: number, encoding?: string): number
```

在Buffer对象的offset偏移处写入指定编码的字符串，写入的字节长度为length。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| offset | number | 否 |
| [length](#length) | number | 否 |
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeBigInt64BE

```TypeScript
writeBigInt64BE(value: bigint, offset?: number): number
```

在Buffer对象的offset偏移处写入有符号的大端序64位BigInt型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeBigInt64LE

```TypeScript
writeBigInt64LE(value: bigint, offset?: number): number
```

在Buffer对象的offset偏移处写入有符号的小端序64位BigInt型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeBigUInt64BE

```TypeScript
writeBigUInt64BE(value: bigint, offset?: number): number
```

在Buffer对象的offset偏移处写入无符号的大端序64位BigUInt型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeBigUInt64LE

```TypeScript
writeBigUInt64LE(value: bigint, offset?: number): number
```

在Buffer对象的offset偏移处写入无符号的小端序64位BigUInt型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeDoubleBE

```TypeScript
writeDoubleBE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的64位双浮点型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeDoubleLE

```TypeScript
writeDoubleLE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的64位双浮点型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeFloatBE

```TypeScript
writeFloatBE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的32位浮点型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeFloatLE

```TypeScript
writeFloatLE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的32位浮点型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeInt16BE

```TypeScript
writeInt16BE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的16位有符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeInt16LE

```TypeScript
writeInt16LE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的16位有符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeInt32BE

```TypeScript
writeInt32BE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的32位有符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeInt32LE

```TypeScript
writeInt32LE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的32位有符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeInt8

```TypeScript
writeInt8(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入8位有符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeIntBE

```TypeScript
writeIntBE(value: number, offset: number, byteLength: number): number
```

在Buffer对象的offset偏移处写入大端序的有符号数据，字节长度为byteLength。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeIntLE

```TypeScript
writeIntLE(value: number, offset: number, byteLength: number): number
```

在Buffer对象的offset偏移处写入小端序的有符号数据，字节长度为byteLength。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUInt16BE

```TypeScript
writeUInt16BE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的16位无符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUInt16LE

```TypeScript
writeUInt16LE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的16位无符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUInt32BE

```TypeScript
writeUInt32BE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入大端序的32位无符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUInt32LE

```TypeScript
writeUInt32LE(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入小端序的32位无符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUInt8

```TypeScript
writeUInt8(value: number, offset?: number): number
```

在Buffer对象的offset偏移处写入8位无符号整型数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUIntBE

```TypeScript
writeUIntBE(value: number, offset: number, byteLength: number): number
```

在Buffer对象的offset偏移处写入大端序的无符号数据，字节长度为byteLength。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## writeUIntLE

```TypeScript
writeUIntLE(value: number, offset: number, byteLength: number): number
```

在Buffer对象的offset偏移处写入小端序的无符号数据，字节长度为byteLength。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| offset | number | 是 |
| byteLength | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

## buffer

```TypeScript
buffer: ArrayBuffer
```

ArrayBuffer对象。

**类型：** ArrayBuffer

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
byteOffset: number
```

当前Buffer所在内存池的偏移量。  
- 当Buffer通过内存池创建时（如使用[allocUninitializedFromPool](arkts-arkts-buffer-allocuninitializedfrompool-f.md)创 建Buffer，或使用buffer.from()传入字符串，且字符串长度加当前内存池偏移量小于4kb），返回相对于内存池的偏移量。  
- 当Buffer直接分配内存时（如使用 [alloc](arkts-arkts-buffer-alloc-f.md)），返回值为0。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Buffer对象的字节长度。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
