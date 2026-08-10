# generateRandomBinaryUUID

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## generateRandomBinaryUUID

```TypeScript
function generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array | undefined
```

Generate a random RFC 4122 version 4 binary UUID using a cryptographically secure random number generator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array | undefined--><!--Device-util-function generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entropyCache | boolean | No | Whether to generate the UUID with using the cache. Default: true. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Return a Uint8Array representing this UUID, or undefined on failure. |

