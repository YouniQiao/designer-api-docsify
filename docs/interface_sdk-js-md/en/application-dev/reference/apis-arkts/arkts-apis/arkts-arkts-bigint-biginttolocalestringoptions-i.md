# BigIntToLocaleStringOptions

Options for BigInt.toLocaleString method.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## compactDisplay

```TypeScript
compactDisplay?: string
```

Specifies the compact display format for large numbers.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## currency

```TypeScript
currency?: string
```

The currency to use for currency formatting. Required when style is "currency". Use ISO 4217 currency codes (e.g., "USD", "EUR", "CNY").

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## currencyDisplay

```TypeScript
currencyDisplay?: string
```

Specifies how to display the currency in the formatted string. Valid values: "code" (ISO currency code like "USD"), "symbol" (currency symbol like "\$"),"narrowSymbol" (short symbol like "\$100"), or "name" (full name like "US dollar").

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## localeMatcher

```TypeScript
localeMatcher?: string
```

The locale matching algorithm to use. Valid values: "lookup" (BCP 47 lookup algorithm) or "best fit" (Intl best fit matcher).

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## maximumFractionDigits

```TypeScript
maximumFractionDigits?: double
```

The maximum number of decimal digits to display. Must be an integer between 0 and 100.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## maximumSignificantDigits

```TypeScript
maximumSignificantDigits?: double
```

The maximum number of significant digits to display. Must be an integer between 0 and 100.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## minimumFractionDigits

```TypeScript
minimumFractionDigits?: double
```

The minimum number of decimal digits to display. Must be an integer between 1 and 21.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## minimumIntegerDigits

```TypeScript
minimumIntegerDigits?: double
```

The minimum number of integer digits to display (before the decimal point). Must be an integer between 1 and 21.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## minimumSignificantDigits

```TypeScript
minimumSignificantDigits?: double
```

The minimum number of significant digits to display. Must be an integer between 1 and 21.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## notation

```TypeScript
notation?: string
```

The notation format to use for displaying the number. Valid values: "standard" (default, e.g., "1000"), "scientific" (e.g., "1e3"),"engineering" (e.g., "1E3"), or "compact" (e.g., "1K" for 1000).

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## numberingSystem

```TypeScript
numberingSystem?: string
```

The numbering system to use for number formatting. This option is currently not implemented and has no effect.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## style

```TypeScript
style?: string
```

The formatting style to use. Valid values: "decimal" (default, for plain numbers), "percent" (for percentages).

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## unit

```TypeScript
unit?: string
```

The unit to use for unit formatting. Required when style is "unit". Use UCUM unit codes (e.g., "meter", "second", "kilogram").

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## unitDisplay

```TypeScript
unitDisplay?: string
```

Specifies how to display the unit in the formatted string. Valid values: "short" (e.g., "m"), "long" (e.g., "meters"), or "narrow" (e.g., "m").

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## useGrouping

```TypeScript
useGrouping?: boolean
```

Whether to use grouping separators (e.g., thousands separator "," in "1,000").

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
