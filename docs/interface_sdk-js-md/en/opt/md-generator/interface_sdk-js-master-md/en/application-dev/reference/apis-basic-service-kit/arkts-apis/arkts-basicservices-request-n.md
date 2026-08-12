# request

The **request** module provides applications with basic upload, download, and background transmission agent capabilities.

- Currently, the **request** module cannot be called in extensions.

**Since:** 6

<!--Device-unnamed-declare namespace request--><!--Device-unnamed-declare namespace request-End-->

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
| [agent](arkts-basicservices-request-agent-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use  [on('complete'\|'pause'\|'remove')](request.DownloadTask.on(type: 'complete' \| 'pause' \|
| [download](arkts-basicservices-request-download-f.md#download-1) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile-1) | Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use  [on('complete'\|'pause'\|'remove')](request.DownloadTask.on(type: 'complete' \| 'pause' \|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | Uploads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use  [on('complete'\|'fail')](request.UploadTask.on(type: 'complete' \|
| [upload](arkts-basicservices-request-upload-f.md#upload-1) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile-1) | Uploads a file. This API uses a promise to return the result. HTTP is supported. You can use  [on('complete'\|'fail')](request.UploadTask.on(type: 'complete' \|

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) |
| [File](arkts-basicservices-request-file-i.md) |
| [RequestData](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | Upload task information, which is the callback parameter of the  [on('complete' \| 'fail')](request.UploadTask.on(type: 'complete' \| 'fail', callback: Callback & lt;Array<[TaskState](arkts-basicservices-request-taskstate-i.md)> & gt; & lt;TaskState & gt;>))and  [off('complete' \ |
| [UploadTask](arkts-basicservices-request-uploadtask-i.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EXCEPTION_PERMISSION](arkts-basicservices-request-con.md#exception_permission) |
| [EXCEPTION_PARAMCHECK](arkts-basicservices-request-con.md#exception_paramcheck) |
| [EXCEPTION_UNSUPPORTED](arkts-basicservices-request-con.md#exception_unsupported) |
| [EXCEPTION_FILEIO](arkts-basicservices-request-con.md#exception_fileio) |
| [EXCEPTION_FILEPATH](arkts-basicservices-request-con.md#exception_filepath) |
| [EXCEPTION_SERVICE](arkts-basicservices-request-con.md#exception_service) |
| [EXCEPTION_OTHERS](arkts-basicservices-request-con.md#exception_others) |
| [NETWORK_MOBILE](arkts-basicservices-request-con.md#network_mobile) |
| [NETWORK_WIFI](arkts-basicservices-request-con.md#network_wifi) |
| [ERROR_CANNOT_RESUME](arkts-basicservices-request-con.md#error_cannot_resume) |
| [ERROR_DEVICE_NOT_FOUND](arkts-basicservices-request-con.md#error_device_not_found) |
| [ERROR_FILE_ALREADY_EXISTS](arkts-basicservices-request-con.md#error_file_already_exists) |
| [ERROR_FILE_ERROR](arkts-basicservices-request-con.md#error_file_error) |
| [ERROR_HTTP_DATA_ERROR](arkts-basicservices-request-con.md#error_http_data_error) |
| [ERROR_INSUFFICIENT_SPACE](arkts-basicservices-request-con.md#error_insufficient_space) |
| [ERROR_TOO_MANY_REDIRECTS](arkts-basicservices-request-con.md#error_too_many_redirects) |
| [ERROR_UNHANDLED_HTTP_CODE](arkts-basicservices-request-con.md#error_unhandled_http_code) |
| [ERROR_UNKNOWN](arkts-basicservices-request-con.md#error_unknown) |
| [ERROR_OFFLINE](arkts-basicservices-request-con.md#error_offline) |
| [ERROR_UNSUPPORTED_NETWORK_TYPE](arkts-basicservices-request-con.md#error_unsupported_network_type) |
| [PAUSED_QUEUED_FOR_WIFI](arkts-basicservices-request-con.md#paused_queued_for_wifi) |
| [PAUSED_WAITING_FOR_NETWORK](arkts-basicservices-request-con.md#paused_waiting_for_network) |
| [PAUSED_WAITING_TO_RETRY](arkts-basicservices-request-con.md#paused_waiting_to_retry) |
| [PAUSED_BY_USER](arkts-basicservices-request-con.md#paused_by_user) |
| [PAUSED_UNKNOWN](arkts-basicservices-request-con.md#paused_unknown) |
| [SESSION_SUCCESSFUL](arkts-basicservices-request-con.md#session_successful) |
| [SESSION_RUNNING](arkts-basicservices-request-con.md#session_running) |
| [SESSION_PENDING](arkts-basicservices-request-con.md#session_pending) |
| [SESSION_PAUSED](arkts-basicservices-request-con.md#session_paused) |
| [SESSION_FAILED](arkts-basicservices-request-con.md#session_failed) |
