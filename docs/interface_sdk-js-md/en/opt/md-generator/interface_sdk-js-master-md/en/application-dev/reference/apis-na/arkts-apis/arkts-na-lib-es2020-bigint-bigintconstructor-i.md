# BigIntConstructor

**Since:** -1

<!--Device-unnamed-interface BigIntConstructor--><!--Device-unnamed-interface BigIntConstructor-End-->

## Modules to Import

```TypeScript
```

## asIntN

```TypeScript
asIntN(bits: number, number: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer. All higher bits are discarded.

**Since:** -1

<!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asIntN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bits](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## asUintN

```TypeScript
asUintN(bits: number, number: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer. All higher bits are discarded.

**Since:** -1

<!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint--><!--Device-BigIntConstructor-asUintN(bits: number, int: bigint): bigint-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bits](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## constructor

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**Since:** -1

<!--Device-BigIntConstructor-(value: bigint | boolean | number | string): bigint--><!--Device-BigIntConstructor-(value: bigint | boolean | number | string): bigint-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint \| boolean \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## prototype

```TypeScript
readonly prototype: BigInt
```

**Type:** [BigInt](arkts-na-lib-es2020-bigint-bigint-i.md)

**Since:** -1

<!--Device-BigIntConstructor-readonly prototype: BigInt--><!--Device-BigIntConstructor-readonly prototype: BigInt-End-->
