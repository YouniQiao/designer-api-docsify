# ConnectCallback (System API)

Callback provided when enabling an accessibility extension app through the [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)) API. The callback is invoked when the connection to the accessibility extension app is disconnected.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-config-export interface ConnectCallback--><!--Device-config-export interface ConnectCallback-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { config } from 'config';
```

## onDisconnect

```TypeScript
onDisconnect: OnDisconnectCallback
```

Callback invoked when the connection to the accessibility extension app is disconnected.

**Type:** [OnDisconnectCallback](arkts-accessibility-config-ondisconnectcallback-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectCallback-onDisconnect: OnDisconnectCallback--><!--Device-ConnectCallback-onDisconnect: OnDisconnectCallback-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

