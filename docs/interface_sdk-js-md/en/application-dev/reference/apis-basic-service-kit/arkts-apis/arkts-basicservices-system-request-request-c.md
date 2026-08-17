# Request(Upload and Download)

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [request](arkts-basicservices-request-n.md#request)

<!--Device-unnamed-export default class Request--><!--Device-unnamed-export default class Request-End-->

**System capability:** SystemCapability.MiscServices.Download

## Modules to Import

```TypeScript
import { DownloadRequestOptions } from 'DownloadRequestOptions';
import { DownloadResponse } from 'DownloadResponse';
import { OnDownloadCompleteOptions } from 'OnDownloadCompleteOptions';
import { OnDownloadCompleteResponse } from 'OnDownloadCompleteResponse';
import { RequestData } from 'RequestData';
import { RequestFile } from 'RequestFile';
import { UploadRequestOptions } from 'UploadRequestOptions';
import { UploadResponse } from 'UploadResponse';
```

## download

```TypeScript
static download(options: DownloadRequestOptions): void
```

Downloads a file. This API returns no value.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile)(context: BaseContext, config: DownloadConfig)

<!--Device-Request-static download(options: DownloadRequestOptions): void--><!--Device-Request-static download(options: DownloadRequestOptions): void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DownloadRequestOptions](arkts-basicservices-system-request-downloadrequestoptions-i.md) | Yes | Download configurations. |

## onDownloadComplete

```TypeScript
static onDownloadComplete(options: OnDownloadCompleteOptions): void
```

Listens for download task status. This API returns no value.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** show(id: string)

<!--Device-Request-static onDownloadComplete(options: OnDownloadCompleteOptions): void--><!--Device-Request-static onDownloadComplete(options: OnDownloadCompleteOptions): void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [OnDownloadCompleteOptions](arkts-basicservices-system-request-ondownloadcompleteoptions-i.md) | Yes | Configurations of the download task. |

## upload

```TypeScript
static upload(options: UploadRequestOptions): void
```

Uploads a file. This API returns no value.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile)(context: BaseContext, config: UploadConfig)

<!--Device-Request-static upload(options: UploadRequestOptions): void--><!--Device-Request-static upload(options: UploadRequestOptions): void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UploadRequestOptions](arkts-basicservices-system-request-uploadrequestoptions-i.md) | Yes | Upload configurations. |

