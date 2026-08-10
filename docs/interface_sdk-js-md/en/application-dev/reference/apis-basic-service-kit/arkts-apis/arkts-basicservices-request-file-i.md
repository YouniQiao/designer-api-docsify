# File

[UploadConfig](arkts-basicservices-request-uploadconfig-i.md)中的文件列表。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-request-interface File--><!--Device-request-interface File-End-->

**System capability:** SystemCapability.MiscServices.Download

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## filename

```TypeScript
filename: string
```

multipart提交时，请求头中的文件名。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-File-filename: string--><!--Device-File-filename: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## name

```TypeScript
name: string
```

multipart提交时，表单项目的名称，缺省为file。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-File-name: string--><!--Device-File-name: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## type

```TypeScript
type: string
```

文件的内容类型，默认根据文件名或路径的后缀获取。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-File-type: string--><!--Device-File-type: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## uri

```TypeScript
uri: string
```

文件的本地存储路径。

仅支持"internal://cache/"，即调用方（传入的context）对应的缓存路径context.cacheDir。

示例：internal://cache/path/to/file.txt

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-File-uri: string--><!--Device-File-uri: string-End-->

**System capability:** SystemCapability.MiscServices.Download

