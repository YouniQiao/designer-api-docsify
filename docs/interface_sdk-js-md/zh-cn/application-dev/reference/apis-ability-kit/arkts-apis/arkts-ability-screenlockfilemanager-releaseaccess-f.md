# releaseAccess

## 导入模块

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(): ReleaseStatus
```

以同步方法释放调用方应用锁屏下敏感数据访问权限。释放成功后，敏感数据密钥的引用计数减少，当计数归零时，密钥可以在屏幕被锁定达到系统配置的时长阈值后被销毁。调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并且先调用[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md)接口成功申请权限后才能使用。

**起始版本：** 12

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 |
| --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-应用未开启锁屏敏感数据保护功能) |
| [29300005](../errorcode-screenLockFileManager.md#29300005-未申请锁屏敏感数据访问权限) |
