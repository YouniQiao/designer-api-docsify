# getSysVpnConfig (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getSysVpnConfig

```TypeScript
function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>
```

Get the configuration of system VPN network by the specified vpnId.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>--><!--Device-vpn-function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vpnId | string | Yes | Indicates the uuid of the VPN network. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SysVpnConfig&gt; | The promise returned by the VPN network configuration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

