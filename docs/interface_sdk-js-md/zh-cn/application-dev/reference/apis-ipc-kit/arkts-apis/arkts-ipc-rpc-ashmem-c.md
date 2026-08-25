# Ashmem

提供与匿名共享内存对象相关的方法，包括创建、关闭、映射和取消映射Ashmem、从Ashmem读取数据和写入数据、获取Ashmem大小、设置Ashmem保护。共享内存只适用与本设备内跨进程通信。  
- 大数据传输：传输大量数据(如图片、文件)时使用共享内存提升效率。  
- 跨进程数据共享：多个进程需要共享访问同一块内存数据。  
- 传输效率问题：大数据通过共享内存传输避免序列化开销，提升传输效率。  
- 内存复用问题：多进程可共享访问同一内存，避免数据拷贝。  
- 提升传输性能：共享内存机制大幅提升大数据传输效率。  
- 减少内存占用：避免数据多次拷贝，节省内存资源。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## closeAshmem

```TypeScript
closeAshmem(): void
```

关闭这个Ashmem。

> **说明：**&gt;
> 关闭Ashmem对象前需要先解除地址映射。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## create

```TypeScript
static create(name: string, size: number): Ashmem
```

静态方法，根据指定的名称和大小创建Ashmem对象。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## create

```TypeScript
static create(ashmem: Ashmem): Ashmem
```

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createAshmem

```TypeScript
static createAshmem(name: string, size: number): Ashmem
```

静态方法，根据指定的名称和大小创建Ashmem对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** create()

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## createAshmemFromExisting

```TypeScript
static createAshmemFromExisting(ashmem: Ashmem): Ashmem
```

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** create()

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## getAshmemSize

```TypeScript
getAshmemSize(): number
```

获取Ashmem对象的内存大小。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## mapAshmem

```TypeScript
mapAshmem(mapType: number): boolean
```

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapTypedAshmem](#maptypedashmem)(mapType: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mapType | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## mapReadAndWriteAshmem

```TypeScript
mapReadAndWriteAshmem(): boolean
```

在此进程虚拟地址空间上创建可读写的共享文件映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapReadWriteAshmem](#mapreadwriteashmem)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## mapReadOnlyAshmem

```TypeScript
mapReadOnlyAshmem(): boolean
```

在此进程虚拟地址空间上创建只读的共享文件映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapReadonlyAshmem](#mapreadonlyashmem)()

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## mapReadonlyAshmem

```TypeScript
mapReadonlyAshmem(): void
```

在此进程虚拟地址空间上创建只读的共享文件映射。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## mapReadWriteAshmem

```TypeScript
mapReadWriteAshmem(): void
```

在此进程虚拟地址空间上创建可读写的共享文件映射。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## mapTypedAshmem

```TypeScript
mapTypedAshmem(mapType: number): void
```

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mapType | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## readAshmem

```TypeScript
readAshmem(size: number, offset: number): number[]
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [readDataFromAshmem](#readdatafromashmem)(size: int, offset: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900004](../errorcode-rpc.md#1900004-共享内存读数据失败) |

## readDataFromAshmem

```TypeScript
readDataFromAshmem(size: number, offset: number): ArrayBuffer
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900004](../errorcode-rpc.md#1900004-共享内存读数据失败) |

## readFromAshmem

```TypeScript
readFromAshmem(size: number, offset: number): number[]
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readDataFromAshmem](#readdatafromashmem)(size: int, offset: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| number[] |

## setProtection

```TypeScript
setProtection(protectionType: number): boolean
```

设置映射内存区域的保护等级。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setProtectionType](#setprotectiontype)(protectionType: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protectionType | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setProtectionType

```TypeScript
setProtectionType(protectionType: number): void
```

设置映射内存区域的保护等级。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protectionType | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900002](../errorcode-rpc.md#1900002-系统调用ioctl失败) |

## unmapAshmem

```TypeScript
unmapAshmem(): void
```

删除该Ashmem对象的地址映射。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## writeAshmem

```TypeScript
writeAshmem(buf: number[], size: number, offset: number): void
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [writeDataToAshmem](#writedatatoashmem)(buf: ArrayBuffer, size: int, offset: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | number[] | 是 |
| size | number | 是 |
| offset | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900003](../errorcode-rpc.md#1900003-共享内存写数据失败) |

## writeDataToAshmem

```TypeScript
writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| size | number | 是 |
| offset | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1900003](../errorcode-rpc.md#1900003-共享内存写数据失败) |

## writeToAshmem

```TypeScript
writeToAshmem(buf: number[], size: number, offset: number): boolean
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**&gt;
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem)进行映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeDataToAshmem](#writedatatoashmem)(buf: ArrayBuffer, size: int, offset: int)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | number[] | 是 |
| size | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## PROT_EXEC

```TypeScript
static readonly PROT_EXEC: number
```

映射内存保护类型，代表映射的内存可执行。

**类型：** number

**默认值：** 4

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_NONE

```TypeScript
static readonly PROT_NONE: number
```

映射内存保护类型，代表映射的内存不可访问。

**类型：** number

**默认值：** 0

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_READ

```TypeScript
static readonly PROT_READ: number
```

映射内存保护类型，代表映射的内存可读。

**类型：** number

**默认值：** 1

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_WRITE

```TypeScript
static readonly PROT_WRITE: number
```

映射内存保护类型，代表映射的内存可写。

**类型：** number

**默认值：** 2

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core
