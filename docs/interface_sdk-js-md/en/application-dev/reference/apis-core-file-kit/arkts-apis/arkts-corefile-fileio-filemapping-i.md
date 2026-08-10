# FileMapping

文件映射对象，在调用FileMapping的方法前，需要先通过[mmap()](arkts-corefile-fileio-mmap-f.md#mmap)或方法[mmapSync()](arkts-corefile-fileio-mmapsync-f.md#mmapsync)构建一个FileMapping实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-fileIo-interface FileMapping--><!--Device-fileIo-interface FileMapping-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): int
```

获取文件映射区的容量。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-capacity(): int--><!--Device-FileMapping-capacity(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | 文件映射区的容量，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## flip

```TypeScript
flip(): void
```

翻转文件映射区，将写入准备状态切换为读取准备状态。调用后，limit被设置为当前position的值，position被重置为0。

推荐在一系列  
[write()](arkts-corefile-fileio-stream-i.md#write)操作完成后，调用此方法准备后续的  
[read()](arkts-corefile-fileio-stream-i.md#read)操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-flip(): void--><!--Device-FileMapping-flip(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## getLimit

```TypeScript
getLimit(): int
```

获取文件映射区可读写区域的上界。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-getLimit(): int--><!--Device-FileMapping-getLimit(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | 当前可读写区域上界值，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## getPosition

```TypeScript
getPosition(): int
```

获取文件映射区的当前位置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-getPosition(): int--><!--Device-FileMapping-getPosition(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | 文件映射区的当前位置，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## msync

```TypeScript
msync(): Promise<void>
```

将整个文件映射区的数据同步到磁盘文件。使用Promise异步回调。

> **说明：**
> 
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(): Promise<void>--><!--Device-FileMapping-msync(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msync

```TypeScript
msync(position: int, length: int): Promise<void>
```

将文件映射区指定范围内的数据同步到磁盘文件。使用Promise异步回调。

> **说明：**
> 
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(position: int, length: int): Promise<void>--><!--Device-FileMapping-msync(position: int, length: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | 期望同步的起始位置，单位为Byte。 |
| length | int | Yes | 期望同步的数据长度，单位为Byte。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msyncSync

```TypeScript
msyncSync(): void
```

以同步方法将整个文件映射区的数据同步到磁盘文件。

> **说明：**
> 
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(): void--><!--Device-FileMapping-msyncSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msyncSync

```TypeScript
msyncSync(position: int, length: int): void
```

以同步方法将文件映射区指定范围内的数据同步到磁盘文件。

> **说明：**
> 
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(position: int, length: int): void--><!--Device-FileMapping-msyncSync(position: int, length: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | 期望同步的起始位置，单位为Byte。 |
| length | int | Yes | 期望同步的数据长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## read

```TypeScript
read(buffer: ArrayBuffer, length?: int): int
```

从当前位置读取数据，并将位置后移实际读取的字节数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | 用于保存读取到的文件数据的缓冲区。 |
| length | int | No | 期望读取数据的长度，单位为Byte。默认缓冲区长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回实际读取的数据长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## read

```TypeScript
read(position: int, buffer: ArrayBuffer, length?: int): int
```

从指定位置读取数据，当前位置不会发生移动。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | 期望读取的起始位置，单位为Byte。 |
| buffer | ArrayBuffer | Yes | 用于保存读取到的文件数据的缓冲区。 |
| length | int | No | 期望读取数据的长度，单位为Byte。默认缓冲区长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回实际读取的数据长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## remaining

```TypeScript
remaining(): int
```

获取从当前位置（position）到可读写区域的上界（limit）之间的剩余字节数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-remaining(): int--><!--Device-FileMapping-remaining(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | 剩余可读或可写的字节数，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## setLimit

```TypeScript
setLimit(limit: int): void
```

设置文件映射区可读写区域的上界。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setLimit(limit: int): void--><!--Device-FileMapping-setLimit(limit: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| limit | int | Yes | 要设置的可读写区域上界值，单位为Byte。 &lt;br&gt;取值需大于等于0，且小于等于当前[capacity](arkts-corefile-fileio-filemapping-i.md#capacity)。若所设值小于文件映射区的当前位置，则当前位置将自动调整至该值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## setPosition

```TypeScript
setPosition(position: int): void
```

设置文件映射区的当前位置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setPosition(position: int): void--><!--Device-FileMapping-setPosition(position: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | 期望设置的目标位置，单位为Byte。 &lt;br&gt;必须为非负数且不大于当前可读写上界的limit，可通过[getLimit()](arkts-corefile-fileio-filemapping-i.md#getlimit)获得可读写上界的limit。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## unmap

```TypeScript
unmap(): Promise<void>
```

释放文件映射区。使用Promise异步回调。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-unmap(): Promise<void>--><!--Device-FileMapping-unmap(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |

## unmapSync

```TypeScript
unmapSync(): void
```

以同步方法释放文件映射区。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-unmapSync(): void--><!--Device-FileMapping-unmapSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |

## write

```TypeScript
write(data: ArrayBuffer, length?: int): int
```

从当前位置写入数据，并将位置后移实际写入的字节数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | 待写入文件的缓冲区数据。 |
| length | int | No | 期望写入数据的长度，单位为Byte。默认缓冲区长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回实际写入的长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## write

```TypeScript
write(position: int, data: ArrayBuffer, length?: int): int
```

从指定位置写入数据，当前位置不会发生移动。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | 期望写入的起始位置，单位为Byte。 |
| data | ArrayBuffer | Yes | 待写入文件的缓冲区数据。 |
| length | int | No | 期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回实际写入的长度，单位为Byte。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

