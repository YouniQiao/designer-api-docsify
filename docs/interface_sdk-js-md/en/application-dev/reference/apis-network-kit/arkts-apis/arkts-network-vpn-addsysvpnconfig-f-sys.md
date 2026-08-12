# addSysVpnConfig (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
```

## addSysVpnConfig

```TypeScript
function addSysVpnConfig(config: SysVpnConfig): Promise<void>
```

Add a system VPN network configuration.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function addSysVpnConfig(config: SysVpnConfig): Promise<void>--><!--Device-vpn-function addSysVpnConfig(config: SysVpnConfig): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [SysVpnConfig](arkts-network-vpn-sysvpnconfig-i-sys.md) | Yes | Indicates the [SysVpnConfig](arkts-network-vpn-sysvpnconfig-i-sys.md#SysVpnConfig) configuration of the VPN network. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200001-invalid-parameter-value) | Invalid parameter value. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) | Operation failed. Cannot connect to service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

