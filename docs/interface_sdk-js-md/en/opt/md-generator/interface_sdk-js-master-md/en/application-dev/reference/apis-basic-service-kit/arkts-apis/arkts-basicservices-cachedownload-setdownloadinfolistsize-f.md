# setDownloadInfoListSize

## Modules to Import

```TypeScript
```

## setDownloadInfoListSize

```TypeScript
function setDownloadInfoListSize(size: number): void
```

Sets the size of the download information list. - The download information list is used to store pre-downloaded information. - Each pre-download generates a piece of download information with a unique URL. Only the latest download information is saved for the same URL. - If the list size is increased using this API, the original information in the list remains unchanged; if the list size is decreased, the LRU mode is used by default to clear excess cached data in the list.

**Since:** 23

<!--Device-cacheDownload-function setDownloadInfoListSize(size: long): void--><!--Device-cacheDownload-function setDownloadInfoListSize(size: long): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Examples**

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // Set the size of the download information list. 
  cacheDownload.setDownloadInfoListSize(2048);
} catch (err) {
  console.error(`Failed to set download information list size. err code: ${err.code}, err message: ${err.message}`);
}
```
