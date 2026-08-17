# DownloadResponse(Upload and Download)

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [UploadConfig](arkts-basicservices-request-uploadconfig-i.md#uploadconfig)

<!--Device-unnamed-export interface DownloadResponse--><!--Device-unnamed-export interface DownloadResponse-End-->

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

## token

```TypeScript
token: string
```

Download token, which is used to obtain the download status

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** tid

<!--Device-DownloadResponse-token: string--><!--Device-DownloadResponse-token: string-End-->

**System capability:** SystemCapability.MiscServices.Download

