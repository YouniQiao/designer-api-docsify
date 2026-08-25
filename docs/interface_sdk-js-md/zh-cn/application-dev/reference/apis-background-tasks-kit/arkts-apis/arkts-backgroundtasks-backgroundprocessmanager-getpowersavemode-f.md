# getPowerSaveMode

## 导入模块

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## getPowerSaveMode

```TypeScript
function getPowerSaveMode(pid: number): Promise<PowerSaveMode>
```

获取进程能效模式。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [31800002](../errorcode-backgroundProcessManager.md#31800002-参数错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
