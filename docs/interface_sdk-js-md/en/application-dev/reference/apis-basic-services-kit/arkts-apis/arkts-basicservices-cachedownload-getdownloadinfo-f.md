# getDownloadInfo

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## getDownloadInfo

```TypeScript
function getDownloadInfo(url: string): DownloadInfo | undefined
```

Obtains the download information based on the URL. The download information is stored in the download information list in memory and is cleared when the application exits.  
- If the specified URL is found in the download information list, the latest  
[DownloadInfo](arkts-basicservices-cachedownload-downloadinfo-i.md) corresponding to the URL is returned.  
- If the specified URL cannot be found in the download information list, **undefined** is returned.  
- If the download information has already cached in the URL, the new cached information will overwrite the old  
one.  
- When the target information is stored in the memory, the existing cache data is replaced in the LRU mode.

**Since:** 20

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| DownloadInfo \| undefined |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
