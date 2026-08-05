# VelocityFieldOptions

Defines velocity field options.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface VelocityFieldOptions--><!--Device-unnamed-export declare interface VelocityFieldOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## region

```TypeScript
region?: FieldRegion
```

The region influenced by the velocity field.

**Type:** FieldRegion

**Default:** {shape:DisturbanceFieldShape.RECT,position:{x:0,y:0},size:{width:0,height:0}}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VelocityFieldOptions-region?: FieldRegion--><!--Device-VelocityFieldOptions-region?: FieldRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## velocity

```TypeScript
velocity?: Vector2T<double>
```

The velocity values in each direction of the velocity field. Particles only acquire this velocity when within the range of the velocity field; once they leave the range of the velocity field, they are no longer influenced by it and do not gain this additional velocity.

**Type:** Vector2T&lt;double&gt;

**Default:** {x:0,y:0}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VelocityFieldOptions-velocity?: Vector2T<double>--><!--Device-VelocityFieldOptions-velocity?: Vector2T<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

