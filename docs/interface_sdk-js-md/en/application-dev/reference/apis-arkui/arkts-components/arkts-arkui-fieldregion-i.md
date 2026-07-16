# FieldRegion

Defines the area information of the particle field.

**Since:** 22

<!--Device-unnamed-declare interface FieldRegion--><!--Device-unnamed-declare interface FieldRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: PositionT<number>
```

The coordinates of the center position of the field. The top-left corner of the component is the origin of the coordinate system. The coordinate unit is vp.

**Type:** PositionT<number>

**Default:** {x:0,y:0}

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FieldRegion-position?: PositionT<number>--><!--Device-FieldRegion-position?: PositionT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: DisturbanceFieldShape
```

The shape of the field

**Type:** DisturbanceFieldShape

**Default:** DisturbanceFieldShape.RECT

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FieldRegion-shape?: DisturbanceFieldShape--><!--Device-FieldRegion-shape?: DisturbanceFieldShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeT<number>
```

The size of the field. The unit of value is vp.

**Type:** SizeT<number>

**Default:** {width:0,height:0}

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FieldRegion-size?: SizeT<number>--><!--Device-FieldRegion-size?: SizeT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

