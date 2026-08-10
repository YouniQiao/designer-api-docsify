# FileReadArrayBufferOption

可选项类型，支持readArrayBuffer接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileReadArrayBufferOption--><!--Device-unnamed-export interface FileReadArrayBufferOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadArrayBufferOption-complete?: () => void--><!--Device-FileReadArrayBufferOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadArrayBufferOption-fail?: (data: string, code: number) => void--><!--Device-FileReadArrayBufferOption-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: FileReadArrayBufferResponse) => void
```

接口调用成功的回调函数。返回[FileReadArrayBufferResponse](arkts-corefile-system-file-filereadarraybufferresponse-depr-i.md)。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadArrayBufferOption-success?: (data: FileReadArrayBufferResponse) => void--><!--Device-FileReadArrayBufferOption-success?: (data: FileReadArrayBufferResponse) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [FileReadArrayBufferResponse](arkts-corefile-system-file-filereadarraybufferresponse-depr-i.md) | Yes |  |

## length

```TypeScript
length?: number
```

需要读取的长度，单位为Byte，缺省则读取到文件结尾。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadArrayBufferOption-length?: number--><!--Device-FileReadArrayBufferOption-length?: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## position

```TypeScript
position?: number
```

读取的起始位置，单位为Byte，缺省为文件的起始位置。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileReadArrayBufferOption-position?: number--><!--Device-FileReadArrayBufferOption-position?: number-End-->

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

<!--Device-FileReadArrayBufferOption-uri: string--><!--Device-FileReadArrayBufferOption-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

