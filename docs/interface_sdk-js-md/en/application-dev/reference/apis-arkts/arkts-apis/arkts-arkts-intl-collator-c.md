# Collator

Collator class for locale-sensitive string comparison.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class Collator--><!--Device-Intl-export class Collator-End-->

**System capability:** SystemCapability.Utils.Lang

## compare

```TypeScript
public compare(x: string, y: string): double
```

Compares two strings.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Collator-public compare(x: string, y: string): double--><!--Device-Collator-public compare(x: string, y: string): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | string | Yes | first string to compare. |
| y | string | Yes | second string to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| double | comparison result. |

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: CollatorOptions)
```

Creates a new Collator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)--><!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No | the locales. |
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | No | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedCollatorOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions--><!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedCollatorOptions](arkts-arkts-intl-resolvedcollatoroptions-i.md) | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]--><!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | Yes | the locales. |
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

