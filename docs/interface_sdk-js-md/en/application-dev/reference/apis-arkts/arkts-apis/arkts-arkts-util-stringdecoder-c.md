# StringDecoder

Provide the ability to decode binary streams into strings. The supported encoding types include: utf-8, iso-8859-2,koi8-r, macintosh, windows-1250, windows-1251, gbk, gb18030, big5, utf-16be, utf-16 le, etc.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-class StringDecoder--><!--Device-util-class StringDecoder-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(encoding?: string)
```

The StringDecoder constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-StringDecoder-constructor(encoding?: string)--><!--Device-StringDecoder-constructor(encoding?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | Encoding type of the input data.Default: utf8. |

## end

```TypeScript
end(chunk?: string | Uint8Array): string
```

Returns any remaining input stored in the internal buffer as a string. After end() is called,this object can be reused for new input.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-StringDecoder-end(chunk?: string | Uint8Array): string--><!--Device-StringDecoder-end(chunk?: string | Uint8Array): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunk | string \| Uint8Array | No | The bytes to decode. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns any remaining input stored in the internal buffer as a string. |

## write

```TypeScript
write(chunk: string | Uint8Array): string
```

Returns a decoded string, ensuring that any incomplete multiple byte characters at the end of the Uint8Array are omitted from the returned string and stored in an internal buffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-StringDecoder-write(chunk: string | Uint8Array): string--><!--Device-StringDecoder-write(chunk: string | Uint8Array): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chunk | string \| Uint8Array | Yes | The bytes to decode. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns a decoded string. |

