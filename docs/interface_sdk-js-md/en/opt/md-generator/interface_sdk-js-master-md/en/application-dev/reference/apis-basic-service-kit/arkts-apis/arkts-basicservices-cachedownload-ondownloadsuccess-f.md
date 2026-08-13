# onDownloadSuccess

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## onDownloadSuccess

```TypeScript
function onDownloadSuccess(url: string, callback: Callback<void>): void
```

Subscribes to the pre-download completion events. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-cacheDownload-function onDownloadSuccess(url: string, callback: Callback<void>): void--><!--Device-cacheDownload-function onDownloadSuccess(url: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const successCallback = () => {
    console.info("Succeeded in getting callback from cacheDownload");
  };
  // Subscribe to the pre-download completion events. Callback is invoked when the download is complete.
  cacheDownload.onDownloadSuccess("https://www.example.com", successCallback)
  // Download the resource. If the download is successful, the resource will be cached to the specified file in the application memory or sandbox directory. 
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```
