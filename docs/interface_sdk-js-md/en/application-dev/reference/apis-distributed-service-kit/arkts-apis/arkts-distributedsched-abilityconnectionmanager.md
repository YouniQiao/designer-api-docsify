# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offconnect) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offdisconnect) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offreceivemessage) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offreceivedata) |
| [offConnect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md) |
| [offDisconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md) |
| [offReceiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md) |
| [offReceiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onconnect) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#ondisconnect) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onreceivemessage) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onreceivedata) |
| [onConnect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md) |
| [onDisconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md) |
| [onReceiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md) |
| [onReceiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md) |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md) |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md) |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f-sys.md#offreceiveimage) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f-sys.md#offcollaborateevent) |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md) |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f-sys.md#onreceiveimage) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f-sys.md#oncollaborateevent) |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md) |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md) |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CollaborateEventInfo](arkts-distributedservice-abilityconnectionmanager-collaborateeventinfo-i.md) |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i.md) |
| [ConnectResult](arkts-distributedservice-abilityconnectionmanager-connectresult-i.md) |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i.md) |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i-sys.md) |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i-sys.md) |
| [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) |
| [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CollaborateEventType](arkts-distributedservice-abilityconnectionmanager-collaborateeventtype-e.md) |
| [CollaborationKeys](arkts-distributedservice-abilityconnectionmanager-collaborationkeys-e.md) |
| [CollaborationValues](arkts-distributedservice-abilityconnectionmanager-collaborationvalues-e.md) |
| [ConnectErrorCode](arkts-distributedservice-abilityconnectionmanager-connecterrorcode-e.md) |
| [DisconnectReason](arkts-distributedservice-abilityconnectionmanager-disconnectreason-e.md) |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md) |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e-sys.md) |
| [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md) |
| [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md) |
<!--DelEnd-->
