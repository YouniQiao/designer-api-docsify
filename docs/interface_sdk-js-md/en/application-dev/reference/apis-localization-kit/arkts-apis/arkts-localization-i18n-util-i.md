# Util

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [i18n.I18NUtil](arkts-localization-i18n-i18nutil-c.md)

<!--Device-i18n-export interface Util--><!--Device-i18n-export interface Util-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## unitConvert

```TypeScript
unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string
```

将fromUnit的单位转换为toUnit的单位，并根据区域与风格进行格式化。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [i18n.I18NUtil.unitConvert](arkts-localization-i18n-i18nutil-c.md#unitconvert)

<!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string--><!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes | 要被转换的单位。 |
| toUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes | 要转换为的单位。 |
| value | double | Yes | 要被转换的单位的数量值。 |
| locale | string | Yes | 格式化时使用的区域ID，如：zh-Hans-CN。 |
| style | string | No | 格式化使用的风格，取值包括：'long', 'short', 'narrow'。默认值：short。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 按照toUnit的单位格式化后，得到的字符串。 |

