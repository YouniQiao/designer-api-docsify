# @ohos.nearlink.manager

Provides methods to manage NearLink devices.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace manager--><!--Device-unnamed-declare namespace manager-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { manager } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getLocalName](arkts-connectivity-manager-getlocalname-f.md) | Gets the local device's name. |
| [getPairedDevices](arkts-connectivity-manager-getpaireddevices-f.md) | Gets the list of devices that have been paired with the current device. If the user has the ohos.permission.GET_NEARLINK_PEER_MAC permission, the real device address is returned. Otherwise, a random device address is returned. |
| [getState](arkts-connectivity-manager-getstate-f.md) | Gets the NearLink state. |
| [isNearLinkSupported](arkts-connectivity-manager-isnearlinksupported-f.md) | Check whether the current device supports NearLink. |
| [offStateChange](arkts-connectivity-manager-offstatechange-f.md) | Unsubscribes from state change events. |
| [onStateChange](arkts-connectivity-manager-onstatechange-f.md) | Subscribes to state change events. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [disable](arkts-connectivity-manager-disable-f-sys.md) | Turns off NearLink. |
| [enable](arkts-connectivity-manager-enable-f-sys.md) | Turns on NearLink. |
| [factoryReset](arkts-connectivity-manager-factoryreset-f-sys.md) | Restores NearLink settings. |
| [getLocalAddress](arkts-connectivity-manager-getlocaladdress-f-sys.md) | Gets the MAC address of the local device. |
| [setConnectionMode](arkts-connectivity-manager-setconnectionmode-f-sys.md) | Sets the NearLink connection mode for a device. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md) | The enum of NearLink state. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ConnectionMode](arkts-connectivity-manager-connectionmode-e-sys.md) | The enum of connection mode. |
<!--DelEnd-->

