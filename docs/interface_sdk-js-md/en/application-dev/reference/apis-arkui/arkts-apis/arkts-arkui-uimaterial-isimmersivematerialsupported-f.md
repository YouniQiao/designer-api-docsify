# isImmersiveMaterialSupported

## Modules to Import

```TypeScript
import { uiMaterial } from 'uiMaterial';
```

## isImmersiveMaterialSupported

```TypeScript
function isImmersiveMaterialSupported(): boolean
```

Check whether [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md#ImmersiveMaterial) is supported on the current device. If it is true, the ImmersiveMaterial object can be used in the systemMaterial attribute. If it is false, setting the ImmersiveMaterial object in the systemMaterial attribute will not take effect. It is defined by the device and cannot be modified.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-uiMaterial-function isImmersiveMaterialSupported(): boolean--><!--Device-uiMaterial-function isImmersiveMaterialSupported(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the current device supports ImmersiveMaterial. The value true indicates that the current device supports ImmersiveMaterial, and false indicates the opposite. |

