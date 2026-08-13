# lstatSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## lstatSync

```TypeScript
declare function lstatSync(path: string): Stat
```

Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function lstatSync(path: string): Stat--><!--Device-unnamed-declare function lstatSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stat](arkts-corefile-file-fs-stat-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |
