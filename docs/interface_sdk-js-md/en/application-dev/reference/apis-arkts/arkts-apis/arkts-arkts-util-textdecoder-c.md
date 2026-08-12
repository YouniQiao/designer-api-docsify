# TextDecoder

The TextDecoder represents a text decoder that accepts a string as input,decodes it in UTF-8 format, and outputs UTF-8 byte stream.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-class TextDecoder--><!--Device-util-class TextDecoder-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

The textDecoder constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-constructor()--><!--Device-TextDecoder-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## create

```TypeScript
static create(encoding?: string, options?: TextDecoderOptions): TextDecoder
```

Replaces the original constructor to process arguments and return a textDecoder object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-static create(encoding?: string, options?: TextDecoderOptions): TextDecoder--><!--Device-TextDecoder-static create(encoding?: string, options?: TextDecoderOptions): TextDecoder-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | Decoding format |
| options | [TextDecoderOptions](arkts-arkts-util-textdecoderoptions-i.md) | No | Options |

**Return value:**

| Type | Description |
| --- | --- |
| [TextDecoder](arkts-arkts-util-textdecoder-c.md) |  |

## decodeToString

```TypeScript
decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string
```

The input is decoded and a string is returned.If options.stream is set to true, any incomplete byte sequences found at the end of the input are internally buffered and will be emitted after the next call to textDecoder.decodeToString().If textDecoder.fatal is set to true, any decoding errors that occur will result in a TypeError being thrown.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string--><!--Device-TextDecoder-decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Uint8Array | Yes | Decoded numbers in accordance with the format. |
| options | [DecodeToStringOptions](arkts-arkts-util-decodetostringoptions-i.md) | No | The default option is set to false. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return decoded text |

## encoding

```TypeScript
get encoding(): string
```

The source encoding's name, lowercased.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-get encoding(): string--><!--Device-TextDecoder-get encoding(): string-End-->

**System capability:** SystemCapability.Utils.Lang

## fatal

```TypeScript
get fatal(): boolean
```

Returns `true` if error mode is "fatal", and `false` otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-get fatal(): boolean--><!--Device-TextDecoder-get fatal(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## ignoreBOM

```TypeScript
get ignoreBOM(): boolean
```

Returns `true` if ignore BOM flag is set, and `false` otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TextDecoder-get ignoreBOM(): boolean--><!--Device-TextDecoder-get ignoreBOM(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

