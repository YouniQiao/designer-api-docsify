# lib.es2020.intl

**ArkTS模式：** 仅支持ArkTS-Dyn

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [DateTimeFormatOptions](arkts-intl-datetimeformatoptions-i.md) |  |
| [DisplayNames](arkts-intl-displaynames-i.md) |  |
| [DisplayNamesOptions](arkts-intl-displaynamesoptions-i.md) |  |
| [Locale](arkts-intl-locale-i.md) |  |
| [LocaleOptions](arkts-intl-localeoptions-i.md) |  |
| [NumberFormatOptions](arkts-intl-numberformatoptions-i.md) |  |
| [RelativeTimeFormat](arkts-intl-relativetimeformat-i.md) |  |
| [RelativeTimeFormatOptions](arkts-intl-relativetimeformatoptions-i.md) | An object with some or all of properties of `options` parameter of `Intl.RelativeTimeFormat` constructor.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#Parameters). |
| [ResolvedDisplayNamesOptions](arkts-intl-resolveddisplaynamesoptions-i.md) |  |
| [ResolvedNumberFormatOptions](arkts-intl-resolvednumberformatoptions-i.md) |  |
| [ResolvedRelativeTimeFormatOptions](arkts-intl-resolvedrelativetimeformatoptions-i.md) | An object with properties reflecting the locale and formatting options computed during initialization of the `Intl.RelativeTimeFormat` object  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#Description). |

### 类型

| 名称 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-intl-bcp47languagetag-t.md) | [BCP 47 language tag](http://tools.ietf.org/html/rfc5646) definition.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument). |
| [DisplayNamesFallback](arkts-intl-displaynamesfallback-t.md) |  |
| [DisplayNamesLanguageDisplay](arkts-intl-displaynameslanguagedisplay-t.md) |  |
| [DisplayNamesType](arkts-intl-displaynamestype-t.md) |  |
| [LocaleCollationCaseFirst](arkts-intl-localecollationcasefirst-t.md) |  |
| [LocaleHourCycleKey](arkts-intl-localehourcyclekey-t.md) |  |
| [LocalesArgument](arkts-intl-localesargument-t.md) | The locale(s) to use  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument). |
| [RelativeTimeFormatLocaleMatcher](arkts-intl-relativetimeformatlocalematcher-t.md) | The locale matching algorithm to use.  [MDN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_negotiation). |
| [RelativeTimeFormatNumeric](arkts-intl-relativetimeformatnumeric-t.md) | The format of output message.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#Parameters). |
| [RelativeTimeFormatPart](arkts-intl-relativetimeformatpart-t.md) | An object representing the relative time format in parts that can be used for custom locale-aware formatting.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts#Using_formatToParts). |
| [RelativeTimeFormatStyle](arkts-intl-relativetimeformatstyle-t.md) | The length of the internationalized message.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#Parameters). |
| [RelativeTimeFormatUnit](arkts-intl-relativetimeformatunit-t.md) | Unit to use in the relative time internationalized message.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#Parameters). |
| [RelativeTimeFormatUnitSingular](arkts-intl-relativetimeformatunitsingular-t.md) | Value of the `unit` property in objects returned by`Intl.RelativeTimeFormat.prototype.formatToParts()`. `formatToParts` and`format` methods accept either singular or plural unit names as input,but `formatToParts` only outputs singular (e.g. "day") not plural (e.g."days").  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts#Using_formatToParts). |
| [UnicodeBCP47LocaleIdentifier](arkts-intl-unicodebcp47localeidentifier-t.md) | [Unicode BCP 47 Locale Identifiers](https://unicode.org/reports/tr35/#Unicode_Language_and_Locale_Identifiers) definition.  [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument). |

### 常量

| 名称 | 说明 |
| --- | --- |
| [DisplayNames](arkts-intl-con.md#displaynames) | The [`Intl.DisplayNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)object enables the consistent translation of language, region and script display names.  [Compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#browser_compatibility). |
| [Locale](arkts-intl-con.md#locale) | Constructor creates [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)objects |
| [RelativeTimeFormat](arkts-intl-con.md#relativetimeformat) | The [`Intl.RelativeTimeFormat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RelativeTimeFormat)object is a constructor for objects that enable language-sensitive relative time formatting.  [Compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat#Browser_compatibility). |

