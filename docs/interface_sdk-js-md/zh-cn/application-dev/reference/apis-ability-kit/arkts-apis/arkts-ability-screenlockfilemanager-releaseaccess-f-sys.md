# releaseAccess（系统接口）

## 导入模块

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## releaseAccess

```TypeScript
function releaseAccess(dataType: DataType): ReleaseStatus
```

以同步方法释放锁屏下指定类型敏感数据访问权限。释放成功后，敏感数据密钥的引用计数减少，当引用计数归零时，密钥可以在锁屏达到系统配置的时长阈值后被销毁。调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并且先调用[acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md)接口成功申请权限后才能使用。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataType | [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-入参错误) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-应用未开启锁屏敏感数据保护功能) |
| [29300005](../errorcode-screenLockFileManager.md#29300005-未申请锁屏敏感数据访问权限) |
