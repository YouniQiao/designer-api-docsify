# SensorStatusEvent

Defines a device status change event.

**Since:** 19

<!--Device-sensor-interface SensorStatusEvent--><!--Device-sensor-interface SensorStatusEvent-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId: number
```

Device ID.

**Type:** number

**Since:** 19

<!--Device-SensorStatusEvent-deviceId: int--><!--Device-SensorStatusEvent-deviceId: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## deviceName

```TypeScript
deviceName: string
```

Device name.

**Type:** string

**Since:** 19

<!--Device-SensorStatusEvent-deviceName: string--><!--Device-SensorStatusEvent-deviceName: string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## isSensorOnline

```TypeScript
isSensorOnline: boolean
```

Sensor status. The value **true** indicates that the sensor is online, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 19

<!--Device-SensorStatusEvent-isSensorOnline: boolean--><!--Device-SensorStatusEvent-isSensorOnline: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorId

```TypeScript
sensorId: number
```

Sensor ID.

**Type:** number

**Since:** 19

<!--Device-SensorStatusEvent-sensorId: int--><!--Device-SensorStatusEvent-sensorId: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorIndex

```TypeScript
sensorIndex: number
```

Sensor index.

**Type:** number

**Since:** 19

<!--Device-SensorStatusEvent-sensorIndex: int--><!--Device-SensorStatusEvent-sensorIndex: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: number
```

Timestamp when an event occurs, in ms.

**Type:** number

**Since:** 19

<!--Device-SensorStatusEvent-timestamp: long--><!--Device-SensorStatusEvent-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

