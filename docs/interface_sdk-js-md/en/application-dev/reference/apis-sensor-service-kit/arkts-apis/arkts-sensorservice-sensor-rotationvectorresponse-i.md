# RotationVectorResponse

```TypeScript
interface RotationVectorResponse extends Response
```

Describes the rotation vector sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** RotationVectorResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## w

```TypeScript
w: number
```

Scalar component of the rotation vector, which describes the rotation status of the device relative to a reference direction. Unit: radian.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## x

```TypeScript
x: number
```

X-axis component of the rotation vector, indicating the projection of the device rotation status on the X axis.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

Y-axis component of the rotation vector, indicating the projection of the device rotation status on the Y axis.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Z-axis component of the rotation vector, indicating the projection of the device rotation status on the z-axis.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
