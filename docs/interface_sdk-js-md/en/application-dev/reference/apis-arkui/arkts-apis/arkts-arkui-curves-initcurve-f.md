# initCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## initCurve

```TypeScript
export function initCurve(curve?: Curve): ICurve
```

Implements initialization for the interpolation curve,which is used to create an interpolation curve based on the input parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function initCurve(curve?: Curve): ICurve--><!--Device-curves-export function initCurve(curve?: Curve): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | No | Curve type.&lt;br&gt;Default value: **Curve.Linear**. |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |  |

