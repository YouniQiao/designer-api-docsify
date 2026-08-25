# createAtManager

## 导入模块

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, Permissions } from 'kits/@kit.AbilityKit';
```

## createAtManager

```TypeScript
function createAtManager(): AtManager
```

创建程序访问控制管理实例，用于权限校验、运行时权限申请、设置页授权引导和权限状态变化监听等场景。调用成功后返回AtManager实例，可用于后续的权限管理操作。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**返回值：**

| 类型 |
| --- |
| [AtManager](arkts-ability-abilityaccessctrl-atmanager-i.md) |
