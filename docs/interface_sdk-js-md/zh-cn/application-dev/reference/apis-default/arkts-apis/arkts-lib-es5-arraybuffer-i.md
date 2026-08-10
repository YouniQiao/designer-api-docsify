# ArrayBuffer

Represents a raw buffer of binary data, which is used to store data for the different typed arrays. ArrayBuffers cannot be read from or written to directly,but can be passed to a typed array or DataView Object to interpret the raw buffer as needed.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface ArrayBuffer--><!--Device-unnamed-interface ArrayBuffer-End-->

## slice

```TypeScript
slice(begin: number, end?: number): ArrayBuffer
```

Returns a section of an ArrayBuffer.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer--><!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 是 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer |  |

## byteLength

```TypeScript
readonly byteLength: number
```

Read-only. The length of the ArrayBuffer (in bytes).

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ArrayBuffer-readonly byteLength: number--><!--Device-ArrayBuffer-readonly byteLength: number-End-->

