# createVpnObserver

## Modules to Import

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## createVpnObserver

```TypeScript
function createVpnObserver(): VpnObserver
```

Create a VPN observer.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-vpnExtension-function createVpnObserver(): VpnObserver--><!--Device-vpnExtension-function createVpnObserver(): VpnObserver-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VpnObserver](arkts-network-vpnextension-vpnobserver-i.md) |

## Examples

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';

let vpnObserver: vpnExtension.VpnObserver = vpnExtension.createVpnObserver();
```
