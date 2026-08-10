# @ohos.app.ability.kioskManager

KioskManager模块提供Kiosk模式管理能力，包括系统进入/退出Kiosk模式操作。Kiosk模式是一种特殊的设备锁定模式，可以确保设备界面只服务于特定的交互场景。在这种模式下，用户只能使用特定的应用。例如，在银行ATM机上，用户只能通过ATM软件进行操作，而不能退出该软件或切换到其他应用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace kioskManager--><!--Device-unnamed-declare namespace kioskManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { kioskManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [enterKioskMode](arkts-ability-kioskmanager-enterkioskmode-f.md#enterkioskmode) | 进入Kiosk模式。使用Promise异步回调。该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。 |
| [exitKioskMode](arkts-ability-kioskmanager-exitkioskmode-f.md#exitkioskmode) | 退出Kiosk模式。使用Promise异步回调。该接口仅对已进入Kiosk模式的应用生效。该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getKioskStatus](arkts-ability-kioskmanager-getkioskstatus-f-sys.md#getkioskstatus) | 获取系统Kiosk模式的状态信息（包括当前系统是否处于Kiosk模式、进入Kiosk模式应用的名称和UID）。使用Promise异步回调。该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。 |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [KioskStatus](arkts-ability-kioskmanager-kioskstatus-t.md) | Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。 |

