# @ohos.nearlink.remoteDevice

Provides interaction methods such as pairing and connection with remote devices.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace remoteDevice--><!--Device-unnamed-declare namespace remoteDevice-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createRemoteDevice](arkts-connectivity-remotedevice-createremotedevice-f.md) | Creates a remote device instance. |
| [offAcbStateChange](arkts-connectivity-remotedevice-offacbstatechange-f.md) | Unsubscribes from the NearLink ACB connection status change event. |
| [offConnectionStateChange](arkts-connectivity-remotedevice-offconnectionstatechange-f.md) | Unsubscribes from NearLink connection state change events. |
| [offPairingStateChange](arkts-connectivity-remotedevice-offpairingstatechange-f.md) | Unsubscribes from NearLink pairing state change events. |
| [onAcbStateChange](arkts-connectivity-remotedevice-onacbstatechange-f.md) | Subscribes to the NearLink ACB connection status change event. |
| [onConnectionStateChange](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) | Subscribes to NearLink connection state change events. |
| [onPairingStateChange](arkts-connectivity-remotedevice-onpairingstatechange-f.md) | Subscribes to NearLink pairing state change events. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [offPairingRequest](arkts-connectivity-remotedevice-offpairingrequest-f-sys.md) | Unsubscribes from pairing request events from remote NearLink devices. |
| [onPairingRequest](arkts-connectivity-remotedevice-onpairingrequest-f-sys.md) | Subscribes to pairing request events from remote NearLink devices. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AcbStateParam](arkts-connectivity-remotedevice-acbstateparam-i.md) | ACB connection status parameter. |
| [ConnectionStateParam](arkts-connectivity-remotedevice-connectionstateparam-i.md) | Describes the connection state parameters. |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) | Describes the remote device information. |
| [PairingRequestParam](arkts-connectivity-remotedevice-pairingrequestparam-i.md) | Describes pairing request parameters. |
| [PairingStateParam](arkts-connectivity-remotedevice-pairingstateparam-i.md) | Describes the pairing state parameters. |
| [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i.md) | Remote device operation methods. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DeviceModel](arkts-connectivity-remotedevice-devicemodel-i-sys.md) | Describes the remote device's model information. |
| [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i-sys.md) | Remote device operation methods. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ConnectionReason](arkts-connectivity-remotedevice-connectionreason-e.md) | Enum for the connection reason. |
| [PairingReason](arkts-connectivity-remotedevice-pairingreason-e.md) | Enum for the pairing reason. |
| [PairingType](arkts-connectivity-remotedevice-pairingtype-e.md) | Enum for the pairing type. |

### Types

| Name | Description |
| --- | --- |
| [AcbState](arkts-connectivity-remotedevice-acbstate-t.md) | Indicates the ACB(Asynchronous Connection-Oriented Bidirectional) connection status. |
| [ConnectionState](arkts-connectivity-remotedevice-connectionstate-t.md) | Indicates the connection state. |
| [DeviceClass](arkts-connectivity-remotedevice-deviceclass-t.md) | Indicates the device class. |
| [PairingState](arkts-connectivity-remotedevice-pairingstate-t.md) | Indicates the pairing state. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [ConnectionInterval](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) | Indicates the connection interval. |
<!--DelEnd-->

