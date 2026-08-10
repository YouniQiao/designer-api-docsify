# MessageParcel

在RPC过程中，发送方可以使用MessageParcel提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageParcel提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

<!--Device-rpc-class MessageParcel--><!--Device-rpc-class MessageParcel-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## closeFileDescriptor

```TypeScript
static closeFileDescriptor(fd: number): void
```

静态方法，关闭给定的文件描述符。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence.closeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#closefiledescriptor)(fd:

<!--Device-MessageParcel-static closeFileDescriptor(fd: number): void--><!--Device-MessageParcel-static closeFileDescriptor(fd: number): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 要关闭的文件描述符。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.closeFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## containFileDescriptors

```TypeScript
containFileDescriptors(): boolean
```

检查此MessageParcel对象是否包含文件描述符。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#containFileDescriptors](arkts-ipc-rpc-messagesequence-c.md#containfiledescriptors)()

<!--Device-MessageParcel-containFileDescriptors(): boolean--><!--Device-MessageParcel-containFileDescriptors(): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：包含文件描述符，false：未包含文件描述符。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
  let containFD = parcel.containFileDescriptors();
  hilog.info(0x0000, 'testTag', 'parcel after write fd containFd result is ' + containFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## create

```TypeScript
static create(): MessageParcel
```

静态方法，创建MessageParcel对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence.create](arkts-ipc-rpc-messagesequence-c.md#create)()

<!--Device-MessageParcel-static create(): MessageParcel--><!--Device-MessageParcel-static create(): MessageParcel-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 返回创建的MessageParcel对象，用于在IPC过程中封装请求和响应数据。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  hilog.info(0x0000, 'testTag', 'data is ' + data);

  // When the MessageParcel object is no longer used, the service calls the reclaim method to release resources.
  data.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## dupFileDescriptor

```TypeScript
static dupFileDescriptor(fd: number): number
```

静态方法，复制给定的文件描述符。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence.dupFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#dupfiledescriptor)(fd:

<!--Device-MessageParcel-static dupFileDescriptor(fd: number): number--><!--Device-MessageParcel-static dupFileDescriptor(fd: number): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 表示已存在的文件描述符。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回新的文件描述符。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.dupFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getCapacity

```TypeScript
getCapacity(): number
```

获取当前MessageParcel的容量。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getCapacity](arkts-ipc-rpc-messagesequence-c.md#getcapacity)()

<!--Device-MessageParcel-getCapacity(): number--><!--Device-MessageParcel-getCapacity(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取的MessageParcel的容量大小。以字节为单位。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.getCapacity();
  hilog.info(0x0000, 'testTag', 'capacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getRawDataCapacity

```TypeScript
getRawDataCapacity(): number
```

获取MessageParcel可以容纳的最大原始数据量。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getRawDataCapacity](arkts-ipc-rpc-messagesequence-c.md#getrawdatacapacity)()

<!--Device-MessageParcel-getRawDataCapacity(): number--><!--Device-MessageParcel-getRawDataCapacity(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回MessageParcel可以容纳的最大原始数据量，即128MB。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let result = parcel.getRawDataCapacity();
  hilog.info(0x0000, 'testTag', 'parcel get RawDataCapacity result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getReadPosition

```TypeScript
getReadPosition(): number
```

获取MessageParcel的读位置。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getReadPosition](arkts-ipc-rpc-messagesequence-c.md#getreadposition)()

<!--Device-MessageParcel-getReadPosition(): number--><!--Device-MessageParcel-getReadPosition(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回MessageParcel实例中的当前读取位置。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let readPos = data.getReadPosition();
  hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getReadableBytes

```TypeScript
getReadableBytes(): number
```

获取MessageParcel的可读字节空间。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getReadableBytes](arkts-ipc-rpc-messagesequence-c.md#getreadablebytes)()

<!--Device-MessageParcel-getReadableBytes(): number--><!--Device-MessageParcel-getReadableBytes(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取到的MessageParcel的可读字节空间。以字节为单位。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let result = data.getReadableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getSize

```TypeScript
getSize(): number
```

获取当前MessageParcel的数据大小。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getSize](arkts-ipc-rpc-messagesequence-c.md#getsize)()

<!--Device-MessageParcel-getSize(): number--><!--Device-MessageParcel-getSize(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取的MessageParcel的数据大小。以字节为单位。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let size = data.getSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getWritableBytes

```TypeScript
getWritableBytes(): number
```

获取MessageParcel的可写字节空间。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getWritableBytes](arkts-ipc-rpc-messagesequence-c.md#getwritablebytes)()

<!--Device-MessageParcel-getWritableBytes(): number--><!--Device-MessageParcel-getWritableBytes(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取到的MessageParcel的可写字节空间。以字节为单位。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let getWritableBytes = data.getWritableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getWritePosition

```TypeScript
getWritePosition(): number
```

获取MessageParcel的写位置。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#getWritePosition](arkts-ipc-rpc-messagesequence-c.md#getwriteposition)()

<!--Device-MessageParcel-getWritePosition(): number--><!--Device-MessageParcel-getWritePosition(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回MessageParcel实例中的当前写入位置。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(10);
  let bwPos = data.getWritePosition();
  hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readAshmem

```TypeScript
readAshmem(): Ashmem
```

从MessageParcel读取匿名共享对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readAshmem](arkts-ipc-rpc-messagesequence-c.md#readashmem)()

<!--Device-MessageParcel-readAshmem(): Ashmem--><!--Device-MessageParcel-readAshmem(): Ashmem-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) | 返回匿名共享对象。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
  let readAshmem = parcel.readAshmem();
  hilog.info(0x0000, 'testTag', 'read ashmem to result is ' + readAshmem);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readBoolean

```TypeScript
readBoolean(): boolean
```

从MessageParcel实例中读取布尔值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readBoolean](arkts-ipc-rpc-messagesequence-c.md#readboolean)()

<!--Device-MessageParcel-readBoolean(): boolean--><!--Device-MessageParcel-readBoolean(): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回读取到的布尔值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
  let ret = data.readBoolean();
  hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readBooleanArray

```TypeScript
readBooleanArray(dataIn: boolean[]): void
```

从MessageParcel实例中读取布尔数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)(dataIn:

<!--Device-MessageParcel-readBooleanArray(dataIn: boolean[]): void--><!--Device-MessageParcel-readBooleanArray(dataIn: boolean[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | boolean[] | Yes | 要读取的布尔数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array: Array<boolean> = new Array(3);
  data.readBooleanArray(array);
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readBooleanArray

```TypeScript
readBooleanArray(): boolean[]
```

从MessageParcel实例中读取布尔数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)()

<!--Device-MessageParcel-readBooleanArray(): boolean[]--><!--Device-MessageParcel-readBooleanArray(): boolean[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean[] | 返回布尔数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array = data.readBooleanArray();
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readByte

```TypeScript
readByte(): number
```

从MessageParcel实例中读取字节值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readByte](arkts-ipc-rpc-messagesequence-c.md#readbyte)()

<!--Device-MessageParcel-readByte(): number--><!--Device-MessageParcel-readByte(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回字节值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
  let ret = data.readByte();
  hilog.info(0x0000, 'testTag', 'readByte is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readByteArray

```TypeScript
readByteArray(dataIn: number[]): void
```

从MessageParcel实例中读取字节数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)(dataIn:

<!--Device-MessageParcel-readByteArray(dataIn: number[]): void--><!--Device-MessageParcel-readByteArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的字节数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  let array: Array<number> = new Array(5);
  data.readByteArray(array);
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readByteArray

```TypeScript
readByteArray(): number[]
```

从MessageParcel实例中读取字节数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)()

<!--Device-MessageParcel-readByteArray(): number[]--><!--Device-MessageParcel-readByteArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回字节数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
  let array = data.readByteArray();
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readChar

```TypeScript
readChar(): number
```

从MessageParcel实例中读取单个字符值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readChar](arkts-ipc-rpc-messagesequence-c.md#readchar)()

<!--Device-MessageParcel-readChar(): number--><!--Device-MessageParcel-readChar(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回单个字符值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
  let ret = data.readChar();
  hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readCharArray

```TypeScript
readCharArray(dataIn: number[]): void
```

从MessageParcel实例中读取单个字符数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)(dataIn:

<!--Device-MessageParcel-readCharArray(dataIn: number[]): void--><!--Device-MessageParcel-readCharArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的单个字符数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 99]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readCharArray(array);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readCharArray

```TypeScript
readCharArray(): number[]
```

从MessageParcel实例中读取单个字符数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)()

<!--Device-MessageParcel-readCharArray(): number[]--><!--Device-MessageParcel-readCharArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回单个字符数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 99]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array = data.readCharArray();
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readDouble

```TypeScript
readDouble(): number
```

从MessageParcel实例中读取双精度浮点值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readDouble](arkts-ipc-rpc-messagesequence-c.md#readdouble)()

<!--Device-MessageParcel-readDouble(): number--><!--Device-MessageParcel-readDouble(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回双精度浮点值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
  let ret = data.readDouble();
  hilog.info(0x0000, 'testTag', 'readDouble is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readDoubleArray

```TypeScript
readDoubleArray(dataIn: number[]): void
```

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)(dataIn:

<!--Device-MessageParcel-readDoubleArray(dataIn: number[]): void--><!--Device-MessageParcel-readDoubleArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的双精度浮点数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readDoubleArray(array);
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readDoubleArray

```TypeScript
readDoubleArray(): number[]
```

从MessageParcel实例中读取双精度浮点数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)()

<!--Device-MessageParcel-readDoubleArray(): number[]--><!--Device-MessageParcel-readDoubleArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array = data.readDoubleArray();
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readException

```TypeScript
readException(): void
```

从MessageParcel中读取异常。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readException](arkts-ipc-rpc-messagesequence-c.md#readexception)()

<!--Device-MessageParcel-readException(): void--><!--Device-MessageParcel-readException(): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Examples

In the sample code provided in this topic, this.getUIContext().getHostContext() is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

The proxy object in the onConnect callback can be assigned a value only after the ability is connected asynchronously. Then, sendRequest() of the proxy object is called to send a message.

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try { 
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeNoException();
  data.writeString('hello');
  if (proxy != undefined) {
    let a = proxy.sendRequest(1, data, reply, option) as Object;
    let b = a as Promise<rpc.SendRequestResult>;
    b.then((result: rpc.SendRequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendRequest got result');
        result.reply.readException();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendRequest got exception: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) { 
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readFileDescriptor

```TypeScript
readFileDescriptor(): number
```

从MessageParcel中读取文件描述符。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#readfiledescriptor)()

<!--Device-MessageParcel-readFileDescriptor(): number--><!--Device-MessageParcel-readFileDescriptor(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回文件描述符。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  parcel.writeFileDescriptor(file.fd);
  let readFD = parcel.readFileDescriptor();
  hilog.info(0x0000, 'testTag', 'parcel read fd is ' + readFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readFloat

```TypeScript
readFloat(): number
```

从MessageParcel实例中读取双精度浮点值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readFloat](arkts-ipc-rpc-messagesequence-c.md#readfloat)()

<!--Device-MessageParcel-readFloat(): number--><!--Device-MessageParcel-readFloat(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回双精度浮点值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
  let ret = data.readFloat();
  hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readFloatArray

```TypeScript
readFloatArray(dataIn: number[]): void
```

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)(dataIn:

<!--Device-MessageParcel-readFloatArray(dataIn: number[]): void--><!--Device-MessageParcel-readFloatArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readFloatArray(array);
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readFloatArray

```TypeScript
readFloatArray(): number[]
```

从MessageParcel实例中读取双精度浮点数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)()

<!--Device-MessageParcel-readFloatArray(): number[]--><!--Device-MessageParcel-readFloatArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回双精度浮点数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array = data.readFloatArray();
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readInt

```TypeScript
readInt(): number
```

从MessageParcel实例中读取整数值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readInt](arkts-ipc-rpc-messagesequence-c.md#readint)()

<!--Device-MessageParcel-readInt(): number--><!--Device-MessageParcel-readInt(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回整数值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
  let ret = data.readInt();
  hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readIntArray

```TypeScript
readIntArray(dataIn: number[]): void
```

从MessageParcel实例中读取整数数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)(dataIn:

<!--Device-MessageParcel-readIntArray(dataIn: number[]): void--><!--Device-MessageParcel-readIntArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readIntArray(array);
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readIntArray

```TypeScript
readIntArray(): number[]
```

从MessageParcel实例中读取整数数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)()

<!--Device-MessageParcel-readIntArray(): number[]--><!--Device-MessageParcel-readIntArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array = data.readIntArray();
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readInterfaceToken

```TypeScript
readInterfaceToken(): string
```

从MessageParcel中读取接口描述符，接口描述符按写入MessageParcel的顺序读取，本地对象可使用该信息检验本次通信。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#readinterfacetoken)()

<!--Device-MessageParcel-readInterfaceToken(): string--><!--Device-MessageParcel-readInterfaceToken(): string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回读取到的接口描述符。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  let interfaceToken = data.readInterfaceToken();
  hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readLong

```TypeScript
readLong(): number
```

从MessageParcel实例中读取长整数值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readLong](arkts-ipc-rpc-messagesequence-c.md#readlong)()

<!--Device-MessageParcel-readLong(): number--><!--Device-MessageParcel-readLong(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回长整数值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
  let ret = data.readLong();
  hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readLongArray

```TypeScript
readLongArray(dataIn: number[]): void
```

从MessageParcel实例中读取长整数数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)(dataIn:

<!--Device-MessageParcel-readLongArray(dataIn: number[]): void--><!--Device-MessageParcel-readLongArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的长整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readLongArray(array);
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readLongArray

```TypeScript
readLongArray(): number[]
```

从MessageParcel实例中读取长整数数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)()

<!--Device-MessageParcel-readLongArray(): number[]--><!--Device-MessageParcel-readLongArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回长整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array = data.readLongArray();
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readRawData

```TypeScript
readRawData(size: number): number[]
```

从MessageParcel读取原始数据。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#readrawdatabuffer)(size:

<!--Device-MessageParcel-readRawData(size: number): number[]--><!--Device-MessageParcel-readRawData(size: number): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | 要读取的原始数据的大小，以字节为单位。 |

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回原始数据（以字节为单位）。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = [1, 2, 3, 4, 5];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
  let result = parcel.readRawData(5);
  hilog.info(0x0000, 'testTag', 'parcel read raw data result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readRemoteObject

```TypeScript
readRemoteObject(): IRemoteObject
```

从MessageParcel读取远程对象。此方法用于反序列化MessageParcel对象以生成IRemoteObject。远程对象按写入MessageParcel的顺序读取。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readRemoteObject](arkts-ipc-rpc-messagesequence-c.md#readremoteobject)()

<!--Device-MessageParcel-readRemoteObject(): IRemoteObject--><!--Device-MessageParcel-readRemoteObject(): IRemoteObject-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 读取到的远程对象，用于IPC/RPC通信。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
  let proxy = data.readRemoteObject();
  hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(objects: IRemoteObject[]): void
```

从MessageParcel读取IRemoteObject对象数组，并将其写入到创建的空数组中。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects:

<!--Device-MessageParcel-readRemoteObjectArray(objects: IRemoteObject[]): void--><!--Device-MessageParcel-readRemoteObjectArray(objects: IRemoteObject[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| objects | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes | 从MessageParcel读取的IRemoteObject对象数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  data.writeRemoteObjectArray(a);
  let b: Array<rpc.IRemoteObject> = new Array(3);
  data.readRemoteObjectArray(b);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(): IRemoteObject[]
```

从MessageParcel读取IRemoteObject对象数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects:

<!--Device-MessageParcel-readRemoteObjectArray(): IRemoteObject[]--><!--Device-MessageParcel-readRemoteObjectArray(): IRemoteObject[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | 返回IRemoteObject对象数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + result);
  let b = data.readRemoteObjectArray();
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readSequenceable

```TypeScript
readSequenceable(dataIn: Sequenceable): boolean
```

从MessageParcel实例中读取成员变量到指定的对象（dataIn）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readParcelable](arkts-ipc-rpc-messagesequence-c.md#readparcelable)(dataIn:

<!--Device-MessageParcel-readSequenceable(dataIn: Sequenceable): boolean--><!--Device-MessageParcel-readSequenceable(dataIn: Sequenceable): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | Yes | 需要从MessageParcel读取成员变量的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：反序列化成功，false：反序列化失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readSequenceableArray

```TypeScript
readSequenceableArray(sequenceableArray: Sequenceable[]): void
```

从MessageParcel实例中读取可序列化对象数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readParcelableArray](arkts-ipc-rpc-messagesequence-c.md#readparcelablearray)(parcelableArray:

<!--Device-MessageParcel-readSequenceableArray(sequenceableArray: Sequenceable[]): void--><!--Device-MessageParcel-readSequenceableArray(sequenceableArray: Sequenceable[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | Yes | 要读取的可序列化对象数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = [sequenceable, sequenceable2, sequenceable3];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
  let b = [new MySequenceable(0, ""), new MySequenceable(0, ""), new MySequenceable(0, "")];
  data.readSequenceableArray(b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readShort

```TypeScript
readShort(): number
```

从MessageParcel实例中读取短整数值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readShort](arkts-ipc-rpc-messagesequence-c.md#readshort)()

<!--Device-MessageParcel-readShort(): number--><!--Device-MessageParcel-readShort(): number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回短整数值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
  let ret = data.readShort();
  hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readShortArray

```TypeScript
readShortArray(dataIn: number[]): void
```

从MessageParcel实例中读取短整数数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)(dataIn:

<!--Device-MessageParcel-readShortArray(dataIn: number[]): void--><!--Device-MessageParcel-readShortArray(dataIn: number[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | number[] | Yes | 要读取的短整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readShortArray(array);
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readShortArray

```TypeScript
readShortArray(): number[]
```

从MessageParcel实例中读取短整数数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)()

<!--Device-MessageParcel-readShortArray(): number[]--><!--Device-MessageParcel-readShortArray(): number[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| number[] | 返回短整数数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array = data.readShortArray();
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readString

```TypeScript
readString(): string
```

从MessageParcel实例中读取字符串值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readString](arkts-ipc-rpc-messagesequence-c.md#readstring)()

<!--Device-MessageParcel-readString(): string--><!--Device-MessageParcel-readString(): string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回字符串值。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
  let ret = data.readString();
  hilog.info(0x0000, 'testTag', 'readString is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readStringArray

```TypeScript
readStringArray(dataIn: string[]): void
```

从MessageParcel实例中读取字符串数组，并将其写入到创建的空数组中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)(dataIn:

<!--Device-MessageParcel-readStringArray(dataIn: string[]): void--><!--Device-MessageParcel-readStringArray(dataIn: string[]): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataIn | string[] | Yes | 要读取的字符串数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array: Array<string> = new Array(2);
  data.readStringArray(array);
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## readStringArray

```TypeScript
readStringArray(): string[]
```

从MessageParcel实例中读取字符串数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)()

<!--Device-MessageParcel-readStringArray(): string[]--><!--Device-MessageParcel-readStringArray(): string[]-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回字符串数组。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array = data.readStringArray();
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## reclaim

```TypeScript
reclaim(): void
```

释放不再使用的MessageParcel对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#reclaim](arkts-ipc-rpc-messagesequence-c.md#reclaim)()

<!--Device-MessageParcel-reclaim(): void--><!--Device-MessageParcel-reclaim(): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let reply = rpc.MessageParcel.create();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## rewindRead

```TypeScript
rewindRead(pos: number): boolean
```

重新偏移读取位置到指定的位置。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#rewindRead](arkts-ipc-rpc-messagesequence-c.md#rewindread)(pos:

<!--Device-MessageParcel-rewindRead(pos: number): boolean--><!--Device-MessageParcel-rewindRead(pos: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | number | Yes | 开始读取数据的目标位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：读取位置发生更改，false：读取位置未发生更改。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(12);
  data.writeString("parcel");
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'number is ' + number);
  data.rewindRead(0);
  let number2 = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## rewindWrite

```TypeScript
rewindWrite(pos: number): boolean
```

重新偏移写位置到指定的位置。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#rewindWrite](arkts-ipc-rpc-messagesequence-c.md#rewindwrite)(pos:

<!--Device-MessageParcel-rewindWrite(pos: number): boolean--><!--Device-MessageParcel-rewindWrite(pos: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | number | Yes | 开始写入数据的目标位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入位置发生更改，false：写入位置未发生更改。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(4);
  data.rewindWrite(0);
  data.writeInt(5);
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindWrite is ' + number);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## setCapacity

```TypeScript
setCapacity(size: number): boolean
```

设置MessageParcel实例的存储容量。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#setCapacity](arkts-ipc-rpc-messagesequence-c.md#setcapacity)(size:

<!--Device-MessageParcel-setCapacity(size: number): boolean--><!--Device-MessageParcel-setCapacity(size: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | MessageParcel实例的存储容量。以字节为单位。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.setCapacity(100);
  hilog.info(0x0000, 'testTag', 'setCapacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## setSize

```TypeScript
setSize(size: number): boolean
```

设置MessageParcel实例中包含的数据大小。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#setSize](arkts-ipc-rpc-messagesequence-c.md#setsize)(size:

<!--Device-MessageParcel-setSize(size: number): boolean--><!--Device-MessageParcel-setSize(size: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | MessageParcel实例的数据大小。以字节为单位。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：设置成功，false：设置失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let setSize = data.setSize(16);
  hilog.info(0x0000, 'testTag', 'setSize is ' + setSize);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeAshmem

```TypeScript
writeAshmem(ashmem: Ashmem): boolean
```

将指定的匿名共享对象写入此MessageParcel。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeAshmem](arkts-ipc-rpc-messagesequence-c.md#writeashmem)(ashmem:

<!--Device-MessageParcel-writeAshmem(ashmem: Ashmem): boolean--><!--Device-MessageParcel-writeAshmem(ashmem: Ashmem): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | Yes | 要写入MessageParcel的匿名共享对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeBoolean

```TypeScript
writeBoolean(val: boolean): boolean
```

将布尔值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeBoolean](arkts-ipc-rpc-messagesequence-c.md#writeboolean)(val:

<!--Device-MessageParcel-writeBoolean(val: boolean): boolean--><!--Device-MessageParcel-writeBoolean(val: boolean): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | boolean | Yes | 要写入的布尔值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeBooleanArray

```TypeScript
writeBooleanArray(booleanArray: boolean[]): boolean
```

将布尔数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeBooleanArray](arkts-ipc-rpc-messagesequence-c.md#writebooleanarray)(booleanArray:

<!--Device-MessageParcel-writeBooleanArray(booleanArray: boolean[]): boolean--><!--Device-MessageParcel-writeBooleanArray(booleanArray: boolean[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| booleanArray | boolean[] | Yes | 要写入的布尔数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeByte

```TypeScript
writeByte(val: number): boolean
```

将字节值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeByte](arkts-ipc-rpc-messagesequence-c.md#writebyte)(val:

<!--Device-MessageParcel-writeByte(val: number): boolean--><!--Device-MessageParcel-writeByte(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的字节值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeByteArray

```TypeScript
writeByteArray(byteArray: number[]): boolean
```

将字节数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeByteArray](arkts-ipc-rpc-messagesequence-c.md#writebytearray)(byteArray:

<!--Device-MessageParcel-writeByteArray(byteArray: number[]): boolean--><!--Device-MessageParcel-writeByteArray(byteArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteArray | number[] | Yes | 要写入的字节数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeChar

```TypeScript
writeChar(val: number): boolean
```

将单个字符值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeChar](arkts-ipc-rpc-messagesequence-c.md#writechar)(val:

<!--Device-MessageParcel-writeChar(val: number): boolean--><!--Device-MessageParcel-writeChar(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的单个字符值。取值范围：[0, 65535]，对应Unicode字符编码范围。超出此范围可能导致字符编码异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeCharArray

```TypeScript
writeCharArray(charArray: number[]): boolean
```

将单个字符数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeCharArray](arkts-ipc-rpc-messagesequence-c.md#writechararray)(charArray:

<!--Device-MessageParcel-writeCharArray(charArray: number[]): boolean--><!--Device-MessageParcel-writeCharArray(charArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| charArray | number[] | Yes | 要写入的单个字符数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 88]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeDouble

```TypeScript
writeDouble(val: number): boolean
```

将双精度浮点值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeDouble](arkts-ipc-rpc-messagesequence-c.md#writedouble)(val:

<!--Device-MessageParcel-writeDouble(val: number): boolean--><!--Device-MessageParcel-writeDouble(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的双精度浮点值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeDoubleArray

```TypeScript
writeDoubleArray(doubleArray: number[]): boolean
```

将双精度浮点数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeDoubleArray](arkts-ipc-rpc-messagesequence-c.md#writedoublearray)(doubleArray:

<!--Device-MessageParcel-writeDoubleArray(doubleArray: number[]): boolean--><!--Device-MessageParcel-writeDoubleArray(doubleArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| doubleArray | number[] | Yes | 要写入的双精度浮点数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeFileDescriptor

```TypeScript
writeFileDescriptor(fd: number): boolean
```

写入文件描述符到MessageParcel。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#writefiledescriptor)(fd:

<!--Device-MessageParcel-writeFileDescriptor(fd: number): boolean--><!--Device-MessageParcel-writeFileDescriptor(fd: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 文件描述符。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeFloat

```TypeScript
writeFloat(val: number): boolean
```

将双精度浮点值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeFloat](arkts-ipc-rpc-messagesequence-c.md#writefloat)(val:

<!--Device-MessageParcel-writeFloat(val: number): boolean--><!--Device-MessageParcel-writeFloat(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的双精度浮点值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeFloatArray

```TypeScript
writeFloatArray(floatArray: number[]): boolean
```

将双精度浮点数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeFloatArray](arkts-ipc-rpc-messagesequence-c.md#writefloatarray)(floatArray:

<!--Device-MessageParcel-writeFloatArray(floatArray: number[]): boolean--><!--Device-MessageParcel-writeFloatArray(floatArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| floatArray | number[] | Yes | 要写入的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeInt

```TypeScript
writeInt(val: number): boolean
```

将整数值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeInt](arkts-ipc-rpc-messagesequence-c.md#writeint)(val:

<!--Device-MessageParcel-writeInt(val: number): boolean--><!--Device-MessageParcel-writeInt(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的整数值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeIntArray

```TypeScript
writeIntArray(intArray: number[]): boolean
```

将整数数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeIntArray](arkts-ipc-rpc-messagesequence-c.md#writeintarray)(intArray:

<!--Device-MessageParcel-writeIntArray(intArray: number[]): boolean--><!--Device-MessageParcel-writeIntArray(intArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intArray | number[] | Yes | 要写入的整数数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeInterfaceToken

```TypeScript
writeInterfaceToken(token: string): boolean
```

将接口描述符写入MessageParcel对象，远端对象可使用该信息校验本次通信。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#writeinterfacetoken)(token:

<!--Device-MessageParcel-writeInterfaceToken(token: string): boolean--><!--Device-MessageParcel-writeInterfaceToken(token: string): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | string | Yes | 字符串类型描述符，其长度应小于40960。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  hilog.info(0x0000, 'testTag', 'RpcServer: writeInterfaceToken is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeLong

```TypeScript
writeLong(val: number): boolean
```

将长整数值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeLong](arkts-ipc-rpc-messagesequence-c.md#writelong)(val:

<!--Device-MessageParcel-writeLong(val: number): boolean--><!--Device-MessageParcel-writeLong(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的长整数值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeLongArray

```TypeScript
writeLongArray(longArray: number[]): boolean
```

将长整数数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeLongArray](arkts-ipc-rpc-messagesequence-c.md#writelongarray)(longArray:

<!--Device-MessageParcel-writeLongArray(longArray: number[]): boolean--><!--Device-MessageParcel-writeLongArray(longArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| longArray | number[] | Yes | 要写入的长整数数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeNoException

```TypeScript
writeNoException(): void
```

向MessageParcel写入“指示未发生异常”的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeNoException](arkts-ipc-rpc-messagesequence-c.md#writenoexception)()

<!--Device-MessageParcel-writeNoException(): void--><!--Device-MessageParcel-writeNoException(): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      reply.writeNoException();
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

## writeRawData

```TypeScript
writeRawData(rawData: number[], size: number): boolean
```

将原始数据写入MessageParcel对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#writerawdatabuffer)(rawData:

<!--Device-MessageParcel-writeRawData(rawData: number[], size: number): boolean--><!--Device-MessageParcel-writeRawData(rawData: number[], size: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rawData | number[] | Yes | 要写入的原始数据，大小不能超过128MB。 |
| size | number | Yes | 发送的原始数据大小，以字节为单位。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = [1, 2, 3, 4, 5];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeRemoteObject

```TypeScript
writeRemoteObject(object: IRemoteObject): boolean
```

序列化远程对象并将其写入MessageParcel对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeRemoteObject](arkts-ipc-rpc-messagesequence-c.md#writeremoteobject)(obj:

<!--Device-MessageParcel-writeRemoteObject(object: IRemoteObject): boolean--><!--Device-MessageParcel-writeRemoteObject(object: IRemoteObject): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | Yes | 要序列化并写入MessageParcel的远程对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：操作成功，false：操作失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeRemoteObjectArray

```TypeScript
writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean
```

将IRemoteObject对象数组写入MessageParcel。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#writeremoteobjectarray)(objectArray:

<!--Device-MessageParcel-writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean--><!--Device-MessageParcel-writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| objectArray | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes | 要写入MessageParcel的IRemoteObject对象数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'writeRemoteObjectArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeSequenceable

```TypeScript
writeSequenceable(val: Sequenceable): boolean
```

将自定义序列化对象写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeParcelable](arkts-ipc-rpc-messagesequence-c.md#writeparcelable)(val:

<!--Device-MessageParcel-writeSequenceable(val: Sequenceable): boolean--><!--Device-MessageParcel-writeSequenceable(val: Sequenceable): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | Yes | 要写入的可序列对象。建议实现marshalling和unmarshalling方法时确保数据完整性，序列化与反序列化的数据结构应保持一致。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeSequenceableArray

```TypeScript
writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean
```

将可序列化对象数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeParcelableArray](arkts-ipc-rpc-messagesequence-c.md#writeparcelablearray)(parcelableArray:

<!--Device-MessageParcel-writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean--><!--Device-MessageParcel-writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | Yes | 要写入的可序列化对象数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = [sequenceable, sequenceable2, sequenceable3];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeShort

```TypeScript
writeShort(val: number): boolean
```

将短整数值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeShort](arkts-ipc-rpc-messagesequence-c.md#writeshort)(val:

<!--Device-MessageParcel-writeShort(val: number): boolean--><!--Device-MessageParcel-writeShort(val: number): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | number | Yes | 要写入的短整数值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeShortArray

```TypeScript
writeShortArray(shortArray: number[]): boolean
```

将短整数数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeShortArray](arkts-ipc-rpc-messagesequence-c.md#writeshortarray)(shortArray:

<!--Device-MessageParcel-writeShortArray(shortArray: number[]): boolean--><!--Device-MessageParcel-writeShortArray(shortArray: number[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shortArray | number[] | Yes | 要写入的短整数数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeString

```TypeScript
writeString(val: string): boolean
```

将字符串值写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeString](arkts-ipc-rpc-messagesequence-c.md#writestring)(val:

<!--Device-MessageParcel-writeString(val: string): boolean--><!--Device-MessageParcel-writeString(val: string): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | string | Yes | 要写入的字符串值，其长度应小于40960。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## writeStringArray

```TypeScript
writeStringArray(stringArray: string[]): boolean
```

将字符串数组写入MessageParcel实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.MessageSequence#writeStringArray](arkts-ipc-rpc-messagesequence-c.md#writestringarray)(stringArray:

<!--Device-MessageParcel-writeStringArray(stringArray: string[]): boolean--><!--Device-MessageParcel-writeStringArray(stringArray: string[]): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stringArray | string[] | Yes | 要写入的字符串数组，数组单个元素的长度应小于40960。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：写入成功，false：写入失败。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

