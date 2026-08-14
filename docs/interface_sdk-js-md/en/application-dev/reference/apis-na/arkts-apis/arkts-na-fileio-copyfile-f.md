# copyFile

## copyFile

```TypeScript
function copyFile(src: string | int, dest: string | int, mode?: int): Promise<void>
```

Copies a file. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function copyFile(src: string | int, dest: string | int, mode?: int): Promise<void>--><!--Device-fileIo-function copyFile(src: string | int, dest: string | int, mode?: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| int | Yes | Path or FD of the file to copy. |
| dest | string \| int | Yes | Destination path of the file or FD of the file created. |
| mode | int | No | Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported. <br>**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |

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
| 13900044 | Network is unreachable |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## copyFile

```TypeScript
function copyFile(src: string | int, dest: string | int, callback: AsyncCallback<void>): void
```

Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function copyFile(src: string | int, dest: string | int, callback: AsyncCallback<void>): void--><!--Device-fileIo-function copyFile(src: string | int, dest: string | int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| int | Yes | Path or FD of the file to copy. |
| dest | string \| int | Yes | Destination path of the file or FD of the file created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file is successfully copied, **err** is **undefined**; otherwise, **err** is an error object. |

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


## copyFile

```TypeScript
function copyFile(
  src: string | int,
  dest: string | int,
  mode: int,
  callback: AsyncCallback<void>
): void
```

Copies a file with the specified mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function copyFile(  src: string | int,  dest: string | int,  mode: int,  callback: AsyncCallback<void>): void--><!--Device-fileIo-function copyFile(  src: string | int,  dest: string | int,  mode: int,  callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| int | Yes | Path or FD of the file to copy. |
| dest | string \| int | Yes | Destination path of the file or FD of the file created. |
| mode | int | Yes | Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported. <br>**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file is successfully copied, **err** is **undefined**; otherwise, **err** is an error object. |

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

