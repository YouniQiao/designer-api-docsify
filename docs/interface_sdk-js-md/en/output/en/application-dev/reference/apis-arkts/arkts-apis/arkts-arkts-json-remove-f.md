# remove

## remove

```TypeScript
function remove(obj: object, property: string): void
```

Removes a key from an ArkTS object. This API can be used for related operations after [JSON.parse]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is called to parse a JSON string. This API supports only valid JSON strings whose outermost layer is in dictionary format (in braces instead of square brackets).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function remove(obj: object, property: string): void--><!--Device-json-function remove(obj: object, property: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | object | Yes | ArkTS object. |
| property | string | Yes | Key to remove. |

