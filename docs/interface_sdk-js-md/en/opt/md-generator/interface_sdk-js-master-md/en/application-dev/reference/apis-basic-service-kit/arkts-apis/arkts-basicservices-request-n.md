# request

The **request** module provides applications with basic upload, download, and background transmission agent capabilities. - Currently, the **request** module cannot be called in extensions.

**Since:** 23

<!--Device-unnamed-declare namespace request--><!--Device-unnamed-declare namespace request-End-->

**System capability:** 
- API version 10 and later: SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
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
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | Downloads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use on('complete'\|'pause'\|
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | Downloads a file. This API uses a promise to return the result. HTTP is supported. You can use on('complete'\|'pause'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | Uploads a file. This API uses an asynchronous callback to return the result. HTTP is supported. You can use [on('complete'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | Uploads a file. This API uses a promise to return the result. HTTP is supported. You can use [on('complete'\|

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) |
| [File](arkts-basicservices-request-file-i.md) |
| [RequestData](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | Upload task information, which is the callback parameter of the [on('complete' \| 'fail')](arkts-basicservices-request-uploadtask-i.md#onprogress) and [off('complete' \|
| [UploadTask](arkts-basicservices-request-uploadtask-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadProgressCallback](arkts-basicservices-request-downloadprogresscallback-t.md) |
| [DownloadCompleteCallback](arkts-basicservices-request-downloadcompletecallback-t.md) |
| [DownloadPauseCallback](arkts-basicservices-request-downloadpausecallback-t.md) |
| [DownloadRemoveCallback](arkts-basicservices-request-downloadremovecallback-t.md) |
| [DownloadFailCallback](arkts-basicservices-request-downloadfailcallback-t.md) |
| [UploadProgressCallback](arkts-basicservices-request-uploadprogresscallback-t.md) |
| [UploadHeaderReceiveCallback](arkts-basicservices-request-uploadheaderreceivecallback-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EXCEPTION_PERMISSION](arkts-basicservices-request-con.md#exceptionpermission) |
| [EXCEPTION_PARAMCHECK](arkts-basicservices-request-con.md#exceptionparamcheck) |
| [EXCEPTION_UNSUPPORTED](arkts-basicservices-request-con.md#exceptionunsupported) |
| [EXCEPTION_FILEIO](arkts-basicservices-request-con.md#exceptionfileio) |
| [EXCEPTION_FILEPATH](arkts-basicservices-request-con.md#exceptionfilepath) |
| [EXCEPTION_SERVICE](arkts-basicservices-request-con.md#exceptionservice) |
| [EXCEPTION_OTHERS](arkts-basicservices-request-con.md#exceptionothers) |
| [NETWORK_MOBILE](arkts-basicservices-request-con.md#networkmobile) |
| [NETWORK_WIFI](arkts-basicservices-request-con.md#networkwifi) |
| [ERROR_CANNOT_RESUME](arkts-basicservices-request-con.md#errorcannotresume) |
| [ERROR_DEVICE_NOT_FOUND](arkts-basicservices-request-con.md#errordevicenotfound) |
| [ERROR_FILE_ALREADY_EXISTS](arkts-basicservices-request-con.md#errorfilealreadyexists) |
| [ERROR_FILE_ERROR](arkts-basicservices-request-con.md#errorfileerror) |
| [ERROR_HTTP_DATA_ERROR](arkts-basicservices-request-con.md#errorhttpdataerror) |
| [ERROR_INSUFFICIENT_SPACE](arkts-basicservices-request-con.md#errorinsufficientspace) |
| [ERROR_TOO_MANY_REDIRECTS](arkts-basicservices-request-con.md#errortoomanyredirects) |
| [ERROR_UNHANDLED_HTTP_CODE](arkts-basicservices-request-con.md#errorunhandledhttpcode) |
| [ERROR_UNKNOWN](arkts-basicservices-request-con.md#errorunknown) |
| [ERROR_OFFLINE](arkts-basicservices-request-con.md#erroroffline) |
| [ERROR_UNSUPPORTED_NETWORK_TYPE](arkts-basicservices-request-con.md#errorunsupportednetworktype) |
| [PAUSED_QUEUED_FOR_WIFI](arkts-basicservices-request-con.md#pausedqueuedforwifi) |
| [PAUSED_WAITING_FOR_NETWORK](arkts-basicservices-request-con.md#pausedwaitingfornetwork) |
| [PAUSED_WAITING_TO_RETRY](arkts-basicservices-request-con.md#pausedwaitingtoretry) |
| [PAUSED_BY_USER](arkts-basicservices-request-con.md#pausedbyuser) |
| [PAUSED_UNKNOWN](arkts-basicservices-request-con.md#pausedunknown) |
| [SESSION_SUCCESSFUL](arkts-basicservices-request-con.md#sessionsuccessful) |
| [SESSION_RUNNING](arkts-basicservices-request-con.md#sessionrunning) |
| [SESSION_PENDING](arkts-basicservices-request-con.md#sessionpending) |
| [SESSION_PAUSED](arkts-basicservices-request-con.md#sessionpaused) |
| [SESSION_FAILED](arkts-basicservices-request-con.md#sessionfailed) |
