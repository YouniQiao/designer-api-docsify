# NumberFormat

提供标准的数字格式化的能力。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-intl-export class NumberFormat--><!--Device-intl-export class NumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

使用当前系统区域创建数字格式化对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberFormat-constructor()--><!--Device-NumberFormat-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object using the current system locale ID.
let formatter: intl.NumberFormat = new intl.NumberFormat();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: NumberOptions)
```

根据指定的区域和配置项创建数字格式化对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberFormat-constructor(locale: string | Array<string>, options?: NumberOptions)--><!--Device-NumberFormat-constructor(locale: string | Array<string>, options?: NumberOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | [NumberOptions](arkts-localization-intl-numberoptions-i.md) | No | 创建数字格式化对象时可设置的配置项。 &lt;br&gt;默认值：所有属性都取默认值时的配置项。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with locale ID being en-GB, style being decimal, and notation being scientific.
let formatter: intl.NumberFormat = new intl.NumberFormat('en-GB', { style: 'decimal', notation: 'scientific' });
```

## format

```TypeScript
format(num: double): string
```

对数字进行格式化，返回格式化后的数字字符串。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberFormat-format(num: double): string--><!--Device-NumberFormat-format(num: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| num | double | Yes | 数字对象。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 格式化后的数字字符串。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with a locale ID array. The locale ID en-GB is valid and therefore is used.
let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
let formattedNumber: string = formatter.format(1223); // formattedNumber = 1.223E3
let options: intl.NumberOptions = {
  roundingPriority: 'lessPrecision',
  maximumFractionDigits: 3,
  maximumSignificantDigits: 3
}
formatter = new intl.NumberFormat('en', options);
let result: string = formatter.format(1.23456); // result = 1.23
```

## formatRange

```TypeScript
formatRange(startRange: double, endRange: double): string
```

对数字范围进行格式化，返回格式化后的数字范围字符串。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NumberFormat-formatRange(startRange: double, endRange: double): string--><!--Device-NumberFormat-formatRange(startRange: double, endRange: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startRange | double | Yes | 数字范围的起始值。 |
| endRange | double | Yes | 数字范围的终止值。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 格式化后的数字范围字符串。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat('en-US', { style: 'unit', unit: 'meter' });
let formattedRange: string = formatter.formatRange(0, 3); // formattedRange: 0–3 m
```

## resolvedOptions

```TypeScript
resolvedOptions(): NumberOptions
```

获取创建数字格式化对象时设置的配置项。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NumberFormat-resolvedOptions(): NumberOptions--><!--Device-NumberFormat-resolvedOptions(): NumberOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [NumberOptions](arkts-localization-intl-numberoptions-i.md) | 创建数字格式化对象时设置的配置项。 |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
// Obtain the options of the NumberFormat object.
let options: intl.NumberOptions = formatter.resolvedOptions();
let style: string | undefined = options.style; // style = 'decimal'
let notation: string | undefined = options.notation; // notation = 'scientific'
```

