# Collator

Provides the string collation capability.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export class Collator--><!--Device-intl-export class Collator-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## compare

```TypeScript
compare(first: string, second: string): int
```

Compares two strings based on the specified collation rules.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-compare(first: string, second: string): int--><!--Device-Collator-compare(first: string, second: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | string | Yes | First string to compare. |
| second | string | Yes | Second string to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Comparison result. If the value is a negative number, the first string comes before the second string. If the value is 0, the first and second strings are in the same sequence. If the value is a positive number, the first string is comes after the second string. |

## constructor

```TypeScript
constructor()
```

Creates a Collator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-constructor()--><!--Device-Collator-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: CollatorOptions)
```

Creates a Collator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)--><!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [CollatorOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-collatoroptions-i.md) | No | Options for creating a Collator object. |

## resolvedOptions

```TypeScript
resolvedOptions(): CollatorOptions
```

Obtains the options for creating a Collator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-resolvedOptions(): CollatorOptions--><!--Device-Collator-resolvedOptions(): CollatorOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [CollatorOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-collatoroptions-i.md) | Options for creating a Collator object. |

