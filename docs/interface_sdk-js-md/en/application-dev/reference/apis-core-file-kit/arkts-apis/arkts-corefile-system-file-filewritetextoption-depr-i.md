# FileWriteTextOption

可选项类型，支持writeText接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileWriteTextOption--><!--Device-unnamed-export interface FileWriteTextOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-complete?: () => void--><!--Device-FileWriteTextOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-fail?: (data: string, code: number) => void--><!--Device-FileWriteTextOption-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: () => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-success?: () => void--><!--Device-FileWriteTextOption-success?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## append

```TypeScript
append?: boolean
```

是否追加模式，默认为false。true为追加，false为不追加。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-append?: boolean--><!--Device-FileWriteTextOption-append?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## encoding

```TypeScript
encoding?: string
```

编码格式，默认为UTF-8。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-encoding?: string--><!--Device-FileWriteTextOption-encoding?: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## text

```TypeScript
text: string
```

写入的字符串。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-text: string--><!--Device-FileWriteTextOption-text: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## uri

```TypeScript
uri: string
```

本地文件URI，如果文件不存在会创建文件。由于轻量级穿戴设备底层文件系统的限制，该值必须满足以下要求：1. URI 中不得包含以下特殊字符：\"*+,:;&lt;=&gt;?[]|\x7F等。2. 最大允许字符长度为128个字符。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteTextOption-uri: string--><!--Device-FileWriteTextOption-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

