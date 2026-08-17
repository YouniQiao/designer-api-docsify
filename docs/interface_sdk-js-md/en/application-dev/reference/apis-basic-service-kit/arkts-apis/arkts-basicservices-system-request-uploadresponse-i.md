# UploadResponse(Upload and Download)

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [UploadConfig](arkts-basicservices-request-uploadconfig-i.md#uploadconfig)

<!--Device-unnamed-export interface UploadResponse--><!--Device-unnamed-export interface UploadResponse-End-->

**System capability:** SystemCapability.MiscServices.Upload

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

## code

```TypeScript
code: number
```

HTTP status code returned by the server.

**Type:** number

**Since:** 3

**Deprecated since:** 9

**Substitutes:** statusCode

<!--Device-UploadResponse-code: number--><!--Device-UploadResponse-code: number-End-->

**System capability:** SystemCapability.MiscServices.Upload

## data

```TypeScript
data: string
```

Content returned by the server. The value type is determined by the type in the returned headers.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** extras

<!--Device-UploadResponse-data: string--><!--Device-UploadResponse-data: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## headers

```TypeScript
headers: Object
```

Headers returned by the server.

**Type:** Object

**Since:** 3

**Deprecated since:** 9

**Substitutes:** headers

<!--Device-UploadResponse-headers: Object--><!--Device-UploadResponse-headers: Object-End-->

**System capability:** SystemCapability.MiscServices.Upload

