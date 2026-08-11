# @ohos.intl(国际化-Intl)

本模块提供基础的应用国际化能力，包括时间日期格式化、数字格式化、排序等，相关接口在ECMA 402标准中定义。

[国际化-I18n](arkts-i18n.md)提供其他非ECMA 402定义的国际化接口，与本模块共同使用可提供完整的国际化支持能力。

> **说明：**
> 
> - 本模块接口基于[CLDR](https://cldr.unicode.org)国际化数据库实现，随着CLDR标准的迭代演进，接口处理结果可能会相应调整。例如数字格式化接口，其返回值仅适用于界面展示场景，开发者请勿对返回格式进行
> 硬编码或假设性判断，否则可能导致版本兼容问题。其中，API version 12 对应[CLDR 42](https://cldr.unicode.org/downloads/cldr-42)版本，具体数据变更详情可查阅
> [CLDR官方文档](https://cldr.unicode.org/)。
> 
> - 从API version 11开始，本模块部分接口支持在ArkTS卡片中使用。
> 
> - 从API version 12开始，本模块全接口支持在原子化服务中使用。

**起始版本：** 6

<!--Device-unnamed-declare namespace intl--><!--Device-unnamed-declare namespace intl-End-->

**系统能力：** SystemCapability.Global.I18n

## 汇总

### 类

| 名称 |
| --- |
| [Collator](arkts-localization-intl-collator-c.md) |
| [DateTimeFormat](arkts-localization-intl-datetimeformat-c.md) |
| [Locale](arkts-localization-intl-locale-c.md) |
| [NumberFormat](arkts-localization-intl-numberformat-c.md) |
| [PluralRules](arkts-localization-intl-pluralrules-c.md) |
| [RelativeTimeFormat](arkts-localization-intl-relativetimeformat-c.md) |

### 接口

| 名称 |
| --- |
| [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) |
| [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) |
| [LocaleOptions](arkts-localization-intl-localeoptions-i.md) |
| [NumberOptions](arkts-localization-intl-numberoptions-i.md) |
| [PluralRulesOptions](arkts-localization-intl-pluralrulesoptions-i.md) |
| [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) |
