# @ohos.i18n

Provides international settings related APIs.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace i18n--><!--Device-unnamed-declare namespace i18n-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCalendar](arkts-i18n-getcalendar-f.md) | Obtains the Calendar object for the specified locale and calendar type. |
| [getChineseCalendar](arkts-i18n-getchinesecalendar-f.md) | Obtains the ChineseCalendar object for the specified locale. |
| [getInstance](arkts-i18n-getinstance-f.md) | Creates an IndexUtil object. |
| [getLineInstance](arkts-i18n-getlineinstance-f.md) | Obtains a BreakIterator object. The BreakIterator object maintains an internal break iterator that can be used to access various line break points. |
| [getSimpleDateTimeFormatByPattern](arkts-i18n-getsimpledatetimeformatbypattern-f.md) | Obtains a SimpleDateTimeFormat object based on the specified pattern string. For details about the display differences between the objects obtained by this API and getSimpleDateTimeFormatBySkeleton, see SimpleDateTimeFormat. |
| [getSimpleDateTimeFormatBySkeleton](arkts-i18n-getsimpledatetimeformatbyskeleton-f.md) | Obtains a SimpleDateTimeFormat object based on the specified skeleton. For details about the display differences between the objects obtained by this API and getSimpleDateTimeFormatByPattern, see SimpleDateTimeFormat. |
| [getSimpleNumberFormatBySkeleton](arkts-i18n-getsimplenumberformatbyskeleton-f.md) | Obtains a SimpleNumberFormat object based on the specified skeleton. |
| [getTimeZone](arkts-i18n-gettimezone-f.md) | Obtains the TimeZone object corresponding to the specified time zone ID. |
| [isRTL](arkts-i18n-isrtl-f.md) | Checks whether the input character is of the right to left (RTL) language. |

### Classes

