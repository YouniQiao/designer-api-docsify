# BigInt

**ArkTS mode:** ArkTS-Dyn only

## toLocaleString

```TypeScript
toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

Returns a string representation appropriate to the host environment's current locale.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No |  |
| options | [BigIntToLocaleStringOptions](../../apis-arkts/arkts-apis/arkts-arkts-bigint-biginttolocalestringoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(radix?: number): string
```

Returns a string representation of an object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt-toString(radix?: number): string--><!--Device-BigInt-toString(radix?: number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): bigint
```

Returns the primitive value of the specified object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt-valueOf(): bigint--><!--Device-BigInt-valueOf(): bigint-End-->

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "BigInt"
```

**Type:** "BigInt"

**ArkTS mode:** ArkTS-Dyn only

