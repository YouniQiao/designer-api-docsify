# ReaderIterator

Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface ReaderIterator--><!--Device-unnamed-declare interface ReaderIterator-End-->

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, Options } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fs.readLines(filePath, options).then((readerIterator: fs.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info("content: " + it.value);
  }
}).catch((err: BusinessError) => {
  console.error("readLines failed with error message: " + err.message + ", error code: " + err.code);
});
```

