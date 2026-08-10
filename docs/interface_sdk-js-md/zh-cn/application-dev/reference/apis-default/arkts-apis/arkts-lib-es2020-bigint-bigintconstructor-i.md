# BigIntConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Call]]

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint \| boolean \| number \| string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## asIntN

```TypeScript
asIntN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer.All higher bits are discarded.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | number | 是 |  |
| int | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## asUintN

```TypeScript
asUintN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer.All higher bits are discarded.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | number | 是 |  |
| int | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## prototype

```TypeScript
readonly prototype: BigInt
```

**类型：** [BigInt](../../apis-arkts/arkts-apis/arkts-arkts-bigint-c.md)

**ArkTS模式：** 仅支持ArkTS-Dyn

