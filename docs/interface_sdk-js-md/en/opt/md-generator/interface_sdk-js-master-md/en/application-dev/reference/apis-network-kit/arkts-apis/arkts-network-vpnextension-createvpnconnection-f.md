# createVpnConnection

## Modules to Import

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: VpnExtensionContext): VpnConnection
```

Create a VPN connection using the VpnExtensionContext.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-vpnExtension-function createVpnConnection(context: VpnExtensionContext): VpnConnection--><!--Device-vpnExtension-function createVpnConnection(context: VpnExtensionContext): VpnConnection-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [VpnExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-common-vpnextensioncontext-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
