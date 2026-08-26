# @ohos.nearlink.remoteDevice(NearLink Remote Device Connection Capability)

This module provides the capabilities of connecting to and managing NearLink remote devices, including connecting to and disconnecting from remote devices, pairing with a trusted device and confirmation, adjusting the connection interval, and subscribing to pairing requests.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import remoteDevice from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createRemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-createremotedevice-f.md) | Creates a **RemoteDevice** instance. |
| [offAcbStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offacbstatechange-f.md) | Unsubscribes from the logical link connection status change event. This API uses an asynchronous callback to return the result. |
| [offConnectionStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offconnectionstatechange-f.md) | Unsubscribes from the connection status change event. This API uses an asynchronous callback to return the result. |
| [offPairingStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offpairingstatechange-f.md) | Unsubscribes from pairing status change events. This API uses an asynchronous callback to return the result. |
| [onAcbStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onacbstatechange-f.md) | Subscribes to the logical link connection status change event. This API uses an asynchronous callback to return the result. This API is applicable when corresponding processing needs to be triggered when a logical link is established or disconnected, for example, checking whether the link is ready before data transfer or clearing resources after disconnection. Unlike [remoteDevice.onConnectionStateChange](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) which listens for the connection status change at the device level, this API listens for the connection status change at the logical link level.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event. |
| [onConnectionStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) | Subscribes to the connection status change event. This API uses an asynchronous callback to return the result. Unlike [remoteDevice.onAcbStateChange](arkts-connectivity-remotedevice-onacbstatechange-f.md) which listens for the connection status change at the logical link level, this API listens for the connection status change at the device level.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event. |
| [onPairingStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onpairingstatechange-f.md) | Subscribes to pairing status change events. This API uses an asynchronous callback to return the result.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [offPairingRequest(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offpairingrequest-f-sys.md) | Unsubscribes from pairing request events from remote NearLink devices. |
| [onPairingRequest(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onpairingrequest-f-sys.md) | Subscribes to pairing request events from remote NearLink devices.This event is accessible only to system applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AcbStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-acbstateparam-i.md) | Represents the result of the logical link connection status change event. |
| [ConnectionStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionstateparam-i.md) | Describes the connection state parameters. |
| [DeviceInformation(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-deviceinformation-i.md) | Describes the remote device information. |
| [PairingRequestParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingrequestparam-i.md) | Describes pairing request parameters. |
| [PairingStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingstateparam-i.md) | Describes the pairing state parameters. |
| [RemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-remotedevice-i.md) | Provides the method for operating on a remote device. Before using this method, you need to call [remoteDevice.createRemoteDevice](arkts-connectivity-remotedevice-createremotedevice-f.md) to create a [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i.md) instance. You need to create only one instance for a device. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DeviceModel(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-devicemodel-i-sys.md) | Describes the model of a remote device. |
| [RemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-remotedevice-i-sys.md) | Provides the method for operating on a remote device. Before using this method, you need to call [remoteDevice.createRemoteDevice](arkts-connectivity-remotedevice-createremotedevice-f.md) to create a [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i.md) instance. You need to create only one instance for a device. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ConnectionReason(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionreason-e.md) | Enum for the connection reason. |
| [PairingReason(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingreason-e.md) | Enum for the pairing reason. |
| [PairingType(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingtype-e.md) | Enumerates the NearLink pairing types. |

### Types

| Name | Description |
| --- | --- |
| [AcbState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-acbstate-t.md) | Enumerates the logical link connection states with a remote device. |
| [ConnectionState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionstate-t.md) | Enumerates the connection states with a remote device. |
| [DeviceClass(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-deviceclass-t.md) | Enumerates the device types. |
| [PairingState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingstate-t.md) | Enumerates the pairing statuses with a remote device. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [ConnectionInterval(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) | Enumerates the connection intervals. |
<!--DelEnd-->
