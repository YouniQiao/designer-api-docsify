# Locale

Locale class for locale-sensitive operations.

**Inheritance/Implementation:** Locale implements [LocaleOptions](arkts-arkts-intl-localeoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class Locale implements LocaleOptions--><!--Device-Intl-export class Locale implements LocaleOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## baseName

```TypeScript
public set baseName(value: string | undefined)
```

Sets the base name.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set baseName(value: string | undefined)--><!--Device-Locale-public set baseName(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the base name. |

## baseName

```TypeScript
public get baseName(): string | undefined
```

Gets the base name.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get baseName(): string | undefined--><!--Device-Locale-public get baseName(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the base name. |

## calendar

```TypeScript
public set calendar(value: string | undefined)
```

Sets the calendar.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set calendar(value: string | undefined)--><!--Device-Locale-public set calendar(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the calendar. |

## calendar

```TypeScript
public get calendar(): string | undefined
```

Gets the calendar.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get calendar(): string | undefined--><!--Device-Locale-public get calendar(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the calendar. |

## caseFirst

```TypeScript
public set caseFirst(value: string | undefined)
```

Sets the case first.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set caseFirst(value: string | undefined)--><!--Device-Locale-public set caseFirst(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the case first. |

## caseFirst

```TypeScript
public get caseFirst(): string | undefined
```

Gets the case first.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get caseFirst(): string | undefined--><!--Device-Locale-public get caseFirst(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the case first. |

## collation

```TypeScript
public set collation(value: string | undefined)
```

Sets the collation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set collation(value: string | undefined)--><!--Device-Locale-public set collation(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the collation. |

## collation

```TypeScript
public get collation(): string | undefined
```

Gets the collation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get collation(): string | undefined--><!--Device-Locale-public get collation(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the collation. |

## constructor

```TypeScript
public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)
```

Creates a new Locale.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)--><!--Device-Locale-public constructor(tag: BCP47LanguageTag | Locale, options?: LocaleOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Locale | Yes | the tag. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the options. |

## defaultTag

```TypeScript
public static defaultTag(): string
```

Gets the default tag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public static defaultTag(): string--><!--Device-Locale-public static defaultTag(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the default tag. |

## hourCycle

```TypeScript
public set hourCycle(value: string | undefined)
```

Sets the hour cycle.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set hourCycle(value: string | undefined)--><!--Device-Locale-public set hourCycle(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the hour cycle. |

## hourCycle

```TypeScript
public get hourCycle(): string | undefined
```

Gets the hour cycle.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get hourCycle(): string | undefined--><!--Device-Locale-public get hourCycle(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the hour cycle. |

## initLocale

```TypeScript
public initLocale(): void
```

Initializes the locale.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public langList(): string--><!--Device-Locale-public langList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the language list. |

## language

```TypeScript
public set language(value: string | undefined)
```

Sets the language.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set language(value: string | undefined)--><!--Device-Locale-public set language(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the language. |

## language

```TypeScript
public get language(): string | undefined
```

Gets the language.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get language(): string | undefined--><!--Device-Locale-public get language(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the language. |

## maximize

```TypeScript
public maximize(): Locale
```

Gets the most likely values for language, script, and region.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public maximize(): Locale--><!--Device-Locale-public maximize(): Locale-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | locale with maximized info. |

## maximizeInfo

```TypeScript
public maximizeInfo(lang: string): string
```

Maximizes the locale info.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public minimize(): Locale--><!--Device-Locale-public minimize(): Locale-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | locale with minimized info. |

## numberingSystem

```TypeScript
public set numberingSystem(value: string | undefined)
```

Sets the numbering system.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set numberingSystem(value: string | undefined)--><!--Device-Locale-public set numberingSystem(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the numbering system. |

## numberingSystem

```TypeScript
public get numberingSystem(): string | undefined
```

Gets the numbering system.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get numberingSystem(): string | undefined--><!--Device-Locale-public get numberingSystem(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the numbering system. |

## numberingSystemList

```TypeScript
public numberingSystemList(): string
```

Gets the numbering system list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public numberingSystemList(): string--><!--Device-Locale-public numberingSystemList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the numbering system list. |

## numeric

```TypeScript
public set numeric(value: boolean | undefined)
```

Sets the numeric.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set numeric(value: boolean | undefined)--><!--Device-Locale-public set numeric(value: boolean | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | the numeric. |

## numeric

```TypeScript
public get numeric(): boolean | undefined
```

Gets the numeric.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get numeric(): boolean | undefined--><!--Device-Locale-public get numeric(): boolean | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the numeric. |

## parseTagImpl

```TypeScript
public parseTagImpl(tag: string): string
```

Parses the tag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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

## region

```TypeScript
public set region(value: string | undefined)
```

Sets the region.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set region(value: string | undefined)--><!--Device-Locale-public set region(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the region. |

## region

```TypeScript
public get region(): string | undefined
```

Gets the region.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get region(): string | undefined--><!--Device-Locale-public get region(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the region. |

## regionList

```TypeScript
public regionList(): string
```

Gets the region list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public regionList(): string--><!--Device-Locale-public regionList(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the region list. |

## script

```TypeScript
public set script(value: string | undefined)
```

Sets the script.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public set script(value: string | undefined)--><!--Device-Locale-public set script(value: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | the script. |

## script

```TypeScript
public get script(): string | undefined
```

Gets the script.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public get script(): string | undefined--><!--Device-Locale-public get script(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the script. |

## scriptList

```TypeScript
public scriptList(): string
```

Gets the script list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-Locale-public toString(): BCP47LanguageTag--><!--Device-Locale-public toString(): BCP47LanguageTag-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the locale identifier. |