| Name | Description |
| --- | --- |
| [AdvancedMeasureFormat](arkts-i18n-advancedmeasureformat-c.md) | Provides the number formatting capability, supporting automatic unit conversion based on specific application scenarios. |
| [BreakIterator](arkts-i18n-breakiterator-c.md) | The BreakIterator class is used for finding the location of break point in text. |
| [Calendar](arkts-i18n-calendar-c.md) | Provides the API for accessing Calendar name, time and date related information. |
| [ChineseCalendar](arkts-i18n-chinesecalendar-c.md) | Provide a ChineseCalendar interface which could handle unique characteristics of the chinese calendar, such as leap month. |
| [EntityRecognizer](arkts-i18n-entityrecognizer-c.md) | Provide some functions to find named entity in text. |
| [HolidayManager](arkts-i18n-holidaymanager-c.md) | Provide some functions to manage holidays in a country or region. Partly follows the RFC2445 standard. |
| [I18NUtil](arkts-i18n-i18nutil-c.md) | Provides util functions. |
| [ISO8601DateTimeFormat](arkts-i18n-iso8601datetimeformat-c.md) | Provide a DateTime formatting interface which could format date to ISO 8601 standard string. [ISO8601](https://iso8601.com/). |
| [IndexUtil](arkts-i18n-indexutil-c.md) | Sequence text can be grouped under the specified area, and grouping index with different lengths can be specified. |
| [Normalizer](arkts-i18n-normalizer-c.md) | Provides the API for text encoding normalization. |
| [PhoneNumberFormat](arkts-i18n-phonenumberformat-c.md) | Provides the API for formatting phone number strings |
| [SimpleDateTimeFormat](arkts-i18n-simpledatetimeformat-c.md) | Provide a simple date time formatting interface. |
| [SimpleNumberFormat](arkts-i18n-simplenumberformat-c.md) | Provide a simple number formatting interface. |
| [StyledDateTimeFormat](arkts-i18n-styleddatetimeformat-c.md) | Provide a DateTime formatting interface which could format DateTime to StyleString. |
| [StyledNumberFormat](arkts-i18n-stylednumberformat-c.md) | Provide a number formatting interface which could format number to StyleString. |
| [SymbolDateTimeFormat](arkts-i18n-symboldatetimeformat-c.md) | Provide a DateTime formatting interface that supports custom symbols. This interface formats date time values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "2:23 PM" with "2:23 afternoon"). |
| [SymbolNumberFormat](arkts-i18n-symbolnumberformat-c.md) | Provide a Number formatting interface that supports custom symbols. This interface formats number values into strings with custom symbols, and can replace variable symbols in the formatted result with custom fixed symbols (e.g., replacing "null" to "NA"). |
| [System](arkts-i18n-system-c.md) | Provides system functions. |
| [TimeZone](arkts-i18n-timezone-c.md) | Provides the API for accessing TimeZone name, rawOffset and offset information. |
| [Transliterator](arkts-i18n-transliterator-c.md) | Provides the API for transliterate text from one format to another. |
| [Unicode](arkts-i18n-unicode-c.md) | Provides the API for accessing unicode character properties. For example, determine whether a character is a number. |
| [ZoneOffsetTransition](arkts-i18n-zoneoffsettransition-c.md) | Provides the API for obtaining a timezone transition information. |
| [ZoneRules](arkts-i18n-zonerules-c.md) | Provides the API for obtaining timezone offset changing rules information. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [System](arkts-i18n-system-c-sys.md) | Provides system functions. |
| [SystemLocaleManager](arkts-i18n-systemlocalemanager-c-sys.md) | Provide some functions for settings and startup guide to select language or region. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AdvancedMeasureFormatOptions](arkts-i18n-advancedmeasureformatoptions-i.md) | Represents optional configuration items for AdvancedMeasureFormat object. |
| [ChineseCalendarTime](arkts-i18n-chinesecalendartime-i.md) | Represents chinese calendar time element for the ChineseCalendar object. |
| [EncodingInfo](arkts-i18n-encodinginfo-i.md) | Defines the detect encoding result information. |
| [EntityInfoItem](arkts-i18n-entityinfoitem-i.md) | Defines a list of entities. |
| [HolidayInfoItem](arkts-i18n-holidayinfoitem-i.md) | Represents the holiday information. |
| [HolidayLocalName](arkts-i18n-holidaylocalname-i.md) | Represents the name of a holiday in different languages. |
| [ISO8601DateTimeFormatOptions](arkts-i18n-iso8601datetimeformatoptions-i.md) | Represents optional configuration items for the ISO8601DateTimeFormat object. These options determine which elements need to be displayed after formatting and the corresponding format. |
| [PhoneNumberFormatOptions](arkts-i18n-phonenumberformatoptions-i.md) | Options for PhoneNumberFormat object initialization. |
| [ResolvedSymbolDateTimeFormatOptions](arkts-i18n-resolvedsymboldatetimeformatoptions-i.md) | Represents optional element for the ResolvedSymbolDateTimeFormatOptions object. Define the resolved symbol element and value that need to get. |
| [ResolvedSymbolNumberFormatOptions](arkts-i18n-resolvedsymbolnumberformatoptions-i.md) | Represents optional element for the ResolvedSymbolNumberFormatOptions object. Define the resolved symbol element and value that need to get. |
| [StyledDateTimeFormatOptions](arkts-i18n-styleddatetimeformatoptions-i.md) | Represents optional configuration items for the DateTimeFormat object. |
| [StyledNumberFormatOptions](arkts-i18n-stylednumberformatoptions-i.md) | Represents optional configuration items for the NumberFormat object. |
| [SymbolDateTimeFormatOptions](arkts-i18n-symboldatetimeformatoptions-i.md) | Represents optional configuration items for the SymbolDateTimeFormat object. Define the symbol element and value that need to be replaced. |
| [SymbolNumberFormatOptions](arkts-i18n-symbolnumberformatoptions-i.md) | Represents optional configuration items for the SymbolNumberFormat object. Define the symbol element and value that need to be replaced. |
| [UnitInfo](arkts-i18n-unitinfo-i.md) | Defines the measurement unit information. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [LocaleItem](arkts-i18n-localeitem-i-sys.md) | Represents the locale information, which consists of the language, script, and country/region. |
| [SortOptions](arkts-i18n-sortoptions-i-sys.md) | Represents the language or country/region sorting option. |
| [TimeZoneCityItem](arkts-i18n-timezonecityitem-i-sys.md) | Represents a time zone and city combination item. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [NormalizerMode](arkts-i18n-normalizermode-e.md) | Enumerates text normalization modes. |
| [TemperatureType](arkts-i18n-temperaturetype-e.md) | Enumerates temperature units. |
| [UnitUsage](arkts-i18n-unitusage-e.md) | Enumerates Scenarios for MeasureFormat. |
| [WeekDay](arkts-i18n-weekday-e.md) | Enumerates the first day of a week. The value ranges from Monday to Sunday. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [SuggestionType](arkts-i18n-suggestiontype-e-sys.md) | Represents the language or country/region suggestion type. |
<!--DelEnd-->

