# RelativeTimeFormat

RelativeTimeFormat class for locale-sensitive relative time formatting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class RelativeTimeFormat--><!--Device-Intl-export class RelativeTimeFormat-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)
```

Creates a new RelativeTimeFormat.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)--><!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No | the locales. |
| options | RelativeTimeFormatOptions | No | the options. |

## format

```TypeScript
public format(value: double, unit: RelativeTimeFormatUnit): string
```

Formats a relative time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string--><!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the value. |
| unit | RelativeTimeFormatUnit | Yes | the unit. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted string. |

## formatToParts

```TypeScript
public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Formats a relative time to parts.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]--><!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | the value. |
| unit | RelativeTimeFormatUnit | Yes | the unit. |

**Return value:**

| Type | Description |
| --- | --- |
| RelativeTimeFormatPart[] | formatted parts. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions--><!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ResolvedRelativeTimeFormatOptions | the resolved options. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]--><!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | Yes | the locales. |
| options | RelativeTimeFormatOptions | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

