# FileMoveOption

可选项类型，支持move接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileMoveOption--><!--Device-unnamed-export interface FileMoveOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileMoveOption-complete?: () => void--><!--Device-FileMoveOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileMoveOption-fail?: (data: string, code: number) => void--><!--Device-FileMoveOption-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (uri: string) => void
```

接口调用成功的回调函数，返回文件要移动到的位置的URI。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileMoveOption-success?: (uri: string) => void--><!--Device-FileMoveOption-success?: (uri: string) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes |  |

## dstUri

```TypeScript
dstUri: string
```

文件要移动到的位置的URI。由于轻量级穿戴设备底层文件系统的限制，该值必须满足以下要求：1. URI 中不得包含以下特殊字符：\"*+,:;&lt;=&gt;?[]|\x7F等。2. 最大允许字符长度为128个字符。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileMoveOption-dstUri: string--><!--Device-FileMoveOption-dstUri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## srcUri

```TypeScript
srcUri: string
```

要移动的文件的URI。由于轻量级穿戴设备底层文件系统的限制，该值必须满足以下要求：1、URI 中不得包含以下特殊字符：“\"*+,:;&lt;=&gt;?[]\

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileMoveOption-srcUri: string--><!--Device-FileMoveOption-srcUri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

