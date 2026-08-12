# lseek

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## lseek

```TypeScript
declare function lseek(fd: number, offset: number, whence?: WhenceType): number
```

Adjusts the position of the file offset pointer.

**Since:** 11

<!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number--><!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| offset | number | Yes |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900038 |
| 13900008 |
| 13900026 |
| 13900042 |
