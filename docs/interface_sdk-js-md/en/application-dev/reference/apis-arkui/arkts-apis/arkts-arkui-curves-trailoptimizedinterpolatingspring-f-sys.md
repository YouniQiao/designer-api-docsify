# trailOptimizedInterpolatingSpring (System API)

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## trailOptimizedInterpolatingSpring

```TypeScript
function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve
```

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |
| mass | number | Yes |
| [stiffness](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |
| [damping](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |
