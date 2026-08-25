# MessageSequence

在RPC或IPC过程中，发送方可以使用MessageSequence提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageSequence提供的读方法从该对象中读取特定格式的数据。 数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。读取顺序必须与写入顺序一致，否则会导致数据解析错误。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## closeFileDescriptor

```TypeScript
static closeFileDescriptor(fd: number): void
```

静态方法，关闭给定的文件描述符。  
- 文件使用完毕后及时关闭，避免资源泄漏。  
- 关闭前确保文件操作已完成。  
- 不要关闭已关闭的文件描述符。  
- 关闭后不能再读写文件。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## containFileDescriptors

```TypeScript
containFileDescriptors(): boolean
```

检查此MessageSequence对象是否包含文件描述符。适用于文件传输场景中判断是否需要处理文件描述符，或在接收数据前检查数据类型以决定处理方式的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## create

```TypeScript
static create(): MessageSequence
```

静态方法，创建MessageSequence对象。调用此方法后，系统会在内存中分配一块连续的缓冲区空间，用于存储待传输的序列化数据。该对象在IPC/RPC通信中用于封装请求和响应数据。  
- 创建的MessageSequence对象必须在使用完毕后调用reclaim()释放资源，否则会导致内存泄漏。  
- MessageSequence对象不能跨线程使用。  
- 建议在需要IPC/RPC通信时按需创建，避免频繁创建和释放。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) |

## dupFileDescriptor

```TypeScript
static dupFileDescriptor(fd: number): number
```

