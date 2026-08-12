# RequestFile

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [File](arkts-basicservices-request-file-i.md#File)

<!--Device-unnamed-export interface RequestFile--><!--Device-unnamed-export interface RequestFile-End-->

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { UploadResponse, RequestData, DownloadRequestOptions, DownloadResponse, RequestFile, OnDownloadCompleteOptions, OnDownloadCompleteResponse, UploadRequestOptions } from '@kit.BasicServicesKit';
```

## filename

```TypeScript
filename?: string
```

File name in the header when **multipart** is used.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [filename](ohos.request.agent.FileSpec.filename)

<!--Device-RequestFile-filename?: string--><!--Device-RequestFile-filename?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## name

```TypeScript
name?: string
```

Name of a form item when **multipart** is used. The default value is **file**.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [name](ohos.request.agent.FormItem.name)

<!--Device-RequestFile-name?: string--><!--Device-RequestFile-name?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## type

```TypeScript
type?: string
```

Type of the file content. By default, the type is obtained based on the extension of the file name or URI.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [contentType](ohos.request.agent.FileSpec.contentType)

<!--Device-RequestFile-type?: string--><!--Device-RequestFile-type?: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## uri

```TypeScript
uri: string
```

Local path for storing files.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [path](ohos.request.agent.FileSpec.path)

<!--Device-RequestFile-uri: string--><!--Device-RequestFile-uri: string-End-->

**System capability:** SystemCapability.MiscServices.Upload
