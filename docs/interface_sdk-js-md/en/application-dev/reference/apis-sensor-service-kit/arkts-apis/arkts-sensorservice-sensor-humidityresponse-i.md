# HumidityResponse

```TypeScript
interface HumidityResponse extends Response
```

Describes the humidity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md).

**Inheritance/Implementation:** HumidityResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## humidity

```TypeScript
humidity: number
```

Relative humidity of the environment, in percentage, indicating the relative humidity percentage of the environment.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
