# VpnObserver

Defines a VPN observer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-vpnExtension-export interface VpnObserver--><!--Device-vpnExtension-export interface VpnObserver-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## offAuthorizationResult

```TypeScript
offAuthorizationResult(callback?: Callback<boolean>): void
```

Unregisters the listener for user authorization results.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnObserver-offAuthorizationResult(callback?: Callback<boolean>): void--><!--Device-VpnObserver-offAuthorizationResult(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | No | the callback used to return the result. |

## onAuthorizationResult

```TypeScript
onAuthorizationResult(callback: Callback<boolean>): void
```

Registers a listener for user authorization results.The authorization results are notified after startVpnExtensionAbility is invoked.Only the results of the current VPN are received.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnObserver-onAuthorizationResult(callback: Callback<boolean>): void--><!--Device-VpnObserver-onAuthorizationResult(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | Yes | the callback used to return the result. |

