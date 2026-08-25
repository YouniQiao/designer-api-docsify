# @ohos.ability.screenLockFileManager(锁屏敏感数据管理)

本模块提供锁屏下应用敏感数据保护的能力，支持申请和释放锁屏下应用敏感数据访问权限，以及查询敏感数据密钥的状态。当敏感数据密钥的引用计数归零，且屏幕被锁定达到系统配置的时长阈值后，密钥会被销毁，此时无法对该数据进行操作。这些密钥只有在屏 幕解锁后才能恢复。通过调用本模块的[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md)接口，可以防止密钥在屏幕被锁定达到系统配置的时长阈值后被销毁。

> **说明：**&gt;
> - 应用开启锁屏下敏感数据保护功能，需在[requestPermissions](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)中配置权限ohos.permission.PROTECT_SCREEN_LOCK_DATA。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

## 导入模块

```TypeScript
import { screenLockFileManager } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [acquireAccess(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-acquireaccess-f.md) |
| [queryAppKeyState(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-queryappkeystate-f.md) |
| [releaseAccess(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-releaseaccess-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [acquireAccess(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-acquireaccess-f-sys.md) |
| [queryAppKeyState(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-queryappkeystate-f-sys.md) |
| [releaseAccess(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-releaseaccess-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AccessStatus(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-accessstatus-e.md) |
| [DataType(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-datatype-e.md) |
| [KeyStatus(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-keystatus-e.md) |
| [ReleaseStatus(锁屏敏感数据管理)](arkts-ability-screenlockfilemanager-releasestatus-e.md) |
