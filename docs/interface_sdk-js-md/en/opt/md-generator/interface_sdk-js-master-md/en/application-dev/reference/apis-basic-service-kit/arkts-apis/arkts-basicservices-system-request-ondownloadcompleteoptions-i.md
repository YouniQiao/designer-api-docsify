# OnDownloadCompleteOptions

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-unnamed-export interface OnDownloadCompleteOptions--><!--Device-unnamed-export interface OnDownloadCompleteOptions-End-->

**System capability:** SystemCapability.MiscServices.Download

## Modules to Import

```TypeScript
import { UploadResponse, RequestData, DownloadRequestOptions, DownloadResponse, RequestFile, OnDownloadCompleteOptions, OnDownloadCompleteResponse, UploadRequestOptions } from 'kits/@kit.BasicServicesKit';
```

## complete

```TypeScript
complete?: () => void
```

Called when API call is complete.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-OnDownloadCompleteOptions-complete?: () => void--><!--Device-OnDownloadCompleteOptions-complete?: () => void-End-->

**System capability:** SystemCapability.MiscServices.Download

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

Called when API call has failed. Header information and HTTP status code returned when the upload task fails.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-OnDownloadCompleteOptions-fail?: (data: any, code: number) => void--><!--Device-OnDownloadCompleteOptions-fail?: (data: any, code: number) => void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | any | Yes |
| code | number | Yes |

## success

```TypeScript
success?: (data: OnDownloadCompleteResponse) => void
```

Called when API call is successful.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-OnDownloadCompleteOptions-success?: (data: OnDownloadCompleteResponse) => void--><!--Device-OnDownloadCompleteOptions-success?: (data: OnDownloadCompleteResponse) => void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [OnDownloadCompleteResponse](arkts-basicservices-system-request-ondownloadcompleteresponse-i.md) | Yes |

## token

```TypeScript
token: string
```

Result token returned by the download API.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.tid

<!--Device-OnDownloadCompleteOptions-token: string--><!--Device-OnDownloadCompleteOptions-token: string-End-->

**System capability:** SystemCapability.MiscServices.Download
