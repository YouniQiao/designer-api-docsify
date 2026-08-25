# getHash

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## getHash

```TypeScript
function getHash(object: object): number
```

Obtains the hash value of an object. If no hash value has been obtained, a random hash value is generated, saved to the **hash** field of the object, and returned. If a hash value has been obtained, the hash value saved in the **hash** field is returned (the same value is returned for the same object).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | object | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
