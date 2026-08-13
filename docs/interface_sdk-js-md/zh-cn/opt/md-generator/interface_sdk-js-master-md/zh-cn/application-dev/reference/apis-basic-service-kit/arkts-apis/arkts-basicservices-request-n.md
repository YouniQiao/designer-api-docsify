# request

request模块给应用提供上传下载文件、后台代理传输的基础功能。 - request暂不支持在Extension中调用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace request--><!--Device-unnamed-declare namespace request-End-->

**系统能力：** 
- API版本10+：SystemCapability.Request.FileTransferAgent

## 汇总

### 命名空间

| 名称 |
| --- |
| [agent](arkts-basicservices-request-agent-n.md) |

### 函数

| 名称 |
| --- |
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) | 创建并启动一个下载任务，使用callback异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [download](arkts-basicservices-request-download-f.md#download) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadFile) | 创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) | 创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过 [on('complete'\|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadFile) | 创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过 [on('complete'\|

### 接口

| 名称 |
| --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) |
| [File](arkts-basicservices-request-file-i.md) |
| [RequestData](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | 上传任务的任务信息，是 [on('complete' \| 'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) 和 [off('complete' \|
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
| [EXCEPTION_PERMISSION](arkts-basicservices-request-con.md#EXCEPTION_PERMISSION) |
| [EXCEPTION_PARAMCHECK](arkts-basicservices-request-con.md#EXCEPTION_PARAMCHECK) |
| [EXCEPTION_UNSUPPORTED](arkts-basicservices-request-con.md#EXCEPTION_UNSUPPORTED) |
| [EXCEPTION_FILEIO](arkts-basicservices-request-con.md#EXCEPTION_FILEIO) |
| [EXCEPTION_FILEPATH](arkts-basicservices-request-con.md#EXCEPTION_FILEPATH) |
| [EXCEPTION_SERVICE](arkts-basicservices-request-con.md#EXCEPTION_SERVICE) |
| [EXCEPTION_OTHERS](arkts-basicservices-request-con.md#EXCEPTION_OTHERS) |
| [NETWORK_MOBILE](arkts-basicservices-request-con.md#NETWORK_MOBILE) |
| [NETWORK_WIFI](arkts-basicservices-request-con.md#NETWORK_WIFI) |
| [ERROR_CANNOT_RESUME](arkts-basicservices-request-con.md#ERROR_CANNOT_RESUME) |
| [ERROR_DEVICE_NOT_FOUND](arkts-basicservices-request-con.md#ERROR_DEVICE_NOT_FOUND) |
| [ERROR_FILE_ALREADY_EXISTS](arkts-basicservices-request-con.md#ERROR_FILE_ALREADY_EXISTS) |
| [ERROR_FILE_ERROR](arkts-basicservices-request-con.md#ERROR_FILE_ERROR) |
| [ERROR_HTTP_DATA_ERROR](arkts-basicservices-request-con.md#ERROR_HTTP_DATA_ERROR) |
| [ERROR_INSUFFICIENT_SPACE](arkts-basicservices-request-con.md#ERROR_INSUFFICIENT_SPACE) |
| [ERROR_TOO_MANY_REDIRECTS](arkts-basicservices-request-con.md#ERROR_TOO_MANY_REDIRECTS) |
| [ERROR_UNHANDLED_HTTP_CODE](arkts-basicservices-request-con.md#ERROR_UNHANDLED_HTTP_CODE) |
| [ERROR_UNKNOWN](arkts-basicservices-request-con.md#ERROR_UNKNOWN) |
| [ERROR_OFFLINE](arkts-basicservices-request-con.md#ERROR_OFFLINE) |
| [ERROR_UNSUPPORTED_NETWORK_TYPE](arkts-basicservices-request-con.md#ERROR_UNSUPPORTED_NETWORK_TYPE) |
| [PAUSED_QUEUED_FOR_WIFI](arkts-basicservices-request-con.md#PAUSED_QUEUED_FOR_WIFI) |
| [PAUSED_WAITING_FOR_NETWORK](arkts-basicservices-request-con.md#PAUSED_WAITING_FOR_NETWORK) |
| [PAUSED_WAITING_TO_RETRY](arkts-basicservices-request-con.md#PAUSED_WAITING_TO_RETRY) |
| [PAUSED_BY_USER](arkts-basicservices-request-con.md#PAUSED_BY_USER) |
| [PAUSED_UNKNOWN](arkts-basicservices-request-con.md#PAUSED_UNKNOWN) |
| [SESSION_SUCCESSFUL](arkts-basicservices-request-con.md#SESSION_SUCCESSFUL) |
| [SESSION_RUNNING](arkts-basicservices-request-con.md#SESSION_RUNNING) |
| [SESSION_PENDING](arkts-basicservices-request-con.md#SESSION_PENDING) |
| [SESSION_PAUSED](arkts-basicservices-request-con.md#SESSION_PAUSED) |
| [SESSION_FAILED](arkts-basicservices-request-con.md#SESSION_FAILED) |
