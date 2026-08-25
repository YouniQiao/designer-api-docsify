# VpnObserver

Defines a VPN observer object. It is used to listen for VPN-related events. Before calling **VpnObserver** APIs, you need to create a VPN connection object by calling [vpnExtension.createVpnObserver](arkts-network-vpnextension-createvpnobserver-f.md).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## offAuthorizationResult

```TypeScript
offAuthorizationResult(callback?: Callback<boolean>): void
```

Unregisters a listener for the user authorization result.

> **NOTE：**&gt;
> If you have called [onAuthorizationResult](#onauthorizationresult) multiple times to register
> listeners and want to unregister the listener, you need to pass the callback passed in the last call or pass no
> parameter.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | No |

## onAuthorizationResult

```TypeScript
onAuthorizationResult(callback: Callback<boolean>): void
```

Registers a listener for the user authorization result. The authorization result is displayed in a dialog box after [startVpnExtensionAbility](arkts-network-vpnextension-startvpnextensionability-f.md) is called. The notification is sent only when the user taps the dialog box, and only the result of the current VPN is received. If you do not need to listen for the authorization result, call [offAuthorizationResult](#offauthorizationresult) to cancel the registration.

> **NOTE：**&gt;
> If this API is called multiple times, only the last callback takes effect.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | Yes |
