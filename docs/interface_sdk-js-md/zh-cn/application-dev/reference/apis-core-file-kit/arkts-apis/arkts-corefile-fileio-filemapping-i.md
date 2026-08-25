# FileMapping

文件映射对象，在调用FileMapping的方法前，需要先通过[mmap()](arkts-corefile-fileio-mmap-f.md)或方法[mmapSync()](arkts-corefile-fileio-mmapsync-f.md)构建一个FileMapping实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): int
```

获取文件映射区的容量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## flip

```TypeScript
flip(): void
```

翻转文件映射区，将写入准备状态切换为读取准备状态。调用后，limit被设置为当前position的值，position被重置为0。推荐在一系列 [write()](arkts-corefile-fileio-stream-i.md#write) 操作完成后，调用此方法准备后续的 [read()](arkts-corefile-fileio-stream-i.md#read) 操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getLimit

```TypeScript
getLimit(): int
```

获取文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getPosition

```TypeScript
getPosition(): int
```

获取文件映射区的当前位置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## msync

```TypeScript
msync(): Promise<void>
```

将整个文件映射区的数据同步到磁盘文件。使用Promise异步回调。

> **说明：**&gt;
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

## msync

```TypeScript
msync(position: int, length: int): Promise<void>
```

将文件映射区指定范围内的数据同步到磁盘文件。使用Promise异步回调。

> **说明：**&gt;
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | int | 是 |
| length | int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

## msyncSync

```TypeScript
msyncSync(): void
```

以同步方法将整个文件映射区的数据同步到磁盘文件。

> **说明：**&gt;
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

## msyncSync

```TypeScript
msyncSync(position: int, length: int): void
```

以同步方法将文件映射区指定范围内的数据同步到磁盘文件。

> **说明：**&gt;
> 如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | int | 是 |
| length | int | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

## read

```TypeScript
read(buffer: ArrayBuffer, length?: int): int
```

从当前位置读取数据，并将位置后移实际读取的字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| length | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900054 |

## read

```TypeScript
read(position: int, buffer: ArrayBuffer, length?: int): int
```

从指定位置读取数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | int | 是 |
| buffer | ArrayBuffer | 是 |
| length | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900054 |

## remaining

```TypeScript
remaining(): int
```

获取从当前位置（position）到可读写区域的上界（limit）之间的剩余字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setLimit

```TypeScript
setLimit(limit: int): void
```

设置文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| limit | int | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setPosition

```TypeScript
setPosition(position: int): void
```

设置文件映射区的当前位置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | int | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## unmap

```TypeScript
unmap(): Promise<void>
```

释放文件映射区。使用Promise异步回调。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |

## unmapSync

```TypeScript
unmapSync(): void
```

以同步方法释放文件映射区。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |

## write

```TypeScript
write(data: ArrayBuffer, length?: int): int
```

从当前位置写入数据，并将位置后移实际写入的字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | ArrayBuffer | 是 |
| length | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |

## write

```TypeScript
write(position: int, data: ArrayBuffer, length?: int): int
```

从指定位置写入数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | int | 是 |
| data | ArrayBuffer | 是 |
| length | int | 否 |

**返回值：**

| 类型 |
| --- |
| int |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |
