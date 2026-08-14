# setxattr

## setxattr

```TypeScript
function setxattr(path: string, key: string, value: string): Promise<void>
```

Sets an extended attribute of a file or directory. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function setxattr(path: string, key: string, value: string): Promise<void>--><!--Device-fileIo-function setxattr(path: string, key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| key | string | Yes | Key of the extended attribute to obtain. The value is a string of less than 256 bytes and can contain only the **user.** prefix. |
| value | string | Yes | Value of the extended attribute to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13900038 | Value too large for defined data type |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900031 | Function not implemented |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

