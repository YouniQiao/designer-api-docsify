# stat

## Modules to Import

```TypeScript
```

## stat

```TypeScript
function stat(file: string | int): Promise<Stat>
```

Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function stat(file: string | int): Promise<Stat>--><!--Device-fileIo-function stat(file: string | int): Promise<Stat>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| int | Yes | Application sandbox path, URI, or FD of the file or directory. <br>**Note：**: URIs can be passed since API version 22. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md)&gt; | Promise used to return the file or directory information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900033 | Too many symbolic links encountered |
| 13900038 | Value too large for defined data type |
| 13900042 | Unknown error |


## stat

```TypeScript
function stat(file: string | int, callback: AsyncCallback<Stat>): void
```

Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function stat(file: string | int, callback: AsyncCallback<Stat>): void--><!--Device-fileIo-function stat(file: string | int, callback: AsyncCallback<Stat>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| int | Yes | Application sandbox path, URI, or FD of the file or directory. <br>**Note：**: URIs can be passed since API version 22. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md)&gt; | Yes | Callback used to return the file or directory information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900033 | Too many symbolic links encountered |
| 13900038 | Value too large for defined data type |
| 13900042 | Unknown error |

