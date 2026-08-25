# from

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## from

```TypeScript
function from(array: number[]): Buffer
```

根据指定数组创建新的Buffer对象，数组中的每个元素作为对应位置的字节存储。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Buffer |


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer
```

创建与`arrayBuffer`共享内存的指定长度的Buffer对象。共享内存意味着Buffer与arrayBuffer引用同一块内存区域，对Buffer数据的修改将同步反映到arrayBuffer中，反之亦然（注意：此方式避免内存拷贝，提升性能，但需注意内存释放时机）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [arrayBuffer](arkts-arkts-buffer-blob-c.md) | ArrayBuffer \| SharedArrayBuffer | 是 |
| byteOffset | number | 否 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |


## from

```TypeScript
function from(buffer: Buffer | Uint8Array): Buffer
```

当入参为Buffer对象时，创建新的Buffer对象并复制入参Buffer对象的数据，然后返回新对象。 基于Uint8Array对象的内存创建新的Buffer对象并返回，新Buffer与原Uint8Array共享同一底层ArrayBuffer内存区域。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [buffer](arkts-buffer.md) | Buffer \| Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Buffer |


## from

```TypeScript
function from(object: Object, offsetOrEncoding: number | string, length: number): Buffer
```

根据指定的`object`类型数据，创建新的Buffer对象。当object的valueOf()返回ArrayBuffer时，按字节偏移量和长度创建Buffer；其他类型则根据编码格式将对象值转换为Buffer。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | Object | 是 |
| offsetOrEncoding | number \| string | 是 |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Buffer |


## from

```TypeScript
function from(string: String, encoding?: BufferEncoding): Buffer
```

根据指定编码格式的字符串，创建新的Buffer对象，字符串按编码格式转换为字节序列存入Buffer。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| string | String | 是 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| Buffer |
