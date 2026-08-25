# @ohos.resourceschedule.backgroundProcessManager(后台子进程管控)

本模块提供了后台子进程管控接口。开发者可以通过本模块接口对子进程进行压制、解压制，避免子进程过多占用系统资源，导致系统使用卡顿。本模块接口仅对通过 [OH_Ability_StartNativeChildProcess](../../../reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess) 接口创建的子进程生效。

**起始版本：** 17

**ArkTS模式：** ArkTS-Dyn起始版本为17；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

## 导入模块

```TypeScript
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getPowerSaveMode(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-getpowersavemode-f.md) |
| [isPowerSaveMode(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-ispowersavemode-f.md) |
| [resetProcessPriority(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-resetprocesspriority-f.md) |
| [setPowerSaveMode(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-setpowersavemode-f.md) |
| [setProcessPriority(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-setprocesspriority-f.md) |

### 枚举

| 名称 |
| --- |
| [PowerSaveMode(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) |
| [ProcessPriority(后台子进程管控)](arkts-backgroundtasks-backgroundprocessmanager-processpriority-e.md) |
