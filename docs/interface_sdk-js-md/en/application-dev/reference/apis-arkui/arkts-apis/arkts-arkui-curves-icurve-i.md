# ICurve

Interface for curve object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-curves-export interface ICurve--><!--Device-curves-export interface ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## interpolate

```TypeScript
interpolate(fraction: double): double
```

Get curve value by fraction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ICurve-interpolate(fraction: double): double--><!--Device-ICurve-interpolate(fraction: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fraction | double | Yes | Indicates the current normalized time parameter. Value range: [0, 1]. Note: If the value is less than 0, it will be processed as 0. If the value is greater than 1, 1 is used. |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

