# readText

## Modules to Import

```TypeScript
import fileIo, { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
```

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: ReadTextOptions
): Promise<string>
```

Reads the text content of a file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | No | The options are as follows:   - **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.   - **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the file length.   - **encoding** (string): format of the data to be encoded.   It is valid only when the data is of the string type. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;string & gt; | Promise used to return the file content read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath).then((str: string) => {
  console.info(`Succeeded in reading text, text is: ${str}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
});
```


## readText

```TypeScript
declare function readText(filePath: string, callback: AsyncCallback<string>): void
```

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the content read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: ReadTextOptions,
  callback: AsyncCallback<string>
): void
```

Reads the text content of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file. |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | Yes | The options are as follows:   - **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.   - **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the file length.   - **encoding** (string): format of the data to be encoded. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the content read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadTextOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stat = fileIo.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fileIo.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```
