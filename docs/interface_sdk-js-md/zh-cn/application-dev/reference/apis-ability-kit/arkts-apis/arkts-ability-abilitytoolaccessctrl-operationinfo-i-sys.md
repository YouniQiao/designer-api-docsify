# OperationInfo（系统接口）

```TypeScript
interface OperationInfo
```

表示操作信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface OperationInfo--><!--Device-abilityToolAccessCtrl-interface OperationInfo-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## info

```TypeScript
info: CliCmdInfo | Permissions
```

操作具体信息。当operationType为CLI时，info为CliCmdInfo；当operationType为API时，info为权限名称。如果operationType和info的类型不匹配，会导致参数错误。

**类型：** [CliCmdInfo](arkts-ability-abilitytoolaccessctrl-clicmdinfo-i.md) &#124; Permissions

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-OperationInfo-info: CliCmdInfo | Permissions--><!--Device-OperationInfo-info: CliCmdInfo | Permissions-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## operationType

```TypeScript
operationType: OperationType
```

操作类型，表示操作是CLI命令还是API接口。

**类型：** OperationType

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-OperationInfo-operationType: OperationType--><!--Device-OperationInfo-operationType: OperationType-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
