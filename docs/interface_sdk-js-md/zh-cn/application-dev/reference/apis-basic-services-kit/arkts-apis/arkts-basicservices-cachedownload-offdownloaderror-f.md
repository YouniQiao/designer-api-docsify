# offDownloadError

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## offDownloadError

```TypeScript
function offDownloadError(url: string, callback?: Callback<DownloadError>): void
```

取消订阅预下载的错误事件。使用callback异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[DownloadError](arkts-basicservices-cachedownload-downloaderror-i.md)&gt; | 否 |
