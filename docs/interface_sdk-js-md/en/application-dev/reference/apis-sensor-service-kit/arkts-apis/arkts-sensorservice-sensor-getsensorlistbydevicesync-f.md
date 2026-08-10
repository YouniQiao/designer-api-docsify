# getSensorListByDeviceSync

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSensorListByDeviceSync

```TypeScript
function getSensorListByDeviceSync(deviceId?: int): Array<Sensor>
```

同步获取设备的所有传感器信息。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-sensor-function getSensorListByDeviceSync(deviceId?: int): Array<Sensor>--><!--Device-sensor-function getSensorListByDeviceSync(deviceId?: int): Array<Sensor>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 设备ID，默认为查询本地设备，默认值为-1，表示本地设备，设备ID需通过 [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist)查询或者监听设备上下线接口 [sensorStatusChange](arkts-sensorservice-sensor-on-f.md#on)获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Sensor&gt; | 传感器属性列表。 |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // The first deviceId is optional. By default, it is set to the ID of the local device.
  const sensorList: sensor.Sensor[] = sensor.getSensorListByDeviceSync(deviceId);
  console.info(`sensorList length: ${sensorList.length}`);
  console.info(`sensorList: ${JSON.stringify(sensorList)}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get sensorList. Code: ${e.code}, message: ${e.message}`);
}
```

