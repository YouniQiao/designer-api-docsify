# FileMapping

Defines a file mapping object. Before calling the **FileMapping** method, construct a **FileMapping** instance using [mmap()](arkts-corefile-fileio-mmap-f.md) or [mmapSync()](arkts-corefile-fileio-mmapsync-f.md).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): int
```

Obtains the capacity of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

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

Flips the file mapping area to switch from the write-ready state to the read-ready state. After this API is called, **limit** is set to the value of **position**, and **position** is reset to **0**.It is recommended that this API be called to prepare for subsequent [read()](arkts-corefile-fileio-stream-i.md#read) operations after the[write()](arkts-corefile-fileio-stream-i.md#write) operations are complete.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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
getLimit(): int
```

Obtains the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## getPosition

```TypeScript
getPosition(): int
```

Gets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

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

Synchronizes data of the entire file mapping area to the disk file synchronously. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the file is not stored on the local device, calling this API does not ensure that all changes are stored
> persistently.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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
msync(position: int, length: int): Promise<void>
```

Synchronizes data in the specified range of the file mapping area to the disk file synchronously. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the file is not stored on the local device, calling this API does not ensure that all changes are stored
> persistently.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | int | Yes |
| length | int | Yes |

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

Synchronizes data of the entire file mapping area to the disk file synchronously.

> **NOTE：**&gt;
> If the file is not stored on the local device, calling this API does not ensure that all changes are stored
> persistently.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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
msyncSync(position: int, length: int): void
```

Synchronizes data in the specified range of the file mapping area to the disk file synchronously.

> **NOTE：**&gt;
> If the file is not stored on the local device, calling this API does not ensure that all changes are stored
> persistently.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | int | Yes |
| length | int | Yes |

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
read(buffer: ArrayBuffer, length?: int): int
```

Reads data from the current position and moves the position backward by the number of bytes actually read.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| length | int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

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
read(position: int, buffer: ArrayBuffer, length?: int): int
```

Reads data from the specified position. The current position does not move.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | int | Yes |
| buffer | ArrayBuffer | Yes |
| length | int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

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
remaining(): int
```

Obtains the number of remaining bytes between the current position (**position**) and the upper bound (**limit**) of the readable and writable area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setLimit

```TypeScript
setLimit(limit: int): void
```

Sets the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| limit | int | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

## setPosition

```TypeScript
setPosition(position: int): void
```

Sets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | int | Yes |

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

Releases the file mapping area. This API uses a promise to return the result. After this API is called, **position**, **limit**, and **capacity** are all reset to **0**, and no operation can be performed on the **FileMapping** object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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

Releases the file mapping area synchronously. After this API is called, **position**, **limit**, and **capacity** are all reset to **0**, and no operation can be performed on the **FileMapping** object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |

## write

```TypeScript
write(data: ArrayBuffer, length?: int): int
```

Writes data from the current position and moves the position backward by the number of bytes actually written.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |
| length | int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

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
write(position: int, data: ArrayBuffer, length?: int): int
```

Writes data to the specified position. The current position does not move.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | int | Yes |
| data | ArrayBuffer | Yes |
| length | int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |
