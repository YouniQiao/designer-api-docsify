# Ashmem

提供与匿名共享内存对象相关的方法，包括创建、关闭、映射和取消映射Ashmem、从Ashmem读取数据和写入数据、获取Ashmem大小、设置Ashmem保护。

共享内存只适用与本设备内跨进程通信。

- 大数据传输：传输大量数据(如图片、文件)时使用共享内存提升效率。  
- 跨进程数据共享：多个进程需要共享访问同一块内存数据。  
- 传输效率问题：大数据通过共享内存传输避免序列化开销，提升传输效率。  
- 内存复用问题：多进程可共享访问同一内存，避免数据拷贝。  
- 提升传输性能：共享内存机制大幅提升大数据传输效率。  
- 减少内存占用：避免数据多次拷贝，节省内存资源。

**起始版本：** 8

<!--Device-rpc-class Ashmem--><!--Device-rpc-class Ashmem-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## closeAshmem

```TypeScript
closeAshmem(): void
```

关闭这个Ashmem。

> **说明：**
> 
> 关闭Ashmem对象前需要先解除地址映射。

**起始版本：** 8

<!--Device-Ashmem-closeAshmem(): void--><!--Device-Ashmem-closeAshmem(): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.closeAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## create

```TypeScript
static create(name: string, size: number): Ashmem
```

静态方法，根据指定的名称和大小创建Ashmem对象。

**起始版本：** 9

<!--Device-Ashmem-static create(name: string, size: int): Ashmem--><!--Device-Ashmem-static create(name: string, size: int): Ashmem-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## create

```TypeScript
static create(ashmem: Ashmem): Ashmem
```

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**起始版本：** 9

<!--Device-Ashmem-static create(ashmem: Ashmem): Ashmem--><!--Device-Ashmem-static create(ashmem: Ashmem): Ashmem-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let ashmem2 = rpc.Ashmem.create(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## createAshmem

```TypeScript
static createAshmem(name: string, size: number): Ashmem
```

静态方法，根据指定的名称和大小创建Ashmem对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [create](arkts-ipc-rpc-ashmem-c.md#create)()

<!--Device-Ashmem-static createAshmem(name: string, size: number): Ashmem--><!--Device-Ashmem-static createAshmem(name: string, size: number): Ashmem-End-->

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

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## createAshmemFromExisting

```TypeScript
static createAshmemFromExisting(ashmem: Ashmem): Ashmem
```

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [create](arkts-ipc-rpc-ashmem-c.md#create)()

<!--Device-Ashmem-static createAshmemFromExisting(ashmem: Ashmem): Ashmem--><!--Device-Ashmem-static createAshmemFromExisting(ashmem: Ashmem): Ashmem-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let ashmem2 = rpc.Ashmem.createAshmemFromExisting(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## getAshmemSize

```TypeScript
getAshmemSize(): number
```

获取Ashmem对象的内存大小。

**起始版本：** 8

<!--Device-Ashmem-getAshmemSize(): int--><!--Device-Ashmem-getAshmemSize(): int-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag', ' size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## mapAshmem

```TypeScript
mapAshmem(mapType: number): boolean
```

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapTypedAshmem](arkts-ipc-rpc-ashmem-c.md#maptypedashmem)(mapType:

<!--Device-Ashmem-mapAshmem(mapType: number): boolean--><!--Device-Ashmem-mapAshmem(mapType: number): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mapType | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapReadAndWrite = ashmem.mapAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapReadAndWrite);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## mapReadAndWriteAshmem

```TypeScript
mapReadAndWriteAshmem(): boolean
```

在此进程虚拟地址空间上创建可读写的共享文件映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)()

<!--Device-Ashmem-mapReadAndWriteAshmem(): boolean--><!--Device-Ashmem-mapReadAndWriteAshmem(): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## mapReadOnlyAshmem

```TypeScript
mapReadOnlyAshmem(): boolean
```

在此进程虚拟地址空间上创建只读的共享文件映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [mapReadonlyAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadonlyashmem)()

<!--Device-Ashmem-mapReadOnlyAshmem(): boolean--><!--Device-Ashmem-mapReadOnlyAshmem(): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadOnlyAshmem();
  hilog.info(0x0000, 'testTag', 'Ashmem mapReadOnlyAshmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## mapReadWriteAshmem

```TypeScript
mapReadWriteAshmem(): void
```

在此进程虚拟地址空间上创建可读写的共享文件映射。

**起始版本：** 9

<!--Device-Ashmem-mapReadWriteAshmem(): void--><!--Device-Ashmem-mapReadWriteAshmem(): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## mapReadonlyAshmem

```TypeScript
mapReadonlyAshmem(): void
```

在此进程虚拟地址空间上创建只读的共享文件映射。

**起始版本：** 9

<!--Device-Ashmem-mapReadonlyAshmem(): void--><!--Device-Ashmem-mapReadonlyAshmem(): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**错误码：**

| 错误码ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadonlyAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## mapTypedAshmem

```TypeScript
mapTypedAshmem(mapType: number): void
```

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**起始版本：** 9

<!--Device-Ashmem-mapTypedAshmem(mapType: int): void--><!--Device-Ashmem-mapTypedAshmem(mapType: int): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mapType | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900001](../errorcode-rpc.md#1900001-系统调用mmap失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapTypedAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## readAshmem

```TypeScript
readAshmem(size: number, offset: number): number[]
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [readDataFromAshmem](arkts-ipc-rpc-ashmem-c.md#readdatafromashmem)(size:

<!--Device-Ashmem-readAshmem(size: number, offset: number): number[]--><!--Device-Ashmem-readAshmem(size: number, offset: number): number[]-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900004](../errorcode-rpc.md#1900004-共享内存读数据失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
  let readResult = ashmem.readAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readResult);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## readDataFromAshmem

```TypeScript
readDataFromAshmem(size: number, offset: number): ArrayBuffer
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 11

<!--Device-Ashmem-readDataFromAshmem(size: int, offset: int): ArrayBuffer--><!--Device-Ashmem-readDataFromAshmem(size: int, offset: int): ArrayBuffer-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900004](../errorcode-rpc.md#1900004-共享内存读数据失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  let readResult = ashmem.readDataFromAshmem(size, 0);
  let readInt32View = new Int32Array(readResult);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## readFromAshmem

```TypeScript
readFromAshmem(size: number, offset: number): number[]
```

从此Ashmem对象关联的共享文件中读取数据。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [readDataFromAshmem](arkts-ipc-rpc-ashmem-c.md#readdatafromashmem)(size:

<!--Device-Ashmem-readFromAshmem(size: number, offset: number): number[]--><!--Device-Ashmem-readFromAshmem(size: number, offset: number): number[]-End-->

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

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
  let readResult = ashmem.readFromAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read to Ashmem result is ' + readResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## setProtection

```TypeScript
setProtection(protectionType: number): boolean
```

设置映射内存区域的保护等级。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setProtectionType](arkts-ipc-rpc-ashmem-c.md#setprotectiontype)(protectionType:

<!--Device-Ashmem-setProtection(protectionType: number): boolean--><!--Device-Ashmem-setProtection(protectionType: number): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protectionType | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let result = ashmem.setProtection(rpc.Ashmem.PROT_READ);
  hilog.info(0x0000, 'testTag', 'Ashmem setProtection result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## setProtectionType

```TypeScript
setProtectionType(protectionType: number): void
```

设置映射内存区域的保护等级。

**起始版本：** 9

<!--Device-Ashmem-setProtectionType(protectionType: int): void--><!--Device-Ashmem-setProtectionType(protectionType: int): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protectionType | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900002](../errorcode-rpc.md#1900002-系统调用ioctl失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.setProtectionType(rpc.Ashmem.PROT_READ);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorMessage ' + e.message);
}
```

## unmapAshmem

```TypeScript
unmapAshmem(): void
```

删除该Ashmem对象的地址映射。

**起始版本：** 8

<!--Device-Ashmem-unmapAshmem(): void--><!--Device-Ashmem-unmapAshmem(): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.unmapAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## writeAshmem

```TypeScript
writeAshmem(buf: number[], size: number, offset: number): void
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [writeDataToAshmem](arkts-ipc-rpc-ashmem-c.md#writedatatoashmem)(buf:

<!--Device-Ashmem-writeAshmem(buf: number[], size: number, offset: number): void--><!--Device-Ashmem-writeAshmem(buf: number[], size: number, offset: number): void-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900003](../errorcode-rpc.md#1900003-共享内存写数据失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorMessage ' + e.message);
}
```

## writeDataToAshmem

```TypeScript
writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 11

<!--Device-Ashmem-writeDataToAshmem(buf: ArrayBuffer, size: int, offset: int): void--><!--Device-Ashmem-writeDataToAshmem(buf: ArrayBuffer, size: int, offset: int): void-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1900003](../errorcode-rpc.md#1900003-共享内存写数据失败) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## writeToAshmem

```TypeScript
writeToAshmem(buf: number[], size: number, offset: number): boolean
```

将数据写入此Ashmem对象关联的共享文件。

> **说明：**
> 
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](arkts-ipc-rpc-ashmem-c.md#mapreadwriteashmem)进行映射。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [writeDataToAshmem](arkts-ipc-rpc-ashmem-c.md#writedatatoashmem)(buf:

<!--Device-Ashmem-writeToAshmem(buf: number[], size: number, offset: number): boolean--><!--Device-Ashmem-writeToAshmem(buf: number[], size: number, offset: number): boolean-End-->

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

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

## PROT_EXEC

```TypeScript
static readonly PROT_EXEC: number
```

映射内存保护类型，代表映射的内存可执行。

**类型：** number

**默认值：** 4

**起始版本：** 8

<!--Device-Ashmem-static readonly PROT_EXEC: number--><!--Device-Ashmem-static readonly PROT_EXEC: number-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_NONE

```TypeScript
static readonly PROT_NONE: number
```

映射内存保护类型，代表映射的内存不可访问。

**类型：** number

**默认值：** 0

**起始版本：** 8

<!--Device-Ashmem-static readonly PROT_NONE: number--><!--Device-Ashmem-static readonly PROT_NONE: number-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_READ

```TypeScript
static readonly PROT_READ: number
```

映射内存保护类型，代表映射的内存可读。

**类型：** number

**默认值：** 1

**起始版本：** 8

<!--Device-Ashmem-static readonly PROT_READ: number--><!--Device-Ashmem-static readonly PROT_READ: number-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## PROT_WRITE

```TypeScript
static readonly PROT_WRITE: number
```

映射内存保护类型，代表映射的内存可写。

**类型：** number

**默认值：** 2

**起始版本：** 8

<!--Device-Ashmem-static readonly PROT_WRITE: number--><!--Device-Ashmem-static readonly PROT_WRITE: number-End-->

**系统能力：** SystemCapability.Communication.IPC.Core
