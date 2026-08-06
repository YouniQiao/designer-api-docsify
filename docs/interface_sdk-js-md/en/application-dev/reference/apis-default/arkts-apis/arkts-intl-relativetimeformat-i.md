# RelativeTimeFormat

**ArkTS mode:** ArkTS-Dyn only

## format

```TypeScript
format(value: number, unit: RelativeTimeFormatUnit): string
```

Formats a value and a unit according to the locale and formatting options of the given  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_object.

While this method automatically provides the correct plural forms,the grammatical form is otherwise as neutral as possible.

It is the caller's responsibility to handle cut-off logic such as deciding between displaying "in 7 days" or "in 1 week".This API does not support relative dates involving compound units.e.g "in 5 days and 4 hours".

**ArkTS mode:** ArkTS-Dyn only

<!--Device-RelativeTimeFormat-format(value: number, unit: RelativeTimeFormatUnit): string--><!--Device-RelativeTimeFormat-format(value: number, unit: RelativeTimeFormatUnit): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes |  |
| unit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string | Internationalized relative time message as string |

## formatToParts

```TypeScript
formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Returns an array of objects representing the relative time format in parts that can be used for custom locale-aware formatting.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-RelativeTimeFormat-formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]--><!--Device-RelativeTimeFormat-formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes |  |
| unit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] |  |

## resolvedOptions

```TypeScript
resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Provides access to the locale and options computed during initialization of this \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ object.

\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-RelativeTimeFormat-resolvedOptions(): ResolvedRelativeTimeFormatOptions--><!--Device-RelativeTimeFormat-resolvedOptions(): ResolvedRelativeTimeFormatOptions-End-->

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

