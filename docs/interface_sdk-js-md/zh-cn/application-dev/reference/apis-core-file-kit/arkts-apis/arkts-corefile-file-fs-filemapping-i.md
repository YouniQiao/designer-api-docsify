# FileMapping

文件映射对象，在调用FileMapping的方法前，需要先通过[mmap()](arkts-corefile-file-fs-mmap-f.md)或方法[mmapSync()](arkts-corefile-file-fs-mmapsync-f.md)构建一个FileMapping实例。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): number
```

获取文件映射区的容量。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

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

翻转文件映射区，将写入准备状态切换为读取准备状态。调用后，limit被设置为当前position的值，position被重置为0。推荐在一系列[write()](#write)操作完成后，调用此方法准备后续的[read()](#read)操作。

**起始版本：** 26.0.0

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
getLimit(): number
```

获取文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getPosition

```TypeScript
getPosition(): number
```

获取文件映射区的当前位置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

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

将整个文件映射区的数据同步到磁盘文件。使用Promise异步回调。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

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
msync(position: number, length: number): Promise<void>
```

将文件映射区指定范围内的数据同步到磁盘文件。使用Promise异步回调。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| length | number | 是 |

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

以同步方法将整个文件映射区的数据同步到磁盘文件。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

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
msyncSync(position: number, length: number): void
```

以同步方法将文件映射区指定范围内的数据同步到磁盘文件。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| length | number | 是 |

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
read(buffer: ArrayBuffer, length?: number): number
```

从当前位置读取数据，并将位置后移实际读取的字节数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

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
read(position: number, buffer: ArrayBuffer, length?: number): number
```

从指定位置读取数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| buffer | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

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
remaining(): number
```

获取从当前位置（position）到可读写区域的上界（limit）之间的剩余字节数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setLimit

```TypeScript
setLimit(limit: number): void
```

设置文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| limit | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setPosition

```TypeScript
setPosition(position: number): void
```

设置文件映射区的当前位置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

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

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |

## write

```TypeScript
write(data: ArrayBuffer, length?: number): number
```

从当前位置写入数据，并将位置后移实际写入的字节数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

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
write(position: number, data: ArrayBuffer, length?: number): number
```

从指定位置写入数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| data | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |
