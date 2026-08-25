# remove

## Modules to Import

```TypeScript
import { JSON } from 'kits/@kit.ArkTS';
```

## remove

```TypeScript
function remove(obj: object, property: string): void
```

Removes a key from an ArkTS object. This API can be used for related operations after [JSON.parse](arkts-arkts-json-parse-f.md) is called to parse a JSON string. This API supports only valid JSON strings whose outermost layer is in dictionary format (in braces instead of square brackets).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | object | Yes |
| property | string | Yes |
