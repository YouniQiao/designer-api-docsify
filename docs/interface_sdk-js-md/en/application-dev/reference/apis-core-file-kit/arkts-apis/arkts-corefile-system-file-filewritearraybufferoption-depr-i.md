# FileWriteArrayBufferOption

可选项类型，支持writeArrayBuffer接口使用。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-unnamed-export interface FileWriteArrayBufferOption--><!--Device-unnamed-export interface FileWriteArrayBufferOption-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteArrayBufferOption-complete?: () => void--><!--Device-FileWriteArrayBufferOption-complete?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteArrayBufferOption-fail?: (data: string, code: number) => void--><!--Device-FileWriteArrayBufferOption-fail?: (data: string, code: number) => void-End-->

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

<!--Device-FileWriteArrayBufferOption-success?: () => void--><!--Device-FileWriteArrayBufferOption-success?: () => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## append

```TypeScript
append?: boolean
```

是否追加模式，默认为false。当设置为true时，position参数无效。true为追加，false为不追加。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteArrayBufferOption-append?: boolean--><!--Device-FileWriteArrayBufferOption-append?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## buffer

```TypeScript
buffer: Uint8Array
```

写入的Buffer。

**Type:** Uint8Array

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteArrayBufferOption-buffer: Uint8Array--><!--Device-FileWriteArrayBufferOption-buffer: Uint8Array-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## position

```TypeScript
position?: number
```

文件写入的起始偏移位置，单位为Byte，默认为0。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 10

<!--Device-FileWriteArrayBufferOption-position?: number--><!--Device-FileWriteArrayBufferOption-position?: number-End-->

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

<!--Device-FileWriteArrayBufferOption-uri: string--><!--Device-FileWriteArrayBufferOption-uri: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

