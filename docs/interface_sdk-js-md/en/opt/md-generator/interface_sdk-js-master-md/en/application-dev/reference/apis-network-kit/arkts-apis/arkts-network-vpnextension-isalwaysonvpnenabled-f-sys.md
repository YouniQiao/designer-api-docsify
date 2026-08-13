# isAlwaysOnVpnEnabled (System API)

## Modules to Import

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## isAlwaysOnVpnEnabled

```TypeScript
function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>
```

Get the Always on VPN mode status for a device.

**Since:** 11

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_VPN

**Model restriction:** This API can be used only in the stage model.

<!--Device-vpnExtension-function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>--><!--Device-vpnExtension-function isAlwaysOnVpnEnabled(bundleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
