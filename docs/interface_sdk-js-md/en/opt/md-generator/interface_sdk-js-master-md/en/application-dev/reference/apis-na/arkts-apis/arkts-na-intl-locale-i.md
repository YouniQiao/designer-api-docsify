# Locale

**Inheritance/Implementation:** Locale extends [LocaleOptions](arkts-na-intl-localeoptions-i.md#LocaleOptions)

**Since:** -1

**Deprecated since:** -1

<!--Device-Intl-interface Locale--><!--Device-Intl-interface Locale-End-->

## maximize

```TypeScript
maximize(): Locale
```

Gets the most likely values for the language, script, and region of the locale based on existing values.

**Since:** -1

**Deprecated since:** -1

<!--Device-Locale-maximize(): Locale--><!--Device-Locale-maximize(): Locale-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Locale](arkts-na-intl-locale-i.md) |

## minimize

```TypeScript
minimize(): Locale
```

Attempts to remove information about the locale that would be added by calling `Locale.maximize()`.

**Since:** -1

**Deprecated since:** -1

<!--Device-Locale-minimize(): Locale--><!--Device-Locale-minimize(): Locale-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Locale](arkts-na-intl-locale-i.md) |

## toString

```TypeScript
toString(): BCP47LanguageTag
```

Returns the locale's full locale identifier string.

**Since:** -1

**Deprecated since:** -1

<!--Device-Locale-toString(): BCP47LanguageTag--><!--Device-Locale-toString(): BCP47LanguageTag-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BCP47LanguageTag](arkts-na-intl-bcp47languagetag-t.md) |

## baseName

```TypeScript
baseName: string
```

A string containing the language, and the script and region if available.

**Type:** string

**Since:** -1

**Deprecated since:** -1

<!--Device-Locale-baseName: string--><!--Device-Locale-baseName: string-End-->

## language

```TypeScript
language: string
```

The primary language subtag associated with the locale.

**Type:** string

**Since:** -1

**Deprecated since:** -1

<!--Device-Locale-language: string--><!--Device-Locale-language: string-End-->
