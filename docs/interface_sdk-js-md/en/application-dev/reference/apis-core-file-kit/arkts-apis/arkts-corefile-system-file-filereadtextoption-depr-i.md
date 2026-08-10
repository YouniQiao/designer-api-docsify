# FileReadTextOption

可选项类型，支持readText接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileReadTextOption--><!--Device-unnamed-export interface FileReadTextOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-complete?: () => void--><!--Device-FileReadTextOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-fail?: (data: string, code: number) => void--><!--Device-FileReadTextOption-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: FileReadTextResponse) => void
```

接口调用成功的回调函数。返回[FileReadTextResponse](arkts-corefile-system-file-filereadtextresponse-depr-i.md)。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-success?: (data: FileReadTextResponse) => void--><!--Device-FileReadTextOption-success?: (data: FileReadTextResponse) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [FileReadTextResponse](arkts-corefile-system-file-filereadtextresponse-depr-i.md) | Yes |  |

## encoding

```TypeScript
encoding?: string
```

编码格式，默认为UTF-8。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-encoding?: string--><!--Device-FileReadTextOption-encoding?: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## length

```TypeScript
length?: number
```

读取的长度，单位为Byte，默认值为4096。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-length?: number--><!--Device-FileReadTextOption-length?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## position

```TypeScript
position?: number
```

读取的起始位置，单位为Byte，默认为文件的起始位置。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-position?: number--><!--Device-FileReadTextOption-position?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## uri

```TypeScript
uri: string
```

本地文件URI。由于轻量级穿戴设备底层文件系统的限制，该值必须满足以下要求：1. URI 中不得包含以下特殊字符：\"*+,:;&lt;=&gt;?[]|\x7F等。2. 最大允许字符长度为128个字符。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadTextOption-uri: string--><!--Device-FileReadTextOption-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

