# trailOptimizedResponsiveSpringMotion (System API)

## Modules to Import

```TypeScript
```

## trailOptimizedResponsiveSpringMotion

```TypeScript
function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md#springmotion), with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve--><!--Device-curves-function trailOptimizedResponsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | number | No |
| dampingFraction | number | No |
| overlapDuration | number | No |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |
