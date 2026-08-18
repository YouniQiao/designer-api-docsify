# VpnObserver

Defines a VPN observer.

**Since:** 26.0.0

<!--Device-vpnExtension-export interface VpnObserver--><!--Device-vpnExtension-export interface VpnObserver-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
```

## offAuthorizationResult

```TypeScript
offAuthorizationResult(callback?: Callback<boolean>): void
```

Unregisters the listener for user authorization results.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnObserver-offAuthorizationResult(callback?: Callback<boolean>): void--><!--Device-VpnObserver-offAuthorizationResult(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | No |

**Examples**

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';

let vpnObserver: vpnExtension.VpnObserver = vpnExtension.createVpnObserver();

let callback = (result: boolean) => {
  console.info('Authorization result: ' + result);
};
// Register a listener.
vpnObserver.onAuthorizationResult(callback);

// Unregister a specified listener.
vpnObserver.offAuthorizationResult(callback);

// Unregister all registered listeners.
vpnObserver.offAuthorizationResult();
```

## onAuthorizationResult

```TypeScript
onAuthorizationResult(callback: Callback<boolean>): void
```

Registers a listener for user authorization results. The authorization results are notified after startVpnExtensionAbility is invoked. Only the results of the current VPN are received.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnObserver-onAuthorizationResult(callback: Callback<boolean>): void--><!--Device-VpnObserver-onAuthorizationResult(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;boolean & gt; | Yes |

**Examples**

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';

let vpnObserver: vpnExtension.VpnObserver = vpnExtension.createVpnObserver();
vpnObserver.onAuthorizationResult((result: boolean) => {
  if (result) {
    console.info('VPN authorization succeeded');
  } else {
    console.error('VPN authorization failed');
  }
});
```
