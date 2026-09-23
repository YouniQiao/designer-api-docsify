# Sensor

```TypeScript
interface Sensor
```

Describes the sensor information.

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId?: number
```

Device ID. The value is **-1** indicates the local device. Default value: **-1**.

**Type:** number

**Since:** 19

**System capability:** SystemCapability.Sensors.Sensor

## deviceName

```TypeScript
deviceName?: string
```

Device name, which identifies the source device of the sensor.

**Type:** string

**Since:** 19

**System capability:** SystemCapability.Sensors.Sensor

## firmwareVersion

```TypeScript
firmwareVersion:string
```

Sensor firmware version, which identifies the current version of the sensor firmware.

**Type:** string

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## hardwareVersion

```TypeScript
hardwareVersion:string
```

Sensor hardware version.

**Type:** string

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## isLocalSensor

```TypeScript
isLocalSensor?: boolean
```

Whether the sensor is a local sensor. The **true** indicates a local sensor, and **false** indicates a non-local sensor (that is, a sensor on a remote device). The default value is **true**.

**Type:** boolean

**Since:** 19

**System capability:** SystemCapability.Sensors.Sensor

## isMockSensor

```TypeScript
isMockSensor?: boolean
```

Indicates whether the sensor is a mock sensor. The value **true** indicates a mock sensor, and **false** indicates a real sensor. The default value is **false**.

**Type:** boolean

**Since:** 23

**System capability:** SystemCapability.Sensors.Sensor

## maxRange

```TypeScript
maxRange:number
```

Maximum measurement range of the sensor. The unit depends on the sensor type (for example, m/s² for an acceleration sensor).

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## maxSamplePeriod

```TypeScript
maxSamplePeriod:number
```

Maximum sampling period of the sensor, in ns

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## minSamplePeriod

```TypeScript
minSamplePeriod:number
```

Minimum sampling period of the sensor, in ns

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## power

```TypeScript
power:number
```

Estimated power consumption of the sensor, in mA.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## precision

```TypeScript
precision:number
```

Precision of the sensor. The unit depends on the sensor type.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## sensorId

```TypeScript
sensorId:number
```

Sensor type ID, corresponding to the enumerated values of [SensorId](arkts-sensorservice-sensor-sensorid-e.md).

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## sensorIndex

```TypeScript
sensorIndex?: number
```

Sensor index. Multiple instances of sensors of the same type may exist, which are distinguished by **sensorIndex**. The default value is **0**.

**Type:** number

**Since:** 19

**System capability:** SystemCapability.Sensors.Sensor

## sensorName

```TypeScript
sensorName:string
```

Sensor name, which identifies the type and model of the sensor.

**Type:** string

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor

## vendorName

```TypeScript
vendorName:string
```

Sensor vendor name, which identifies the sensor manufacturer.

**Type:** string

**Since:** 9

**System capability:** SystemCapability.Sensors.Sensor
