# trailOptimizedInterpolatingSpring (System API)

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## trailOptimizedInterpolatingSpring

```TypeScript
function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve
```

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve--><!--Device-curves-function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |
| mass | number | Yes |
| stiffness | number | Yes |
| damping | number | Yes |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |
