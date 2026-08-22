# ListFormat

ListFormat class for locale-sensitive list formatting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-Intl-export class ListFormat--><!--Device-Intl-export class ListFormat-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: ListFormatOptions)
```

Creates a new ListFormat.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)--><!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No | the locales. |
| options | ListFormatOptions | No | the options. |

## format

```TypeScript
public format(list: Iterable<string>): string
```

Formats a list.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFormat-public format(list: Iterable<string>): string--><!--Device-ListFormat-public format(list: Iterable<string>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | Yes | the list to format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | formatted string. |

## formatToParts

```TypeScript
public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>
```

Formats a list to parts.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>--><!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | Yes | the list to format. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[FormatToPartsResult](arkts-arkts-intl-formattopartsresult-i.md)&gt; | formatted parts. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]--><!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | Yes | the locales. |
| options | ListFormatLocaleMatcher | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | supported locales. |

