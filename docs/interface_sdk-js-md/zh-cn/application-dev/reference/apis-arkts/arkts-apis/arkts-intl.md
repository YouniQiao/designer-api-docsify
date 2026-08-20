# Intl

Intl。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export namespace Intl--><!--Device-unnamed-export namespace Intl-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [intlBestFitLocale](arkts-arkts-intl-intlbestfitlocale-f.md) | 从给定的语言标签中获取最佳匹配的区域设置。 |
| [intlBestFitLocales](arkts-arkts-intl-intlbestfitlocales-f.md) | 从给定的语言标签中获取最佳匹配的区域设置列表。 |
| [intlLocalesToLanguageTags](arkts-arkts-intl-intllocalestolanguagetags-f.md) | 将区域设置转换为语言标签。 |
| [intlLookUpLocale](arkts-arkts-intl-intllookuplocale-f.md) | 从给定的语言标签中查找区域设置。 |
| [intlLookUpLocales](arkts-arkts-intl-intllookuplocales-f.md) | 从给定的语言标签中查找区域设置列表。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [Collator](arkts-arkts-intl-collator-c.md) | 用于按区域设置比较字符串的Collator类。 |
| [DateTimeFormat](arkts-arkts-intl-datetimeformat-c.md) | 用于按区域设置格式化日期的日期时间格式化类。 |
| [DisplayNames](arkts-arkts-intl-displaynames-c.md) | 用于按区域设置展示名称的DisplayNames类。 |
| [ListFormat](arkts-arkts-intl-listformat-c.md) | 用于按区域设置格式化列表的ListFormat类。 |
| [Locale](arkts-arkts-intl-locale-c.md) | 用于区域相关操作的Locale类。 |
| [NumberFormat](arkts-arkts-intl-numberformat-c.md) | 用于按区域设置格式化数字的NumberFormat类。 |
| [NumberFormatPart](arkts-arkts-intl-numberformatpart-c.md) | 数字格式化片段。 |
| [NumberRangeFormatPart](arkts-arkts-intl-numberrangeformatpart-c.md) | 数字区间格式化片段。 |
| [PluralRules](arkts-arkts-intl-pluralrules-c.md) | 用于按区域设置处理复数形式的PluralRules类。 |
| [RelativeTimeFormat](arkts-arkts-intl-relativetimeformat-c.md) | 用于按区域设置格式化相对时间的RelativeTimeFormat类。 |
| [Segmenter](arkts-arkts-intl-segmenter-c.md) | 用于按区域设置进行文本分段的Segmenter类。 |
| [Segments](arkts-arkts-intl-segments-c.md) | 分段迭代器类。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | 排序器选项。 |
| [DateTimeFormatOptions](arkts-arkts-intl-datetimeformatoptions-i.md) | 日期时间格式化选项。 |
| [DateTimeFormatPart](arkts-arkts-intl-datetimeformatpart-i.md) | 日期时间格式化片段。 |
| [DateTimeRangeFormatPart](arkts-arkts-intl-datetimerangeformatpart-i.md) | 日期时间区间格式化片段。 |
| [DisplayNamesLocaleMatcherOptions](arkts-arkts-intl-displaynameslocalematcheroptions-i.md) | 使用supportedLocalesOf时的区域匹配选项。 |
| [DisplayNamesOptions](arkts-arkts-intl-displaynamesoptions-i.md) | 创建DisplayNames对象的选项。 |
| [FormatToPartsResult](arkts-arkts-intl-formattopartsresult-i.md) | 格式化为片段的结果。 |
| [ListFormatOptions](arkts-arkts-intl-listformatoptions-i.md) | 列表格式化选项。 |
| [LocaleOptions](arkts-arkts-intl-localeoptions-i.md) | 区域设置选项。 |
| [NumberFormatOptions](arkts-arkts-intl-numberformatoptions-i.md) | 数字格式化选项。 |
| [PickLocaleMatchSegmenterOptions](arkts-arkts-intl-picklocalematchsegmenteroptions-i.md) | Segmenter的supportedLocalesOf中区域匹配的选项。 |
| [PluralRulesOptions](arkts-arkts-intl-pluralrulesoptions-i.md) | PluralRules选项。 |
| [PluralRulesSelectOptions](arkts-arkts-intl-pluralrulesselectoptions-i.md) | PluralRules的select选项。 |
| [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 相对时间格式化选项。 |
| [RelativeTimeFormatPart](arkts-arkts-intl-relativetimeformatpart-i.md) | 相对时间格式化片段。 |
| [ResolvedCollatorOptions](arkts-arkts-intl-resolvedcollatoroptions-i.md) | 解析后的排序器选项。 |
| [ResolvedDateTimeFormatOptions](arkts-arkts-intl-resolveddatetimeformatoptions-i.md) | 解析后的日期时间格式化选项。 |
| [ResolvedDisplayNamesOptions](arkts-arkts-intl-resolveddisplaynamesoptions-i.md) | resolvedOptions方法返回的解析后选项。 |
| [ResolvedNumberFormatOptions](arkts-arkts-intl-resolvednumberformatoptions-i.md) | 解析后的数字格式化选项。 |
| [ResolvedPluralRulesOptions](arkts-arkts-intl-resolvedpluralrulesoptions-i.md) | 解析后的PluralRules选项。 |
| [ResolvedRelativeTimeFormatOptions](arkts-arkts-intl-resolvedrelativetimeformatoptions-i.md) | 解析后的相对时间格式化选项。 |
| [ResolvedSegmenterOptions](arkts-arkts-intl-resolvedsegmenteroptions-i.md) | 解析后的分段器选项。 |
| [SegmentData](arkts-arkts-intl-segmentdata-i.md) | 分段数据接口。 |
| [SegmenterOptions](arkts-arkts-intl-segmenteroptions-i.md) | 分段器选项。 |
| [SupportedLocalesOfOptions](arkts-arkts-intl-supportedlocalesofoptions-i.md) | supportedLocalesOf的选项。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) | BCP 47语言标签类型。 |
| [DateStyle](arkts-arkts-intl-datestyle-t.md) | DateTimeFormat的日期样式。 |
| [DateTimeFormatPartTypes](arkts-arkts-intl-datetimeformatparttypes-t.md) | 日期时间格式化片段类型。 |
| [DateTimeRangeFormatPartSource](arkts-arkts-intl-datetimerangeformatpartsource-t.md) | 日期时间区间格式化片段来源。 |
| [DisplayNamesFallback](arkts-arkts-intl-displaynamesfallback-t.md) | 展示名称的回退选项。 |
| [DisplayNamesLanguageDisplay](arkts-arkts-intl-displaynameslanguagedisplay-t.md) | 语言展示选项。 |
| [DisplayNamesType](arkts-arkts-intl-displaynamestype-t.md) | 展示名称的类型。 |
| [ES2018NumberFormatPartType](arkts-arkts-intl-es2018numberformatparttype-t.md) | ES2018定义的数字格式化片段类型。 |
| [ES2020NumberFormatPartType](arkts-arkts-intl-es2020numberformatparttype-t.md) | ES2020定义的数字格式化片段类型。 |
| [LDMLPluralRule](arkts-arkts-intl-ldmlpluralrule-t.md) | LDML复数规则类型。 |
| [ListFormatLocaleMatcher](arkts-arkts-intl-listformatlocalematcher-t.md) | 区域匹配算法选项。 |
| [ListFormatStyle](arkts-arkts-intl-listformatstyle-t.md) | 列表格式化样式。 |
| [ListFormatType](arkts-arkts-intl-listformattype-t.md) | 列表格式化类型。 |
| [LocaleCollationCaseFirst](arkts-arkts-intl-localecollationcasefirst-t.md) | 区域排序中的大小写优先选项。 |
| [LocaleHourCycleKey](arkts-arkts-intl-localehourcyclekey-t.md) | 区域设置的小时制键。 |
| [LocalesArgument](arkts-arkts-intl-localesargument-t.md) | 区域设置参数类型。 |
| [NumberFormatPartTypes](arkts-arkts-intl-numberformatparttypes-t.md) | NumberFormat片段类型。 |
| [PluralRuleType](arkts-arkts-intl-pluralruletype-t.md) | 复数规则类型。 |
| [RelativeTimeFormatLocaleMatcher](arkts-arkts-intl-relativetimeformatlocalematcher-t.md) | 相对时间格式化的区域匹配算法。 |
| [RelativeTimeFormatNumeric](arkts-arkts-intl-relativetimeformatnumeric-t.md) | 相对时间格式化的数值选项。 |
| [RelativeTimeFormatStyle](arkts-arkts-intl-relativetimeformatstyle-t.md) | 相对时间格式化样式。 |
| [RelativeTimeFormatUnit](arkts-arkts-intl-relativetimeformatunit-t.md) | 相对时间格式化单位。 |
| [RelativeTimeFormatUnitSingular](arkts-arkts-intl-relativetimeformatunitsingular-t.md) | 相对时间格式化单位的单数形式。 |
| [SegmenterGranularity](arkts-arkts-intl-segmentergranularity-t.md) | 文本分段的粒度类型。 |
| [TimeStyle](arkts-arkts-intl-timestyle-t.md) | DateTimeFormat的时间样式。 |
| [TimeZoneName](arkts-arkts-intl-timezonename-t.md) | DateTimeFormat的时区名称样式。 |
| [UnicodeBCP47LocaleIdentifier](arkts-arkts-intl-unicodebcp47localeidentifier-t.md) | Unicode BCP 47区域设置标识符。 |

