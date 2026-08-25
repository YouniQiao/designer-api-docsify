# acquireAccess

## 导入模块

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## acquireAccess

```TypeScript
function acquireAccess(): AccessStatus
```

以同步方法申请调用方应用锁屏下敏感数据访问权限。申请成功后，敏感数据密钥的引用计数增加，防止密钥在屏幕被锁定达到系统配置的时长阈值后被销毁。该方法需与[releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md)配对使用。调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并通过[queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md)接口查询密钥状态为KEY_EXIST。

**起始版本：** 12

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-应用未开启锁屏敏感数据保护功能) |
| [29300004](../errorcode-screenLockFileManager.md#29300004-锁屏敏感数据访问权限已释放) |
