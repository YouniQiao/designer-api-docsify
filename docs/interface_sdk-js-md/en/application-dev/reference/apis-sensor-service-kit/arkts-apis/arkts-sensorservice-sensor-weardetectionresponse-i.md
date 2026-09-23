# WearDetectionResponse

```TypeScript
interface WearDetectionResponse extends Response
```

Describes the wear detection sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** WearDetectionResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## value

```TypeScript
value: number
```

Device wear status. The value can be **0** (not worn) or **1** (worn).

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
