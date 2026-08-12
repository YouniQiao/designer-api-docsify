# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 18

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
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md#acceptconnect) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md#connect) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md#createabilityconnectionsession) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md#destroyabilityconnectionsession) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md#disconnect) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getpeerinfobyid) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#off) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#off-1) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#off-2) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#off-3) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#on) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#on-1) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#on-2) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#on-3) |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md#reject) |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md#senddata) |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md#sendmessage) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md#createstream) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md#destroystream) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md#getsurfaceid) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f-sys.md#off-4) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f-sys.md#off-5) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f-sys.md#on-4) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f-sys.md#on-5) |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md#sendimage) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md#setsurfaceid) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md#startstream) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md#stopstream) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md#updatesurfaceparam) |
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
