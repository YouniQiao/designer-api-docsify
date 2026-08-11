# acquireAccess（系统接口）

## acquireAccess

```TypeScript
function acquireAccess(dataType: DataType): AccessStatus
```

以同步方法申请锁屏下指定类型的敏感数据访问权限。申请成功后，敏感数据密钥的引用计数增加，防止密钥在锁屏达到系统配置的时长阈值后被销毁。该方法需与[releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseaccess)配对使用。

调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并通过[queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryappkeystate)接口查询密钥状态为KEY_EXIST。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

<!--Device-screenLockFileManager-function acquireAccess(dataType: DataType): AccessStatus--><!--Device-screenLockFileManager-function acquireAccess(dataType: DataType): AccessStatus-End-->

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataType | [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [29300004](../errorcode-screenLockFileManager.md#29300004-锁屏敏感数据访问权限已释放) |
| [29300003](../errorcode-screenLockFileManager.md#29300003-应用未开启锁屏敏感数据保护功能) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-入参错误) |

## 示例

```TypeScript
// 申请锁屏下媒体类型数据的访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // 申请访问权限
    let acquireStatus = screenLockFileManager.acquireAccess(screenLockFileManager.DataType.MEDIA_DATA);
    if (acquireStatus === screenLockFileManager.AccessStatus.ACCESS_GRANTED) {
        hilog.info(0x0000, 'testTag', 'acquireAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'acquireAccess failed: %{public}s', message);
}
```
