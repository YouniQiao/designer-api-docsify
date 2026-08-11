# addSysVpnConfig (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## addSysVpnConfig

```TypeScript
function addSysVpnConfig(config: SysVpnConfig): Promise<void>
```

Add a system VPN network configuration.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function addSysVpnConfig(config: SysVpnConfig): Promise<void>--><!--Device-vpn-function addSysVpnConfig(config: SysVpnConfig): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [SysVpnConfig](arkts-network-vpn-sysvpnconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-sharing.md#2200001-invalid-parameter-value) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2200003](../errorcode-net-sharing.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-sharing.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
