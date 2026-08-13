# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md#acceptConnect) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md#connect) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md#createAbilityConnectionSession) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md#destroyAbilityConnectionSession) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md#disconnect) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getPeerInfoById) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getPeerInfoById) |
| [offConnect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md#offConnect) |
| [offDisconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md#offDisconnect) |
| [offReceiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md#offReceiveData) |
| [offReceiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md#offReceiveMessage) |
| off_connect |
| off_disconnect |
| off_receiveData |
| [off_receiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md) |
| [onConnect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md#onConnect) |
| [onDisconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md#onDisconnect) |
| [onReceiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md#onReceiveData) |
| [onReceiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md#onReceiveMessage) |
| on_connect |
| on_disconnect |
| on_receiveData |
| [on_receiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md) |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md#reject) |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md#sendData) |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md#sendMessage) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md#createStream-(System-API)) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md#destroyStream-(System-API)) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md#getSurfaceId-(System-API)) |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md#offCollaborateEvent-(System-API)) |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md#offReceiveImage-(System-API)) |
| [off_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md) |
| [off_receiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md) |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md#onCollaborateEvent-(System-API)) |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md#onReceiveImage-(System-API)) |
| [on_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md) |
| [on_receiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md) |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md#sendImage-(System-API)) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md#setSurfaceId-(System-API)) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md#startStream-(System-API)) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md#stopStream-(System-API)) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md#updateSurfaceParam-(System-API)) |
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
