# has

## Modules to Import

```TypeScript
```

## has

```TypeScript
function has(obj: object, property: string): boolean
```

Checks whether an ArkTS object contains a key. This API can be used for related operations after [JSON.parse](arkts-arkts-json-parse-f.md#parse) is called to parse a JSON string. This API supports only valid JSON strings whose outermost layer is in dictionary format (in braces instead of square brackets).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function has(obj: object, property: string): boolean--><!--Device-json-function has(obj: object, property: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | object | Yes |
| property | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |
