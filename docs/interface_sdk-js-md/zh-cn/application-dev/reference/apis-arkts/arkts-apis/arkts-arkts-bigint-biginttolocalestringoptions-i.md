# BigIntToLocaleStringOptions

BigInt.toLocaleString方法的选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export interface BigIntToLocaleStringOptions--><!--Device-unnamed-export interface BigIntToLocaleStringOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## compactDisplay

```TypeScript
compactDisplay?: string
```

指定大数值的紧凑显示格式。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-compactDisplay?: string--><!--Device-BigIntToLocaleStringOptions-compactDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## currency

```TypeScript
currency?: string
```

货币格式化所使用的货币。 当style为"currency"时必填，使用ISO 4217货币代码（例如"USD"、"EUR"、"CNY"）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-currency?: string--><!--Device-BigIntToLocaleStringOptions-currency?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## currencyDisplay

```TypeScript
currencyDisplay?: string
```

指定货币在格式化结果字符串中的显示方式。 取值："code"（ISO货币代码，如"USD"）、"symbol"（货币符号，如"\$"）、 "narrowSymbol"（窄符号，如"\$100"）或"name"（全称，如"US dollar"）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-currencyDisplay?: string--><!--Device-BigIntToLocaleStringOptions-currencyDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## localeMatcher

```TypeScript
localeMatcher?: string
```

所使用的区域匹配算法。 取值："lookup"（BCP 47查找算法）或"best fit"（Intl最佳匹配算法）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-localeMatcher?: string--><!--Device-BigIntToLocaleStringOptions-localeMatcher?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## maximumFractionDigits

```TypeScript
maximumFractionDigits?: double
```

显示的小数位数上限。 取值约束：必须为0到100之间的整数。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-maximumFractionDigits?: double--><!--Device-BigIntToLocaleStringOptions-maximumFractionDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## maximumSignificantDigits

```TypeScript
maximumSignificantDigits?: double
```

显示的有效数字位数上限。 取值约束：必须为0到100之间的整数。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-maximumSignificantDigits?: double--><!--Device-BigIntToLocaleStringOptions-maximumSignificantDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumFractionDigits

```TypeScript
minimumFractionDigits?: double
```

显示的小数位数下限。 取值约束：必须为1到21之间的整数。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumFractionDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumFractionDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumIntegerDigits

```TypeScript
minimumIntegerDigits?: double
```

显示的整数位数下限（小数点前）。 取值约束：必须为1到21之间的整数。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumIntegerDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumIntegerDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## minimumSignificantDigits

```TypeScript
minimumSignificantDigits?: double
```

显示的有效数字位数下限。 取值约束：必须为1到21之间的整数。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-minimumSignificantDigits?: double--><!--Device-BigIntToLocaleStringOptions-minimumSignificantDigits?: double-End-->

**系统能力：** SystemCapability.Utils.Lang

## notation

```TypeScript
notation?: string
```

显示数值时使用的计数法格式。 取值："standard"（默认，如"1000"）、"scientific"（如"1e3"）、 "engineering"（如"1E3"）或"compact"（如1000显示为"1K"）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-notation?: string--><!--Device-BigIntToLocaleStringOptions-notation?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## numberingSystem

```TypeScript
numberingSystem?: string
```

数值格式化所使用的记数系统。 该选项当前尚未实现，不生效。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-numberingSystem?: string--><!--Device-BigIntToLocaleStringOptions-numberingSystem?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## style

```TypeScript
style?: string
```

所使用的格式化样式。 取值："decimal"（默认，用于普通数值）或"percent"（用于百分比）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-style?: string--><!--Device-BigIntToLocaleStringOptions-style?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## unit

```TypeScript
unit?: string
```

单位格式化所使用的单位。 当style为"unit"时必填，使用UCUM单位代码（例如"meter"、"second"、"kilogram"）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-unit?: string--><!--Device-BigIntToLocaleStringOptions-unit?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## unitDisplay

```TypeScript
unitDisplay?: string
```

指定单位在格式化结果字符串中的显示方式。 取值："short"（如"m"）、"long"（如"meters"）或"narrow"（如"m"）。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-unitDisplay?: string--><!--Device-BigIntToLocaleStringOptions-unitDisplay?: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## useGrouping

```TypeScript
useGrouping?: boolean
```

是否使用分组分隔符（例如"1,000"中的千位分隔符","）。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigIntToLocaleStringOptions-useGrouping?: boolean--><!--Device-BigIntToLocaleStringOptions-useGrouping?: boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

