# setGlobalTimeoutOptions

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## setGlobalTimeoutOptions

```TypeScript
function setGlobalTimeoutOptions(options?: TimeoutOptions): void
```

Sets timeout configuration for all tasks. Used when task-specific timeout configuration is not configured.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-cacheDownload-function setGlobalTimeoutOptions(options?: TimeoutOptions): void--><!--Device-cacheDownload-function setGlobalTimeoutOptions(options?: TimeoutOptions): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md) | No |

## Examples

```TypeScript
try {
  // Set the global timeout options of a task.
  cacheDownload.setGlobalTimeoutOptions({
    networkCheckTimeout: 20,
    httpTotalTimeout: 60,
  })
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err?.code}, err message: ${err?.message}`);
}
```
