# Util

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [I18NUtil](arkts-localization-i18n-i18nutil-c.md#I18NUtil)

<!--Device-i18n-export interface Util--><!--Device-i18n-export interface Util-End-->

**系统能力：** SystemCapability.Global.I18n

## unitConvert

```TypeScript
unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string
```

将fromUnit的单位转换为toUnit的单位，并根据区域与风格进行格式化。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [unitConvert](arkts-localization-i18n-i18nutil-c.md#unitConvert)

<!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string--><!--Device-Util-unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: double, locale: string, style?: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fromUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | 是 |
| toUnit | [UnitInfo](arkts-localization-i18n-unitinfo-i.md) | 是 |
| value | number | 是 |
| locale | string | 是 |
| style | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |
