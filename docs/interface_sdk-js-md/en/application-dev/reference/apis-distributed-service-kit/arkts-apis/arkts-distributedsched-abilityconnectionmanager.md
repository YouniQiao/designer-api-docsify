# @ohos.distributedsched.abilityConnectionManager

The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful networking between devices (login with the same account and enabling of Bluetooth on the devices), a system application and a third-party application can start a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md) of the same application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be transmitted across the devices over the connection.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md) | Accepts the UIAbility connection after a collaboration session is set up and the session ID is obtained. |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md) | Sets up a UIAbility connection after a collaboration session is created and the session ID is obtained. This API uses a promise to return the result. |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md) | Creates a collaboration session between applications. |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md) | Destroys a collaboration session between applications. |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md) | Disconnects the UIAbility connection to end the collaboration session. |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md) | Obtains information about the peer application in the specified session. |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md) | Get the application information in the ability connection session |
| [off_connect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md) | Disables listening for **connect** events. |
| [off_disconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md) | Disables listening for **disconnect** events. |
| [off_receiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md) | Disables listening for **receiveData** events. |
| [off_receiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md) | Disables listening for **receiveMessage** events. |
| [offConnect](arkts-distributedservice-abilityconnectionmanager-offconnect-f.md) | Unregisters connect event. |
| [offDisconnect](arkts-distributedservice-abilityconnectionmanager-offdisconnect-f.md) | Unregisters disconnect event. |
| [offReceiveData](arkts-distributedservice-abilityconnectionmanager-offreceivedata-f.md) | Unregisters receiveData event. |
| [offReceiveMessage](arkts-distributedservice-abilityconnectionmanager-offreceivemessage-f.md) | Unregisters receiveMessage event. |
| [on_connect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md) | Enables listening for **connect** events. This API uses an asynchronous callback to return the result. |
| [on_disconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md) | Enables listening for **disconnect** events. |
| [on_receiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md) | Enables listening for **receiveData** events. |
| [on_receiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md) | Enables listening for **receiveMessage** events. |
| [onConnect](arkts-distributedservice-abilityconnectionmanager-onconnect-f.md) | Registers connect event. |
| [onDisconnect](arkts-distributedservice-abilityconnectionmanager-ondisconnect-f.md) | Registers disconnect event. |
| [onReceiveData](arkts-distributedservice-abilityconnectionmanager-onreceivedata-f.md) | Registers receiveData event. |
| [onReceiveMessage](arkts-distributedservice-abilityconnectionmanager-onreceivemessage-f.md) | Registers receiveMessage event. |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md) | Rejects a connection request in a cross-device collaboration session. After a connection request sent from the peer application is rejected, a rejection reason is returned. |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md) | Sends [ArrayBuffer](../../../arkts-utils/arraybuffer-object.md) byte streams from one device to another after a connection is successfully established. |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md) | Sends text messages after a collaboration session is set up. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md) | Creating a Stream. |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md) | Destroy the Stream. |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md) | Obtains the transmission surface. |
| [off_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md) | Unregisters collaborateEvent event. |
| [off_receiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md) | Unregisters receiveImage event. |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md) | Unregisters collaborateEvent event. |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md) | Unregisters receiveImage event. |
| [on_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md) | Registers collaborateEvent event. |
| [on_receiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md) | Registers receiveImage event. |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md) | Registers collaborateEvent event. |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md) | Registers receiveImage event. |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md) | Send image data. |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md) | Sets the transmission surface. |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md) | Start Streaming |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md) | Stop Streaming |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md) | Update surface parameters. |
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
### Interfaces(System API)

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
### Enums(System API)

| Name | Description |
| --- | --- |
| [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md) | Flip option. |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e-sys.md) | Enumerates application start options. |
| [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md) | Stream transmission role. |
| [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md) | Video pixelFormat Configuration Options. |
<!--DelEnd-->

