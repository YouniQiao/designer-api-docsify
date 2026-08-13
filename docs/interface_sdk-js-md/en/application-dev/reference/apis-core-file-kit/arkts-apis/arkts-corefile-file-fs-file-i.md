# File

Represents a **File** object opened by **open()**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-unnamed-declare interface File--><!--Device-unnamed-declare interface File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## getParent

```TypeScript
getParent(): string
```

Obtains the parent directory of this file object.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-File-getParent(): string--><!--Device-File-getParent(): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| string | Parent directory obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 14300002 | Invalid URI |
| 13900042 | Unknown error |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
console.info('The parent path is: ' + file.getParent());
fs.closeSync(file);
```

## lock

```TypeScript
lock(exclusive?: boolean): Promise<void>
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-File-lock(exclusive?: boolean): Promise<void>--><!--Device-File-lock(exclusive?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | No | Lock to apply.&lt;br&gt; The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info("lock file succeed");
}).catch((err: BusinessError) => {
  console.error("lock file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

## lock

```TypeScript
lock(callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-File-lock(callback: AsyncCallback<void>): void--><!--Device-File-lock(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## lock

```TypeScript
lock(exclusive: boolean, callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void--><!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | Yes | Lock to apply.&lt;br&gt; The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## tryLock

```TypeScript
tryLock(exclusive?: boolean): void
```

Applies an exclusive lock or a shared lock on this file in non-blocking mode.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-File-tryLock(exclusive?: boolean): void--><!--Device-File-tryLock(exclusive?: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | No | Lock to apply.&lt;br&gt; The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
console.info("lock file succeed");
fs.closeSync(file);
```

## unlock

```TypeScript
unlock(): void
```

Unlocks a file. This API returns the result synchronously.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-File-unlock(): void--><!--Device-File-unlock(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info("unlock file succeed");
fs.closeSync(file);
```

## fd

```TypeScript
readonly fd: number
```

FD of the file.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-readonly fd: number--><!--Device-File-readonly fd: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## name

```TypeScript
readonly name: string
```

Name of the file.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-File-readonly name: string--><!--Device-File-readonly name: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-File-readonly path: string--><!--Device-File-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

