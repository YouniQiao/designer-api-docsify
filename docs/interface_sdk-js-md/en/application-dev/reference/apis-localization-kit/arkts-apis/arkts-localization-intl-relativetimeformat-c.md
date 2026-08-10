# RelativeTimeFormat

提供相对时间格式化的能力。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

<!--Device-intl-export class RelativeTimeFormat--><!--Device-intl-export class RelativeTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建相对时间格式化对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-constructor()--><!--Device-RelativeTimeFormat-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object using the current system locale ID.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)
```

创建相对时间格式化对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)--><!--Device-RelativeTimeFormat-constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) | No | 创建相对时间格式化对象时的配置项。 &lt;br&gt;默认值：所有属性都取默认值时的配置项。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Use locale ID zh-CN to create a RelativeTimeFormat object with the localeMatcher set to lookup, numeric set to always, and style set to long.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});
```

## format

```TypeScript
format(value: double, unit: string): string
```

对相对时间进行格式化，返回相对时间字符串。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-format(value: double, unit: string): string--><!--Device-RelativeTimeFormat-format(value: double, unit: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 相对时间格式化的数值。 |
| unit | string | Yes | 相对时间格式化的单位， &lt;br&gt;取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 格式化后的相对时间。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// Obtain the localized representation (in unit of quarter) of number 3 in locale zh-CN.
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3 quarters later'
```

## formatToParts

```TypeScript
formatToParts(value: double, unit: string): Array<object>
```

对相对时间进行格式化，获取格式化结果中各个部分的对象数组。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>--><!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 相对时间格式化的数值。 |
| unit | string | Yes | 相对时间格式化的单位， &lt;br&gt;取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;object&gt; | 格式化结果中各个部分的对象数组。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en and numeric being auto.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en', { numeric: 'auto' });
let parts: Array<object> = formatter.formatToParts(10, 'seconds'); // parts = [ {type: 'literal', value: 'in'}, {type: 'integer', value: 10, unit: 'second'}, {type: 'literal', value: 'seconds'} ]
```

## resolvedOptions

```TypeScript
resolvedOptions(): RelativeTimeFormatResolvedOptions
```

获取相对时间格式化对象的格式化配置项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-resolvedOptions(): RelativeTimeFormatResolvedOptions--><!--Device-RelativeTimeFormat-resolvedOptions(): RelativeTimeFormatResolvedOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) | 相对时间格式化对象的格式化配置项。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en-GB.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// Obtain the options of the RelativeTimeFormat object.
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'
```

