# readLinesSync

## Modules to Import

```TypeScript
import fileIo, { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
```

## readLinesSync

```TypeScript
declare function readLinesSync(filePath: string, options?: Options): ReaderIterator
```

Reads the text content of a file line by line. This API returns the result synchronously.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](arkts-corefile-file-fs-options-i.md) | No | Options for reading the text. The options are as follows:   - **encoding** (string): format of the data to be encoded.   It is valid only when the data is of the string type.The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) | ReaderIterator** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900015 | File exists |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900030 | File name too number |
| 13900033 | Too many symbolic links encountered |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fileIo.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info(`Succeeded in reading lines, content: ${it.value}`);
}
```
