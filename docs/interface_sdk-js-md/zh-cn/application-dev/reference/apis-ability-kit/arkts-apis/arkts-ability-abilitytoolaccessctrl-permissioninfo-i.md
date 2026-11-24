# PermissionInfo

```TypeScript
interface PermissionInfo
```

表示权限信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface PermissionInfo--><!--Device-abilityToolAccessCtrl-interface PermissionInfo-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## permission

```TypeScript
permission: string
```

权限名称，合法的权限名取值可在应用权限列表中查询。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionInfo-permission: string--><!--Device-PermissionInfo-permission: string-End-->

**系统能力：** SystemCapability.Security.Asset

## permissionStatus

```TypeScript
permissionStatus: abilityAccessCtrl.PermissionStatus
```

权限状态。

**类型：** [abilityAccessCtrl.PermissionStatus](arkts-ability-abilityaccessctrl-permissionstatus-e.md)

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionInfo-permissionStatus: abilityAccessCtrl.PermissionStatus--><!--Device-PermissionInfo-permissionStatus: abilityAccessCtrl.PermissionStatus-End-->

**系统能力：** SystemCapability.Security.Asset
