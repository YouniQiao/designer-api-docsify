# getAltitude

## getAltitude

```TypeScript
function getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void
```

根据气压值获取设备所在的海拔高度，使用Callback异步方式返回结果。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [sensor.getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude)(seaPressure: double, currentPressure: double, callback: AsyncCallback&lt;double&gt;)

<!--Device-sensor-function getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void--><!--Device-sensor-function getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seaPressure | number | 是 |
| currentPressure | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getAltitude(0, 200, (err: BusinessError, data: number) => {
  if (err) {
    console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info("Succeeded in getting getAltitude interface get data: " + data);
});
```


## getAltitude

```TypeScript
function getAltitude(seaPressure: number, currentPressure: number): Promise<number>
```

根据气压值获取设备所在的海拔高度，使用Promise异步方式返回结果。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [sensor.getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude)(seaPressure: double, currentPressure: double)

<!--Device-sensor-function getAltitude(seaPressure: number, currentPressure: number): Promise<number>--><!--Device-sensor-function getAltitude(seaPressure: number, currentPressure: number): Promise<number>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seaPressure | number | 是 |
| currentPressure | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getAltitude(0, 200);
promise.then((data: number) => {
  console.info('Succeeded in getting sensor_getAltitude_Promise success', data);
}).catch((err: BusinessError) => {
  console.error(`Failed to operate.`);
})
```
