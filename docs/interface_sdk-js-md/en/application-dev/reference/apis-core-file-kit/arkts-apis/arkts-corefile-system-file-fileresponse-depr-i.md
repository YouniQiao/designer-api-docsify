# FileResponse

文件返回。包含文件的信息。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileResponse--><!--Device-unnamed-export interface FileResponse-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## lastModifiedTime

```TypeScript
lastModifiedTime: number
```

文件保存时的时间戳，从1970/01/01?00:00:00到当前时间的毫秒数。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileResponse-lastModifiedTime: number--><!--Device-FileResponse-lastModifiedTime: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## length

```TypeScript
length: number
```

文件长度，单位为Byte。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileResponse-length: number--><!--Device-FileResponse-length: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## subFiles

```TypeScript
subFiles?: Array<FileResponse>
```

文件列表。

**Type:** Array&lt;[FileResponse](arkts-corefile-system-file-fileresponse-depr-i.md)&gt;

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileResponse-subFiles?: Array<FileResponse>--><!--Device-FileResponse-subFiles?: Array<FileResponse>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## type

```TypeScript
type: 'dir' | 'file'
```

文件类型，可选值为：  
-dir：目录；  
-file：文件。

**Type:** 'dir' \| 'file'

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileResponse-type: 'dir' | 'file'--><!--Device-FileResponse-type: 'dir' | 'file'-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## uri

```TypeScript
uri: string
```

文件的URI。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileResponse-uri: string--><!--Device-FileResponse-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

