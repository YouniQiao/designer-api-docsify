# getState

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## getState

```TypeScript
function getState(): NearlinkState
```

获取星闪状态。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getState(): NearlinkState--><!--Device-manager-function getState(): NearlinkState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| [NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md) | 返回NearLink状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

