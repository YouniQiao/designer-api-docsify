# AccelerationOptions

粒子加速度配置。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface AccelerationOptions<  ACC_SPEED_UPDATER extends ParticleUpdater,  ACC_ANGLE_UPDATER extends ParticleUpdater>--><!--Device-unnamed-declare interface AccelerationOptions<  ACC_SPEED_UPDATER extends ParticleUpdater,  ACC_ANGLE_UPDATER extends ParticleUpdater>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: ParticlePropertyOptions<number, ACC_ANGLE_UPDATER>
```

表示加速度方向（单位为角度）。

默认值：{range:[0.0,0.0]}

**Type:** [ParticlePropertyOptions](arkts-arkui-particlepropertyoptions-i.md)&lt;number, ACC_ANGLE_UPDATER&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AccelerationOptions-angle?: ParticlePropertyOptions<number, ACC_ANGLE_UPDATER>--><!--Device-AccelerationOptions-angle?: ParticlePropertyOptions<number, ACC_ANGLE_UPDATER>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed?: ParticlePropertyOptions<number, ACC_SPEED_UPDATER>
```

表示加速度大小。

默认值：{range:[0.0,0.0]}

**Type:** [ParticlePropertyOptions](arkts-arkui-particlepropertyoptions-i.md)&lt;number, ACC_SPEED_UPDATER&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AccelerationOptions-speed?: ParticlePropertyOptions<number, ACC_SPEED_UPDATER>--><!--Device-AccelerationOptions-speed?: ParticlePropertyOptions<number, ACC_SPEED_UPDATER>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

