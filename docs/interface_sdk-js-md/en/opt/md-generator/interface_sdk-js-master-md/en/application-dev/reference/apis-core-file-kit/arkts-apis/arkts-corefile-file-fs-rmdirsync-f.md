# rmdirSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## rmdirSync

```TypeScript
declare function rmdirSync(path: string): void
```

Removes a directory and all its subdirectories and files synchronously.

> **NOTE：**
> 
> This API can be used to remove a single file. However, you are advised to use **unlinkSync** instead.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function rmdirSync(path: string): void--><!--Device-unnamed-declare function rmdirSync(path: string): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900032 |
| 13900001 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900030 |
| 13900042 |
| 13900011 |
| 13900027 |
