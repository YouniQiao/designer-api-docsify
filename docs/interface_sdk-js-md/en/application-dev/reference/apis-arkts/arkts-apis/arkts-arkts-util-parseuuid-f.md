# parseUUID

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## parseUUID

```TypeScript
function parseUUID(uuid: string): Uint8Array
```

Parse a UUID from the string standard representation as described in the RFC 4122 version 4.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function parseUUID(uuid: string): Uint8Array--><!--Device-util-function parseUUID(uuid: string): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | string | Yes | String that specifies a UUID |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Return a Uint8Array representing this UUID. Throw SyntaxError if parsing fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkts/errorcode-utils.md#10200002-parameter-parsing-error) | Invalid uuid string. |

