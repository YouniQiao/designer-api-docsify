# @ohos.app.ability.kioskManager

KioskManager模块提供Kiosk模式管理能力，包括系统进入/退出Kiosk模式操作。 Kiosk模式是一种特殊的设备锁定模式，可以确保设备界面只服务于特定的交互场景。在这种模式下，用户只能使用特定的应用。例如，在银行ATM机上，用户只能通过ATM软件进行操作，而不能退出该软件或切换到其他应用。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { kioskManager } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [enterKioskMode](arkts-ability-kioskmanager-enterkioskmode-f.md) |
| [exitKioskMode](arkts-ability-kioskmanager-exitkioskmode-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getKioskStatus](arkts-ability-kioskmanager-getkioskstatus-f-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [KioskStatus](arkts-ability-kioskmanager-kioskstatus-t.md) |
