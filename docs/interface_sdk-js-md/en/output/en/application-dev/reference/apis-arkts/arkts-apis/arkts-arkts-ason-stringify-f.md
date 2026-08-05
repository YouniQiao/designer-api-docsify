# stringify

## stringify

```TypeScript
function stringify(value: Object | null | undefined): string
```

Converts an ArkTS value to a JavaScript Object Notation (JSON) string. Extra supports Map and Set.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-function stringify(value: Object | null | undefined): string--><!--Device-ASON-function stringify(value: Object | null | undefined): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object \| null \| undefined | Yes | The value to stringify.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 18 |

**Return value:**

| Type | Description |
| --- | --- |
| string | The JSON string representation of the value. |

