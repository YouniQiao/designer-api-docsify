# moveDirSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## moveDirSync

```TypeScript
declare function moveDirSync(src: string, dest: string, mode?: number): void
```

Moves the source directory to the destination directory. This API returns the result synchronously.

> **NOTE：**
> 
> This API is not supported in a distributed directory.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare function moveDirSync(src: string, dest: string, mode?: number): void--><!--Device-unnamed-declare function moveDirSync(src: string, dest: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | number | No | Move mode. The default value is **0**.&lt;br&gt;- **0**: Throw an exception if a directory conflict occurs.&lt;br&gt; An exception will be thrown if the destination directory contains a directory with the same name as the source directory.&lt;br&gt;- **1**: Throw an exception if a file conflict occurs.&lt;br&gt; An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt; [ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md)&gt; format.&lt;br&gt;- **2**: Forcibly overwrite the conflicting files in the destination directory.&lt;br&gt; When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained.&lt;br&gt;- **3**: Forcibly overwrite the conflicting directory.&lt;br &gt; The source directory is moved to the destination directory, and the content of the moved directory is the same as that of the source directory. If the destination directory contains a directory with the same name as the source directory, all original files in the directory will be deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900016 | Cross-device link |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900028 | Too many links |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900032 | Directory not empty |
| 13900001 | Operation not permitted |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

