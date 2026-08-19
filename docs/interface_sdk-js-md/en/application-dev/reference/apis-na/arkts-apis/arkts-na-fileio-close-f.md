# close

## Modules to Import

```TypeScript
```

## close

```TypeScript
function close(file: int | File): Promise<void>
```

Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function close(file: int | File): Promise<void>--><!--Device-fileIo-function close(file: int | File): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | int \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | File** object or FD of the file to close. After the function is disabled, the **File** object or FD cannot be used for read and write operations. If the file object or file descriptor is still used, an error may occur or the operation may fail. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |


## close

```TypeScript
function close(file: int | File, callback: AsyncCallback<void>): void
```

Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function close(file: int | File, callback: AsyncCallback<void>): void--><!--Device-fileIo-function close(file: int | File, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | int \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | File** object or FD of the file to close. After the function is disabled, the **File** object or FD cannot be used for read and write operations. If the file object or file descriptor is still used, an error may occur or the operation may fail. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. When the file or directory is successfully closed asynchronously, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

