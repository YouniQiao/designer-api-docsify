# rmdirSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## rmdirSync

```TypeScript
declare function rmdirSync(path: string): void
```

Removes a directory and all its subdirectories and files synchronously.

> **NOTE：**&gt;
> This API can be used to remove a single file. However, you are advised to use **unlinkSync** instead.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900018 |
| 13900020 |
| 13900027 |
| 13900030 |
| 13900032 |
| 13900042 |

**Examples**

```TypeScript
let dirPath = pathDir + "/testDir";
fs.rmdirSync(dirPath);
```
