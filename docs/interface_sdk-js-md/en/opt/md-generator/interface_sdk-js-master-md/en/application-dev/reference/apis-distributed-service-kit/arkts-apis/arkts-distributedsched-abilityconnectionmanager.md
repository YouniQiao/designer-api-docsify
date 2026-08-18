# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#uiability) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md#acceptconnect) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md#connect) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md#createabilityconnectionsession) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md#destroyabilityconnectionsession) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md#disconnect) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getpeerinfobyid) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getpeerinfobyid) |
| [offConnect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md#offconnect) |
| [offDisconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md#offdisconnect) |
| [offReceiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md#offreceivedata) |
| [offReceiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md#offreceivemessage) |
| [off_connect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md#offconnect) |
| [off_disconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md#offdisconnect) |
| [off_receiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md#offreceivedata) |
| [off_receiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md#offreceivemessage) |
| [onConnect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md#onconnect) |
| [onDisconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md#ondisconnect) |
| [onReceiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md#onreceivedata) |
| [onReceiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md#onreceivemessage) |
| [on_connect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md#onconnect) |
| [on_disconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md#ondisconnect) |
| [on_receiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md#onreceivedata) |
| [on_receiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md#onreceivemessage) |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md#reject) |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md#senddata) |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md#sendmessage) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md#createstream-system-api) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md#destroystream-system-api) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md#getsurfaceid-system-api) |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md#offcollaborateevent) |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md#offreceiveimage) |
| [off_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md#offcollaborateevent) |
| [off_receiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md#offreceiveimage) |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md#oncollaborateevent) |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md#onreceiveimage) |
| [on_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md#oncollaborateevent) |
| [on_receiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md#onreceiveimage) |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md#sendimage-system-api) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md#setsurfaceid-system-api) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md#startstream-system-api) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md#stopstream-system-api) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md#updatesurfaceparam-system-api) |
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
### Interfaces（系统接口）

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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md) |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e-sys.md) |
| [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md) |
| [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md) |
<!--DelEnd-->
