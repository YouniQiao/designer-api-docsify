# request

The **request** module provides applications with basic upload, download, and background transmission agent capabilities. - Currently, the **request** module cannot be called in extensions.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace request--><!--Device-unnamed-declare namespace request-End-->

**System capability:** 
- API version 10 and later: SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [agent](arkts-basicservices-request-agent-n.md) | The request agent api. Supports "background" and "frontend" tasks as while. Though "background" and "frontend" here do not the same with process's concept. All tasks will be executed at request manager service and recorded. Background tasks is for concurrent transfer, such as caching videos for a later play. Frontend tasks is for instant transfer, such as submitting forms for a consumption bill. Background tasks use notification to tell user tasks' status information. Frontend tasks use callback to tell caller tasks' status information. Background has some automatically restore mechanism. Frontend tasks controlled by caller. Uses `multipart/form-data` in client request for upload. A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download. More details, please see the architecture documents of the request subsystem. Only front-end mode is supported in cross-platform scenarios. |

### Functions

| Name | Description |
| --- | --- |
| [download](arkts-basicservices-request-download-f.md#download) | Downloads a file. This API uses an asynchronous callback to return the result. |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) | Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use on('complete'\|'pause'\|'remove') to obtain the download task state, including task completion, pause, and removal. You can also use on('fail') to obtain the task download error information. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > . |
| [download](arkts-basicservices-request-download-f.md#download) | Downloads a file. This API uses a promise to return the result. |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) | Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use on('complete'\|'pause'\|'remove') to obtain the download task state, including task completion, pause, and removal. You can also use on('fail') to obtain the task download error information. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > . |
| [upload](arkts-basicservices-request-upload-f.md#upload) | Uploads a file. This API uses an asynchronous callback to return the result. |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) | Uploads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use [on('complete'\|'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) to obtain the upload success or error information. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > . |
| [upload](arkts-basicservices-request-upload-f.md#upload) | Uploads a file. This API uses a promise to return the result. |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) | Uploads a file. This API uses a promise to return the result. HTTP is supported. You can use [on('complete'\|'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) to obtain the upload success or error information. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > . |

### Interfaces

| Name | Description |
| --- | --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | Defines the download task configuration. |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) | Defines the download task information, which is the callback parameter of the [getTaskInfo](arkts-basicservices-request-downloadtask-i.md#getTaskInfo) API. |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) | Implements file downloads. Before using any APIs of this class, you must obtain a **DownloadTask** object, from a promise through [request.downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) or from a callback through [request.downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) . |
| [File](arkts-basicservices-request-file-i.md) | Describes the list of files in [UploadConfig](arkts-basicservices-request-uploadconfig-i.md#UploadConfig). |
| [RequestData](arkts-basicservices-request-requestdata-i.md) | Describes the form data in [UploadConfig](arkts-basicservices-request-uploadconfig-i.md#UploadConfig). |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | Describes the configuration of an upload task. |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | Upload task information, which is the callback parameter of the [on('complete' \| 'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) and [off('complete' \| 'fail')](arkts-basicservices-request-uploadtask-i.md#off_progress) APIs. |
| [UploadTask](arkts-basicservices-request-uploadtask-i.md) | Implements file uploads. Before using any APIs of this class, you must obtain an **UploadTask** object, from a promise through [request.uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) or from a callback through [request.uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) . |

### Types

| Name | Description |
| --- | --- |
| [DownloadProgressCallback](arkts-basicservices-request-downloadprogresscallback-t.md) | The callback function for the download progress event. |
| [DownloadCompleteCallback](arkts-basicservices-request-downloadcompletecallback-t.md) | The callback function for the download complete event. |
| [DownloadPauseCallback](arkts-basicservices-request-downloadpausecallback-t.md) | The callback function for the download pause event. |
| [DownloadRemoveCallback](arkts-basicservices-request-downloadremovecallback-t.md) | The callback function for the download remove event. |
| [DownloadFailCallback](arkts-basicservices-request-downloadfailcallback-t.md) | The callback function for the download fail event. |
| [UploadProgressCallback](arkts-basicservices-request-uploadprogresscallback-t.md) | The callback function for the download progress event. |
| [UploadHeaderReceiveCallback](arkts-basicservices-request-uploadheaderreceivecallback-t.md) | The callback function for the HTTP Response Header event. |

### Constants

| Name | Description |
| --- | --- |
| [EXCEPTION_PERMISSION](arkts-basicservices-request-con.md#EXCEPTION_PERMISSION) | (Universal error codes) Permission verification failed. |
| [EXCEPTION_PARAMCHECK](arkts-basicservices-request-con.md#EXCEPTION_PARAMCHECK) | (Universal error codes) Parameter check failed. |
| [EXCEPTION_UNSUPPORTED](arkts-basicservices-request-con.md#EXCEPTION_UNSUPPORTED) | (Universal error codes) The device does not support this API. |
| [EXCEPTION_FILEIO](arkts-basicservices-request-con.md#EXCEPTION_FILEIO) | (Specific error codes) Abnormal file operation. |
| [EXCEPTION_FILEPATH](arkts-basicservices-request-con.md#EXCEPTION_FILEPATH) | (Specific error codes) Abnormal file path. |
| [EXCEPTION_SERVICE](arkts-basicservices-request-con.md#EXCEPTION_SERVICE) | (Specific error codes) Abnormal service. |
| [EXCEPTION_OTHERS](arkts-basicservices-request-con.md#EXCEPTION_OTHERS) | (Specific error codes) Other errors. |
| [NETWORK_MOBILE](arkts-basicservices-request-con.md#NETWORK_MOBILE) | (Network type) Bit flag download allowed on a mobile network. |
| [NETWORK_WIFI](arkts-basicservices-request-con.md#NETWORK_WIFI) | (Network type) Bit flag download allowed on a WLAN. |
| [ERROR_CANNOT_RESUME](arkts-basicservices-request-con.md#ERROR_CANNOT_RESUME) | (Download error codes) Failure to resume the download due to network errors. |
| [ERROR_DEVICE_NOT_FOUND](arkts-basicservices-request-con.md#ERROR_DEVICE_NOT_FOUND) | (Download error codes) Failure to find a storage device such as a memory card. |
| [ERROR_FILE_ALREADY_EXISTS](arkts-basicservices-request-con.md#ERROR_FILE_ALREADY_EXISTS) | (Download error codes) Failure to download the file because it already exists. |
| [ERROR_FILE_ERROR](arkts-basicservices-request-con.md#ERROR_FILE_ERROR) | (Download error codes) File operation failed. |
| [ERROR_HTTP_DATA_ERROR](arkts-basicservices-request-con.md#ERROR_HTTP_DATA_ERROR) | (Download error codes) HTTP transmission failed. |
| [ERROR_INSUFFICIENT_SPACE](arkts-basicservices-request-con.md#ERROR_INSUFFICIENT_SPACE) | (Download error codes) Insufficient storage space. |
| [ERROR_TOO_MANY_REDIRECTS](arkts-basicservices-request-con.md#ERROR_TOO_MANY_REDIRECTS) | (Download error codes) Error caused by too many network redirections. |
| [ERROR_UNHANDLED_HTTP_CODE](arkts-basicservices-request-con.md#ERROR_UNHANDLED_HTTP_CODE) | (Download error codes) Unidentified HTTP code. |
| [ERROR_UNKNOWN](arkts-basicservices-request-con.md#ERROR_UNKNOWN) | (Download error codes) Unknown error. In API version 12 or earlier, only serial connection to the IP addresses associated with the specified domain name is supported, and the connection time for a single IP address is not controllable. If the first IP address returned by the DNS is blocked, a handshake timeout may occur, leading to an ERROR_UNKNOWN error. |
| [ERROR_OFFLINE](arkts-basicservices-request-con.md#ERROR_OFFLINE) | (Download error codes) No network connection. |
| [ERROR_UNSUPPORTED_NETWORK_TYPE](arkts-basicservices-request-con.md#ERROR_UNSUPPORTED_NETWORK_TYPE) | (Download error codes) Network type mismatch. |
| [PAUSED_QUEUED_FOR_WIFI](arkts-basicservices-request-con.md#PAUSED_QUEUED_FOR_WIFI) | (Causes of download pause) Download paused and queuing for a WLAN connection because the file size exceeds the maximum value allowed for a mobile network session. |
| [PAUSED_WAITING_FOR_NETWORK](arkts-basicservices-request-con.md#PAUSED_WAITING_FOR_NETWORK) | (Causes of download pause) Download paused due to a network connection problem. Example: network disconnection |
| [PAUSED_WAITING_TO_RETRY](arkts-basicservices-request-con.md#PAUSED_WAITING_TO_RETRY) | (Causes of download pause) Download paused due to network error and then retried. |
| [PAUSED_BY_USER](arkts-basicservices-request-con.md#PAUSED_BY_USER) | (Causes of download pause) The user paused the session. |
| [PAUSED_UNKNOWN](arkts-basicservices-request-con.md#PAUSED_UNKNOWN) | (Causes of download pause) Download paused due to unknown reasons. |
| [SESSION_SUCCESSFUL](arkts-basicservices-request-con.md#SESSION_SUCCESSFUL) | (Download task status codes) Successful download. |
| [SESSION_RUNNING](arkts-basicservices-request-con.md#SESSION_RUNNING) | (Download task status codes) Download in progress. |
| [SESSION_PENDING](arkts-basicservices-request-con.md#SESSION_PENDING) | (Download task status codes) Download pending. |
| [SESSION_PAUSED](arkts-basicservices-request-con.md#SESSION_PAUSED) | (Download task status codes) Download paused. |
| [SESSION_FAILED](arkts-basicservices-request-con.md#SESSION_FAILED) | (Download task status codes) Download failure without retry. |

