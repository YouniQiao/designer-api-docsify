# moveDirWithConflictFiles

## Modules to Import

```TypeScript
```

## moveDirWithConflictFiles

```TypeScript
function moveDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,
  Array<ConflictFiles>>): void
```

Moves the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory.

> **NOTE：**&gt;
> This API is not supported in a distributed directory.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function moveDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,  Array<ConflictFiles>>): void--><!--Device-fileIo-function moveDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,  Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |


## moveDirWithConflictFiles

```TypeScript
function moveDirWithConflictFiles(src: string, dest: string, mode: int,
    callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function moveDirWithConflictFiles(src: string, dest: string, mode: int,    callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-fileIo-function moveDirWithConflictFiles(src: string, dest: string, mode: int,    callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | int | Yes | Move mode. The default value is **0**. <br>- **0**: Throw an exception if a directory conflict occurs. <br> An exception will be thrown if the destination directory contains a directory with the same name as the source directory. <br>- **1**: Throw an exception if a file conflict occurs. <br> An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be moved to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;[ConflictFiles](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-conflictfiles-i.md)&gt; format. <br>- **2**: Forcibly overwrite the conflicting files in the destination directory. <br> When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained. <br>- **3**: Forcibly overwrite the conflicting directory. <br> The source directory is moved to the destination directory, and the content of the moved directory is the same as that of the source directory. If the destination directory contains a directory with the same name as the source directory, all original files in the directory will be deleted. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |

