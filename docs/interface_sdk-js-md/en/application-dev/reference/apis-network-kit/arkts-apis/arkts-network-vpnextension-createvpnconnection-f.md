# createVpnConnection

## Modules to Import

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: VpnExtensionContext): VpnConnection
```

Creates a **VpnConnection** object.

> **NOTE：**&gt;
> Before calling **createVpnConnection**, call **startVpnExtensionAbility** to enable the VPN function.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