静态方法，复制给定的文件描述符。  
- IPC传输前复制，避免原描述符被关闭。  
- 多进程共享同一文件。  
- 需要独立管理文件偏移量。  
- 复制后两个描述符需要分别关闭。  
- 不要复制无效的文件描述符。  
- 复制后独立管理生命周期。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900013](../errorcode-rpc.md#1900013-系统调用dup失败) |

## getCapacity

```TypeScript
getCapacity(): number
```

获取当前MessageSequence对象的容量大小。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getRawDataCapacity

```TypeScript
getRawDataCapacity(): number
```

获取MessageSequence可以容纳的最大原始数据量。适用于大数据传输前检查容量是否满足需求，或在处理大批量数据时预先判断数据大小的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getReadableBytes

```TypeScript
getReadableBytes(): number
```

获取MessageSequence的可读字节空间。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getReadPosition

```TypeScript
getReadPosition(): number
```

获取MessageSequence的读位置。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

获取当前创建的MessageSequence对象的数据大小。  
- 查看已写入数据的总大小。  
- 判断缓冲区使用情况。  
- 在数据传输前检查数据大小。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getWritableBytes

```TypeScript
getWritableBytes(): number
```

获取MessageSequence的可写字节空间大小。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getWritePosition

```TypeScript
getWritePosition(): number
```

获取MessageSequence的写位置。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readArrayBuffer

```TypeScript
readArrayBuffer(typeCode: TypeCode): ArrayBuffer
```

从MessageSequence读取ArrayBuffer类型数据。  
- 必须与[writeArrayBuffer](#writearraybuffer)配对使用。  
- 读取typeCode必须与写入typeCode一致，顺序必须匹配。  
- typeCode必须正确匹配，不匹配会导致数据异常或错误，建议根据业务类型选择合适的[TypeCode](arkts-ipc-rpc-typecode-e.md)。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [typeCode](../../apis-notification-kit/arkts-apis/arkts-notification-notificationcontent-notificationsystemliveviewcontent-i.md) | [TypeCode](arkts-ipc-rpc-typecode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readAshmem

```TypeScript
readAshmem(): Ashmem
```

从MessageSequence读取匿名共享对象。使用前需先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)方法进行内存映射。  
- readAshmem()获取对象。  
- [mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)映射内存。  
- [readDataFromAshmem](arkts-ipc-rpc-ashmem-c.md#readdatafromashmem)读取数据。  
- unmapAshmem()取消映射。  
- closeAshmem()关闭对象。  
- 必须先映射才能读取数据。  
- 数据读取后需要取消映射。  
- 及时关闭避免内存泄漏。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readBoolean

```TypeScript
readBoolean(): boolean
```

从MessageSequence实例中读取布尔值。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readBooleanArray

```TypeScript
readBooleanArray(dataIn: boolean[]): void
```

从MessageSequence实例中读取布尔数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | boolean[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readBooleanArray

```TypeScript
readBooleanArray(): boolean[]
```

从MessageSequence实例中读取布尔数组。  
- 返回新创建的数组，无需预先创建。  
- 数组元素为布尔值。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readByte

```TypeScript
readByte(): number
```

从MessageSequence实例中读取字节值。  
- 必须与[writeByte](#writebyte)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readByteArray

```TypeScript
readByteArray(dataIn: number[]): void
```

从MessageSequence实例中读取字节数组，并将其写入到创建的空数组中。读取后dataIn数组会被填充读取的字节数据，读指针向后移动相应字节数。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readByteArray

```TypeScript
readByteArray(): number[]
```

从MessageSequence实例中读取字节数组。读取后返回字节数组数据，读指针向后移动相应字节数。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readChar

```TypeScript
readChar(): number
```

从MessageSequence实例中读取单个字符值。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readCharArray

```TypeScript
readCharArray(dataIn: number[]): void
```

从MessageSequence实例中读取单个字符数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readCharArray

```TypeScript
readCharArray(): number[]
```

从MessageSequence实例中读取单个字符数组。  
- 返回新创建的数组，无需预先创建。  
- 数组元素为字符编码，取值范围[0, 65535]。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readDouble

```TypeScript
readDouble(): number
```

从MessageSequence实例中读取双精度浮点值。  
- 返回新创建的数组，无需预先创建。  
- 数组元素为双精度浮点数。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readDoubleArray

```TypeScript
readDoubleArray(dataIn: number[]): void
```

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readDoubleArray

```TypeScript
readDoubleArray(): number[]
```

从MessageSequence实例中读取双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readException

```TypeScript
readException(): void
```

从MessageSequence中读取异常。适用于接收远端服务响应后检查异常状态的场景。  
- 在IPC/RPC通信的客户端使用。  
- 在调用sendMessageRequest收到响应后调用。  
- 在每次IPC/RPC调用后优先调用此方法。  
- 如有异常立即处理并终止后续数据读取，异常处理后建议调用reclaim()释放MessageSequence对象。  
- 此方法与[writeNoException](#writenoexception)方法配对使用。  
- 调用顺序：服务端处理请求 → [writeNoException](#writenoexception) → 客户端收到响应 →  
[readException](#readexception) - 如果服务端未调用 [writeNoException](#writenoexception)，调用此方法会失败。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readFileDescriptor

```TypeScript
readFileDescriptor(): number
```

从MessageSequence中读取文件描述符。接收端读取到的是映射后的新文件描述符编号，与发送端写入的描述符编号不同，但指向同一个文件资源。读取后建议及时使用并关闭，防止资源泄漏。 如需长期使用，可调用dupFileDescriptor复制描述符。  
- 必须与[writeFileDescriptor](#writefiledescriptor)配对使用。  
- 不要依赖源端的fd编号。  
- 读取后需要管理生命周期。  
- 建议及时使用避免资源浪费。  
- 使用完毕后及时关闭。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readFloat

```TypeScript
readFloat(): number
```

从MessageSequence实例中读取浮点值。由于系统内部对float类型的数据是按照double处理的，读取的数据按double精度返回。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readFloatArray

```TypeScript
readFloatArray(dataIn: number[]): void
```

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readFloatArray

```TypeScript
readFloatArray(): number[]
```

从MessageSequence实例中读取双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readInt

```TypeScript
readInt(): number
```

从MessageSequence实例中读取整数值。  
- 整数值占用4字节存储空间。  
- 存储范围：[-2^31, 2^31-1]。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readIntArray

```TypeScript
readIntArray(dataIn: number[]): void
```

从MessageSequence实例中读取整数数组，并将其写入到创建的空数组中。  
- 需预先创建空数组且长度应与写入时的数组长度一致。  
- 数组元素取值范围:[-2^31, 2^31-1]。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readIntArray

```TypeScript
readIntArray(): number[]
```

从MessageSequence实例中读取整数数组。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readInterfaceToken

```TypeScript
readInterfaceToken(): string
```

从MessageSequence对象中读取接口描述符，接口描述符按写入MessageSequence的顺序读取，本地对象可使用该信息检验本次通信。  
- 必须与[writeInterfaceToken](#writeinterfacetoken)配对使用。  
- 读取前应确保缓冲区中有可读数据。  
- 建议在收到IPC请求后立即读取校验。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readLong

```TypeScript
readLong(): number
```

从MessageSequence实例中读取长整数值。  
- 取值范围：[-2^63, 2^63-1]。  
- 长整数占用8字节存储空间。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readLongArray

```TypeScript
readLongArray(dataIn: number[]): void
```

从MessageSequence实例中读取长整数数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readLongArray

```TypeScript
readLongArray(): number[]
```

从MessageSequence实例中读取长整数数组。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readParcelable

```TypeScript
readParcelable(dataIn: Parcelable): void
```

从MessageSequence实例中读取成员变量到指定的对象（dataIn）。  
- dataIn参数必须为已实例化的Parcelable对象。  
- unmarshalling方法必须按与marshalling相同的顺序读取。  
- 反序列化顺序必须与序列化顺序一致。  
- 建议在unmarshalling中处理异常情况。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | [Parcelable](arkts-ipc-rpc-parcelable-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |
| [1900012](../errorcode-rpc.md#1900012-js回调方法执行失败) |

## readParcelableArray

```TypeScript
readParcelableArray(parcelableArray: Parcelable[]): void
```

从MessageSequence实例中读取可序列化对象数组。适用于接收批量传输的多个自定义数据结构对象的场景，如读取多条业务记录、批量配置信息、多个实体对象等。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parcelableArray | [Parcelable](arkts-ipc-rpc-parcelable-i.md)[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |
| [1900012](../errorcode-rpc.md#1900012-js回调方法执行失败) |

## readRawData

```TypeScript
readRawData(size: number): number[]
```

从MessageSequence读取原始数据。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [readRawDataBuffer](#readrawdatabuffer)(size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readRawDataBuffer

```TypeScript
readRawDataBuffer(size: number): ArrayBuffer
```

从MessageSequence读取原始数据。  
- 需与写入时的数据大小匹配。  
- 该接口是一次性接口,不允许在一次parcel通信中多次调用。  
- 大数据量传输时注意系统资源占用。  
- 必须与[writeRawDataBuffer](#writerawdatabuffer)配对使用。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readRemoteObject

```TypeScript
readRemoteObject(): IRemoteObject
```

从MessageSequence读取远程对象。此方法用于反序列化MessageSequence对象以生成IRemoteObject。远程对象按写入MessageSequence的顺序读取。调用此方法后，会从 MessageSequence缓冲区中读取已序列化的远程对象数据，并反序列化为IRemoteObject实例。读取操作会更新内部读指针位置。  
- 读取前应确保缓冲区中有可读数据。  
- 如果写入的是RemoteObject，读取得到的是RemoteProxy。  
- 读取失败时会抛出异常，建议使用try-catch捕获。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(objects: IRemoteObject[]): void
```

从MessageSequence读取IRemoteObject对象数组，并将其写入到创建的空数组中。适用于接收批量传递的多个远程对象的场景，如批量获取服务代理、接收多个回调接口、多服务端点管理等。  
- 需预先创建空数组且长度应与写入时的数组长度一致。  
- 读取失败时会抛出异常，建议使用try-catch捕获。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| objects | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(): IRemoteObject[]
```

从MessageSequence读取IRemoteObject对象数组。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readShort

```TypeScript
readShort(): number
```

从MessageSequence实例中读取短整数值。  
- 必须与[writeShort](#writeshort)配对使用。  
- 注意写入时的取值范围[-2^15, 2^15-1]，超出此范围会导致数据截断。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readShortArray

```TypeScript
readShortArray(dataIn: number[]): void
```

从MessageSequence实例中读取短整数数组，并将其写入到创建的空数组中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readShortArray

```TypeScript
readShortArray(): number[]
```

从MessageSequence实例中读取短整数数组。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readString

```TypeScript
readString(): string
```

从MessageSequence实例中读取字符串值。  
- 先读取长度，再读取内容。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readStringArray

```TypeScript
readStringArray(dataIn: string[]): void
```

从MessageSequence实例中读取字符串数组，并将其写入到创建的空数组中。  
- 需预先创建空数组且长度应与写入时的数组长度一致。  
- 读取后dataIn数组会被填充读取的字节数据。  
- 读指针向后移动相应字节数。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | string[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## readStringArray

```TypeScript
readStringArray(): string[]
```

从MessageSequence实例中读取字符串数组。  
- 返回新创建的数组，无需预先创建。  
- 数组单个元素的长度范围0-40959字节。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string[] |

**错误码：**

| 错误码ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## reclaim

```TypeScript
reclaim(): void
```

释放不再使用的MessageSequence对象。  
- 必须与create()方法配对使用，调用create()创建MessageSequence对象后，必须在使用完毕后调用reclaim()释放资源。未及时调用reclaim()会导致内存资源泄漏。  
- 调用后对象不能再被使用。  
- 建议在finally块或任务结束时调用，确保资源释放。  
- 不要在异步操作中跨线程释放。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

## rewindRead

```TypeScript
rewindRead(pos: number): void
```

重新偏移读取位置到指定的位置。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900010](../errorcode-rpc.md#1900010-读取messagesequence数据失败) |

## rewindWrite

```TypeScript
rewindWrite(pos: number): void
```

重新偏移写位置到指定的位置。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## setCapacity

```TypeScript
setCapacity(size: number): void
```

设置MessageSequence对象的存储容量。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |
| [1900011](../errorcode-rpc.md#1900011-内存分配失败) |

## setSize

```TypeScript
setSize(size: number): void
```

设置MessageSequence对象中包含的数据大小。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeArrayBuffer

```TypeScript
writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void
```

将ArrayBuffer类型数据写入MessageSequence对象。  
- 此方法与[readArrayBuffer](#readarraybuffer)方法配对使用。  
- 写入的typeCode必须与读取的typeCode一致，否则会导致数据异常。  
- 调用顺序：先调用writeArrayBuffer()写入数据 → 再调用[readArrayBuffer](#readarraybuffer)读取数据。  
- typeCode参数决定了数据的写入和读取方式。  
- 读写typeCode不匹配会导致数据解析错误。  
- 必须根据实际数据类型选择正确的[TypeCode](arkts-ipc-rpc-typecode-e.md)枚举值。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| [typeCode](../../apis-notification-kit/arkts-apis/arkts-notification-notificationcontent-notificationsystemliveviewcontent-i.md) | [TypeCode](arkts-ipc-rpc-typecode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeAshmem

```TypeScript
writeAshmem(ashmem: Ashmem): void
```

将指定的匿名共享对象写入此MessageSequence。  
- 创建Ashmem对象：Ashmem.create()。  
- 映射内存并写入数据：[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem) +  
[writeDataToAshmem](arkts-ipc-rpc-ashmem-c.md#writedatatoashmem)。  
- 将Ashmem写入MessageSequence：writeAshmem()。  
- 接收端读取Ashmem：[readAshmem](#readashmem)。  
- 接收端映射内存并读取数据：mapReadWriteAshmem() + readDataFromAshmem()。  
- 此方法与readAshmem()方法配对使用。  
- 调用顺序：writeAshmem() → 传输MessageSequence → [readAshmem](#readashmem) →  
[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem) → [readDataFromAshmem](arkts-ipc-rpc-ashmem-c.md#readdatafromashmem)。  
- 使用前需先创建Ashmem对象并写入数据。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeBoolean

```TypeScript
writeBoolean(val: boolean): void
```

将布尔值写入MessageSequence实例。  
- 必须与[readBoolean](#readboolean)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeBooleanArray

```TypeScript
writeBooleanArray(booleanArray: boolean[]): void
```

将布尔数组写入MessageSequence实例。  
- 必须与[readBooleanArray](#readbooleanarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| booleanArray | boolean[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeByte

```TypeScript
writeByte(val: number): void
```

将字节值写入MessageSequence实例。调用此方法后，字节值会被以8位无符号整数形式存入缓冲区当前写指针位置，并自动更新写指针。该方法适用于传输小范围整数或标志位数据。  
- 存储范围:[0, 255](无符号)或[-128, 127](有符号)。  
- 数据对齐方式为字节对齐。  
- 数值必须在字节范围内，超出范围可能导致数据截断。  
- 读取时必须使用[readByte](#readbyte)方法配对读取。  
- 不适合传输大范围数值，大范围数值建议使用[writeInt](#writeint)/  
[writeLong](#writelong)等。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeByteArray

```TypeScript
writeByteArray(byteArray: number[]): void
```

将字节数组写入MessageSequence实例。  
- 必须与[readByteArray](#readbytearray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| byteArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeChar

```TypeScript
writeChar(val: number): void
```

将单个字符值写入MessageSequence实例。  
- 必须与[readChar](#readchar)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeCharArray

```TypeScript
writeCharArray(charArray: number[]): void
```

将单个字符数组写入MessageSequence实例。  
- 必须与[readCharArray](#readchararray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeDouble

```TypeScript
writeDouble(val: number): void
```

将双精度浮点值写入MessageSequence实例。  
- 必须与[readDouble](#readdouble)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeDoubleArray

```TypeScript
writeDoubleArray(doubleArray: number[]): void
```

将双精度浮点数组写入MessageSequence实例。  
- 必须与[readDoubleArray](#readdoublearray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| doubleArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeFileDescriptor

```TypeScript
writeFileDescriptor(fd: number): void
```

写入文件描述符到MessageSequence。 调用此方法后，文件描述符会被封装并通过Binder机制跨进程传递。接收端可通过readFileDescriptor获取文件描述符并进行文件操作。  
- 文件描述符通过Binder的FD传递机制跨进程传输。  
- 接收端获得的是映射后的新文件描述符。  
- 实际指向同一个文件资源。  
- 支持普通文件、管道、socket等多种描述符。  
- 文件描述符必须是有效的、已打开的描述符。  
- 写入后原描述符仍然有效，需要业务自行管理。  
- 建议使用dupFileDescriptor复制后再传递。  
- 传递后接收端应及时使用，避免资源浪费。  
- 读取后建议及时关闭，防止资源泄漏。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeFloat

```TypeScript
writeFloat(val: number): void
```

将双精度浮点值写入MessageSequence实例。由于系统内部对float类型的数据是按照double处理的，实际写入的数据按双精度格式存储。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeFloatArray

```TypeScript
writeFloatArray(floatArray: number[]): void
```

将双精度浮点数组写入MessageSequence实例。  
- 必须与[readFloatArray](#readfloatarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| floatArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeInt

```TypeScript
writeInt(val: number): void
```

将整数值写入MessageSequence实例。 调用此方法后，整数值会被以32位有符号整数形式存入缓冲区当前写指针位置，并自动更新写指针。该方法适用于传输标准整数数据。对于小范围数值建议使用 [writeByte](#writebyte)/[writeShort](#writeshort)提高效率；对于大范围数值建议 使用[writeLong](#writelong)。  
- 必须与[readInt](#readint)配对使用。  
- 一次写入对应一次读取  
- 占用4字节(32位)存储空间。  
- 采用系统默认字节序存储。  
- 超出范围会导致数据截断或写入失败。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeIntArray

```TypeScript
writeIntArray(intArray: number[]): void
```

将整数数组写入MessageSequence实例。  
- 必须与[readIntArray](#readintarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| intArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeInterfaceToken

```TypeScript
writeInterfaceToken(token: string): void
```

将接口描述符写入MessageSequence对象，远端对象可使用该信息校验本次通信。适用于需要验证通信双方接口一致性的场景，如跨进程服务调用、安全通信验证以及标识服务端提供的接口类型。建议使用唯一且有意义的描述符字符串（如"com.example.service"），避免使用敏感信息，长度应小于40960。调用此方法后，接口描述符字符串会被序列化并存入MessageSequence缓冲区。远端在接收到通信请求后，可读取该描述符来验证请求来源的合法 性。  
- 必须与[readInterfaceToken](#readinterfacetoken)配对使用。  
- 长度超过限制会抛出参数错误异常。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeLong

```TypeScript
writeLong(val: number): void
```

将长整数值写入MessageSequence实例。  
- 必须与[readLong](#readlong)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeLongArray

```TypeScript
writeLongArray(longArray: number[]): void
```

将长整数数组写入MessageSequence实例。  
- 必须与[readLongArray](#readlongarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| longArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeNoException

```TypeScript
writeNoException(): void
```

向MessageSequence写入“指示未发生异常”的信息。通常在IPC/RPC通信的服务端实现以及onRemoteMessageRequest回调中调用。  
- 此方法与[readException](#readexception)方法配对使用。  
- 服务端在处理请求完成后，应调用writeNoException()写入未发生异常的信息。  
- 客户端在收到响应后，应调用[readException](#readexception)读取异常信息。  
- 如果服务端未调用writeNoException()，客户端调用[readException](#readexception)会读取失败。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeParcelable

```TypeScript
writeParcelable(val: Parcelable): void
```

将自定义序列化对象写入MessageSequence实例。调用此方法后，会调用Parcelable对象的marshalling方法，将对象的成员变量逐个序列化写入MessageSequence。该方法支持传输自定义数据结构对象 适用于传输复杂数据结构、业务对象、配置信息等场景。  
- Parcelable接口定义了序列化和反序列化的标准方法。  
- marshalling负责将对象状态写入MessageSequence。  
- unmarshalling负责从MessageSequence恢复对象状态。  
- 业务需自行实现具体的序列化逻辑。  
- 必须传入实现了Parcelable接口的对象。  
- marshalling方法必须正确实现所有成员变量的写入。  
- 序列化顺序必须与反序列化顺序一致。  
- 建议在marshalling中处理异常情况。  
- 复杂对象可能占用较多缓冲区空间。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | [Parcelable](arkts-ipc-rpc-parcelable-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeParcelableArray

```TypeScript
writeParcelableArray(parcelableArray: Parcelable[]): void
```

将可序列化对象数组写入MessageSequence实例。适用于批量传输多个自定义数据结构对象的场景，如传输多条业务记录、批量配置信息、多个实体对象等。  
- 必须与[readParcelableArray](#readparcelablearray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parcelableArray | [Parcelable](arkts-ipc-rpc-parcelable-i.md)[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeRawData

```TypeScript
writeRawData(rawData: number[], size: number): void
```

将原始数据写入MessageSequence对象。

> **说明：**&gt;
> 该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。&gt;
> 该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [writeRawDataBuffer](#writerawdatabuffer)(rawData: ArrayBuffer, size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawData | number[] | 是 |
| size | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeRawDataBuffer

```TypeScript
writeRawDataBuffer(rawData: ArrayBuffer, size: number): void
```

将原始数据写入MessageSequence对象。

> **说明：**&gt;
> 该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。&gt;
> 该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawData | ArrayBuffer | 是 |
| size | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeRemoteObject

```TypeScript
writeRemoteObject(obj: IRemoteObject): void
```

序列化远程对象并将其写入[MessageSequence](#messagesequence)对象。调用此方法后，IRemoteObject对象会被序列化为特定格式并存入MessageSequence的缓冲区 中，同时会更新内部写指针位置。该序列化对象可在接收端通过readRemoteObject方法反序列化读取。  
- 只能写入有效的IRemoteObject对象，传入无效对象会抛出异常。  
- 序列化后的对象占用固定大小的缓冲区空间。  
- 写入的对象必须与对应的readRemoteObject方法配对使用。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900008](../errorcode-rpc.md#1900008-非法的ipc对象) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeRemoteObjectArray

```TypeScript
writeRemoteObjectArray(objectArray: IRemoteObject[]): void
```

将IRemoteObject对象数组写入MessageSequence。适用于需要传递多个远程对象的场景，如批量注册多个服务代理、传递多个回调接口、多服务端点管理等。  
- 必须与[readRemoteObjectArray](#readremoteobjectarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| objectArray | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeShort

```TypeScript
writeShort(val: number): void
```

将短整数值写入MessageSequence实例。  
- 超出范围会导致数据截断。  
- 必须与[readShort](#readshort)配对使用。  
- 一次写入对应一次读取。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeShortArray

```TypeScript
writeShortArray(shortArray: number[]): void
```

将短整数数组写入MessageSequence实例。  
- 必须与[readShortArray](#readshortarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shortArray | number[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeString

```TypeScript
writeString(val: string): void
```

将字符串值写入MessageSequence实例。调用此方法后，字符串会被序列化存入缓冲区。写入时会先存储字符串长度，再存储字节数据。  
- 此方法与[readString](#readstring)方法配对使用。  
- 先写入长度，再写入内容。  
- 支持多语言字符集。  
- 长度信息便于[readString](#readstring)确定读取边界。  
- 注意区分字符数和字节数，中文字符占用更多字节。  
- 长字符串会占用较多缓冲区空间。  
- 空字符串也可以正常写入。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |

## writeStringArray

```TypeScript
writeStringArray(stringArray: string[]): void
```

将字符串数组写入MessageSequence实例。  
- 必须与[readStringArray](#readstringarray)配对使用。  
- 读取数组长度必须与写入数组长度一致。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stringArray | string[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900009](../errorcode-rpc.md#1900009-向messagesequence写入数据失败) |
