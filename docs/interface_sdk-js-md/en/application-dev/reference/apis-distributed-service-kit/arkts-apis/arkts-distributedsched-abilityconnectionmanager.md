# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md#acceptConnect) | Accepts the UIAbility connection after a collaboration session is set up and the session ID is obtained. |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md#connect) | Sets up a UIAbility connection after a collaboration session is created and the session ID is obtained. This API uses a promise to return the result. |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md#createAbilityConnectionSession) | Creates a collaboration session between applications. |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md#destroyAbilityConnectionSession) | Destroys a collaboration session between applications. |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md#disconnect) | Disconnects the UIAbility connection to end the collaboration session. |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getPeerInfoById) | Obtains information about the peer application in the specified session. |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md#getPeerInfoById) | Get the application information in the ability connection session |
| [offConnect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md#offConnect) | Unregisters connect event. |
| [offDisconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md#offDisconnect) | Unregisters disconnect event. |
| [offReceiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md#offReceiveData) | Unregisters receiveData event. |
| [offReceiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md#offReceiveMessage) | Unregisters receiveMessage event. |
| off_connect | Disables listening for **connect** events. |
| off_disconnect | Disables listening for **disconnect** events. |
| off_receiveData | Disables listening for **receiveData** events. |
| off_receiveMessage | Disables listening for **receiveMessage** events. |
| [onConnect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md#onConnect) | Registers connect event. |
| [onDisconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md#onDisconnect) | Registers disconnect event. |
| [onReceiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md#onReceiveData) | Registers receiveData event. |
| [onReceiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md#onReceiveMessage) | Registers receiveMessage event. |
| on_connect | Enables listening for **connect** events. This API uses an asynchronous callback to return the result. |
| on_disconnect | Enables listening for **disconnect** events. |
| on_receiveData | Enables listening for **receiveData** events. |
| on_receiveMessage | Enables listening for **receiveMessage** events. |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md#reject) | Rejects a connection request in a cross-device collaboration session. After a connection request sent from the peer application is rejected, a rejection reason is returned. |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md#sendData) | Sends [ArrayBuffer](../../../arkts-utils/arraybuffer-object.md) byte streams from one device to another after a connection is successfully established. |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md#sendMessage) | Sends text messages after a collaboration session is set up. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md#createStream) | Creating a Stream. |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md#destroyStream) | Destroy the Stream. |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md#getSurfaceId) | Obtains the transmission surface. |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md#offCollaborateEvent) | Unregisters collaborateEvent event. |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md#offReceiveImage) | Unregisters receiveImage event. |
| off_collaborateEvent | Unregisters collaborateEvent event. |
| off_receiveImage | Unregisters receiveImage event. |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md#onCollaborateEvent) | Registers collaborateEvent event. |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md#onReceiveImage) | Registers receiveImage event. |
| on_collaborateEvent | Registers collaborateEvent event. |
| on_receiveImage | Registers receiveImage event. |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md#sendImage) | Send image data. |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md#setSurfaceId) | Sets the transmission surface. |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md#startStream) | Start Streaming |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md#stopStream) | Stop Streaming |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md#updateSurfaceParam) | Update surface parameters. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CollaborateEventInfo](arkts-distributedservice-abilityconnectionmanager-collaborateeventinfo-i.md) | Collaboration event information. |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i.md) | Connection options for the application. |
| [ConnectResult](arkts-distributedservice-abilityconnectionmanager-connectresult-i.md) | Defines the connection result. |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i.md) | Defines the event callback information. |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) | Defines the application collaboration information. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i-sys.md) | Connection options for the application. |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i-sys.md) | Defines the event callback information. |
| [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) | Streaming configuration parameters. |
| [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | Surface configuration parameters. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CollaborateEventType](arkts-distributedservice-abilityconnectionmanager-collaborateeventtype-e.md) | Enumerates collaboration event types. |
| [CollaborationKeys](arkts-distributedservice-abilityconnectionmanager-collaborationkeys-e.md) | Enumerates application collaboration key values. |
| [CollaborationValues](arkts-distributedservice-abilityconnectionmanager-collaborationvalues-e.md) | Enumerates application collaboration key values. |
| [ConnectErrorCode](arkts-distributedservice-abilityconnectionmanager-connecterrorcode-e.md) | Enumerates connection error codes. |
| [DisconnectReason](arkts-distributedservice-abilityconnectionmanager-disconnectreason-e.md) | Enumerates the disconnection reasons. |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e.md) | Enumerates application start options. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md) | Flip option. |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e-sys.md) | Enumerates application start options. |
| [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md) | Stream transmission role. |
| [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md) | Video pixelFormat Configuration Options. |
<!--DelEnd-->

