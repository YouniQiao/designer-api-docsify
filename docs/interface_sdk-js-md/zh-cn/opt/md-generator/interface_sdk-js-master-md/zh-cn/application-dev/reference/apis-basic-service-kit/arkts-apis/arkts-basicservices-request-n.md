# request

request模块给应用提供上传下载文件、后台代理传输的基础功能。

- request暂不支持在Extension中调用。

**起始版本：** 6

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
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile) | 创建并启动一个下载任务，使用callback异步回调，支持HTTP协议。通过  [on('complete'\|'pause'\|'remove')](request.DownloadTask.on(type: 'complete' \| 'pause' \|
| [download](arkts-basicservices-request-download-f.md#download-1) |
| [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile-1) | 创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。通过  [on('complete'\|'pause'\|'remove')](request.DownloadTask.on(type: 'complete' \| 'pause' \|
| [upload](arkts-basicservices-request-upload-f.md#upload) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile) | 创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过  [on('complete'\|'fail')](request.UploadTask.on(type: 'complete' \|
| [upload](arkts-basicservices-request-upload-f.md#upload-1) |
| [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile-1) | 创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过  [on('complete'\|'fail')](request.UploadTask.on(type: 'complete' \|

### 接口

| 名称 |
| --- |
| [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask](arkts-basicservices-request-downloadtask-i.md) |
| [File](arkts-basicservices-request-file-i.md) |
| [RequestData](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState](arkts-basicservices-request-taskstate-i.md) | 上传任务的任务信息，是  [on('complete' \| 'fail')](request.UploadTask.on(type: 'complete' \| 'fail', callback: Callback&lt;Array<TaskState>&gt;&lt;TaskState&gt;>))和  [off('complete' \| 'fail')](request.UploadTask.off(type: 'complete' \|
| [UploadTask](arkts-basicservices-request-uploadtask-i.md) |

### 常量

| 名称 |
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
