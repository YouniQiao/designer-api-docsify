# @ohos.nearlink.remoteDevice(NearLink Remote Device Connection Capability)

This module provides the capabilities of connecting to and managing NearLink remote devices, including connecting to and disconnecting from remote devices, pairing with a trusted device and confirmation, adjusting the connection interval, and subscribing to pairing requests.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createRemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-createremotedevice-f.md) |
| [offAcbStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offacbstatechange-f.md) |
| [offConnectionStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offconnectionstatechange-f.md) |
| [offPairingStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offpairingstatechange-f.md) |
| [onAcbStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onacbstatechange-f.md) |
| [onConnectionStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) |
| [onPairingStateChange(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onpairingstatechange-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offPairingRequest(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-offpairingrequest-f-sys.md) |
| [onPairingRequest(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-onpairingrequest-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AcbStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-acbstateparam-i.md) |
| [ConnectionStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionstateparam-i.md) |
| [DeviceInformation(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-deviceinformation-i.md) |
| [PairingRequestParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingrequestparam-i.md) |
| [PairingStateParam(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingstateparam-i.md) |
| [RemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-remotedevice-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceModel(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-devicemodel-i-sys.md) |
| [RemoteDevice(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-remotedevice-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionReason(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionreason-e.md) |
| [PairingReason(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingreason-e.md) |
| [PairingType(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AcbState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-acbstate-t.md) |
| [ConnectionState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectionstate-t.md) |
| [DeviceClass(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-deviceclass-t.md) |
| [PairingState(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-pairingstate-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionInterval(NearLink Remote Device Connection Capability)](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) |
<!--DelEnd-->
