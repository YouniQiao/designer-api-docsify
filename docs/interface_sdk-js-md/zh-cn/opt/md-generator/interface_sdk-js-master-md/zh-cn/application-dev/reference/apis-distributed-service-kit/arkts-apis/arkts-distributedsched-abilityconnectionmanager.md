# @ohos.distributedsched.abilityConnectionManager

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后，系统应用和三方应用可以跨设备拉起同应用的一个 [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility)，拉起并连接成功后可实现跨设备数据传输（文本信息）。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 汇总

### 函数

| 名称 |
| --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md#acceptConnect) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md#connect) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md#createAbilityConnectionSession) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md#destroyAbilityConnectionSession) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md#disconnect) |
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
### 函数（系统接口）

| 名称 |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md#createStream（系统接口）) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md#destroyStream（系统接口）) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md#getSurfaceId（系统接口）) |
| [offCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md#offCollaborateEvent（系统接口）) |
| [offReceiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md#offReceiveImage（系统接口）) |
| [off_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-offcollaborateevent-f-sys.md) |
| [off_receiveImage](arkts-distributedservice-abilityconnectionmanager-offreceiveimage-f-sys.md) |
| [onCollaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md#onCollaborateEvent（系统接口）) |
| [onReceiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md#onReceiveImage（系统接口）) |
| [on_collaborateEvent](arkts-distributedservice-abilityconnectionmanager-oncollaborateevent-f-sys.md) |
| [on_receiveImage](arkts-distributedservice-abilityconnectionmanager-onreceiveimage-f-sys.md) |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md#sendImage（系统接口）) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md#setSurfaceId（系统接口）) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md#startStream（系统接口）) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md#stopStream（系统接口）) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md#updateSurfaceParam（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CollaborateEventInfo](arkts-distributedservice-abilityconnectionmanager-collaborateeventinfo-i.md) |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i.md) |
| [ConnectResult](arkts-distributedservice-abilityconnectionmanager-connectresult-i.md) |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i.md) |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ConnectOptions](arkts-distributedservice-abilityconnectionmanager-connectoptions-i-sys.md) |
| [EventCallbackInfo](arkts-distributedservice-abilityconnectionmanager-eventcallbackinfo-i-sys.md) |
| [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) |
| [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [CollaborateEventType](arkts-distributedservice-abilityconnectionmanager-collaborateeventtype-e.md) |
| [CollaborationKeys](arkts-distributedservice-abilityconnectionmanager-collaborationkeys-e.md) |
| [CollaborationValues](arkts-distributedservice-abilityconnectionmanager-collaborationvalues-e.md) |
| [ConnectErrorCode](arkts-distributedservice-abilityconnectionmanager-connecterrorcode-e.md) |
| [DisconnectReason](arkts-distributedservice-abilityconnectionmanager-disconnectreason-e.md) |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md) |
| [StartOptionParams](arkts-distributedservice-abilityconnectionmanager-startoptionparams-e-sys.md) |
| [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md) |
| [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md) |
<!--DelEnd-->
