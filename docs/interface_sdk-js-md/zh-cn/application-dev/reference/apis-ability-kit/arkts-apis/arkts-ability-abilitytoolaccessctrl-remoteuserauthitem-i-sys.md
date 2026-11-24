# RemoteUserAuthItem（系统接口）

```TypeScript
interface RemoteUserAuthItem
```

表示远程用户授权项。

**起始版本：** 26.0.1

<!--Device-abilityToolAccessCtrl-interface RemoteUserAuthItem--><!--Device-abilityToolAccessCtrl-interface RemoteUserAuthItem-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## authResult

```TypeScript
authResult: string
```

授权结果，表示权限的授权状态。支持的取值包括"DENIED"（用户未授权）、"GRANTED"（已授权）、"NOT_DETERMINED"（未操作授权）、INVALID（无效权限）、RESTRICTED（限制授权）。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteUserAuthItem-authResult: string--><!--Device-RemoteUserAuthItem-authResult: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## permission

```TypeScript
permission: string
```

权限名称，合法的权限名取值可在应用权限列表中查询。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteUserAuthItem-permission: string--><!--Device-RemoteUserAuthItem-permission: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
