# GyroscopeResponse

Describes the gyroscope sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** GyroscopeResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 8

<!--Device-sensor-interface GyroscopeResponse extends Response--><!--Device-sensor-interface GyroscopeResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## x

```TypeScript
x: number
```

Angular velocity of rotation around the x-axis of the device, in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GyroscopeResponse-x: double--><!--Device-GyroscopeResponse-x: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

Angular velocity of rotation around the y-axis of the device, in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GyroscopeResponse-y: double--><!--Device-GyroscopeResponse-y: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Angular velocity of rotation around the z-axis of the device, in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GyroscopeResponse-z: double--><!--Device-GyroscopeResponse-z: double-End-->

**System capability:** SystemCapability.Sensors.Sensor
