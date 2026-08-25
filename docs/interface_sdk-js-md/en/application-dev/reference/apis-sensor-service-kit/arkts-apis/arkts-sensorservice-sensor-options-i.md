# Options

Describes the sensor data reporting frequency.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## interval

```TypeScript
interval?: long | SensorFrequency
```

Frequency at which a sensor reports data. The default value is 200,000,000 ns. The maximum and minimum values of this parameter are determined by the reporting frequency supported by the hardware. If the configured frequency is greater than the maximum value, the maximum value is used for data reporting. If the configured frequency is less than the minimum value, the minimum value is used for data reporting.

**Type:** ArkTS-Dyn: number \| [SensorFrequency](arkts-sensorservice-sensor-sensorfrequency-t.md)  <br>ArkTS-Sta：long \| [SensorFrequency](arkts-sensorservice-sensor-sensorfrequency-t.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Sensors.Sensor

## sensorInfoParam

```TypeScript
sensorInfoParam?: SensorInfoParam
```

Sensor parameters, including **deviceId** and **sensorIndex**.This API can be used in atomic services since API version 19.

**Type:** [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Sensors.Sensor
