# mkdtempSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## mkdtempSync

```TypeScript
declare function mkdtempSync(prefix: string): string
```

Creates a temporary directory. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function mkdtempSync(prefix: string): string--><!--Device-unnamed-declare function mkdtempSync(prefix: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900018 |
| 13900028 |
| 13900030 |
| 13900025 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
