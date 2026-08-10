# RequestFile

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** [@ohos.request:request.File](arkts-basicservices-request-file-i.md)

<!--Device-unnamed-export interface RequestFile--><!--Device-unnamed-export interface RequestFile-End-->

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { UploadResponse, RequestData, DownloadRequestOptions, DownloadResponse, RequestFile, OnDownloadCompleteOptions, OnDownloadCompleteResponse, UploadRequestOptions } from 'kits/@kit.BasicServicesKit';
```

## filename

```TypeScript
filename?: string
```

multipart 提交时，请求头中的文件名。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.FileSpec.filename

<!--Device-RequestFile-filename?: string--><!--Device-RequestFile-filename?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## name

```TypeScript
name?: string
```

multipart 提交时，表单项目的名称，缺省为file。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.FormItem.name

<!--Device-RequestFile-name?: string--><!--Device-RequestFile-name?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## type

```TypeScript
type?: string
```

文件的内容类型，默认根据文件名或路径的后缀获取。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.FileSpec.contentType

<!--Device-RequestFile-type?: string--><!--Device-RequestFile-type?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## uri

```TypeScript
uri: string
```

文件的本地存储路径。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

**Substitutes:** ohos.request.agent.FileSpec.path

<!--Device-RequestFile-uri: string--><!--Device-RequestFile-uri: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

