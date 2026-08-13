# SpotLight

Spotlight, which inherits from [Light](arkts-arkgraphics3d-scenenodes-light-i.md#Light). A spotlight emits a conical beam of light in a specific direction, with the intensity of the light decaying according to the angles defined by the innerAngle and outerAngle parameters. Like a point light, a spotlight's intensity also diminishes with distance from the source. > **NOTE：**> > Ensure that the innerAngle and outerAngle values are proper. > If the value set for outerAngle is greater than PI/2, it is forcibly set to PI/2 internally. > If the value set for outerAngle is less than innerAngle, it is forcibly set to innerAngle internally.

**Inheritance/Implementation:** SpotLight extends [Light](arkts-arkgraphics3d-scenenodes-light-i.md#Light)

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface SpotLight--><!--Device-unnamed-export interface SpotLight-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## innerAngle

```TypeScript
innerAngle?: number
```

The inner angle of the spot light, the unit is radian.

**Type:** number

**Default:** 0

**Since:** 23

**Deprecated since:** -1

<!--Device-SpotLight-innerAngle?: double--><!--Device-SpotLight-innerAngle?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## outerAngle

```TypeScript
outerAngle?: number
```

The outer angle of the spot light, the unit is radian.

**Type:** number

**Default:** PI / 4.0

**Since:** 23

**Deprecated since:** -1

<!--Device-SpotLight-outerAngle?: double--><!--Device-SpotLight-outerAngle?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
