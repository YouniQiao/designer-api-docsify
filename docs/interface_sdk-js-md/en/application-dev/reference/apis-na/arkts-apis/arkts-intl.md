# Intl

/*
 Copyright (c) 2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the 'License'),
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an 'AS IS' BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export namespace Intl--><!--Device-unnamed-export namespace Intl-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [intlBestFitLocale](arkts-na-intl-intlbestfitlocale-f.md#intlbestfitlocale) | Gets the best fit locale from the given language tags. |
| [intlBestFitLocales](arkts-na-intl-intlbestfitlocales-f.md#intlbestfitlocales) | Gets the best fit locales from the given language tags. |
| [intlLocalesToLanguageTags](arkts-na-intl-intllocalestolanguagetags-f.md#intllocalestolanguagetags) | Converts locales to language tags. |
| [intlLookUpLocale](arkts-na-intl-intllookuplocale-f.md#intllookuplocale) | Looks up a locale from the given language tags. |
| [intlLookUpLocales](arkts-na-intl-intllookuplocales-f.md#intllookuplocales) | Looks up locales from the given language tags. |

### Classes

| Name | Description |
| --- | --- |
| [Collator](arkts-na-intl-collator-c.md) | Collator class for locale-sensitive string comparison. |
| [DateTimeFormat](arkts-na-intl-datetimeformat-c.md) | Date time format class for locale-sensitive date formatting. |
| [DisplayNames](arkts-na-intl-displaynames-c.md) | DisplayNames class for locale-sensitive name display. |
| [ListFormat](arkts-na-intl-listformat-c.md) | ListFormat class for locale-sensitive list formatting. |
| [Locale](arkts-na-intl-locale-c.md) | Locale class for locale-sensitive operations. |
| [NumberFormat](arkts-na-intl-numberformat-c.md) | NumberFormat class for locale-sensitive number formatting. |
| [NumberFormatPart](arkts-na-intl-numberformatpart-c.md) | Number format part. |
| [NumberRangeFormatPart](arkts-na-intl-numberrangeformatpart-c.md) | Number range format part. |
| [PluralRules](arkts-na-intl-pluralrules-c.md) | PluralRules class for locale-sensitive plural formatting. |
| [RelativeTimeFormat](arkts-na-intl-relativetimeformat-c.md) | RelativeTimeFormat class for locale-sensitive relative time formatting. |
| [Segmenter](arkts-na-intl-segmenter-c.md) | Segmenter class for locale-sensitive text segmentation. |
| [Segments](arkts-na-intl-segments-c.md) | Segments iterator class. |

### Interfaces

| Name | Description |
| --- | --- |
| [CollatorOptions](arkts-na-intl-collatoroptions-i.md) | Collator options. |
| [DateTimeFormatOptions](arkts-na-intl-datetimeformatoptions-i.md) | Date time format options. |
| [DateTimeFormatPart](arkts-na-intl-datetimeformatpart-i.md) | Date time format part. |
| [DateTimeRangeFormatPart](arkts-na-intl-datetimerangeformatpart-i.md) | Date time range format part. |
| [DisplayNamesLocaleMatcherOptions](arkts-na-intl-displaynameslocalematcheroptions-i.md) | Options for locale matching when using supportedLocalesOf. |
| [DisplayNamesOptions](arkts-na-intl-displaynamesoptions-i.md) | Options for creating a DisplayNames object. |
| [FormatToPartsResult](arkts-na-intl-formattopartsresult-i.md) | Format to parts result. |
| [ListFormatOptions](arkts-na-intl-listformatoptions-i.md) | List format options. |
| [LocaleOptions](arkts-na-intl-localeoptions-i.md) | Locale options. |
| [NumberFormatOptions](arkts-na-intl-numberformatoptions-i.md) | Number format options. |
| [PickLocaleMatchSegmenterOptions](arkts-na-intl-picklocalematchsegmenteroptions-i.md) | Options for locale matching in Segmenter supportedLocalesOf. |
| [PluralRulesOptions](arkts-na-intl-pluralrulesoptions-i.md) | PluralRules options. |
| [PluralRulesSelectOptions](arkts-na-intl-pluralrulesselectoptions-i.md) | PluralRules select options. |
| [RelativeTimeFormatOptions](arkts-na-intl-relativetimeformatoptions-i.md) | Relative time format options. |
| [RelativeTimeFormatPart](arkts-na-intl-relativetimeformatpart-i.md) | Relative time format part. |
| [ResolvedCollatorOptions](arkts-na-intl-resolvedcollatoroptions-i.md) | Resolved collator options. |
| [ResolvedDateTimeFormatOptions](arkts-na-intl-resolveddatetimeformatoptions-i.md) | Resolved date time format options. |
| [ResolvedDisplayNamesOptions](arkts-na-intl-resolveddisplaynamesoptions-i.md) | Resolved options returned by the resolvedOptions method. |
| [ResolvedNumberFormatOptions](arkts-na-intl-resolvednumberformatoptions-i.md) | Resolved number format options. |
| [ResolvedPluralRulesOptions](arkts-na-intl-resolvedpluralrulesoptions-i.md) | Resolved PluralRules options. |
| [ResolvedRelativeTimeFormatOptions](arkts-na-intl-resolvedrelativetimeformatoptions-i.md) | Resolved relative time format options. |
| [ResolvedSegmenterOptions](arkts-na-intl-resolvedsegmenteroptions-i.md) | Resolved segmenter options. |
| [SegmentData](arkts-na-intl-segmentdata-i.md) | Segment data interface. |
| [SegmenterOptions](arkts-na-intl-segmenteroptions-i.md) | Segmenter options. |
| [SupportedLocalesOfOptions](arkts-na-intl-supportedlocalesofoptions-i.md) | Supported locales of options. |

### Types

| Name | Description |
| --- | --- |
| [BCP47LanguageTag](arkts-na-intl-bcp47languagetag-t.md) | BCP 47 language tag type. |
| [DateStyle](arkts-na-intl-datestyle-t.md) | Date style for DateTimeFormat. |
| [DateTimeFormatPartTypes](arkts-na-intl-datetimeformatparttypes-t.md) | Date time format part types. |
| [DateTimeRangeFormatPartSource](arkts-na-intl-datetimerangeformatpartsource-t.md) | Date time range format part source. |
| [DisplayNamesFallback](arkts-na-intl-displaynamesfallback-t.md) | Fallback option for display names. |
| [DisplayNamesLanguageDisplay](arkts-na-intl-displaynameslanguagedisplay-t.md) | Language display option. |
| [DisplayNamesType](arkts-na-intl-displaynamestype-t.md) | Type of display names. |
| [ES2018NumberFormatPartType](arkts-na-intl-es2018numberformatparttype-t.md) | Number format part types from ES2018. |
| [ES2020NumberFormatPartType](arkts-na-intl-es2020numberformatparttype-t.md) | Number format part types from ES2020. |
| [LDMLPluralRule](arkts-na-intl-ldmlpluralrule-t.md) | LDML plural rule type. |
| [ListFormatLocaleMatcher](arkts-na-intl-listformatlocalematcher-t.md) | Locale matcher option. |
| [ListFormatStyle](arkts-na-intl-listformatstyle-t.md) | List format style. |
| [ListFormatType](arkts-na-intl-listformattype-t.md) | List format type. |
| [LocaleCollationCaseFirst](arkts-na-intl-localecollationcasefirst-t.md) | Locale collation case first option. |
| [LocaleHourCycleKey](arkts-na-intl-localehourcyclekey-t.md) | Locale hour cycle key. |
| [LocalesArgument](arkts-na-intl-localesargument-t.md) | Locales argument type. |
| [NumberFormatPartTypes](arkts-na-intl-numberformatparttypes-t.md) | NumberFormat part type. |
| [PluralRuleType](arkts-na-intl-pluralruletype-t.md) | Plural rule type. |
| [RelativeTimeFormatLocaleMatcher](arkts-na-intl-relativetimeformatlocalematcher-t.md) | Relative time format locale matcher. |
| [RelativeTimeFormatNumeric](arkts-na-intl-relativetimeformatnumeric-t.md) | Relative time format numeric option. |
| [RelativeTimeFormatStyle](arkts-na-intl-relativetimeformatstyle-t.md) | Relative time format style. |
| [RelativeTimeFormatUnit](arkts-na-intl-relativetimeformatunit-t.md) | Relative time format unit. |
| [RelativeTimeFormatUnitSingular](arkts-na-intl-relativetimeformatunitsingular-t.md) | Relative time format unit singular. |
| [SegmenterGranularity](arkts-na-intl-segmentergranularity-t.md) | Granularity type for text segmentation. |
| [TimeStyle](arkts-na-intl-timestyle-t.md) | Time style for DateTimeFormat. |
| [TimeZoneName](arkts-na-intl-timezonename-t.md) | Time zone name style for DateTimeFormat. |
| [UnicodeBCP47LocaleIdentifier](arkts-na-intl-unicodebcp47localeidentifier-t.md) | Unicode BCP 47 locale identifier. |

