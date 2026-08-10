# ParticleOptions

设置粒子参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ParticleOptions--><!--Device-unnamed-export interface ParticleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceleration

```TypeScript
acceleration?: AccelerationOptions
```

粒子加速度配置。 

**说明：**

speed表示加速度大小，angle表示加速度方向（单位为角度）。

默认值：{ speed:{range:[0.0,0.0]},angle:{range:[0.0,0.0]} }

**Type:** [AccelerationOptions](arkts-arkui-particle-accelerationoptions-i.md)

**Default:** {speed:{range:[0,0]};angle:{range:[0,0]}}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-acceleration?: AccelerationOptions--><!--Device-ParticleOptions-acceleration?: AccelerationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ParticleColorPropertyOptions
```

粒子颜色配置。

**说明：**

默认值：{ range:[Color.White,Color.White] } 。图片粒子不支持设置颜色。

**Type:** [ParticleColorPropertyOptions](../arkts-components/arkts-arkui-particlecolorpropertyoptions-i.md)

**Default:** {range:['#FFFFFF','#FFFFFF']}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-color?: ParticleColorPropertyOptions--><!--Device-ParticleOptions-color?: ParticleColorPropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## emitter

```TypeScript
emitter: EmitterOptions
```

粒子发射器配置。

**Type:** [EmitterOptions](../arkts-components/arkts-arkui-emitteroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-emitter: EmitterOptions--><!--Device-ParticleOptions-emitter: EmitterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
opacity?: ParticlePropertyOptions
```

粒子透明度配置。

默认值：{ range:[1.0,1.0] }

**Type:** [ParticlePropertyOptions](../arkts-components/arkts-arkui-particlepropertyoptions-i.md)

**Default:** {range:[1.0,1.0]}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-opacity?: ParticlePropertyOptions--><!--Device-ParticleOptions-opacity?: ParticlePropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: ParticlePropertyOptions
```

粒子大小配置。

默认值：{ range:[1.0,1.0] }

**Type:** [ParticlePropertyOptions](../arkts-components/arkts-arkui-particlepropertyoptions-i.md)

**Default:** {range:[1.0,1.0]}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-scale?: ParticlePropertyOptions--><!--Device-ParticleOptions-scale?: ParticlePropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spin

```TypeScript
spin?: ParticlePropertyOptions
```

粒子自旋角度配置。 

默认值：{range:[0.0,0.0]}

方向：正数表示顺时针旋转，负数表示逆时针旋转。

**Type:** [ParticlePropertyOptions](../arkts-components/arkts-arkui-particlepropertyoptions-i.md)

**Default:** {range:[0,0]}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-spin?: ParticlePropertyOptions--><!--Device-ParticleOptions-spin?: ParticlePropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## velocity

```TypeScript
velocity?: VelocityOptions
```

粒子速度配置。

**说明：**

speed表示速度大小。angle表示速度的方向（单位为角度），以元素几何中心为坐标原点，水平方向为X轴，正数表示顺时针方向旋转角度。

默认值：{ speed:[0.0,0.0],angle:[0.0,0.0] }

**Type:** [VelocityOptions](arkts-arkui-particle-velocityoptions-i.md)

**Default:** {speed:[0,0];angle:[0,0]}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleOptions-velocity?: VelocityOptions--><!--Device-ParticleOptions-velocity?: VelocityOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

