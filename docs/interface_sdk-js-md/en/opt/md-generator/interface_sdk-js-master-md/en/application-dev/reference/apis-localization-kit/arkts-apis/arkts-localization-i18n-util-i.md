# Util

Provides util functions.

**Since:** 8

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
unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string
```

Converts one measurement unit into another and formats the unit based on the specified locale and style.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [i18n.I18NUtil.unitConvert](arkts-localization-i18n-i18nutil-c.md#unitconvert)

<!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string--><!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes |
| toUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | Yes |
| value | number | Yes |
| locale | string | Yes |
| style | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
