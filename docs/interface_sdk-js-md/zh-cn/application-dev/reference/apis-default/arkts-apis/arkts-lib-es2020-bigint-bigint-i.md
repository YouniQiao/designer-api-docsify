# BigInt

**ArkTS模式：** 仅支持ArkTS-Dyn

## toLocaleString

```TypeScript
toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

Returns a string representation appropriate to the host environment's current locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |  |
| options | [BigIntToLocaleStringOptions](../../apis-arkts/arkts-apis/arkts-arkts-bigint-biginttolocalestringoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(radix?: number): string
```

Returns a string representation of an object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt-toString(radix?: number): string--><!--Device-BigInt-toString(radix?: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): bigint
```

Returns the primitive value of the specified object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-BigInt-valueOf(): bigint--><!--Device-BigInt-valueOf(): bigint-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "BigInt"
```

**类型：** "BigInt"

**ArkTS模式：** 仅支持ArkTS-Dyn

