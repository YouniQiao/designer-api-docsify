# @ohos.abilityToolAccessCtrl(工具访问控制)

工具访问控制模块提供工具（CLI命令和API接口）的权限管理能力，包括权限查询、用户授权、远程授权等功能。当需要查询CLI命令或API接口的权限状态、进行工具权限授权、或管理远程设备的授权时，使用本模块接口。

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-unnamed-declare namespace abilityToolAccessCtrl--><!--Device-unnamed-declare namespace abilityToolAccessCtrl-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [queryControlAppStatus](arkts-ability-abilitytoolaccessctrl-querycontrolappstatus-f.md#querycontrolappstatus-1) | 查询指定应用的控制权限状态。使用Promise异步回调。检查输入列表中的每个应用是否被允许或拒绝被外部工具控制。结果列表与输入列表顺序一一对应。使用Promise异步回调。 |
| [registerControlComponentResultCallback](arkts-ability-abilitytoolaccessctrl-registercontrolcomponentresultcallback-f.md#registercontrolcomponentresultcallback-1) | 注册控制组件模拟点击结果回调。注册后，控制组件每次模拟点击的结果通过该回调返回。同一进程内仅支持注册一个回调，重复注册将覆盖先前注册的回调。 |
| [requestControlAppPermissionFromUser](arkts-ability-abilitytoolaccessctrl-requestcontrolapppermissionfromuser-f.md#requestcontrolapppermissionfromuser-1) | 向用户请求指定应用的控制权限。弹出用户对话框，获取用户对每个应用的控制授权决定。返回结果反映用户对每个应用的允许或拒绝决策，与输入列表顺序一一对应。使用Promise异步回调。 |
| [requestToolTicket](arkts-ability-abilitytoolaccessctrl-requesttoolticket-f.md#requesttoolticket-1) | 获取CLI工具的执行认证ticket。传入CLI命令列表，如果用户尚未授权CLI工具所需的权限，返回需要授权的权限列表及其状态；如果用户已授权所有所需权限，返回已认证的ticket。使用Promise异步回调。 |
| [unregisterControlComponentResultCallback](arkts-ability-abilitytoolaccessctrl-unregistercontrolcomponentresultcallback-f.md#unregistercontrolcomponentresultcallback-1) | 注销控制组件模拟点击结果回调。用于在业务结束时释放回调资源。 |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [generateControlledDevicePackage](arkts-ability-abilitytoolaccessctrl-generatecontrolleddevicepackage-f-sys.md#generatecontrolleddevicepackage-1) | 在被控设备上，根据权限查询列表生成远程授权请求包。生成的包可以发送到主控设备上，完成完整性校验后，发起用户授权确认。使用Promise异步回调。 |
| [generateControllerDevicePackage](arkts-ability-abilitytoolaccessctrl-generatecontrollerdevicepackage-f-sys.md#generatecontrollerdevicepackage-1) | 在主控设备上，生成远程授权结果包。生成的包可以发送到被控设备上，完成完整性校验后，执行权限授权。使用Promise异步回调。 |
| [generateTaskChallenge](arkts-ability-abilitytoolaccessctrl-generatetaskchallenge-f-sys.md#generatetaskchallenge-1) | 基于任务身份信息生成挑战值。使用Promise异步回调。 |
| [generateTaskIdentity](arkts-ability-abilitytoolaccessctrl-generatetaskidentity-f-sys.md#generatetaskidentity-1) | 为智能体命令生成任务标识。该函数根据调用者身份和基本任务属性（例如任务ID和任务过期时间）生成该标识。使用Promise异步回调。 |
| [getRemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-getremotegrantstatus-f-sys.md#getremotegrantstatus-1) | 查询远程授权开关的使能状态。启用时设备可以发起远程授权，禁用时不允许远程授权。使用Promise异步回调。 |
| [grantToolPermissionsByUser](arkts-ability-abilitytoolaccessctrl-granttoolpermissionsbyuser-f-sys.md#granttoolpermissionsbyuser-1) | 根据用户授权结果，为工具（CLI命令或API接口）授予权限。授权成功后，生成可用于权限验证的ticket。使用Promise异步回调。 |
| [requestToolPermissions](arkts-ability-abilitytoolaccessctrl-requesttoolpermissions-f-sys.md#requesttoolpermissions-1) | 根据指定操作查询工具权限。检查入参permissionQuery的operationInfo属性中指定的CLI命令或API接口的权限状态，返回每个操作的权限状态、授权状态以及是否需要用户弹窗。当permissionQuery.needTicket设置为true时，将生成用于远程授权的ticket。使用Promise异步回调。 |
| [revokeTaskIdentity](arkts-ability-abilitytoolaccessctrl-revoketaskidentity-f-sys.md#revoketaskidentity-1) | 批量撤销智能体命令的任务标识，并删除任务属性的本地缓存。使用Promise异步回调。 |
| [updateRemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-updateremotegrantstatus-f-sys.md#updateremotegrantstatus-1) | 更新远程授权开关状态，开启或关闭远程授权使能开关。启用时设备可以发起远程授权，禁用时不允许远程授权。使用Promise异步回调。 |
| [verifyControlledDevicePackage](arkts-ability-abilitytoolaccessctrl-verifycontrolleddevicepackage-f-sys.md#verifycontrolleddevicepackage-1) | 验证被控设备发送的授权请求包，检查消息凭据以确保授权请求合法。使用Promise异步回调。 |
| [verifyControllerDevicePackage](arkts-ability-abilitytoolaccessctrl-verifycontrollerdevicepackage-f-sys.md#verifycontrollerdevicepackage-1) | 验证主控设备发送的远程授权结果包，检查消息凭据和远程设备信息以确保授权结果合法。使用Promise异步回调。 |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AppInfo](arkts-ability-abilitytoolaccessctrl-appinfo-i.md) | 表示应用信息。 |
| [CliCmdInfo](arkts-ability-abilitytoolaccessctrl-clicmdinfo-i.md) | 表示CLI（Command Line Interface，命令行界面）命令信息。 |
| [ControlAppStatusResult](arkts-ability-abilitytoolaccessctrl-controlappstatusresult-i.md) | 表示应用控制权限状态查询结果。 |
| [ControlComponentClickResult](arkts-ability-abilitytoolaccessctrl-controlcomponentclickresult-i.md) | 模拟点击操作结果。 |
| [PermissionInfo](arkts-ability-abilitytoolaccessctrl-permissioninfo-i.md) | 表示权限信息。 |
| [TicketParams](arkts-ability-abilitytoolaccessctrl-ticketparams-i.md) | 表示生成ticket的参数。各字段均为可选，未传入的字段使用默认值。 |
| [TicketQueryResult](arkts-ability-abilitytoolaccessctrl-ticketqueryresult-i.md) | 表示ticket查询结果。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AuthStatusInfo](arkts-ability-abilitytoolaccessctrl-authstatusinfo-i-sys.md) | 表示授权状态信息。 |
| [OperationInfo](arkts-ability-abilitytoolaccessctrl-operationinfo-i-sys.md) | 表示操作信息。 |
| [PermissionInfo](arkts-ability-abilitytoolaccessctrl-permissioninfo-i-sys.md) | 表示权限信息。 |
| [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | 表示权限查询信息。 |
| [PermissionQueryResult](arkts-ability-abilitytoolaccessctrl-permissionqueryresult-i-sys.md) | 表示权限查询结果。 |
| [RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md) | 表示远程授权包。 |
| [RemoteControlParams](arkts-ability-abilitytoolaccessctrl-remotecontrolparams-i-sys.md) | 表示远程控制交互参数。 |
| [RemoteInfo](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md) | 表示远端设备信息。 |
| [RemoteUserAuthItem](arkts-ability-abilitytoolaccessctrl-remoteuserauthitem-i-sys.md) | 表示远程用户授权项。 |
| [RemoteUserAuthResults](arkts-ability-abilitytoolaccessctrl-remoteuserauthresults-i-sys.md) | 表示远程用户授权结果。 |
| [TaskIdentity](arkts-ability-abilitytoolaccessctrl-taskidentity-i-sys.md) | 任务标识。 |
| [TaskIdentityInfo](arkts-ability-abilitytoolaccessctrl-taskidentityinfo-i-sys.md) | 任务标识的输入参数，包含任务ID、过期时间、执行类型等信息，用于生成任务挑战值或任务标识。 |
| [TicketInfo](arkts-ability-abilitytoolaccessctrl-ticketinfo-i-sys.md) | 表示ticket信息。 |
| [UserAuthResult](arkts-ability-abilitytoolaccessctrl-userauthresult-i-sys.md) | 表示用户授权结果。 |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [ResultCallback](arkts-ability-abilitytoolaccessctrl-resultcallback-t.md) | 用于接收每次模拟点击操作结果的回调函数类型。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ControlAppStatus](arkts-ability-abilitytoolaccessctrl-controlappstatus-e.md) | 表示应用控制权限状态枚举。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AuthStatus](arkts-ability-abilitytoolaccessctrl-authstatus-e-sys.md) | 表示授权状态枚举。 |
| [ExecuteType](arkts-ability-abilitytoolaccessctrl-executetype-e-sys.md) | 任务执行类别。 |
| [OperationType](arkts-ability-abilitytoolaccessctrl-operationtype-e-sys.md) | 表示操作类型枚举。 |
| [RemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md) | 表示远程授权状态枚举。 |
| [Role](arkts-ability-abilitytoolaccessctrl-role-e-sys.md) | 表示设备角色枚举。 |
<!--DelEnd-->
