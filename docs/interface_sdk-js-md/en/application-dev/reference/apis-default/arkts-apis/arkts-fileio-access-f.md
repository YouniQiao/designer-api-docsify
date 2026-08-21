# access

## Modules to Import

```TypeScript
```

## access

```TypeScript
function access(path: string, mode?: AccessModeType): Promise<boolean>
```

Checks whether a file or directory exists or has the operation permission. This API uses a promise to return the result.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function access(path: string, mode?: AccessModeType): Promise<boolean>--><!--Device-fileIo-function access(path: string, mode?: AccessModeType): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode | [AccessModeType](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-accessmodetype-e.md) | No | Permission on the file or directory to check. If this parameter is left blank, the system checks whether the file exists. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the file or directory exists; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900023 | Text file busy |
| 13900030 | File name too long |
| 13900033 | Too many symbolic links encountered |
| 13900042 | Unknown error |


## access

```TypeScript
function access(path: string, callback: AsyncCallback<boolean>): void
```

Checks whether a file or directory exists. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function access(path: string, callback: AsyncCallback<boolean>): void--><!--Device-fileIo-function access(path: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the file exists; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900023 | Text file busy |
| 13900030 | File name too long |
| 13900033 | Too many symbolic links encountered |
| 13900042 | Unknown error |


## access

```TypeScript
function access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>
```

Checks whether the file or directory is on the local host or verifies the operation permission. This API uses a promise to return the result.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>--><!--Device-fileIo-function access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode | [AccessModeType](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-accessmodetype-e.md) | Yes | Permission on the file or directory to check. |
| flag | [AccessFlagType](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-accessflagtype-e.md) | Yes | Position of the file or directory to check. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the file or directory is a local one and has the related permission. The value **false** means the file or directory does not exist or is on the cloud or a distributed device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13900005 | I/O error |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |
| 13900023 | Text file busy |
| 13900030 | File name too long |
| 13900033 | Too many symbolic links encountered |

