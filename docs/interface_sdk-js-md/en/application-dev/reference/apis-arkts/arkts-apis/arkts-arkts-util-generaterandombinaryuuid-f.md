# generateRandomBinaryUUID

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## generateRandomBinaryUUID

```TypeScript
function generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array
```

Uses a secure random number generator to generate a random universally unique identifier (UUID) of RFC 4122 version 4.

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
| Uint8Array |
