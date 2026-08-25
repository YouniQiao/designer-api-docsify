# offDownloadSuccess

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## offDownloadSuccess

```TypeScript
function offDownloadSuccess(url: string, callback?: Callback<void>): void
```

取消订阅预下载的完成事件。使用callback异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |
