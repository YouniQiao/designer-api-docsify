# Locale

Locale class for locale-sensitive operations.

**继承/实现关系：** Locale implements [LocaleOptions](arkts-arkts-intl-localeoptions-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Locale implements LocaleOptions--><!--Device-Intl-export class Locale implements LocaleOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)
```

Creates a new Locale.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)--><!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| Locale | 是 | the tag. |
| options | [LocaleOptions](arkts-arkts-intl-localeoptions-i.md) | 否 | the options. |

## defaultTag

```TypeScript
public static defaultTag(): string
```

Gets the default tag.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public static defaultTag(): string--><!--Device-Locale-public static defaultTag(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the default tag. |

## initLocale

```TypeScript
public initLocale(): void
```

Initializes the locale.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public initLocale(): void--><!--Device-Locale-public initLocale(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## isTagValid

```TypeScript
public isTagValid(tag: string): int
```

Checks if the tag is valid.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public isTagValid(tag: string): int--><!--Device-Locale-public isTagValid(tag: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | the tag. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 1 if valid, 0 otherwise. |

## langList

```TypeScript
public langList(): string
```

Gets the language list.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public langList(): string--><!--Device-Locale-public langList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the language list. |

## maximize

```TypeScript
public maximize(): Locale
```

Gets the most likely values for language, script, and region.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public maximize(): Locale--><!--Device-Locale-public maximize(): Locale-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Locale](../../apis-localization-kit/arkts-apis/arkts-localization-intl-locale-c.md) | locale with maximized info. |

## maximizeInfo

```TypeScript
public maximizeInfo(lang: string): string
```

Maximizes the locale info.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public maximizeInfo(lang: string): string--><!--Device-Locale-public maximizeInfo(lang: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lang | string | 是 | the language. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the maximized info. |

## minimize

```TypeScript
public minimize(): Locale
```

Removes information that would be added by maximize().

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public minimize(): Locale--><!--Device-Locale-public minimize(): Locale-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Locale](../../apis-localization-kit/arkts-apis/arkts-localization-intl-locale-c.md) | locale with minimized info. |

## numberingSystemList

```TypeScript
public numberingSystemList(): string
```

Gets the numbering system list.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public numberingSystemList(): string--><!--Device-Locale-public numberingSystemList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the numbering system list. |

## parseTagImpl

```TypeScript
public parseTagImpl(tag: string): string
```

Parses the tag.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public parseTagImpl(tag: string): string--><!--Device-Locale-public parseTagImpl(tag: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | the tag. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the parsed tag. |

## regionList

```TypeScript
public regionList(): string
```

Gets the region list.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public regionList(): string--><!--Device-Locale-public regionList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the region list. |

## scriptList

```TypeScript
public scriptList(): string
```

Gets the script list.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public scriptList(): string--><!--Device-Locale-public scriptList(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the script list. |

## toString

```TypeScript
public toString(): BCP47LanguageTag
```

Returns the full locale identifier string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public toString(): BCP47LanguageTag--><!--Device-Locale-public toString(): BCP47LanguageTag-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) | the locale identifier. |

## baseName

```TypeScript
public get baseName(): string | undefined
```

Gets the base name.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get baseName(): string | undefined--><!--Device-Locale-public get baseName(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## calendar

```TypeScript
public get calendar(): string | undefined
```

Gets the calendar.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get calendar(): string | undefined--><!--Device-Locale-public get calendar(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## caseFirst

```TypeScript
public get caseFirst(): string | undefined
```

Gets the case first.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get caseFirst(): string | undefined--><!--Device-Locale-public get caseFirst(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## collation

```TypeScript
public get collation(): string | undefined
```

Gets the collation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get collation(): string | undefined--><!--Device-Locale-public get collation(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## hourCycle

```TypeScript
public get hourCycle(): string | undefined
```

Gets the hour cycle.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get hourCycle(): string | undefined--><!--Device-Locale-public get hourCycle(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## language

```TypeScript
public get language(): string | undefined
```

Gets the language.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get language(): string | undefined--><!--Device-Locale-public get language(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## numberingSystem

```TypeScript
public get numberingSystem(): string | undefined
```

Gets the numbering system.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get numberingSystem(): string | undefined--><!--Device-Locale-public get numberingSystem(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## numeric

```TypeScript
public get numeric(): boolean | undefined
```

Gets the numeric.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get numeric(): boolean | undefined--><!--Device-Locale-public get numeric(): boolean | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## region

```TypeScript
public get region(): string | undefined
```

Gets the region.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get region(): string | undefined--><!--Device-Locale-public get region(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

## script

```TypeScript
public get script(): string | undefined
```

Gets the script.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Locale-public get script(): string | undefined--><!--Device-Locale-public get script(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

