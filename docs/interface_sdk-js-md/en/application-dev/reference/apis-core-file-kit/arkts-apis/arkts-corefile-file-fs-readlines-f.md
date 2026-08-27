# readLines

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
```

## readLines

```TypeScript
declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8 format are supported.

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
| Promise&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | Promise used to return a **ReaderIterator** object. |

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
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info(`Succeeded in reading lines, content: ${it.value}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
});
```


## readLines

```TypeScript
declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes | Callback used to return a **ReaderIterator** object. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readLines(filePath, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
  if (err) {
    console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info(`Succeeded in reading lines, content: ${it.value}`);
    }
  }
});
```


## readLines

```TypeScript
declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [Options](arkts-corefile-file-fs-options-i.md) | Yes | Options for reading the text. The options are as follows:   - **encoding** (string): format of the data to be encoded.   It is valid only when the data is of the string type.The default value is **'utf-8'**, which is the only value supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes | Callback used to return a **ReaderIterator** object. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
  if (err) {
    console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info(`Succeeded in reading lines, content: ${it.value}`);
    }
  }
});
```
