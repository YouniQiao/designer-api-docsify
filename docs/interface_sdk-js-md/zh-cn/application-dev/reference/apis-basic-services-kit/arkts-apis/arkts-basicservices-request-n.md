# request(上传下载)

request模块给应用提供上传下载文件、后台代理传输的基础功能。  
- request暂不支持在Extension中调用。

**起始版本：** 6

**系统能力：** 
- API版本10+：SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [agent(上传下载)](arkts-basicservices-request-agent-n.md) |

### 函数

| 名称 |
| --- |
| [download(上传下载)](arkts-basicservices-request-download-f.md) |
| [downloadFile(上传下载)](arkts-basicservices-request-downloadfile-f.md) | 创建并启动一个下载任务，使用callback异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [download(上传下载)](arkts-basicservices-request-download-f.md) |
| [downloadFile(上传下载)](arkts-basicservices-request-downloadfile-f.md) | 创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'\|'pause'\|
| [upload(上传下载)](arkts-basicservices-request-upload-f.md) |
| [uploadFile(上传下载)](arkts-basicservices-request-uploadfile-f.md) | 创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过 on('complete'\|
| [upload(上传下载)](arkts-basicservices-request-upload-f.md) |
| [uploadFile(上传下载)](arkts-basicservices-request-uploadfile-f.md) | 创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'\|

### 接口

| 名称 |
| --- |
| [DownloadConfig(上传下载)](arkts-basicservices-request-downloadconfig-i.md) |
| [DownloadInfo(上传下载)](arkts-basicservices-request-downloadinfo-i.md) |
| [DownloadTask(上传下载)](arkts-basicservices-request-downloadtask-i.md) |
| [File(上传下载)](arkts-basicservices-request-file-i.md) |
| [RequestData(上传下载)](arkts-basicservices-request-requestdata-i.md) |
| [UploadConfig(上传下载)](arkts-basicservices-request-uploadconfig-i.md) |
| [TaskState(上传下载)](arkts-basicservices-request-taskstate-i.md) | 上传任务的任务信息，是 on('complete' \| 'fail') 和 off('complete' \|
| [UploadTask(上传下载)](arkts-basicservices-request-uploadtask-i.md) |

### 常量

| 名称 |
| --- |
| [EXCEPTION_PERMISSION(上传下载)](arkts-basicservices-request-con.md#exception_permission) |
| [EXCEPTION_PARAMCHECK(上传下载)](arkts-basicservices-request-con.md#exception_paramcheck) |
| [EXCEPTION_UNSUPPORTED(上传下载)](arkts-basicservices-request-con.md#exception_unsupported) |
| [EXCEPTION_FILEIO(上传下载)](arkts-basicservices-request-con.md#exception_fileio) |
| [EXCEPTION_FILEPATH(上传下载)](arkts-basicservices-request-con.md#exception_filepath) |
| [EXCEPTION_SERVICE(上传下载)](arkts-basicservices-request-con.md#exception_service) |
| [EXCEPTION_OTHERS(上传下载)](arkts-basicservices-request-con.md#exception_others) |
| [NETWORK_MOBILE(上传下载)](arkts-basicservices-request-con.md#network_mobile) |
| [NETWORK_WIFI(上传下载)](arkts-basicservices-request-con.md#network_wifi) |
| [ERROR_CANNOT_RESUME(上传下载)](arkts-basicservices-request-con.md#error_cannot_resume) |
| [ERROR_DEVICE_NOT_FOUND(上传下载)](arkts-basicservices-request-con.md#error_device_not_found) |
| [ERROR_FILE_ALREADY_EXISTS(上传下载)](arkts-basicservices-request-con.md#error_file_already_exists) |
| [ERROR_FILE_ERROR(上传下载)](arkts-basicservices-request-con.md#error_file_error) |
| [ERROR_HTTP_DATA_ERROR(上传下载)](arkts-basicservices-request-con.md#error_http_data_error) |
| [ERROR_INSUFFICIENT_SPACE(上传下载)](arkts-basicservices-request-con.md#error_insufficient_space) |
| [ERROR_TOO_MANY_REDIRECTS(上传下载)](arkts-basicservices-request-con.md#error_too_many_redirects) |
| [ERROR_UNHANDLED_HTTP_CODE(上传下载)](arkts-basicservices-request-con.md#error_unhandled_http_code) |
| [ERROR_UNKNOWN(上传下载)](arkts-basicservices-request-con.md#error_unknown) |
| [ERROR_OFFLINE(上传下载)](arkts-basicservices-request-con.md#error_offline) |
| [ERROR_UNSUPPORTED_NETWORK_TYPE(上传下载)](arkts-basicservices-request-con.md#error_unsupported_network_type) |
| [PAUSED_QUEUED_FOR_WIFI(上传下载)](arkts-basicservices-request-con.md#paused_queued_for_wifi) |
| [PAUSED_WAITING_FOR_NETWORK(上传下载)](arkts-basicservices-request-con.md#paused_waiting_for_network) |
| [PAUSED_WAITING_TO_RETRY(上传下载)](arkts-basicservices-request-con.md#paused_waiting_to_retry) |
| [PAUSED_BY_USER(上传下载)](arkts-basicservices-request-con.md#paused_by_user) |
| [PAUSED_UNKNOWN(上传下载)](arkts-basicservices-request-con.md#paused_unknown) |
| [SESSION_SUCCESSFUL(上传下载)](arkts-basicservices-request-con.md#session_successful) |
| [SESSION_RUNNING(上传下载)](arkts-basicservices-request-con.md#session_running) |
| [SESSION_PENDING(上传下载)](arkts-basicservices-request-con.md#session_pending) |
| [SESSION_PAUSED(上传下载)](arkts-basicservices-request-con.md#session_paused) |
| [SESSION_FAILED(上传下载)](arkts-basicservices-request-con.md#session_failed) |
