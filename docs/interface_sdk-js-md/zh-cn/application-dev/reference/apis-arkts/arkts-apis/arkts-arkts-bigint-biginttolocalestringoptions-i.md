# BigIntToLocaleStringOptions

Options for BigInt.toLocaleString method.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface BigIntToLocaleStringOptions--><!--Device-unnamed-export interface BigIntToLocaleStringOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

## compactDisplay

```TypeScript
compactDisplay?: string
```

Specifies the compact display format for large numbers.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-compactDisplay?: string--><!--Device-BigIntToLocaleStringOptions-compactDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## currency

```TypeScript
currency?: string
```

The currency to use for currency formatting.Required when style is "currency". Use ISO 4217 currency codes (e.g., "USD", "EUR", "CNY").

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-currency?: string--><!--Device-BigIntToLocaleStringOptions-currency?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## currencyDisplay

```TypeScript
currencyDisplay?: string
```

Specifies how to display the currency in the formatted string.Valid values: "code" (ISO currency code like "USD"), "symbol" (currency symbol like "\$"),"narrowSymbol" (short symbol like "\$100"), or "name" (full name like "US dollar").

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-currencyDisplay?: string--><!--Device-BigIntToLocaleStringOptions-currencyDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## localeMatcher

```TypeScript
localeMatcher?: string
```

The locale matching algorithm to use.Valid values: "lookup" (BCP 47 lookup algorithm) or "best fit" (Intl best fit matcher).

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-localeMatcher?: string--><!--Device-BigIntToLocaleStringOptions-localeMatcher?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## maximumFractionDigits

```TypeScript
maximumFractionDigits?: double
```

The maximum number of decimal digits to display.Must be an integer between 0 and 100.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-maximumFractionDigits?: double--><!--Device-BigIntToLocaleStringOptions-maximumFractionDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## maximumSignificantDigits

```TypeScript
maximumSignificantDigits?: double
```

The maximum number of significant digits to display.Must be an integer between 0 and 100.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-maximumSignificantDigits?: double--><!--Device-BigIntToLocaleStringOptions-maximumSignificantDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumFractionDigits

```TypeScript
minimumFractionDigits?: double
```

The minimum number of decimal digits to display.Must be an integer between 1 and 21.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumFractionDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumFractionDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumIntegerDigits

```TypeScript
minimumIntegerDigits?: double
```

The minimum number of integer digits to display (before the decimal point).Must be an integer between 1 and 21.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumIntegerDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumIntegerDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumSignificantDigits

```TypeScript
minimumSignificantDigits?: double
```

The minimum number of significant digits to display.Must be an integer between 1 and 21.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumSignificantDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumSignificantDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## notation

```TypeScript
notation?: string
```

The notation format to use for displaying the number.Valid values: "standard" (default, e.g., "1000"), "scientific" (e.g., "1e3"),"engineering" (e.g., "1E3"), or "compact" (e.g., "1K" for 1000).

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-notation?: string--><!--Device-BigIntToLocaleStringOptions-notation?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## numberingSystem

```TypeScript
numberingSystem?: string
```

The numbering system to use for number formatting.This option is currently not implemented and has no effect.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-numberingSystem?: string--><!--Device-BigIntToLocaleStringOptions-numberingSystem?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## style

```TypeScript
style?: string
```

The formatting style to use.Valid values: "decimal" (default, for plain numbers), "percent" (for percentages).

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-style?: string--><!--Device-BigIntToLocaleStringOptions-style?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## unit

```TypeScript
unit?: string
```

The unit to use for unit formatting.Required when style is "unit". Use UCUM unit codes (e.g., "meter", "second", "kilogram").

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-unit?: string--><!--Device-BigIntToLocaleStringOptions-unit?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## unitDisplay

```TypeScript
unitDisplay?: string
```

Specifies how to display the unit in the formatted string.Valid values: "short" (e.g., "m"), "long" (e.g., "meters"), or "narrow" (e.g., "m").

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-unitDisplay?: string--><!--Device-BigIntToLocaleStringOptions-unitDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## useGrouping

```TypeScript
useGrouping?: boolean
```

Whether to use grouping separators (e.g., thousands separator "," in "1,000").

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-useGrouping?: boolean--><!--Device-BigIntToLocaleStringOptions-useGrouping?: boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

