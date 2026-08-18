# ContinuousParam

Defines the parameters for continuous vibration.

**Since:** 23

<!--Device-vibrator-interface ContinuousParam--><!--Device-vibrator-interface ContinuousParam-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
```

## frequency

```TypeScript
frequency?: number
```

Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **50**.

**Type:** number

**Since:** 23

<!--Device-ContinuousParam-frequency?: int--><!--Device-ContinuousParam-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## index

```TypeScript
index?: number
```

Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the default value is **0**.

**Type:** number

**Since:** 23

<!--Device-ContinuousParam-index?: int--><!--Device-ContinuousParam-index?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: number
```

Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the default value is **100**.

**Type:** number

**Since:** 23

<!--Device-ContinuousParam-intensity?: int--><!--Device-ContinuousParam-intensity?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## points

```TypeScript
points?: VibratorCurvePoint[]
```

Adjustment points of the vibration curve.

**Type:** [VibratorCurvePoint](arkts-sensorservice-vibrator-vibratorcurvepoint-i.md)[]

**Since:** 23

<!--Device-ContinuousParam-points?: VibratorCurvePoint[]--><!--Device-ContinuousParam-points?: VibratorCurvePoint[]-End-->

**System capability:** SystemCapability.Sensors.MiscDevice
