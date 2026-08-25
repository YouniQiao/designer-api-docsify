# request(Upload and Download)

The **request** module provides applications with basic upload, download, and background transmission agent capabilities.  
- Currently, the **request** module cannot be called in extensions.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** 
- API version 10 and later: SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [agent(Upload and Download)](arkts-basicservices-request-agent-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [download(Upload and Download)](arkts-basicservices-request-download-f.md) |
| [downloadFile(Upload and Download)](arkts-basicservices-request-downloadfile-f.md) | Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use on('complete'\|'pause'\|
| [download(Upload and Download)](arkts-basicservices-request-download-f.md) |
| [downloadFile(Upload and Download)](arkts-basicservices-request-downloadfile-f.md) | Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use on('complete'\|'pause'\|
| [upload(Upload and Download)](arkts-basicservices-request-upload-f.md) |
| [uploadFile(Upload and Download)](arkts-basicservices-request-uploadfile-f.md) | Uploads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use on('complete'\|
| [upload(Upload and Download)](arkts-basicservices-request-upload-f.md) |
| [uploadFile(Upload and Download)](arkts-basicservices-request-uploadfile-f.md) | Uploads a file. This API uses a promise to return the result. HTTP is supported. You can use on('complete'\|

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadConfig(Upload and Download)](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo(Upload and Download)](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask(Upload and Download)](arkts-basicservices-request-downloadtask-i.md) |
| [File(Upload and Download)](arkts-basicservices-request-file-i.md) |
| [RequestData(Upload and Download)](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig(Upload and Download)](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState(Upload and Download)](arkts-basicservices-request-taskstate-i.md) | Upload task information, which is the callback parameter of the on('complete' \| 'fail') and off('complete' \|
| [UploadTask(Upload and Download)](arkts-basicservices-request-uploadtask-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadProgressCallback(Upload and Download)](arkts-basicservices-request-downloadprogresscallback-t.md) |
| [DownloadCompleteCallback(Upload and Download)](arkts-basicservices-request-downloadcompletecallback-t.md) |
| [DownloadPauseCallback(Upload and Download)](arkts-basicservices-request-downloadpausecallback-t.md) |
| [DownloadRemoveCallback(Upload and Download)](arkts-basicservices-request-downloadremovecallback-t.md) |
| [DownloadFailCallback(Upload and Download)](arkts-basicservices-request-downloadfailcallback-t.md) |
| [UploadProgressCallback(Upload and Download)](arkts-basicservices-request-uploadprogresscallback-t.md) |
| [UploadHeaderReceiveCallback(Upload and Download)](arkts-basicservices-request-uploadheaderreceivecallback-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EXCEPTION_PERMISSION(Upload and Download)](arkts-basicservices-request-con.md#exception_permission) |
| [EXCEPTION_PARAMCHECK(Upload and Download)](arkts-basicservices-request-con.md#exception_paramcheck) |
| [EXCEPTION_UNSUPPORTED(Upload and Download)](arkts-basicservices-request-con.md#exception_unsupported) |
| [EXCEPTION_FILEIO(Upload and Download)](arkts-basicservices-request-con.md#exception_fileio) |
| [EXCEPTION_FILEPATH(Upload and Download)](arkts-basicservices-request-con.md#exception_filepath) |
| [EXCEPTION_SERVICE(Upload and Download)](arkts-basicservices-request-con.md#exception_service) |
| [EXCEPTION_OTHERS(Upload and Download)](arkts-basicservices-request-con.md#exception_others) |
| [NETWORK_MOBILE(Upload and Download)](arkts-basicservices-request-con.md#network_mobile) |
| [NETWORK_WIFI(Upload and Download)](arkts-basicservices-request-con.md#network_wifi) |
| [ERROR_CANNOT_RESUME(Upload and Download)](arkts-basicservices-request-con.md#error_cannot_resume) |
| [ERROR_DEVICE_NOT_FOUND(Upload and Download)](arkts-basicservices-request-con.md#error_device_not_found) |
| [ERROR_FILE_ALREADY_EXISTS(Upload and Download)](arkts-basicservices-request-con.md#error_file_already_exists) |
| [ERROR_FILE_ERROR(Upload and Download)](arkts-basicservices-request-con.md#error_file_error) |
| [ERROR_HTTP_DATA_ERROR(Upload and Download)](arkts-basicservices-request-con.md#error_http_data_error) |
| [ERROR_INSUFFICIENT_SPACE(Upload and Download)](arkts-basicservices-request-con.md#error_insufficient_space) |
| [ERROR_TOO_MANY_REDIRECTS(Upload and Download)](arkts-basicservices-request-con.md#error_too_many_redirects) |
| [ERROR_UNHANDLED_HTTP_CODE(Upload and Download)](arkts-basicservices-request-con.md#error_unhandled_http_code) |
| [ERROR_UNKNOWN(Upload and Download)](arkts-basicservices-request-con.md#error_unknown) |
| [ERROR_OFFLINE(Upload and Download)](arkts-basicservices-request-con.md#error_offline) |
| [ERROR_UNSUPPORTED_NETWORK_TYPE(Upload and Download)](arkts-basicservices-request-con.md#error_unsupported_network_type) |
| [PAUSED_QUEUED_FOR_WIFI(Upload and Download)](arkts-basicservices-request-con.md#paused_queued_for_wifi) |
| [PAUSED_WAITING_FOR_NETWORK(Upload and Download)](arkts-basicservices-request-con.md#paused_waiting_for_network) |
| [PAUSED_WAITING_TO_RETRY(Upload and Download)](arkts-basicservices-request-con.md#paused_waiting_to_retry) |
| [PAUSED_BY_USER(Upload and Download)](arkts-basicservices-request-con.md#paused_by_user) |
| [PAUSED_UNKNOWN(Upload and Download)](arkts-basicservices-request-con.md#paused_unknown) |
| [SESSION_SUCCESSFUL(Upload and Download)](arkts-basicservices-request-con.md#session_successful) |
| [SESSION_RUNNING(Upload and Download)](arkts-basicservices-request-con.md#session_running) |
| [SESSION_PENDING(Upload and Download)](arkts-basicservices-request-con.md#session_pending) |
| [SESSION_PAUSED(Upload and Download)](arkts-basicservices-request-con.md#session_paused) |
| [SESSION_FAILED(Upload and Download)](arkts-basicservices-request-con.md#session_failed) |
