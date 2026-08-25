# @ohos.i18n

This module provides system-related and enhanced [i18n](../../../internationalization/i18n-l10n.md) capabilities, such as locale management, phone number formatting, and calendar, through supplementary i18n APIs that are not defined in [ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/). The [intl](arkts-intl.md) module provides basic i18n capabilities through the standard i18n APIs defined in ECMA
402. It works with the **i18n** module to provide a complete suite of i18n capabilities. The terms used in the APIs
are defined as follows:  
- Pattern string, which is a string consisting of  
[Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and custom text enclosed by single quotation marks.  
- Skeleton string: a string that consists of  
[Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and does not support custom text.

> **NOTE：**&gt;
> - The APIs of this module are based on the [CLDR](https://cldr.unicode.org) internationalization database. The
> processing results of the APIs may be adjusted as the CLDR standard evolves. For example, the return value of the
> [date and time formatting API](arkts-localization-i18n-simplenumberformat-c.md) is used only for UI display. Do not hardcode the
> return value or make assumptions about the return value. Otherwise, version compatibility problems may occur. API
> version 12 corresponds to [CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42). For details about data
> changes, see the official CLDR documentation.&gt;
> - Since API version 11, some APIs of this module are supported in ArkTS widgets.

**Since:** 7

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPreferredLanguage](arkts-localization-i18n-addpreferredlanguage-f.md) |
| [getCalendar](arkts-localization-i18n-getcalendar-f.md) |
| [getChineseCalendar](arkts-localization-i18n-getchinesecalendar-f.md) |
| [getDisplayCountry](arkts-localization-i18n-getdisplaycountry-f.md) |
| [getDisplayLanguage](arkts-localization-i18n-getdisplaylanguage-f.md) |
| [getFirstPreferredLanguage](arkts-localization-i18n-getfirstpreferredlanguage-f.md) |
| [getInstance](arkts-localization-i18n-getinstance-f.md) |
| [getLineInstance](arkts-localization-i18n-getlineinstance-f.md) |
| [getPreferredLanguageList](arkts-localization-i18n-getpreferredlanguagelist-f.md) |
| [getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md) |
| [getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md) |
| [getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md) |
| [getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md) |
| [getSimpleNumberFormatBySkeleton](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md) |
| [getSimpleNumberFormatBySkeleton](arkts-localization-i18n-getsimplenumberformatbyskeleton-f.md) |
| [getSystemLanguage](arkts-localization-i18n-getsystemlanguage-f.md) |
| [getSystemLocale](arkts-localization-i18n-getsystemlocale-f.md) |
| [getSystemRegion](arkts-localization-i18n-getsystemregion-f.md) |
| [getTimeZone](arkts-localization-i18n-gettimezone-f.md) |
| [is24HourClock](arkts-localization-i18n-is24hourclock-f.md) |
| [isRTL](arkts-localization-i18n-isrtl-f.md) |
| [removePreferredLanguage](arkts-localization-i18n-removepreferredlanguage-f.md) |
| [set24HourClock](arkts-localization-i18n-set24hourclock-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdvancedMeasureFormat](arkts-localization-i18n-advancedmeasureformat-c.md) |
| [BreakIterator](arkts-localization-i18n-breakiterator-c.md) |
| [Calendar](arkts-localization-i18n-calendar-c.md) |
| [Character](arkts-localization-i18n-character-c.md) |
| [ChineseCalendar](arkts-localization-i18n-chinesecalendar-c.md) |
| [EntityRecognizer](arkts-localization-i18n-entityrecognizer-c.md) |
| [HolidayManager](arkts-localization-i18n-holidaymanager-c.md) |
| [I18NUtil](arkts-localization-i18n-i18nutil-c.md) |
| [IndexUtil](arkts-localization-i18n-indexutil-c.md) |
| [ISO8601DateTimeFormat](arkts-localization-i18n-iso8601datetimeformat-c.md) |
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
### Classes(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [System](arkts-localization-i18n-system-c-sys.md) |
| [SystemLocaleManager](arkts-localization-i18n-systemlocalemanager-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LocaleItem](arkts-localization-i18n-localeitem-i-sys.md) |
| [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) |
| [TimeZoneCityItem](arkts-localization-i18n-timezonecityitem-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NormalizerMode](arkts-localization-i18n-normalizermode-e.md) |
| [TemperatureType](arkts-localization-i18n-temperaturetype-e.md) |
| [UnitUsage](arkts-localization-i18n-unitusage-e.md) |
| [WeekDay](arkts-localization-i18n-weekday-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SuggestionType](arkts-localization-i18n-suggestiontype-e-sys.md) |
<!--DelEnd-->
