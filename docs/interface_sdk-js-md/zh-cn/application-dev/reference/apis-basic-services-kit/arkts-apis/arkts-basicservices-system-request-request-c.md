# Request

**起始版本：** 3

**废弃版本：** 9

**替代接口：** [request](arkts-basicservices-request-n.md)

**系统能力：** SystemCapability.MiscServices.Download

## 导入模块

```TypeScript
import { Request, DownloadRequestOptions, DownloadResponse, OnDownloadCompleteOptions, OnDownloadCompleteResponse, RequestData, RequestFile, UploadRequestOptions, UploadResponse } from 'kits/@kit.BasicServicesKit';
```

## download

```TypeScript
static download(options: DownloadRequestOptions): void
```

下载文件，无返回值。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** [downloadFile](arkts-basicservices-request-downloadfile-f.md)(context: BaseContext, config: DownloadConfig)

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DownloadRequestOptions](arkts-basicservices-system-request-downloadrequestoptions-i.md) | 是 |

## onDownloadComplete

```TypeScript
static onDownloadComplete(options: OnDownloadCompleteOptions): void
```

获取下载任务状态，无返回值。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** show(id: string)

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [OnDownloadCompleteOptions](arkts-basicservices-system-request-ondownloadcompleteoptions-i.md) | 是 |

## upload

```TypeScript
static upload(options: UploadRequestOptions): void
```

上传文件，无返回值。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** [uploadFile](arkts-basicservices-request-uploadfile-f.md)(context: BaseContext, config: UploadConfig)

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [UploadRequestOptions](arkts-basicservices-system-request-uploadrequestoptions-i.md) | 是 |
