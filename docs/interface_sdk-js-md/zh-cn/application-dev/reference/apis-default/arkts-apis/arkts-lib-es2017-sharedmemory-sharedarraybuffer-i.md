# SharedArrayBuffer

**ArkTS模式：** 仅支持ArkTS-Dyn

## slice

```TypeScript
slice(begin: number, end?: number): SharedArrayBuffer
```

Returns a section of an SharedArrayBuffer.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SharedArrayBuffer-slice(begin: number, end?: number): SharedArrayBuffer--><!--Device-SharedArrayBuffer-slice(begin: number, end?: number): SharedArrayBuffer-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 是 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SharedArrayBuffer |  |

## [Symbol.species]

```TypeScript
readonly [Symbol.species]: SharedArrayBuffer
```

**类型：** SharedArrayBuffer

**ArkTS模式：** 仅支持ArkTS-Dyn

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "SharedArrayBuffer"
```

**类型：** "SharedArrayBuffer"

**ArkTS模式：** 仅支持ArkTS-Dyn

## byteLength

```TypeScript
readonly byteLength: number
```

Read-only. The length of the ArrayBuffer (in bytes).

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SharedArrayBuffer-readonly byteLength: number--><!--Device-SharedArrayBuffer-readonly byteLength: number-End-->

