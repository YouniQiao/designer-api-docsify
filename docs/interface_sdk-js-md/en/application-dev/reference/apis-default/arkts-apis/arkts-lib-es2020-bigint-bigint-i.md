# BigInt

**Since:** -1

<!--Device-unnamed-interface BigInt--><!--Device-unnamed-interface BigInt-End-->

## Modules to Import

```TypeScript
```

## toLocaleString

```TypeScript
toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

Returns a string representation appropriate to the host environment's current locale.

**Since:** -1

<!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No |  |
| options | [BigIntToLocaleStringOptions](arkts-lib-es2020-bigint-biginttolocalestringoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## toString

```TypeScript
toString(radix?: number): string
```

Returns a string representation of an object.

**Since:** -1

<!--Device-BigInt-toString(radix?: number): string--><!--Device-BigInt-toString(radix?: number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## valueOf

```TypeScript
valueOf(): bigint
```

Returns the primitive value of the specified object.

**Since:** -1

<!--Device-BigInt-valueOf(): bigint--><!--Device-BigInt-valueOf(): bigint-End-->

**Return value:**

| Type | Description |
| --- | --- |
## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "BigInt"
```

**Type:** "BigInt"

**Since:** -1

<!--Device-BigInt-readonly [Symbol.toStringTag]: "BigInt"--><!--Device-BigInt-readonly [Symbol.toStringTag]: "BigInt"-End-->

