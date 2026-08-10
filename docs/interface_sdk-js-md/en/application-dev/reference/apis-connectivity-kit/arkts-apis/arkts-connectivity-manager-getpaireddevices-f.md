# getPairedDevices

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## getPairedDevices

```TypeScript
function getPairedDevices(): string[]
```

获取已与当前设备配对的设备列表。如果用户有ohos.permission.GET_NEARLINK_PEER_MAC权限，则返回真实设备地址。否则，返回随机的设备地址

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getPairedDevices(): string[]--><!--Device-manager-function getPairedDevices(): string[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| string[] | Returns a list of paired devices' address in MAC format (e.g., "11:22:33:AA:BB:FF"). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |

