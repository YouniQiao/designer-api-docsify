# TicketQueryResult

```TypeScript
interface TicketQueryResult
```

表示ticket查询结果。

**起始版本：** 26.1.0

<!--Device-abilityToolAccessCtrl-interface TicketQueryResult--><!--Device-abilityToolAccessCtrl-interface TicketQueryResult-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## permissionResults

```TypeScript
permissionResults: PermissionInfo[]
```

权限状态结果列表。当用户尚未授权CLI工具所需的权限时，返回需要授权的权限列表及其状态。

**类型：** [PermissionInfo](arkts-ability-abilitytoolaccessctrl-permissioninfo-i.md)[]

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketQueryResult-permissionResults: PermissionInfo[]--><!--Device-TicketQueryResult-permissionResults: PermissionInfo[]-End-->

**系统能力：** SystemCapability.Security.Asset

## ticket

```TypeScript
ticket: string
```

ticket字符串，用于权限验证。当用户已授权所有所需权限时，返回已认证的ticket；当用户尚未授权所有权限时，该项为空字符串。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketQueryResult-ticket: string--><!--Device-TicketQueryResult-ticket: string-End-->

**系统能力：** SystemCapability.Security.Asset
