# queryAppKeyState（系统接口）

## queryAppKeyState

```TypeScript
function queryAppKeyState(dataType: DataType): KeyStatus
```

以同步方法查询锁屏下指定类型敏感数据密钥的状态。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

<!--Device-screenLockFileManager-function queryAppKeyState(dataType: DataType): KeyStatus--><!--Device-screenLockFileManager-function queryAppKeyState(dataType: DataType): KeyStatus-End-->

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataType | [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-入参错误) |

## 示例

```TypeScript
// 查询锁屏下媒体类型数据的访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // 查询密钥状态
    let keyStatus = screenLockFileManager.queryAppKeyState(screenLockFileManager.DataType.MEDIA_DATA);
    // 判断密钥状态并处理不同情况
    if (keyStatus === screenLockFileManager.KeyStatus.KEY_NOT_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key does not exist.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_RELEASED) {
        hilog.info(0x0000, 'testTag', 'Key has been released.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key exists.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'queryAppKeyState failed: %{public}s', message);
}
```
