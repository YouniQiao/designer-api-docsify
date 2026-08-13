# copyDir

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode?: number): Promise<void>
```

Copies the source directory to the destination path. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | Copy mode. The default value is **0**.&lt;br&gt;- **0**: Throw an exception if a file conflict occurs.&lt;br&gt; An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;[ConflictFiles](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md#ConflictFiles)&gt; format.&lt;br&gt;- **1**: Forcibly overwrite the files with the same name in the destination directory.&lt;br&gt; When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900034 | Operation would block |
| 13900012 | Permission denied |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void
```

Copies the source directory to the destination directory. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900034 | Operation would block |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Copies the source directory to the destination path. This API uses an asynchronous callback to return the result. An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array\&lt;[ConflictFiles](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md#ConflictFiles)&gt; format.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

Copies the source directory to the destination directory. You can set the copy mode. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | Yes | Copy mode. The default value is 0. &lt;br&gt;0: Throw an exception if a file conflict occurs. &lt;br&gt;An exception will be thrown if the destination directory contains a directory with &lt;br&gt;the same name as the source directory, and a file with the same name exists in the conflict directory. &lt;br&gt;All the non-conflicting files in the source directory will be moved &lt;br&gt;to the destination directory, and the non-conflicting files in the destination directory will be retained. &lt;br&gt;The data attribute in the error returned provides information about the &lt;br&gt;conflicting files in the Array&lt;ConflictFiles&gt; format. &lt;br&gt;1: Forcibly overwrite the files with the same name in the destination directory. &lt;br&gt;When the destination directory contains a directory with the same name as the source directory, &lt;br&gt;the files with the same names in the destination directory are overwritten forcibly; &lt;br&gt;the files without conflicts in the destination directory are retained. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900034 | Operation would block |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Copies the source directory to the destination path. You can set the copy mode. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | Yes | Copy mode. The default value is **0**.&lt;br&gt;- **0**: Throw an exception if a file conflict occurs.&lt;br&gt; An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;[ConflictFiles](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md#ConflictFiles)&gt; format.&lt;br&gt;- **1**: Forcibly overwrite the files with the same name in the destination directory.&lt;br&gt; When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](../../apis-na/arkts-apis/arkts-na-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |

