# createVpnConnection (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: AbilityContext): VpnConnection
```

Create a VPN connection using the AbilityContext.

**Since:** 10

**Deprecated since:** -1

<!--Device-vpn-function createVpnConnection(context: AbilityContext): VpnConnection--><!--Device-vpn-function createVpnConnection(context: AbilityContext): VpnConnection-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [AbilityContext](arkts-network-vpn-abilitycontext-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

Stage model:

```TypeScript
import { vpn } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private VpnConnection: vpn.VpnConnection = vpn.createVpnConnection(this.context);
  functiontest()
  {
    console.info("vpn createVpnConnection: " + JSON.stringify(this.VpnConnection));
  }
  build() {  }
}
```
