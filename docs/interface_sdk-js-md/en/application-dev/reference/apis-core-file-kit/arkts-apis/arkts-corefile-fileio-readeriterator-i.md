# ReaderIterator

Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-interface ReaderIterator--><!--Device-fileIo-interface ReaderIterator-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## next

```TypeScript
next(): ReaderIteratorResult
```

Obtains the **ReaderIterator** result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReaderIterator-next(): ReaderIteratorResult--><!--Device-ReaderIterator-next(): ReaderIteratorResult-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [ReaderIteratorResult](arkts-corefile-file-fs-readeriteratorresult-i.md) | ReaderIteratorResult** object obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900037 | No data available |
| 13900042 | Unknown error |

