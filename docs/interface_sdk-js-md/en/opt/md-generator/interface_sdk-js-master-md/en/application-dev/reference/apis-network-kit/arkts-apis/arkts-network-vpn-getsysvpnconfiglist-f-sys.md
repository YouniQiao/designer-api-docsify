# getSysVpnConfigList (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getSysVpnConfigList

```TypeScript
function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>
```

Get all system VPN network configuration.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>--><!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;SysVpnConfig&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200003](../errorcode-net-sharing.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-sharing.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
