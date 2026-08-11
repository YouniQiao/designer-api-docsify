# BigIntConstructor

## [[Call]]

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint \| boolean \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## asIntN

```TypeScript
asIntN(bits: number, number: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer.All higher bits are discarded.

<!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bits | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## asUintN

```TypeScript
asUintN(bits: number, number: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer.All higher bits are discarded.

<!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bits | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## prototype

```TypeScript
readonly prototype: BigInt
```

**Type:** BigInt
