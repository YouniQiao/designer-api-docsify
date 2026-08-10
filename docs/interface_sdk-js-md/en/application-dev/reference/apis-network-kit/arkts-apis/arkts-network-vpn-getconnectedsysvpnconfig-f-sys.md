# getConnectedSysVpnConfig (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getConnectedSysVpnConfig

```TypeScript
function getConnectedSysVpnConfig(): Promise<SysVpnConfig>
```

Get the connected VPN network configuration.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getConnectedSysVpnConfig(): Promise<SysVpnConfig>--><!--Device-vpn-function getConnectedSysVpnConfig(): Promise<SysVpnConfig>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SysVpnConfig&gt; | The promise returned by the connected VPN network configuration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

