# FileGetOption

可选项类型，支持get接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileGetOption--><!--Device-unnamed-export interface FileGetOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileGetOption-complete?: () => void--><!--Device-FileGetOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileGetOption-fail?: (data: string, code: number) => void--><!--Device-FileGetOption-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (file: FileResponse) => void
```

接口调用成功的回调函数。 返回[FileResponse](arkts-corefile-system-file-fileresponse-depr-i.md)。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileGetOption-success?: (file: FileResponse) => void--><!--Device-FileGetOption-success?: (file: FileResponse) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | [FileResponse](arkts-corefile-system-file-fileresponse-depr-i.md) | Yes |  |

## recursive

```TypeScript
recursive?: boolean
```

是否进行递归获取子目录文件列表，true为进行该操作，缺省为false。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileGetOption-recursive?: boolean--><!--Device-FileGetOption-recursive?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## uri

```TypeScript
uri: string
```

文件的URI。由于轻量级穿戴设备底层文件系统的限制，该值必须满足以下要求：1. URI 中不得包含以下特殊字符：\"*+,:;&lt;=&gt;?[]|\x7F等。2. 最大允许字符长度为128个字符。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileGetOption-uri: string--><!--Device-FileGetOption-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

