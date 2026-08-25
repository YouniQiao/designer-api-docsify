# from

## 导入模块

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## from

```TypeScript
function from(array: number[]): FastBuffer
```

根据指定数组创建新的FastBuffer对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |


## from

```TypeScript
function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer
```

创建与`arrayBuffer`共享内存的指定长度的FastBuffer对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |
| [10200068](../errorcode-utils.md#10200068-引用已释放或分离的arraybuffer) |


## from

```TypeScript
function from(buffer: FastBuffer | Uint8Array): FastBuffer
```

当入参为FastBuffer对象时，创建新的FastBuffer对象并复制入参数据。新旧对象数据独立，互不影响。当入参为Uint8Array对象时，基于其内存创建新的FastBuffer对象。两个对象保持内存关联，修改任一对象的数据会同步影响另一对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-引用已释放或分离的arraybuffer) |


## from

```TypeScript
function from(value: string, encoding?: BufferEncoding): FastBuffer
```

根据指定编码格式的字符串，创建新的FastBuffer对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |
| encoding | BufferEncoding | 否 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |
