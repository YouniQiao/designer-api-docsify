# copyDirWithConflictFiles

## copyDirWithConflictFiles

```TypeScript
function copyDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,
  Array<ConflictFiles>>): void
```

Copies the source directory to the destination path. This API uses an asynchronous callback to return the result. An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;ConflictFiles&gt; format.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function copyDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,  Array<ConflictFiles>>): void--><!--Device-fileIo-function copyDirWithConflictFiles(src: string, dest: string, callback: AsyncCallback<void,  Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](arkts-na-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |


## copyDirWithConflictFiles

```TypeScript
function copyDirWithConflictFiles(src: string, dest: string, mode: int,
  callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Copies the source directory to the destination directory. You can set the copy mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function copyDirWithConflictFiles(src: string, dest: string, mode: int,  callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-fileIo-function copyDirWithConflictFiles(src: string, dest: string, mode: int,  callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string | Yes | Application sandbox path of the source directory. |
| dest | string | Yes | Application sandbox path of the destination directory. |
| mode | int | Yes | Copy mode. The default value is **0**. <br>- **0**: Throw an exception if a file conflict occurs. <br> An exception will be thrown if the destination directory contains a directory with the same name as the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. The **data** attribute in the error returned provides information about the conflicting files in the Array&lt;[ConflictFiles](arkts-na-file-fs-conflictfiles-i.md#ConflictFiles)&gt; format. <br>- **1**: Forcibly overwrite the files with the same name in the destination directory. <br> When the destination directory contains a directory with the same name as the source directory, the files with the same names in the destination directory are overwritten forcibly; the files without conflicts in the destination directory are retained. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](arkts-na-file-fs-conflictfiles-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900015 | File exists |

