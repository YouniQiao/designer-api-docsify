# getGeomagneticInfo

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## getGeomagneticInfo

```TypeScript
function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void
```

Obtains the geomagnetic field of a geographic location at a certain time. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long, callback: AsyncCallback<GeomagneticResponse>): void--><!--Device-sensor-function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long, callback: AsyncCallback<GeomagneticResponse>): void-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | Yes |
| timeMillis | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
      (err: BusinessError, data: sensor.GeomagneticResponse) => {
    if (err) {
      console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
}
```


## getGeomagneticInfo

```TypeScript
function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>
```

Obtains the geomagnetic field of a geographic location at a certain time. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-sensor-function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long): Promise<GeomagneticResponse>--><!--Device-sensor-function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long): Promise<GeomagneticResponse>-End-->

**System capability:** SystemCapability.Sensors.Sensor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locationOptions | [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | Yes |
| timeMillis | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14500101](../errorcode-sensor.md#14500101-service-exception) |

## Examples

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  const promise = sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
  promise.then((data: sensor.GeomagneticResponse) => {
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  }, (err: BusinessError) => {
    console.error(`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}`);
}
```
