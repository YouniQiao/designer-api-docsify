# MessageParcel

在RPC过程中，发送方可以使用MessageParcel提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageParcel提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、 接口描述符和自定义序列化对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [closeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#closefiledescriptor)(fd: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

## containFileDescriptors

```TypeScript
containFileDescriptors(): boolean
```

检查此MessageParcel对象是否包含文件描述符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [containFileDescriptors](arkts-ipc-rpc-messagesequence-c.md#containfiledescriptors)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## create

```TypeScript
static create(): MessageParcel
```

静态方法，创建MessageParcel对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [create](arkts-ipc-rpc-messagesequence-c.md#create)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) |

## dupFileDescriptor

```TypeScript
static dupFileDescriptor(fd: number): number
```

静态方法，复制给定的文件描述符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [dupFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#dupfiledescriptor)(fd: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getCapacity

```TypeScript
getCapacity(): number
```

获取当前MessageParcel的容量。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCapacity](arkts-ipc-rpc-messagesequence-c.md#getcapacity)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getRawDataCapacity

```TypeScript
getRawDataCapacity(): number
```

获取MessageParcel可以容纳的最大原始数据量。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawDataCapacity](arkts-ipc-rpc-messagesequence-c.md#getrawdatacapacity)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getReadableBytes

```TypeScript
getReadableBytes(): number
```

获取MessageParcel的可读字节空间。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getReadableBytes](arkts-ipc-rpc-messagesequence-c.md#getreadablebytes)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getReadPosition

```TypeScript
getReadPosition(): number
```

获取MessageParcel的读位置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getReadPosition](arkts-ipc-rpc-messagesequence-c.md#getreadposition)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

获取当前MessageParcel的数据大小。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getSize](arkts-ipc-rpc-messagesequence-c.md#getsize)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getWritableBytes

```TypeScript
getWritableBytes(): number
```

获取MessageParcel的可写字节空间。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWritableBytes](arkts-ipc-rpc-messagesequence-c.md#getwritablebytes)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getWritePosition

```TypeScript
getWritePosition(): number
```

获取MessageParcel的写位置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWritePosition](arkts-ipc-rpc-messagesequence-c.md#getwriteposition)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readAshmem

```TypeScript
readAshmem(): Ashmem
```

从MessageParcel读取匿名共享对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readAshmem](arkts-ipc-rpc-messagesequence-c.md#readashmem)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## readBoolean

```TypeScript
readBoolean(): boolean
```

从MessageParcel实例中读取布尔值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readBoolean](arkts-ipc-rpc-messagesequence-c.md#readboolean)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## readBooleanArray

```TypeScript
readBooleanArray(dataIn: boolean[]): void
```

从MessageParcel实例中读取布尔数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)(dataIn: boolean[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | boolean[] | 是 |

## readBooleanArray

```TypeScript
readBooleanArray(): boolean[]
```

从MessageParcel实例中读取布尔数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean[] |

## readByte

```TypeScript
readByte(): number
```

从MessageParcel实例中读取字节值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readByte](arkts-ipc-rpc-messagesequence-c.md#readbyte)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readByteArray

```TypeScript
readByteArray(dataIn: number[]): void
```

从MessageParcel实例中读取字节数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)(dataIn: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readByteArray

```TypeScript
readByteArray(): number[]
```

从MessageParcel实例中读取字节数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readChar

```TypeScript
readChar(): number
```

从MessageParcel实例中读取单个字符值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readChar](arkts-ipc-rpc-messagesequence-c.md#readchar)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readCharArray

```TypeScript
readCharArray(dataIn: number[]): void
```

从MessageParcel实例中读取单个字符数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)(dataIn: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readCharArray

```TypeScript
readCharArray(): number[]
```

从MessageParcel实例中读取单个字符数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readDouble

```TypeScript
readDouble(): number
```

从MessageParcel实例中读取双精度浮点值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readDouble](arkts-ipc-rpc-messagesequence-c.md#readdouble)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readDoubleArray

```TypeScript
readDoubleArray(dataIn: number[]): void
```

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)(dataIn: double[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readDoubleArray

```TypeScript
readDoubleArray(): number[]
```

从MessageParcel实例中读取双精度浮点数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readException

```TypeScript
readException(): void
```

从MessageParcel中读取异常。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readException](arkts-ipc-rpc-messagesequence-c.md#readexception)()

**系统能力：** SystemCapability.Communication.IPC.Core

## readFileDescriptor

```TypeScript
readFileDescriptor(): number
```

从MessageParcel中读取文件描述符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#readfiledescriptor)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readFloat

```TypeScript
readFloat(): number
```

从MessageParcel实例中读取双精度浮点值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readFloat](arkts-ipc-rpc-messagesequence-c.md#readfloat)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readFloatArray

```TypeScript
readFloatArray(dataIn: number[]): void
```

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)(dataIn: double[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readFloatArray

```TypeScript
readFloatArray(): number[]
```

从MessageParcel实例中读取双精度浮点数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readInt

```TypeScript
readInt(): number
```

从MessageParcel实例中读取整数值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readInt](arkts-ipc-rpc-messagesequence-c.md#readint)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readIntArray

```TypeScript
readIntArray(dataIn: number[]): void
```

从MessageParcel实例中读取整数数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)(dataIn: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readIntArray

```TypeScript
readIntArray(): number[]
```

从MessageParcel实例中读取整数数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readInterfaceToken

```TypeScript
readInterfaceToken(): string
```

从MessageParcel中读取接口描述符，接口描述符按写入MessageParcel的顺序读取，本地对象可使用该信息检验本次通信。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#readinterfacetoken)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## readLong

```TypeScript
readLong(): number
```

从MessageParcel实例中读取长整数值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readLong](arkts-ipc-rpc-messagesequence-c.md#readlong)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readLongArray

```TypeScript
readLongArray(dataIn: number[]): void
```

从MessageParcel实例中读取长整数数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)(dataIn: long[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readLongArray

```TypeScript
readLongArray(): number[]
```

从MessageParcel实例中读取长整数数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readRawData

```TypeScript
readRawData(size: number): number[]
```

从MessageParcel读取原始数据。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#readrawdatabuffer)(size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

## readRemoteObject

```TypeScript
readRemoteObject(): IRemoteObject
```

从MessageParcel读取远程对象。此方法用于反序列化MessageParcel对象以生成IRemoteObject。远程对象按写入MessageParcel的顺序读取。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readRemoteObject](arkts-ipc-rpc-messagesequence-c.md#readremoteobject)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(objects: IRemoteObject[]): void
```

从MessageParcel读取IRemoteObject对象数组，并将其写入到创建的空数组中。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects: IRemoteObject[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| objects | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | 是 |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(): IRemoteObject[]
```

从MessageParcel读取IRemoteObject对象数组。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects: IRemoteObject[])

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] |

## readSequenceable

```TypeScript
readSequenceable(dataIn: Sequenceable): boolean
```

从MessageParcel实例中读取成员变量到指定的对象（dataIn）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readParcelable](arkts-ipc-rpc-messagesequence-c.md#readparcelable)(dataIn: Parcelable)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## readSequenceableArray

```TypeScript
readSequenceableArray(sequenceableArray: Sequenceable[]): void
```

从MessageParcel实例中读取可序列化对象数组。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readParcelableArray](arkts-ipc-rpc-messagesequence-c.md#readparcelablearray)(parcelableArray: Parcelable[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | 是 |

## readShort

```TypeScript
readShort(): number
```

从MessageParcel实例中读取短整数值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readShort](arkts-ipc-rpc-messagesequence-c.md#readshort)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## readShortArray

```TypeScript
readShortArray(dataIn: number[]): void
```

从MessageParcel实例中读取短整数数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)(dataIn: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | number[] | 是 |

## readShortArray

```TypeScript
readShortArray(): number[]
```

从MessageParcel实例中读取短整数数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number[] |

## readString

```TypeScript
readString(): string
```

从MessageParcel实例中读取字符串值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readString](arkts-ipc-rpc-messagesequence-c.md#readstring)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## readStringArray

```TypeScript
readStringArray(dataIn: string[]): void
```

从MessageParcel实例中读取字符串数组，并将其写入到创建的空数组中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)(dataIn: string[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | string[] | 是 |

## readStringArray

```TypeScript
readStringArray(): string[]
```

从MessageParcel实例中读取字符串数组。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string[] |

## reclaim

```TypeScript
reclaim(): void
```

释放不再使用的MessageParcel对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [reclaim](arkts-ipc-rpc-messagesequence-c.md#reclaim)()

**系统能力：** SystemCapability.Communication.IPC.Core

## rewindRead

```TypeScript
rewindRead(pos: number): boolean
```

重新偏移读取位置到指定的位置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [rewindRead](arkts-ipc-rpc-messagesequence-c.md#rewindread)(pos: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## rewindWrite

```TypeScript
rewindWrite(pos: number): boolean
```

重新偏移写位置到指定的位置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [rewindWrite](arkts-ipc-rpc-messagesequence-c.md#rewindwrite)(pos: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setCapacity

```TypeScript
setCapacity(size: number): boolean
```

设置MessageParcel实例的存储容量。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCapacity](arkts-ipc-rpc-messagesequence-c.md#setcapacity)(size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setSize

```TypeScript
setSize(size: number): boolean
```

设置MessageParcel实例中包含的数据大小。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setSize](arkts-ipc-rpc-messagesequence-c.md#setsize)(size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeAshmem

```TypeScript
writeAshmem(ashmem: Ashmem): boolean
```

将指定的匿名共享对象写入此MessageParcel。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeAshmem](arkts-ipc-rpc-messagesequence-c.md#writeashmem)(ashmem: Ashmem)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeBoolean

```TypeScript
writeBoolean(val: boolean): boolean
```

将布尔值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeBoolean](arkts-ipc-rpc-messagesequence-c.md#writeboolean)(val: boolean)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeBooleanArray

```TypeScript
writeBooleanArray(booleanArray: boolean[]): boolean
```

将布尔数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeBooleanArray](arkts-ipc-rpc-messagesequence-c.md#writebooleanarray)(booleanArray: boolean[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| booleanArray | boolean[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeByte

```TypeScript
writeByte(val: number): boolean
```

将字节值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeByte](arkts-ipc-rpc-messagesequence-c.md#writebyte)(val: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeByteArray

```TypeScript
writeByteArray(byteArray: number[]): boolean
```

将字节数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeByteArray](arkts-ipc-rpc-messagesequence-c.md#writebytearray)(byteArray: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| byteArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeChar

```TypeScript
writeChar(val: number): boolean
```

将单个字符值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeChar](arkts-ipc-rpc-messagesequence-c.md#writechar)(val: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeCharArray

```TypeScript
writeCharArray(charArray: number[]): boolean
```

将单个字符数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeCharArray](arkts-ipc-rpc-messagesequence-c.md#writechararray)(charArray: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeDouble

```TypeScript
writeDouble(val: number): boolean
```

将双精度浮点值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeDouble](arkts-ipc-rpc-messagesequence-c.md#writedouble)(val: double)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeDoubleArray

```TypeScript
writeDoubleArray(doubleArray: number[]): boolean
```

将双精度浮点数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeDoubleArray](arkts-ipc-rpc-messagesequence-c.md#writedoublearray)(doubleArray: double[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| doubleArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeFileDescriptor

```TypeScript
writeFileDescriptor(fd: number): boolean
```

写入文件描述符到MessageParcel。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#writefiledescriptor)(fd: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeFloat

```TypeScript
writeFloat(val: number): boolean
```

将双精度浮点值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeFloat](arkts-ipc-rpc-messagesequence-c.md#writefloat)(val: double)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeFloatArray

```TypeScript
writeFloatArray(floatArray: number[]): boolean
```

将双精度浮点数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeFloatArray](arkts-ipc-rpc-messagesequence-c.md#writefloatarray)(floatArray: double[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| floatArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeInt

```TypeScript
writeInt(val: number): boolean
```

将整数值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeInt](arkts-ipc-rpc-messagesequence-c.md#writeint)(val: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeIntArray

```TypeScript
writeIntArray(intArray: number[]): boolean
```

将整数数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeIntArray](arkts-ipc-rpc-messagesequence-c.md#writeintarray)(intArray: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| intArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeInterfaceToken

```TypeScript
writeInterfaceToken(token: string): boolean
```

将接口描述符写入MessageParcel对象，远端对象可使用该信息校验本次通信。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#writeinterfacetoken)(token: string)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeLong

```TypeScript
writeLong(val: number): boolean
```

将长整数值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeLong](arkts-ipc-rpc-messagesequence-c.md#writelong)(val: long)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeLongArray

```TypeScript
writeLongArray(longArray: number[]): boolean
```

将长整数数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeLongArray](arkts-ipc-rpc-messagesequence-c.md#writelongarray)(longArray: long[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| longArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeNoException

```TypeScript
writeNoException(): void
```

向MessageParcel写入“指示未发生异常”的信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeNoException](arkts-ipc-rpc-messagesequence-c.md#writenoexception)()

**系统能力：** SystemCapability.Communication.IPC.Core

## writeRawData

```TypeScript
writeRawData(rawData: number[], size: number): boolean
```

将原始数据写入MessageParcel对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#writerawdatabuffer)(rawData: ArrayBuffer, size: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawData | number[] | 是 |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeRemoteObject

```TypeScript
writeRemoteObject(object: IRemoteObject): boolean
```

序列化远程对象并将其写入MessageParcel对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeRemoteObject](arkts-ipc-rpc-messagesequence-c.md#writeremoteobject)(obj: IRemoteObject)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeRemoteObjectArray

```TypeScript
writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean
```

将IRemoteObject对象数组写入MessageParcel。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#writeremoteobjectarray)(objectArray: IRemoteObject[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| objectArray | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeSequenceable

```TypeScript
writeSequenceable(val: Sequenceable): boolean
```

将自定义序列化对象写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeParcelable](arkts-ipc-rpc-messagesequence-c.md#writeparcelable)(val: Parcelable)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeSequenceableArray

```TypeScript
writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean
```

将可序列化对象数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeParcelableArray](arkts-ipc-rpc-messagesequence-c.md#writeparcelablearray)(parcelableArray: Parcelable[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeShort

```TypeScript
writeShort(val: number): boolean
```

将短整数值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeShort](arkts-ipc-rpc-messagesequence-c.md#writeshort)(val: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeShortArray

```TypeScript
writeShortArray(shortArray: number[]): boolean
```

将短整数数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeShortArray](arkts-ipc-rpc-messagesequence-c.md#writeshortarray)(shortArray: int[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shortArray | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeString

```TypeScript
writeString(val: string): boolean
```

将字符串值写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeString](arkts-ipc-rpc-messagesequence-c.md#writestring)(val: string)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## writeStringArray

```TypeScript
writeStringArray(stringArray: string[]): boolean
```

将字符串数组写入MessageParcel实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [writeStringArray](arkts-ipc-rpc-messagesequence-c.md#writestringarray)(stringArray: string[])

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stringArray | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
