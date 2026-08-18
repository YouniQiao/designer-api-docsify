# getPowerSaveMode

## 导入模块

```TypeScript
```

## getPowerSaveMode

```TypeScript
function getPowerSaveMode(pid: number): Promise<PowerSaveMode>
```

获取进程能效模式。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

<!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>--><!--Device-backgroundProcessManager-function getPowerSaveMode(pid: int): Promise<PowerSaveMode>-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31800002](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800002-参数错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let pid = 33333;  // 请开发者替换为实际的进程号
try {
  backgroundProcessManager.getPowerSaveMode(pid).then((result: backgroundProcessManager.PowerSaveMode) => {
    console.info(`getPowerSaveMode: ${result}`);
  }).catch((err: BusinessError) => {
    console.error(`getPowerSaveMode failed, promise errCode: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`getPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
