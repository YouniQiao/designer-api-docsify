# onSystemAutoStartup

## Modules to Import

```TypeScript
import { autoStartupManager } from 'kits/@kit.AbilityKit';
```

## onSystemAutoStartup

```TypeScript
function onSystemAutoStartup(callback: AutoStartupCallback): void
```

注册监听应用组件开机自启动状态变化的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function onSystemAutoStartup(callback: AutoStartupCallback): void--><!--Device-autoStartupManager-function onSystemAutoStartup(callback: AutoStartupCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AutoStartupCallback](arkts-ability-autostartupcallback-i-sys.md) | Yes | 监听应用组件开机自启动状态变化的回调对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Connect to system server failed. |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.MANAGE_APP_BOOT". |
| 202 | Permission denied, non-system app called system api. |

