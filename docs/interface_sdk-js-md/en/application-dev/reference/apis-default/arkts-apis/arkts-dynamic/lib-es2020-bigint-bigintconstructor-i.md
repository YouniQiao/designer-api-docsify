# BigIntConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Call]]

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint \| boolean \| number \| string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## asIntN

```TypeScript
asIntN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer.All higher bits are discarded.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | number | Yes |  |
| int | bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## asUintN

```TypeScript
asUintN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer.All higher bits are discarded.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | number | Yes |  |
| int | bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## prototype

```TypeScript
readonly prototype: BigInt
```

**Type:** BigInt

**ArkTS mode:** ArkTS-Dyn only

