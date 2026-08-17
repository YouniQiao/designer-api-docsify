# RequestFile(Upload and Download)

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [File](arkts-basicservices-request-file-i.md#file)

<!--Device-unnamed-export interface RequestFile--><!--Device-unnamed-export interface RequestFile-End-->

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

## filename

```TypeScript
filename?: string
```

File name in the header when **multipart** is used.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**Substitutes:** filename

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

**Substitutes:** name

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

**Substitutes:** contentType

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

**Substitutes:** path

<!--Device-RequestFile-uri: string--><!--Device-RequestFile-uri: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

