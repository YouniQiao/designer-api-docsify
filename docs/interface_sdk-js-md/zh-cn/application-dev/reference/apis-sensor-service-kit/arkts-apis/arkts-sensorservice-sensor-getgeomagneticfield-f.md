# getGeomagneticField

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getGeomagneticField

```TypeScript
function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void
```

获取地球上特定位置的地磁场。使用callback异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getGeomagneticInfo]
> [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md)(locationOptions: LocationOptions, timeMillis: long, callback: AsyncCallback&lt;GeomagneticResponse&gt;)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | 是 |
| timeMillis | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md)&gt; | 是 |


## getGeomagneticField

```TypeScript
function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>
```

获取地球上特定位置的地磁场。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [sensor.getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md)替
> 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md)(locationOptions: LocationOptions, timeMillis: long)

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | 是 |
| timeMillis | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md)&gt; |
