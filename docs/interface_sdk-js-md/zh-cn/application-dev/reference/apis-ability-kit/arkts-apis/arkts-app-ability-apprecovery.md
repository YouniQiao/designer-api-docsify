# @ohos.app.ability.appRecovery(应用故障恢复)

appRecovery模块提供了应用在故障状态下的恢复能力。

> **说明：**&gt;
> API9仅支持单进程中单Ability的应用恢复。&gt;
> API10支持进程中包含多个Ability的场景。&gt;
> API24支持发生CPP_CRASH时应用恢复。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { appRecovery } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [enableAppRecovery(应用故障恢复)](arkts-ability-apprecovery-enableapprecovery-f.md) |
| [restartApp(应用故障恢复)](arkts-ability-apprecovery-restartapp-f.md) |
| [saveAppState(应用故障恢复)](arkts-ability-apprecovery-saveappstate-f.md) |
| [saveAppState(应用故障恢复)](arkts-ability-apprecovery-saveappstate-f.md) |
| [setRestartWant(应用故障恢复)](arkts-ability-apprecovery-setrestartwant-f.md) |

### 枚举

| 名称 |
| --- |
| [RestartFlag(应用故障恢复)](arkts-ability-apprecovery-restartflag-e.md) |
| [SaveModeFlag(应用故障恢复)](arkts-ability-apprecovery-savemodeflag-e.md) |
| [SaveOccasionFlag(应用故障恢复)](arkts-ability-apprecovery-saveoccasionflag-e.md) |
