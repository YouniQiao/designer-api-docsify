# ArrayBuffer

Represents a raw buffer of binary data, which is used to store data for the different typed arrays. ArrayBuffers cannot be read from or written to directly, but can be passed to a typed array or DataView Object to interpret the raw buffer as needed.

**Since:** -1

<!--Device-unnamed-interface ArrayBuffer--><!--Device-unnamed-interface ArrayBuffer-End-->

## Modules to Import

```TypeScript
```

## slice

```TypeScript
slice(begin: number, end?: number): ArrayBuffer
```

Returns a section of an ArrayBuffer.

**Since:** -1

<!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer--><!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| begin | number | Yes |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

## byteLength

```TypeScript
readonly byteLength: number
```

Read-only. The length of the ArrayBuffer (in bytes).

**Type:** number

**Since:** -1

<!--Device-ArrayBuffer-readonly byteLength: number--><!--Device-ArrayBuffer-readonly byteLength: number-End-->
