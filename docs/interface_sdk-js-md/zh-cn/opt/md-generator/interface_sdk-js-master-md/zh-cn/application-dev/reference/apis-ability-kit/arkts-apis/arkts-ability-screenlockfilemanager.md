# @ohos.ability.screenLockFileManager(锁屏敏感数据管理)

本模块提供锁屏下应用敏感数据保护的能力，支持申请和释放锁屏下应用敏感数据访问权限，以及查询敏感数据密钥的状态。当敏感数据密钥的引用计数归零，且屏幕被锁定达到系统配置的时长阈值后，密钥会被销毁，此时无法对该数据进行操作。这些密钥只有在屏幕解锁后才能恢复。通过调用本模块的[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess)接口，可以防止密钥在屏幕被锁定达到系统配置的时长阈值后被销毁。

> **说明：**
> 
> - 应用开启锁屏下敏感数据保护功能，需在[requestPermissions](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)中配置权限ohos.permission.PROTECT_SCREEN_LOCK_DATA。

**起始版本：** 12

<!--Device-unnamed-declare namespace screenLockFileManager--><!--Device-unnamed-declare namespace screenLockFileManager-End-->

**系统能力：** SystemCapability.Security.ScreenLockFileManager

## 汇总

### 函数

| 名称 |
| --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireaccess) |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryappkeystate) |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseaccess) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f-sys.md#acquireaccess-1) |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f-sys.md#queryappkeystate-1) |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f-sys.md#releaseaccess-1) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |
| [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |
