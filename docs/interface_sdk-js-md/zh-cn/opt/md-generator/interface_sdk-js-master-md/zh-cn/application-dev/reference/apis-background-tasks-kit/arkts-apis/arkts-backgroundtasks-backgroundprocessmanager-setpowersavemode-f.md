# setPowerSaveMode

## setPowerSaveMode

```TypeScript
function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>
```

设置进程的能效模式，使用Promise异步回调。 当应用满足以下条件时，可以设置自身是否进入能效模式： - 应用未获取系统焦点，未执行音频或界面刷新操作。 - 无法通过框架层获取电源锁。 - 应用需要执行压缩、解压缩、编译等耗时较长的计算任务，不希望这些任务受到显著的CPU资源限制（即被迫进入能效模式）。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

<!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>--><!--Device-backgroundProcessManager-function setPowerSaveMode(pid: int, powerSaveMode: PowerSaveMode): Promise<void>-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pid | number | 是 |
| powerSaveMode | [PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [31800004](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800004-系统调度原因导致设置失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31800003](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800003-已经被任务管理器设置) |
| [31800002](../../apis-backgroundtasks-kit/errorcode-backgroundProcessManager.md#31800002-参数错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';

let pid = 33333;  // 请开发者替换为实际的进程号
try {
  backgroundProcessManager.setPowerSaveMode(pid, backgroundProcessManager.PowerSaveMode.EFFICIENCY_MODE).then(() => {
    console.info('setPowerSaveMode promise');
  }).catch((err: BusinessError) => {
    console.error(`setPowerSaveMode failed, promise errCode: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`setPowerSaveMode failed, errCode: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
