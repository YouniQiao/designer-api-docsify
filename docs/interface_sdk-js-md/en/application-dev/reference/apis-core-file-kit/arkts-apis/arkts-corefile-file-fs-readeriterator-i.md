# ReaderIterator

Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-declare interface ReaderIterator--><!--Device-unnamed-declare interface ReaderIterator-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
```

## next

```TypeScript
next(): ReaderIteratorResult
```

Obtains the **ReaderIterator** result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

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

