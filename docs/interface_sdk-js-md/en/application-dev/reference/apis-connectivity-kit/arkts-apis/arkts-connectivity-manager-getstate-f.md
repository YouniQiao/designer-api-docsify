# getState

## Modules to Import

```TypeScript
import { manager } from 'manager';
```

## getState

```TypeScript
function getState(): NearlinkState
```

Gets the NearLink state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getState(): NearlinkState--><!--Device-manager-function getState(): NearlinkState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| [NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md) | Returns the NearLink state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

