# DisplayNames

DisplayNames class for locale-sensitive name display.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class DisplayNames--><!--Device-Intl-export class DisplayNames-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)
```

Creates a new DisplayNames.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)--><!--Device-DisplayNames-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: DisplayNamesOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| BCP47LanguageTag[] | No | the locales. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the options. |

## of

```TypeScript
public of(code: string): string | undefined
```

Returns the localized display name for the provided code.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisplayNames-public of(code: string): string | undefined--><!--Device-DisplayNames-public of(code: string): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | string | Yes | the code to get display name for. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the display name. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedDisplayNamesOptions
```

Returns the resolved options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions--><!--Device-DisplayNames-public resolvedOptions(): ResolvedDisplayNamesOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]
```

Returns an array of supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]--><!--Device-DisplayNames-public static supportedLocalesOf(locales: string | Locale | FixedArray<string | Locale>): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| Locale \| FixedArray&lt;string \| Locale&gt; | Yes | the locales. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

