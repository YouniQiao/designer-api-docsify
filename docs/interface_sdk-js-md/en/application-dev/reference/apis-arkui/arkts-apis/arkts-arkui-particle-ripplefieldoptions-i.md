# RippleFieldOptions

Defines ripple field options.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface RippleFieldOptions--><!--Device-unnamed-export declare interface RippleFieldOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## amplitude

```TypeScript
amplitude?: double
```

The amplitude of the ripple field. The greater the amplitude, the stronger the force of the ripple field.Range of values:[0, +∞)

**Type:** double

**Default:** 0

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-amplitude?: double--><!--Device-RippleFieldOptions-amplitude?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attenuation

```TypeScript
attenuation?: double
```

The attenuation coefficient of the ripple field. The larger the attenuation coefficient, the faster the wave attenuates over time. Range of values:[0,1]

**Type:** double

**Default:** 0

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-attenuation?: double--><!--Device-RippleFieldOptions-attenuation?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## center

```TypeScript
center?: PositionT<double>
```

The central point where the ripple field generates force. The top-left corner of the component is the origin of coordinates. The coordinate unit is vp.

**Type:** [PositionT](arkts-arkui-positiont-t.md)&lt;double&gt;

**Default:** {x:0,y:0}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-center?: PositionT<double>--><!--Device-RippleFieldOptions-center?: PositionT<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## region

```TypeScript
region?: FieldRegion
```

The region influenced by the ripple field.

**Type:** [FieldRegion](arkts-arkui-particle-fieldregion-i.md)

**Default:** {shape:DisturbanceFieldShape.RECT,position:{x:0,y:0},size:{width:0,height:0}}

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-region?: FieldRegion--><!--Device-RippleFieldOptions-region?: FieldRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## waveSpeed

```TypeScript
waveSpeed?: double
```

Wave speed. The greater the wave speed, the faster the wave changes over time, and the more pronounced the wave motion. Range of values:[0, +∞)

**Type:** double

**Default:** 0

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-waveSpeed?: double--><!--Device-RippleFieldOptions-waveSpeed?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wavelength

```TypeScript
wavelength?: double
```

Wavelength, which is the distance over which a wave cycle changes. The larger the wavelength, the slower the wave changes with distance, and the less pronounced the wave fluctiations.Range of values:[0, +∞)

**Type:** double

**Default:** 0

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RippleFieldOptions-wavelength?: double--><!--Device-RippleFieldOptions-wavelength?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

