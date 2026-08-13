# lstat

## lstat

```TypeScript
function lstat(path: string): Promise<Stat>
```

Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function lstat(path: string): Promise<Stat>--><!--Device-fileIo-function lstat(path: string): Promise<Stat>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of the file. &lt;br&gt;**Note：**: URIs can be passed since API version 22. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md)&gt; | Promise used to return the **Stat** object. For details, see **Stat**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900030 | File name too long |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## lstat

```TypeScript
function lstat(path: string, callback: AsyncCallback<Stat>): void
```

Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function lstat(path: string, callback: AsyncCallback<Stat>): void--><!--Device-fileIo-function lstat(path: string, callback: AsyncCallback<Stat>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of the file. &lt;br&gt;**Note：**: URIs can be passed since API version 22. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md)&gt; | Yes | Callback used to return the **Stat** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900030 | File name too long |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

