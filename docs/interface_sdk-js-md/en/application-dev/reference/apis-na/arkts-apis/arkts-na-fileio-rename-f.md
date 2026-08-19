# rename

## Modules to Import

```TypeScript
```

## rename

```TypeScript
function rename(oldPath: string, newPath: string): Promise<void>
```

Renames a file or directory. This API uses a promise to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function rename(oldPath: string, newPath: string): Promise<void>--><!--Device-fileIo-function rename(oldPath: string, newPath: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldPath | string | Yes | Original application sandbox path of the file or directory. |
| newPath | string | Yes | New application sandbox path of the file or directory. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

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


## rename

```TypeScript
function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void
```

Renames a file or directory. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void--><!--Device-fileIo-function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldPath | string | Yes | Original application sandbox path of the file or directory. |
| newPath | string | Yes | New application sandbox path of the file or directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file is renamed successfully, **err** is **undefined**; otherwise, **err** is an error object. |

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

