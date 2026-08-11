# getGeomagneticField

## getGeomagneticField

```TypeScript
function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void
```

获取地球上特定位置的地磁场，使用callback异步方式返回结果。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getGeomagneticInfo]
> {@link sensor.getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long, callback: AsyncCallback&lt;GeomagneticResponse&gt;)}
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sensor.getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo)(locationOptions:

<!--Device-sensor-function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void--><!--Device-sensor-function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | 是 |
| timeMillis | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;GeomagneticResponse&gt; | 是 |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000, 
                           (err: BusinessError, data: sensor.GeomagneticResponse) => {
  if (err) {
    console.error(`Failed to operate. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting sensor_getGeomagneticField_callback x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
});
```


## getGeomagneticField

```TypeScript
function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>
```

获取地球上特定位置的地磁场，使用Promise异步方式返回结果。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo)替
> 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sensor.getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo)(locationOptions:

<!--Device-sensor-function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>--><!--Device-sensor-function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | 是 |
| timeMillis | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;GeomagneticResponse&gt; |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
promise.then((data: sensor.GeomagneticResponse) => {
  console.info('Succeeded in getting sensor_getGeomagneticField_promise x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
}).catch((reason: BusinessError) => {
  console.error(`Failed to operate.`);
})
```
