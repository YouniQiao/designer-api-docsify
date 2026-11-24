# PermissionQuery（系统接口）

```TypeScript
interface PermissionQuery
```

表示权限查询信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface PermissionQuery--><!--Device-abilityToolAccessCtrl-interface PermissionQuery-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## callerTokenId

```TypeScript
callerTokenId?: number
```

调用方进程的tokenId。当需要为其他进程查询或授权时，可指定目标进程的tokenId。如果未传入该参数，默认获取调用方进程的tokenId。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-callerTokenId?: long--><!--Device-PermissionQuery-callerTokenId?: long-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## domainId

```TypeScript
domainId?: string
```

域标识。如果未传入该参数，则默认使用调用方当前的域标识。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-domainId?: string--><!--Device-PermissionQuery-domainId?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## needTicket

```TypeScript
needTicket?: boolean
```

是否需要生成ticket用于本地或远程授权。true表示需要生成ticket，false表示不需要。当设置为true时，仅在本次查询结果通过的情况下才会返回ticket信息。默认值：false

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-needTicket?: boolean--><!--Device-PermissionQuery-needTicket?: boolean-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## operationInfo

```TypeScript
operationInfo: OperationInfo[]
```

操作信息列表，指定待查询的CLI命令或API接口。

**类型：** [OperationInfo](arkts-ability-abilitytoolaccessctrl-operationinfo-i-sys.md)[]

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-operationInfo: OperationInfo[]--><!--Device-PermissionQuery-operationInfo: OperationInfo[]-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## remoteInfo

```TypeScript
remoteInfo?: RemoteInfo
```

远端设备信息，包含设备角色、设备ID、域标识等。用于远程授权场景。

**类型：** [RemoteInfo](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md)

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-remoteInfo?: RemoteInfo--><!--Device-PermissionQuery-remoteInfo?: RemoteInfo-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## taskIdentity

```TypeScript
taskIdentity?: TaskIdentity
```

任务标识，用于智能体命令的任务身份验证。可通过generateTaskIdentity获取。默认值：空。

**类型：** [TaskIdentity](arkts-ability-abilitytoolaccessctrl-taskidentity-i-sys.md)

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-taskIdentity?: TaskIdentity--><!--Device-PermissionQuery-taskIdentity?: TaskIdentity-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## ticketExpireTimeMs

```TypeScript
ticketExpireTimeMs?: number
```

ticket过期时间，单位为毫秒。需配合needTicket参数使用，仅当needTicket为true时本参数生效。常规授权场景取值范围：1~60000（60秒），长时间远程授权场景取值范围：1~86400000（24小时），超过最大值将返回错误码24010000。默认值：10000

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionQuery-ticketExpireTimeMs?: long--><!--Device-PermissionQuery-ticketExpireTimeMs?: long-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
