# setGlobalRetryOptions

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## setGlobalRetryOptions

```TypeScript
function setGlobalRetryOptions(options?: RetryOptions): void
```

Sets retry options for all tasks. Used when task-specific retry configuration is not configured.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-cacheDownload-function setGlobalRetryOptions(options?: RetryOptions): void--><!--Device-cacheDownload-function setGlobalRetryOptions(options?: RetryOptions): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RetryOptions](arkts-basicservices-cachedownload-retryoptions-i.md) | No | Task retry configurations. <br>Default value: Refer to the default value of RetryOptions. |

