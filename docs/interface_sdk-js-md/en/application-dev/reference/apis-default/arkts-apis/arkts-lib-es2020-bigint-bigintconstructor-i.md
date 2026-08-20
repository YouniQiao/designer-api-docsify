# BigIntConstructor

**Since:** -1

<!--Device-unnamed-interface BigIntConstructor--><!--Device-unnamed-interface BigIntConstructor-End-->

## Modules to Import

```TypeScript
```

## asIntN

```TypeScript
asIntN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer. All higher bits are discarded.

**Since:** -1

<!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | number | Yes |  |
| int | bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## asUintN

```TypeScript
asUintN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer. All higher bits are discarded.

**Since:** -1

<!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bits | number | Yes |  |
| int | bigint | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## constructor

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**Since:** -1

<!--Device-BigIntConstructor-(value: bigint | boolean | number | string): bigint--><!--Device-BigIntConstructor-(value: bigint | boolean | number | string): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint \| boolean \| number \| string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## prototype

```TypeScript
readonly prototype: BigInt
```

**Type:** [BigInt](arkts-lib-es2020-bigint-bigint-i.md)

**Since:** -1

<!--Device-BigIntConstructor-readonly prototype: BigInt--><!--Device-BigIntConstructor-readonly prototype: BigInt-End-->

