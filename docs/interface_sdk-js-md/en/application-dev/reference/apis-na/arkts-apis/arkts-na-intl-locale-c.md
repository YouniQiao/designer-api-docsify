# Locale

Locale class for locale-sensitive operations.

**Inheritance/Implementation:** Locale implements [LocaleOptions](arkts-na-intl-localeoptions-i.md#LocaleOptions)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-Intl-export class Locale--><!--Device-Intl-export class Locale-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)
```

Creates a new Locale.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)--><!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | BCP47LanguageTag \| Locale | Yes | the tag. |
| options | LocaleOptions | No | the options. |

## defaultTag

```TypeScript
public static defaultTag(): string
```

Gets the default tag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public static defaultTag(): string--><!--Device-Locale-public static defaultTag(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the default tag. |

## initLocale

```TypeScript
public initLocale(): void
```

Initializes the locale.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public initLocale(): void--><!--Device-Locale-public initLocale(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## isTagValid

```TypeScript
public isTagValid(tag: string): int
```

Checks if the tag is valid.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public isTagValid(tag: string): int--><!--Device-Locale-public isTagValid(tag: string): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| int | 1 if valid, 0 otherwise. |

## langList

```TypeScript
public langList(): string
```

Gets the language list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public langList(): string--><!--Device-Locale-public langList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the language list. |

## maximize

```TypeScript
public maximize(): Locale
```

Gets the most likely values for language, script, and region.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public maximize(): Locale--><!--Device-Locale-public maximize(): Locale-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Locale | locale with maximized info. |

## maximizeInfo

```TypeScript
public maximizeInfo(lang: string): string
```

Maximizes the locale info.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public maximizeInfo(lang: string): string--><!--Device-Locale-public maximizeInfo(lang: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lang | string | Yes | the language. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the maximized info. |

## minimize

```TypeScript
public minimize(): Locale
```

Removes information that would be added by maximize().

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public minimize(): Locale--><!--Device-Locale-public minimize(): Locale-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Locale | locale with minimized info. |

## numberingSystemList

```TypeScript
public numberingSystemList(): string
```

Gets the numbering system list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public numberingSystemList(): string--><!--Device-Locale-public numberingSystemList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the numbering system list. |

## parseTagImpl

```TypeScript
public parseTagImpl(tag: string): string
```

Parses the tag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public parseTagImpl(tag: string): string--><!--Device-Locale-public parseTagImpl(tag: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the parsed tag. |

## regionList

```TypeScript
public regionList(): string
```

Gets the region list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public regionList(): string--><!--Device-Locale-public regionList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the region list. |

## scriptList

```TypeScript
public scriptList(): string
```

Gets the script list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public scriptList(): string--><!--Device-Locale-public scriptList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the script list. |

## toString

```TypeScript
public toString(): BCP47LanguageTag
```

Returns the full locale identifier string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public toString(): BCP47LanguageTag--><!--Device-Locale-public toString(): BCP47LanguageTag-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| BCP47LanguageTag | the locale identifier. |

