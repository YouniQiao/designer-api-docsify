# ContinuousParam

Defines the parameters for continuous vibration.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface ContinuousParam--><!--Device-vibrator-interface ContinuousParam-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## frequency

```TypeScript
frequency?: int
```

Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **50**.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ContinuousParam-frequency?: int--><!--Device-ContinuousParam-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## index

```TypeScript
index?: int
```

Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the default value is **0**.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ContinuousParam-index?: int--><!--Device-ContinuousParam-index?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: int
```

Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **100**.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ContinuousParam-intensity?: int--><!--Device-ContinuousParam-intensity?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## points

```TypeScript
points?: VibratorCurvePoint[]
```

Adjustment points of the vibration curve.

**Type:** VibratorCurvePoint[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ContinuousParam-points?: VibratorCurvePoint[]--><!--Device-ContinuousParam-points?: VibratorCurvePoint[]-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

