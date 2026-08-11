# File

Represents a **File** object opened by **open()**. It contains the FD and provides capabilities such as locking a file and obtaining the parent directory.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-interface File--><!--Device-fileIo-interface File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## getParent

```TypeScript
getParent(): string
```

Obtains the parent directory of this file object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

## lock

```TypeScript
lock(exclusive?: boolean): Promise<void>
```

Applies an exclusive lock or a shared lock on a file in blocking mode. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-lock(exclusive?: boolean): Promise<void>--><!--Device-File-lock(exclusive?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | No | Lock to apply. &lt;br&gt; The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |

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

## lock

```TypeScript
lock(callback: AsyncCallback<void>): void
```

Applies a shared lock on a file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-lock(callback: AsyncCallback<void>): void--><!--Device-File-lock(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file is locked successfully, **err** is **undefined**. Otherwise, **err** is an error object. |

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

Applies an exclusive lock or a shared lock on a file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void--><!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | Yes | Whether to apply an exclusive lock. The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file is locked successfully, **err** is **undefined**. Otherwise, **err** is an error object. |

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-tryLock(exclusive?: boolean): void--><!--Device-File-tryLock(exclusive?: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclusive | boolean | No | Lock to apply. &lt;br&gt; The value **true** means an exclusive lock, and the value **false** (default) means a shared lock. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900043 | No record locks available |

## unlock

```TypeScript
unlock(): void
```

Unlocks a file. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

## fd

```TypeScript
readonly fd: int
```

FD of the file.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-readonly fd: int--><!--Device-File-readonly fd: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## name

```TypeScript
readonly name: string
```

Name of the file.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-readonly name: string--><!--Device-File-readonly name: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-File-readonly path: string--><!--Device-File-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

