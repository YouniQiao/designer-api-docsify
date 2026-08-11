# UploadResponse

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** [@ohos.request:request.UploadConfig](arkts-basicservices-request-uploadconfig-i.md)

<!--Device-unnamed-export interface UploadResponse--><!--Device-unnamed-export interface UploadResponse-End-->

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { UploadResponse, RequestData, DownloadRequestOptions, DownloadResponse, RequestFile, OnDownloadCompleteOptions, OnDownloadCompleteResponse, UploadRequestOptions } from 'kits/@kit.BasicServicesKit';
```

## code

```TypeScript
code: number
```

HTTP status code returned by the server.

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.HttpResponse.statusCode

<!--Device-UploadResponse-code: number--><!--Device-UploadResponse-code: number-End-->

**System capability:** SystemCapability.MiscServices.Upload

## data

```TypeScript
data: string
```

Content returned by the server. The value type is determined by the type in the returned headers.

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Progress.extras

<!--Device-UploadResponse-data: string--><!--Device-UploadResponse-data: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## headers

```TypeScript
headers: Object
```

Headers returned by the server.

**Type:** Object

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.HttpResponse.headers

<!--Device-UploadResponse-headers: Object--><!--Device-UploadResponse-headers: Object-End-->

**System capability:** SystemCapability.MiscServices.Upload

