# query (System API)

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## query

```TypeScript
function query(id: string, callback: AsyncCallback<TaskInfo>): void
```

Queries specified task details. Creates a group based on GroupConfig

**Since:** 10

**Required permissions:** ohos.permission.DOWNLOAD_SESSION_MANAGER or ohos.permission.UPLOAD_SESSION_MANAGER

**System capability:** SystemCapability.Request.FileTransferAgent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | the task id. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | Yes | callback function with a `TaskInfo` argument for informations of the current task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900006](../errorcode-request.md#21900006-task-not-found) | Task removed or not found. |

**Examples**

```TypeScript
downloadTask.query().then((downloadInfo) => {    
  console.info('Succeeded in querying the download task.')
}).catch((err: BusinessError) => {
  console.error(`Failed to query the download task. Code: ${err.code}, message: ${err.message}`)
});
```

```TypeScript
downloadTask.query((err: BusinessError, downloadInfo: request.DownloadInfo)=>{
  if(err) {
    console.error(`Failed to query the download mimeType. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in querying the download task.');
  }
});
```


## query

```TypeScript
function query(id: string): Promise<TaskInfo>
```

Queries specified task details.

**Since:** 10

**Required permissions:** ohos.permission.DOWNLOAD_SESSION_MANAGER or ohos.permission.UPLOAD_SESSION_MANAGER

**System capability:** SystemCapability.Request.FileTransferAgent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | the task id. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TaskInfo&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900006](../errorcode-request.md#21900006-task-not-found) | Task removed or not found. |

**Examples**

See [query](#query)
