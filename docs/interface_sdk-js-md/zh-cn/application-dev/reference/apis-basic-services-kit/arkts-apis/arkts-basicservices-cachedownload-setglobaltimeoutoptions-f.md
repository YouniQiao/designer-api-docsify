# setGlobalTimeoutOptions

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## setGlobalTimeoutOptions

```TypeScript
function setGlobalTimeoutOptions(options?: TimeoutOptions): void
```

Sets timeout configuration for all tasks. Used when task-specific timeout configuration is not configured.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md) | 否 |
