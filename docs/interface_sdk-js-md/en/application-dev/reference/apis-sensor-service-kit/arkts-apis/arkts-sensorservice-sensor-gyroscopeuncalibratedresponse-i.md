# GyroscopeUncalibratedResponse

```TypeScript
interface GyroscopeUncalibratedResponse extends Response
```

Describes the uncalibrated gyroscope sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** GyroscopeUncalibratedResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## biasX

```TypeScript
biasX: number
```

Uncalibrated rotational angular velocity bias (estimated angular velocity bias) of the x-axis, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## biasY

```TypeScript
biasY: number
```

Uncalibrated rotational angular velocity bias (estimated angular velocity bias) along the y-axis of the device, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## biasZ

```TypeScript
biasZ: number
```

Uncalibrated rotational angular velocity bias (estimated angular velocity bias) along the z-axis of the device, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## x

```TypeScript
x: number
```

Uncalibrated rotational angular velocity of the x-axis, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

Uncalibrated rotational angular velocity of the y-axis, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Uncalibrated rotational angular velocity of the z-axis, in rad/s.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
