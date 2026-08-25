# FileMapping

File mapping object. Before invoking the FileMapping method, you need to use the mmap() method (synchronous or asynchronous) to construct a FileMapping instance.

**Since:** 26.0.0

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): number
```

Obtains the capacity of the file mapping area.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## flip

```TypeScript
flip(): void
```

Mode reversal. That is, the limit attribute is set to the current position, and then the current position is set to 0.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getLimit

```TypeScript
getLimit(): number
```

Obtains the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getPosition

```TypeScript
getPosition(): number
```

Gets the current location of the file mapping area.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## msync

```TypeScript
msync(): Promise<void>
```

Synchronizes the dirty page data in the entire file mapping area to the disk file and uses the promise asynchronous callback function. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
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

Synchronizes the dirty page data in the specified range of the file mapping area to the disk file and uses the promise asynchronous callback function. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
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

Synchronizes the dirty page data of the entire file mapping area to the disk file by using the synchronization method. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
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

Synchronize the dirty page data in the specified range of the file mapping area to the disk file by using the synchronization method. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |
| length | number | Yes |

**Error codes:**

| Error Code ID |
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

Reads data from the current position and moves the position backward by the number of bytes actually read.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
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

Reads data from the specified location without affecting the current location.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |
| buffer | ArrayBuffer | Yes |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
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

Obtains the number of remaining bytes between the current position (position) and the upper bound (limit) of the readable and writable area.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setLimit

```TypeScript
setLimit(limit: number): void
```

Sets the upper bound of the readable and writable area of the file mapping area. The upper bound does not exceed the total capacity of the mapping area (0 &lt;= limit &lt;= capacity).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| limit | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setPosition

```TypeScript
setPosition(position: number): void
```

Sets the current location of the file mapping area.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## unmap

```TypeScript
unmap(): Promise<void>
```

Releases the file mapping area and use the promise asynchronous callback function.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |

## unmapSync

```TypeScript
unmapSync(): void
```

Releases the file mapping area by using the synchronization method.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |

## write

```TypeScript
write(data: ArrayBuffer, length?: number): number
```

Writes data from the current location and moves the location backward by the number of bytes actually written.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
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

Writes data from the specified location without affecting the current location.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |
| data | ArrayBuffer | Yes |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |
