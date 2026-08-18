# request

request模块给应用提供上传下载文件、后台代理传输的基础功能。 - request暂不支持在Extension中调用。

**起始版本：** 23

<!--Device-unnamed-declare namespace request--><!--Device-unnamed-declare namespace request-End-->

**系统能力：** 
- API版本10+：SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [agent](arkts-basicservices-request-agent-n.md) |

### 函数

| 名称 |
| --- |
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | 创建并启动一个下载任务，使用callback异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | 创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | 创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过 [on('complete'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | 创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过 [on('complete'\|

### 接口

| 名称 |
| --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) |
| [File](arkts-basicservices-request-file-i.md) |
| [RequestData](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | 上传任务的任务信息，是 [on('complete' \| 'fail')](arkts-basicservices-request-uploadtask-i.md#onprogress) 和 [off('complete' \|
| [UploadTask](arkts-basicservices-request-uploadtask-i.md) |

### 类型

| 名称 |
| --- |
| [DownloadProgressCallback](arkts-basicservices-request-downloadprogresscallback-t.md) |
| [DownloadCompleteCallback](arkts-basicservices-request-downloadcompletecallback-t.md) |
| [DownloadPauseCallback](arkts-basicservices-request-downloadpausecallback-t.md) |
| [DownloadRemoveCallback](arkts-basicservices-request-downloadremovecallback-t.md) |
| [DownloadFailCallback](arkts-basicservices-request-downloadfailcallback-t.md) |
| [UploadProgressCallback](arkts-basicservices-request-uploadprogresscallback-t.md) |
| [UploadHeaderReceiveCallback](arkts-basicservices-request-uploadheaderreceivecallback-t.md) |

### 常量

| 名称 |
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
