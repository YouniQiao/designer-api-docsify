# @ohos.distributedsched.abilityConnectionManager

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后， 系统应用和三方应用可以跨设备拉起同应用的一个[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)， 拉起并连接成功后可实现跨设备数据传输（文本信息）。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [acceptConnect](arkts-distributedservice-abilityconnectionmanager-acceptconnect-f.md) |
| [connect](arkts-distributedservice-abilityconnectionmanager-connect-f.md) |
| [createAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-createabilityconnectionsession-f.md) |
| [destroyAbilityConnectionSession](arkts-distributedservice-abilityconnectionmanager-destroyabilityconnectionsession-f.md) |
| [disconnect](arkts-distributedservice-abilityconnectionmanager-disconnect-f.md) |
| [getPeerInfoById](arkts-distributedservice-abilityconnectionmanager-getpeerinfobyid-f.md) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offconnect) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offdisconnect) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offreceivemessage) |
| [off](arkts-distributedservice-abilityconnectionmanager-off-f.md#offreceivedata) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onconnect) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#ondisconnect) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onreceivemessage) |
| [on](arkts-distributedservice-abilityconnectionmanager-on-f.md#onreceivedata) |
| [reject](arkts-distributedservice-abilityconnectionmanager-reject-f.md) |
| [sendData](arkts-distributedservice-abilityconnectionmanager-senddata-f.md) |
| [sendMessage](arkts-distributedservice-abilityconnectionmanager-sendmessage-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createStream](arkts-distributedservice-abilityconnectionmanager-createstream-f-sys.md) |
| [destroyStream](arkts-distributedservice-abilityconnectionmanager-destroystream-f-sys.md) |
| [getSurfaceId](arkts-distributedservice-abilityconnectionmanager-getsurfaceid-f-sys.md) |
| off |
| off |
| on |
| on |
| [sendImage](arkts-distributedservice-abilityconnectionmanager-sendimage-f-sys.md) |
| [setSurfaceId](arkts-distributedservice-abilityconnectionmanager-setsurfaceid-f-sys.md) |
| [startStream](arkts-distributedservice-abilityconnectionmanager-startstream-f-sys.md) |
| [stopStream](arkts-distributedservice-abilityconnectionmanager-stopstream-f-sys.md) |
| [updateSurfaceParam](arkts-distributedservice-abilityconnectionmanager-updatesurfaceparam-f-sys.md) |
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
