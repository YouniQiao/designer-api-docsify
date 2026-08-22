# readSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: ReadOptions
): number
```

Reads data from a file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number--><!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let buf = new ArrayBuffer(4096);
fs.readSync(file.fd, buf);
fs.closeSync(file);
```

```TypeScript
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fs.closeSync(file);
```

