# FieldRegion

Defines particle field region params.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface FieldRegion--><!--Device-unnamed-export declare interface FieldRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: PositionT<double>
```

The coordinates of the center position of the field. The top-left corner of the component is the origin of the coordinate system. The coordinate unit is vp.

**Type:** [PositionT](arkts-arkui-positiont-t.md)&lt;double&gt;

**Default:** {x:0,y:0}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldRegion-position?: PositionT<double>--><!--Device-FieldRegion-position?: PositionT<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: DisturbanceFieldShape
```

The shape of the field

**Type:** [DisturbanceFieldShape](arkts-arkui-particle-disturbancefieldshape-e.md)

**Default:** DisturbanceFieldShape.RECT

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldRegion-shape?: DisturbanceFieldShape--><!--Device-FieldRegion-shape?: DisturbanceFieldShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeT<double>
```

The size of the field. The unit of value is vp.

**Type:** [SizeT](arkts-arkui-graphics-sizet-i.md)&lt;double&gt;

**Default:** {width:0,height:0}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldRegion-size?: SizeT<double>--><!--Device-FieldRegion-size?: SizeT<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

