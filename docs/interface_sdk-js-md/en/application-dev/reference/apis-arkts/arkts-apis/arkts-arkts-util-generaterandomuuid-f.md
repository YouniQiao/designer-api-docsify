# generateRandomUUID

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## generateRandomUUID

```TypeScript
function generateRandomUUID(entropyCache?: boolean): string
```

Generate a random RFC 4122 version 4 UUID using a cryptographically secure random number generator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function generateRandomUUID(entropyCache?: boolean): string--><!--Device-util-function generateRandomUUID(entropyCache?: boolean): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| entropyCache | boolean | No | Whether to generate the UUID with using the cache. Default: true. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return a string representing this UUID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Incorrect parameter types. |

