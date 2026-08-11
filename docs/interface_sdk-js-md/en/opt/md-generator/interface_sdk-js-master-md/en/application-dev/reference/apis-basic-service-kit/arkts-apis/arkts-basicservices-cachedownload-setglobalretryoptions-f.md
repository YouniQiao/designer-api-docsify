# setGlobalRetryOptions

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## setGlobalRetryOptions

```TypeScript
function setGlobalRetryOptions(options?: RetryOptions): void
```

Sets retry options for all tasks.Used when task-specific retry configuration is not configured.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-cacheDownload-function setGlobalRetryOptions(options?: RetryOptions): void--><!--Device-cacheDownload-function setGlobalRetryOptions(options?: RetryOptions): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RetryOptions](arkts-basicservices-cachedownload-retryoptions-i.md) | No |

## Examples

```TypeScript
try {
  // Set the maximum number of retries for a task globally.
  cacheDownload.setGlobalRetryOptions({
    maxRetryCount: 1
  });
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err?.code}, err message: ${err?.message}`);
}
```
