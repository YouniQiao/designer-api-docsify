# generateRandomUUID

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## generateRandomUUID

```TypeScript
function generateRandomUUID(entropyCache?: boolean): string
```

Uses a secure random number generator to generate a random universally unique identifier (UUID) of the string type in RFC 4122 version 4. To improve performance, this API uses cached UUIDs by default, in which **entropyCache** is set to **true**. A maximum of 128 random UUIDs can be cached. After all the 128 UUIDs in the cache are used, a new set of UUIDs is generated to maintain their random distribution. If you do not need to use the cached UUID, set **entropyCache** to **false**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| entropyCache | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
