# mkdtemp

## Modules to Import

```TypeScript
```

## mkdtemp

```TypeScript
function mkdtemp(prefix: string): Promise<string>
```

Create a temporary directory. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function mkdtemp(prefix: string): Promise<string>--><!--Device-fileIo-function mkdtemp(prefix: string): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the unique directory generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900028 | Too many links |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900001 | Operation not permitted |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## mkdtemp

```TypeScript
function mkdtemp(prefix: string, callback: AsyncCallback<string>): void
```

Create a temporary directory. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function mkdtemp(prefix: string, callback: AsyncCallback<string>): void--><!--Device-fileIo-function mkdtemp(prefix: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;string&gt; | Yes | Callback used to return the temporary directory. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900028 | Too many links |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900001 | Operation not permitted |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

