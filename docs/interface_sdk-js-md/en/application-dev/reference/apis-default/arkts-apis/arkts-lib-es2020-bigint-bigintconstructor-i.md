# BigIntConstructor

**ArkTS mode:** 

## Modules to Import

```TypeScript
```

## [[Call]]

```TypeScript
(value: bigint | boolean | number | string): bigint
```

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint \| boolean \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## asIntN

```TypeScript
asIntN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as a 2's-complement signed integer. All higher bits are discarded.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bits](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## asUintN

```TypeScript
asUintN(bits: number, int: bigint): bigint
```

Interprets the low bits of a BigInt as an unsigned integer. All higher bits are discarded.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [bits](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| int | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## prototype

```TypeScript
readonly prototype: BigInt
```

**Type:** [BigInt](arkts-lib-es2020-bigint-bigint-i.md)

**ArkTS mode:** 
