# getSysVpnConfig (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
```

## getSysVpnConfig

```TypeScript
function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>
```

Get the configuration of system VPN network by the specified vpnId.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>--><!--Device-vpn-function getSysVpnConfig(vpnId: string): Promise<SysVpnConfig>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vpnId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SysVpnConfig](arkts-network-vpn-sysvpnconfig-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
