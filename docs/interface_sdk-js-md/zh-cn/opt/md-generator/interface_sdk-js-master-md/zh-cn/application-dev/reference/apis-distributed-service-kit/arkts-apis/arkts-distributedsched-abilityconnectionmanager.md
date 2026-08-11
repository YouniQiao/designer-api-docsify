# @ohos.distributedsched.abilityConnectionManager

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后，系统应用和三方应用可以跨设备拉起同应用的一个  
[UIAbility](../../apis-ability-kit/arkts-apis/arkts-app-ability-uiability.md/arkts-app-ability-uiability.md)，拉起并连接成功后可实现跨设备数据传输（文本信息）。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace abilityConnectionManager--><!--Device-unnamed-declare namespace abilityConnectionManager-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
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
