# @ohos.i18n

本模块提供系统相关的以及增强的[国际化](../../../internationalization/i18n-l10n.md)能力，包括区域管理、电话号码处理、日历等，相关接口为 [ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/)标准中未定义的补充接口。 [国际化-Intl](arkts-intl.md#@ohos.intl(国际化-Intl))模块提供了ECMA 402标准定义的基础国际化接口，与本模块共同使用可提供完整的国际化能力。接口中使用的名词定义如下： - 模式字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table)和单引号包裹的自定义文本自由组 合而成的字符串。 - 框架字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table)自由组合而成的字符串，不支持自 定义文本。 > **说明：** > > - 本模块接口基于[CLDR](https://cldr.unicode.org)国际化数据库实现，随着CLDR标准的迭代演进，接口处理结果可能会相应调整。例如时间日期格式化接口，其返回值仅适用于界面展示场景，开发者请勿对返回格式 > 进行硬编码或假设性判断，否则可能导致版本兼容问题。其中，API version 12 对应[CLDR 42](https://cldr.unicode.org/downloads/cldr-42)版本，具体数据变更详情可查阅 > [CLDR官方文档](https://cldr.unicode.org/)。 > > - 从API version 11开始，本模块部分接口支持在ArkTS卡片中使用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace i18n--><!--Device-unnamed-declare namespace i18n-End-->

**系统能力：** SystemCapability.Global.I18n

## 汇总

### 函数

| 名称 |
| --- |
| [addPreferredLanguage](arkts-localization-i18n-addpreferredlanguage-f.md#addPreferredLanguage) |
| [getCalendar](arkts-localization-i18n-getcalendar-f.md#getCalendar) |
| [getChineseCalendar](arkts-localization-i18n-getchinesecalendar-f.md#getChineseCalendar) |
| [getDisplayCountry](arkts-localization-i18n-getdisplaycountry-f.md#getDisplayCountry) |
| [getDisplayLanguage](arkts-localization-i18n-getdisplaylanguage-f.md#getDisplayLanguage) |
| [getFirstPreferredLanguage](arkts-localization-i18n-getfirstpreferredlanguage-f.md#getFirstPreferredLanguage) |
| [getInstance](arkts-localization-i18n-getinstance-f.md#getInstance) |
| [getLineInstance](arkts-localization-i18n-getlineinstance-f.md#getLineInstance) |
| [getPreferredLanguageList](arkts-localization-i18n-getpreferredlanguagelist-f.md#getPreferredLanguageList) |
| [getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md#getSimpleDateTimeFormatByPattern) |
| [getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md#getSimpleDateTimeFormatByPattern) |
| [getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton) |
| [getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton) |
| [getSimpleNumberFormatBySkeleton](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md#getSimpleNumberFormatBySkeleton) |
| [getSimpleNumberFormatBySkeleton](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md#getSimpleNumberFormatBySkeleton) |
| [getSystemLanguage](arkts-localization-i18n-getsystemlanguage-f.md#getSystemLanguage) |
| [getSystemLocale](arkts-localization-i18n-getsystemlocale-f.md#getSystemLocale) |
| [getSystemRegion](arkts-localization-i18n-getsystemregion-f.md#getSystemRegion) |
| [getTimeZone](arkts-localization-i18n-gettimezone-f.md#getTimeZone) |
| [is24HourClock](arkts-localization-i18n-is24hourclock-f.md#is24HourClock) |
| [isRTL](arkts-localization-i18n-isrtl-f.md#isRTL) |
| [removePreferredLanguage](arkts-localization-i18n-removepreferredlanguage-f.md#removePreferredLanguage) |
| [set24HourClock](arkts-localization-i18n-set24hourclock-f.md#set24HourClock) |

### 类

| 名称 |
| --- |
| [AdvancedMeasureFormat](arkts-localization-i18n-advancedmeasureformat-c.md) |
| [BreakIterator](arkts-localization-i18n-breakiterator-c.md) |
| [Calendar](arkts-localization-i18n-calendar-c.md) |
| [Character](arkts-localization-i18n-character-c.md) |
| [ChineseCalendar](arkts-localization-i18n-chinesecalendar-c.md) |
| [EntityRecognizer](arkts-localization-i18n-entityrecognizer-c.md) |
| [HolidayManager](arkts-localization-i18n-holidaymanager-c.md) |
| [I18NUtil](arkts-localization-i18n-i18nutil-c.md) |
| [ISO8601DateTimeFormat](arkts-localization-i18n-iso8601datetimeformat-c.md) |
| [IndexUtil](arkts-localization-i18n-indexutil-c.md) |
| [Normalizer](arkts-localization-i18n-normalizer-c.md) |
| [PhoneNumberFormat](arkts-localization-i18n-phonenumberformat-c.md) |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |
| [SimpleNumberFormat](arkts-localization-i18n-simplenumberformat-c.md) |
| [StyledDateTimeFormat](arkts-localization-i18n-styleddatetimeformat-c.md) |
| [StyledNumberFormat](arkts-localization-i18n-stylednumberformat-c.md) |
| [SymbolDateTimeFormat](arkts-localization-i18n-symboldatetimeformat-c.md) |
| [SymbolNumberFormat](arkts-localization-i18n-symbolnumberformat-c.md) |
| [System](arkts-localization-i18n-system-c.md) |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |
| [Transliterator](arkts-localization-i18n-transliterator-c.md) |
| [Unicode](arkts-localization-i18n-unicode-c.md) |
| [ZoneOffsetTransition](arkts-localization-i18n-zoneoffsettransition-c.md) |
| [ZoneRules](arkts-localization-i18n-zonerules-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [System](arkts-localization-i18n-system-c-sys.md) |
| [SystemLocaleManager](arkts-localization-i18n-systemlocalemanager-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AdvancedMeasureFormatOptions](arkts-localization-i18n-advancedmeasureformatoptions-i.md) |
| [ChineseCalendarTime](arkts-localization-i18n-chinesecalendartime-i.md) |
| [EncodingInfo](arkts-localization-i18n-encodinginfo-i.md) |
| [EntityInfoItem](arkts-localization-i18n-entityinfoitem-i.md) |
| [HolidayInfoItem](arkts-localization-i18n-holidayinfoitem-i.md) |
| [HolidayLocalName](arkts-localization-i18n-holidaylocalname-i.md) |
| [ISO8601DateTimeFormatOptions](arkts-localization-i18n-iso8601datetimeformatoptions-i.md) |
| [PhoneNumberFormatOptions](arkts-localization-i18n-phonenumberformatoptions-i.md) |
| [ResolvedSymbolDateTimeFormatOptions](arkts-localization-i18n-resolvedsymboldatetimeformatoptions-i.md) |
| [ResolvedSymbolNumberFormatOptions](arkts-localization-i18n-resolvedsymbolnumberformatoptions-i.md) |
| [StyledDateTimeFormatOptions](arkts-localization-i18n-styleddatetimeformatoptions-i.md) |
| [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) |
| [SymbolDateTimeFormatOptions](arkts-localization-i18n-symboldatetimeformatoptions-i.md) |
| [SymbolNumberFormatOptions](arkts-localization-i18n-symbolnumberformatoptions-i.md) |
| [UnitInfo](arkts-localization-i18n-unitinfo-i.md) |
| [Util](arkts-localization-i18n-util-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [LocaleItem](arkts-localization-i18n-localeitem-i-sys.md) |
| [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) |
| [TimeZoneCityItem](arkts-localization-i18n-timezonecityitem-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [NormalizerMode](arkts-localization-i18n-normalizermode-e.md) |
| [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) |
| [UnitUsage](arkts-localization-i18n-unitusage-e.md) |
| [WeekDay](arkts-localization-i18n-weekday-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SuggestionType](arkts-localization-i18n-suggestiontype-e-sys.md) |
<!--DelEnd-->
