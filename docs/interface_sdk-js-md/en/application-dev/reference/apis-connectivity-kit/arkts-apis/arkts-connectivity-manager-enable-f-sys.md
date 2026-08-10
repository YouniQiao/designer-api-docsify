# enable (System API)

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## enable

```TypeScript
function enable(): void
```

开启星闪。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function enable(): void--><!--Device-manager-function enable(): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 203 | EDM denied. |

