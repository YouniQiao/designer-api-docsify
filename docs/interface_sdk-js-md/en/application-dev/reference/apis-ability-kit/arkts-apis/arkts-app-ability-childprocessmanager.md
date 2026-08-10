# @ohos.app.ability.childProcessManager

childProcessManager模块提供子进程管理能力，支持子进程创建和启动操作。创建的子进程会随着父进程的退出而退出，无法脱离父进程独立运行。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace childProcessManager--><!--Device-unnamed-declare namespace childProcessManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [startArkChildProcess](arkts-ability-childprocessmanager-startarkchildprocess-f.md#startarkchildprocess) | 启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用Promise异步回调。该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。 |
| [startChildProcess](arkts-ability-childprocessmanager-startchildprocess-f.md#startchildprocess) | 启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用Promise异步回调。该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。 |
| [startChildProcess](arkts-ability-childprocessmanager-startchildprocess-f.md#startchildprocess-1) | 启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用callback异步回调。该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。 |
| [startNativeChildProcess](arkts-ability-childprocessmanager-startnativechildprocess-f.md#startnativechildprocess) | 启动[Native子进程](../../../application-models/ability-terminology.md#native子进程)。使用Promise异步回调。该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回801错误码。 |

### Enums

| Name | Description |
| --- | --- |
| [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | 子进程启动模式枚举。 |

