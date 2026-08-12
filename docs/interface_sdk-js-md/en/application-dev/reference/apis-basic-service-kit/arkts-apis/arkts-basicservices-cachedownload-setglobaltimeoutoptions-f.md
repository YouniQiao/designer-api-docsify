# setGlobalTimeoutOptions

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## setGlobalTimeoutOptions

```TypeScript
function setGlobalTimeoutOptions(options?: TimeoutOptions): void
```

Sets timeout configuration for all tasks.Used when task-specific timeout configuration is not configured.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-cacheDownload-function setGlobalTimeoutOptions(options?: TimeoutOptions): void--><!--Device-cacheDownload-function setGlobalTimeoutOptions(options?: TimeoutOptions): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md) | No | Task timeout configuration. &lt;br&gt;Default value: Refer to the default value of TimeoutOptions. |

