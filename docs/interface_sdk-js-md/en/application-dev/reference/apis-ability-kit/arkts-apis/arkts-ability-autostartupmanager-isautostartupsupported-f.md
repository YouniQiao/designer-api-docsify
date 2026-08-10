# isAutoStartupSupported

## Modules to Import

```TypeScript
import { autoStartupManager } from 'kits/@kit.AbilityKit';
```

## isAutoStartupSupported

```TypeScript
function isAutoStartupSupported(): boolean
```

检查当前设备是否支持开机自启动。

> **说明：**
> 
> 建议在调用[autoStartupManager.getAutoStartupStatusForSelf](arkts-ability-autostartupmanager-getautostartupstatusforself-f.md#getautostartupstatusforself) 之前，先调
> 用该接口检查设备能力。如果返回false，则表明当前设备不支持开机自启动。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function isAutoStartupSupported(): boolean--><!--Device-autoStartupManager-function isAutoStartupSupported(): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前设备是否支持开机自启动。true：支持，false：不支持。 |

