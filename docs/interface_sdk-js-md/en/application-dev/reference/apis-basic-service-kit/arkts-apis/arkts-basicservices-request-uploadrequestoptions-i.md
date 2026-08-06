# UploadRequestOptions

    **NOTE**  
    
    This API has been supported since API version 3 and deprecated since API version 9. You are advised to use  
    [UploadConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** [@ohos.request:request.UploadConfig](arkts-basicservices-request-uploadconfig-i.md)

<!--Device-unnamed-export interface UploadRequestOptions--><!--Device-unnamed-export interface UploadRequestOptions-End-->

**System capability:** SystemCapability.MiscServices.Upload

## complete

```TypeScript
complete?: () => void
```

Called when the execution is completed.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-UploadRequestOptions-complete?: () => void--><!--Device-UploadRequestOptions-complete?: () => void-End-->

**System capability:** SystemCapability.MiscServices.Upload

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

Called when uploading fails.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-UploadRequestOptions-fail?: (data: any, code: number) => void--><!--Device-UploadRequestOptions-fail?: (data: any, code: number) => void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | any | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: UploadResponse) => void
```

Called when the files are uploaded successfully.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Task.on

<!--Device-UploadRequestOptions-success?: (data: UploadResponse) => void--><!--Device-UploadRequestOptions-success?: (data: UploadResponse) => void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## data

```TypeScript
data?: Array<RequestData>
```

Form data in the request body.

**Type:** Array&lt;RequestData&gt;

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Config.data

<!--Device-UploadRequestOptions-data?: Array<RequestData>--><!--Device-UploadRequestOptions-data?: Array<RequestData>-End-->

**System capability:** SystemCapability.MiscServices.Upload

## files

```TypeScript
files: Array<RequestFile>
```

List of files to upload, which is submitted through multipart/form-data.

**Type:** Array&lt;RequestFile&gt;

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Config.data

<!--Device-UploadRequestOptions-files: Array<RequestFile>--><!--Device-UploadRequestOptions-files: Array<RequestFile>-End-->

**System capability:** SystemCapability.MiscServices.Upload

## header

```TypeScript
header?: Object
```

Request header.

**Type:** Object

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Config.headers

<!--Device-UploadRequestOptions-header?: Object--><!--Device-UploadRequestOptions-header?: Object-End-->

**System capability:** SystemCapability.MiscServices.Upload

## method

```TypeScript
method?: string
```

Request methods available: POST and PUT. The default value is POST.

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Config.method

<!--Device-UploadRequestOptions-method?: string--><!--Device-UploadRequestOptions-method?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## url

```TypeScript
url: string
```

Resource URL.

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.Config.url

<!--Device-UploadRequestOptions-url: string--><!--Device-UploadRequestOptions-url: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

