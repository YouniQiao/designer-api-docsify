# getSysVpnConfigList (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
```

## getSysVpnConfigList

```TypeScript
function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>
```

Get all system VPN network configuration.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>--><!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[SysVpnConfig](arkts-network-vpn-sysvpnconfig-i-sys.md)&gt;&gt; | The promise returned by the all VPN network configuration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) | Operation failed. Cannot connect to service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

