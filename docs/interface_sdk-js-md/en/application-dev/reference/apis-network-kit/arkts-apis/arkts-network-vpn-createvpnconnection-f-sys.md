# createVpnConnection (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
import { vpnExtension } from '@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: AbilityContext): VpnConnection
```

Creates a VPN connection.

**Since:** 10

<!--Device-vpn-function createVpnConnection(context: AbilityContext): VpnConnection--><!--Device-vpn-function createVpnConnection(context: AbilityContext): VpnConnection-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [AbilityContext](arkts-network-vpn-abilitycontext-t.md) | Yes | Specified context. |

**Return value:**

| Type | Description |
| --- | --- |
| VpnConnection | VPN connection object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

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

