# @ohos.i18n(国际化-I18n)

本模块提供系统相关的以及增强的[国际化](../../../internationalization/i18n-l10n.md)能力，包括区域管理、电话号码处理、日历等，相关接口为 [ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/)标准中未定义的补充接口。 [国际化-Intl](arkts-intl.md)模块提供了ECMA 402标准定义的基础国际化接口，与本模块共同使用可提供完整的国际化能力。接口中使用的名词定义如下：  
- 模式字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table)和单引号包裹的自定义文本自由组 合而成的字符串。 - 框架字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table)自由组合而成的字符串，不支持自 定义文本。

> **说明：**&gt;
> - 本模块接口基于[CLDR](https://cldr.unicode.org)国际化数据库实现，随着CLDR标准的迭代演进，接口处理结果可能会相应调整。例如时间日期格式化接口，其返回值仅适用于界面展示场景，开发者请勿对返回格式
> 进行硬编码或假设性判断，否则可能导致版本兼容问题。其中，API version 12 对应[CLDR 42](https://cldr.unicode.org/downloads/cldr-42)版本，具体数据变更详情可查阅
> [CLDR官方文档](https://cldr.unicode.org/)。&gt;
> - 从API version 11开始，本模块部分接口支持在ArkTS卡片中使用。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addPreferredLanguage(国际化-I18n)](arkts-localization-i18n-addpreferredlanguage-f.md) |
| [getCalendar(国际化-I18n)](arkts-localization-i18n-getcalendar-f.md) |
| [getChineseCalendar(国际化-I18n)](arkts-localization-i18n-getchinesecalendar-f.md) |
| [getDisplayCountry(国际化-I18n)](arkts-localization-i18n-getdisplaycountry-f.md) |
| [getDisplayLanguage(国际化-I18n)](arkts-localization-i18n-getdisplaylanguage-f.md) |
| [getFirstPreferredLanguage(国际化-I18n)](arkts-localization-i18n-getfirstpreferredlanguage-f.md) |
| [getInstance(国际化-I18n)](arkts-localization-i18n-getinstance-f.md) |
| [getLineInstance(国际化-I18n)](arkts-localization-i18n-getlineinstance-f.md) |
| [getPreferredLanguageList(国际化-I18n)](arkts-localization-i18n-getpreferredlanguagelist-f.md) |
| [getSimpleDateTimeFormatByPattern(国际化-I18n)](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md) |
| [getSimpleDateTimeFormatByPattern(国际化-I18n)](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md) |
| [getSimpleDateTimeFormatBySkeleton(国际化-I18n)](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md) |
| [getSimpleDateTimeFormatBySkeleton(国际化-I18n)](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md) |
| [getSimpleNumberFormatBySkeleton(国际化-I18n)](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md) |
| [getSimpleNumberFormatBySkeleton(国际化-I18n)](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md) |
| [getSystemLanguage(国际化-I18n)](arkts-localization-i18n-getsystemlanguage-f.md) |
| [getSystemLocale(国际化-I18n)](arkts-localization-i18n-getsystemlocale-f.md) |
| [getSystemRegion(国际化-I18n)](arkts-localization-i18n-getsystemregion-f.md) |
| [getTimeZone(国际化-I18n)](arkts-localization-i18n-gettimezone-f.md) |
| [is24HourClock(国际化-I18n)](arkts-localization-i18n-is24hourclock-f.md) |
| [isRTL(国际化-I18n)](arkts-localization-i18n-isrtl-f.md) |
| [removePreferredLanguage(国际化-I18n)](arkts-localization-i18n-removepreferredlanguage-f.md) |
| [set24HourClock(国际化-I18n)](arkts-localization-i18n-set24hourclock-f.md) |

### 类

| 名称 |
| --- |
| [AdvancedMeasureFormat(国际化-I18n)](arkts-localization-i18n-advancedmeasureformat-c.md) |
| [BreakIterator(国际化-I18n)](arkts-localization-i18n-breakiterator-c.md) |
| [Calendar(国际化-I18n)](arkts-localization-i18n-calendar-c.md) |
| [Character(国际化-I18n)](arkts-localization-i18n-character-c.md) |
| [ChineseCalendar(国际化-I18n)](arkts-localization-i18n-chinesecalendar-c.md) |
| [EntityRecognizer(国际化-I18n)](arkts-localization-i18n-entityrecognizer-c.md) |
| [HolidayManager(国际化-I18n)](arkts-localization-i18n-holidaymanager-c.md) |
| [I18NUtil(国际化-I18n)](arkts-localization-i18n-i18nutil-c.md) |
| [IndexUtil(国际化-I18n)](arkts-localization-i18n-indexutil-c.md) |
| [ISO8601DateTimeFormat(国际化-I18n)](arkts-localization-i18n-iso8601datetimeformat-c.md) |
| [Normalizer(国际化-I18n)](arkts-localization-i18n-normalizer-c.md) |
| [PhoneNumberFormat(国际化-I18n)](arkts-localization-i18n-phonenumberformat-c.md) |
| [SimpleDateTimeFormat(国际化-I18n)](arkts-localization-i18n-simpledatetimeformat-c.md) |
| [SimpleNumberFormat(国际化-I18n)](arkts-localization-i18n-simplenumberformat-c.md) |
| [StyledDateTimeFormat(国际化-I18n)](arkts-localization-i18n-styleddatetimeformat-c.md) |
| [StyledNumberFormat(国际化-I18n)](arkts-localization-i18n-stylednumberformat-c.md) |
| [SymbolDateTimeFormat(国际化-I18n)](arkts-localization-i18n-symboldatetimeformat-c.md) |
| [SymbolNumberFormat(国际化-I18n)](arkts-localization-i18n-symbolnumberformat-c.md) |
| [System(国际化-I18n)](arkts-localization-i18n-system-c.md) |
| [TimeZone(国际化-I18n)](arkts-localization-i18n-timezone-c.md) |
| [Transliterator(国际化-I18n)](arkts-localization-i18n-transliterator-c.md) |
| [Unicode(国际化-I18n)](arkts-localization-i18n-unicode-c.md) |
| [ZoneOffsetTransition(国际化-I18n)](arkts-localization-i18n-zoneoffsettransition-c.md) |
| [ZoneRules(国际化-I18n)](arkts-localization-i18n-zonerules-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [System(国际化-I18n)](arkts-localization-i18n-system-c-sys.md) |
| [SystemLocaleManager(国际化-I18n)](arkts-localization-i18n-systemlocalemanager-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AdvancedMeasureFormatOptions(国际化-I18n)](arkts-localization-i18n-advancedmeasureformatoptions-i.md) |
| [ChineseCalendarTime(国际化-I18n)](arkts-localization-i18n-chinesecalendartime-i.md) |
| [EncodingInfo(国际化-I18n)](arkts-localization-i18n-encodinginfo-i.md) |
| [EntityInfoItem(国际化-I18n)](arkts-localization-i18n-entityinfoitem-i.md) |
| [HolidayInfoItem(国际化-I18n)](arkts-localization-i18n-holidayinfoitem-i.md) |
| [HolidayLocalName(国际化-I18n)](arkts-localization-i18n-holidaylocalname-i.md) |
| [ISO8601DateTimeFormatOptions(国际化-I18n)](arkts-localization-i18n-iso8601datetimeformatoptions-i.md) |
| [PhoneNumberFormatOptions(国际化-I18n)](arkts-localization-i18n-phonenumberformatoptions-i.md) |
| [ResolvedSymbolDateTimeFormatOptions(国际化-I18n)](arkts-localization-i18n-resolvedsymboldatetimeformatoptions-i.md) |
| [ResolvedSymbolNumberFormatOptions(国际化-I18n)](arkts-localization-i18n-resolvedsymbolnumberformatoptions-i.md) |
| [StyledDateTimeFormatOptions(国际化-I18n)](arkts-localization-i18n-styleddatetimeformatoptions-i.md) |
| [StyledNumberFormatOptions(国际化-I18n)](arkts-localization-i18n-stylednumberformatoptions-i.md) |
| [SymbolDateTimeFormatOptions(国际化-I18n)](arkts-localization-i18n-symboldatetimeformatoptions-i.md) |
| [SymbolNumberFormatOptions(国际化-I18n)](arkts-localization-i18n-symbolnumberformatoptions-i.md) |
| [UnitInfo(国际化-I18n)](arkts-localization-i18n-unitinfo-i.md) |
| [Util(国际化-I18n)](arkts-localization-i18n-util-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [LocaleItem(国际化-I18n)](arkts-localization-i18n-localeitem-i-sys.md) |
| [SortOptions(国际化-I18n)](arkts-localization-i18n-sortoptions-i-sys.md) |
| [TimeZoneCityItem(国际化-I18n)](arkts-localization-i18n-timezonecityitem-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [NormalizerMode(国际化-I18n)](arkts-localization-i18n-normalizermode-e.md) |
| [TemperatureType(国际化-I18n)](arkts-localization-i18n-temperaturetype-e.md) |
| [UnitUsage(国际化-I18n)](arkts-localization-i18n-unitusage-e.md) |
| [WeekDay(国际化-I18n)](arkts-localization-i18n-weekday-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SuggestionType(国际化-I18n)](arkts-localization-i18n-suggestiontype-e-sys.md) |
<!--DelEnd-->
