# GyroscopeResponse

```TypeScript
interface GyroscopeResponse extends Response
```

Describes the gyroscope sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**Inheritance/Implementation:** GyroscopeResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## x

```TypeScript
x: number
```

Rotational angular velocity of the x-axis. in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

Rotational angular velocity of the y-axis. in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Rotational angular velocity of the z-axis. in rad/s. The value is equal to the reported physical quantity.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Sensors.Sensor
