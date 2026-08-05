# NumberFormat

Provides the API for formatting number strings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export class NumberFormat--><!--Device-intl-export class NumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor()
```

Creates a NumberFormat object for the specified locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NumberFormat-constructor()--><!--Device-NumberFormat-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: NumberOptions)
```

Creates a NumberFormat object for the specified locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NumberFormat-constructor(locale: string | Array<string>, options?: NumberOptions)--><!--Device-NumberFormat-constructor(locale: string | Array<string>, options?: NumberOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | Locale ID or locale ID array. If the input is a locale ID array,the first valid locale ID is used. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options for creating the NumberFormat object. |

## format

```TypeScript
format(num: double): string
```

Formats a number.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NumberFormat-format(num: double): string--><!--Device-NumberFormat-format(num: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| num | double | Yes | Number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted number. |

## formatRange

```TypeScript
formatRange(startRange: double, endRange: double): string
```

Formats a number range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NumberFormat-formatRange(startRange: double, endRange: double): string--><!--Device-NumberFormat-formatRange(startRange: double, endRange: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startRange | double | Yes | Start number. |
| endRange | double | Yes | End number. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted number range. |

## resolvedOptions

```TypeScript
resolvedOptions(): NumberOptions
```

Obtains the options for creating a NumberFormat object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NumberFormat-resolvedOptions(): NumberOptions--><!--Device-NumberFormat-resolvedOptions(): NumberOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Options for creating the NumberFormat object. |

