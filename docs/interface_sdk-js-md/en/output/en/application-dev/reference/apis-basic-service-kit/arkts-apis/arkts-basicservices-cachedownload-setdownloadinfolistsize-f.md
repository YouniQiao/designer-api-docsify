# setDownloadInfoListSize

## setDownloadInfoListSize

```TypeScript
function setDownloadInfoListSize(size: long): void
```

Sets the size of the download information list. - The download information list is used to store pre-downloaded information. - Each pre-download generates a piece of download information with a unique URL. Only the latest download information is saved for the same URL. - If the list size is increased using this API, the original information in the list remains unchanged; if the list size is decreased, the LRU mode is used by default to clear excess cached data in the list.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cacheDownload-function setDownloadInfoListSize(size: long): void--><!--Device-cacheDownload-function setDownloadInfoListSize(size: long): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Size of the download information list. The value ranges from 0 to 8192. The default value is **0**, indicating that no download information is stored. |

**Example**

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // Set the size of the download information list. 
  cacheDownload.setDownloadInfoListSize(2048);
} catch (err) {
  console.error(`Failed to set download information list size. err code: ${err.code}, err message: ${err.message}`);
}
```

