# isAlwaysOnVpnEnabled (System API)

## Modules to Import

```TypeScript
import { vpnExtension } from 'vpnExtension';
```

## isAlwaysOnVpnEnabled

```TypeScript
function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>
```

Get the Always on VPN mode status for a device.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_VPN

**Model restriction:** This API can be used only in the stage model.

<!--Device-vpnExtension-function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>--><!--Device-vpnExtension-function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | bundleName is used to retrieve whether it has the always on. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | return the mode for alway on vpn status |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

