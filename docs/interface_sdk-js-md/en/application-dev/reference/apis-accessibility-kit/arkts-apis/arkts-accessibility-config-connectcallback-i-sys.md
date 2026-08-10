# ConnectCallback (System API)

通过[enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableabilitywithcallback)接口启用辅助扩展应用时提供的回调函数。辅助扩展应用连接断开时，回调函数将被调用。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-config-export interface ConnectCallback--><!--Device-config-export interface ConnectCallback-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## onDisconnect

```TypeScript
onDisconnect: OnDisconnectCallback
```

辅助扩展应用的连接断开时调用的回调函数。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectCallback-onDisconnect: OnDisconnectCallback--><!--Device-ConnectCallback-onDisconnect: OnDisconnectCallback-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

