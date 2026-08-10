# Locale

**ArkTS模式：** 仅支持ArkTS-Dyn

## maximize

```TypeScript
maximize(): Locale
```

Gets the most likely values for the language, script, and region of the locale based on existing values.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Locale-maximize(): Locale--><!--Device-Locale-maximize(): Locale-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Locale](../../apis-localization-kit/arkts-apis/arkts-localization-intl-locale-c.md) |  |

## minimize

```TypeScript
minimize(): Locale
```

Attempts to remove information about the locale that would be added by calling `Locale.maximize()`.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Locale-minimize(): Locale--><!--Device-Locale-minimize(): Locale-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Locale](../../apis-localization-kit/arkts-apis/arkts-localization-intl-locale-c.md) |  |

## toString

```TypeScript
toString(): BCP47LanguageTag
```

Returns the locale's full locale identifier string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Locale-toString(): BCP47LanguageTag--><!--Device-Locale-toString(): BCP47LanguageTag-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BCP47LanguageTag](../../apis-arkts/arkts-apis/arkts-arkts-intl-bcp47languagetag-t.md) |  |

## baseName

```TypeScript
baseName: string
```

A string containing the language, and the script and region if available.

**类型：** string

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Locale-baseName: string--><!--Device-Locale-baseName: string-End-->

## language

```TypeScript
language: string
```

The primary language subtag associated with the locale.

**类型：** string

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Locale-language: string--><!--Device-Locale-language: string-End-->

