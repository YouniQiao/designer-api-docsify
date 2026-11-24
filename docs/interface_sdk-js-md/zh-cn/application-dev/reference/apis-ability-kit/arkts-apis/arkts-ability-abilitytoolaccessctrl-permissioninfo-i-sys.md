# PermissionInfo（系统接口）

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

## authStatusInfo

```TypeScript
authStatusInfo?: AuthStatusInfo
```

授权状态信息。该项作为出参；当PermissionInfo作为入参时，该项无需传入，若传入会被忽略。默认值：undefined。

**类型：** [AuthStatusInfo](arkts-ability-abilitytoolaccessctrl-authstatusinfo-i-sys.md)

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-PermissionInfo-authStatusInfo?: AuthStatusInfo--><!--Device-PermissionInfo-authStatusInfo?: AuthStatusInfo-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
