# @ohos.sensor

The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides some common sensor algorithms.

**Since:** 8

<!--Device-unnamed-declare namespace sensor--><!--Device-unnamed-declare namespace sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion) |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion-1) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix-1) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix-2) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix-3) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude-1) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify-1) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation-1) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude-1) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection-1) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip-1) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield-1) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo-1) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination-1) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation-1) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion-1) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix-1) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix-2) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix-3) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist-1) |
| [getSensorListByDeviceSync](arkts-sensorservice-sensor-getsensorlistbydevicesync-f.md#getsensorlistbydevicesync) |
| [getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md#getsensorlistsync) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor-1) |
| [getSingleSensorByDeviceSync](arkts-sensorservice-sensor-getsinglesensorbydevicesync-f.md#getsinglesensorbydevicesync) |
| [getSingleSensorSync](arkts-sensorservice-sensor-getsinglesensorsync-f.md#getsinglesensorsync) |
| [off](arkts-sensorservice-sensor-off-f.md#off-4) |
| [off](arkts-sensorservice-sensor-off-f.md#off-5) |
| [off](arkts-sensorservice-sensor-off-f.md#off-6) |
| [off](arkts-sensorservice-sensor-off-f.md#off-7) |
| [off](arkts-sensorservice-sensor-off-f.md#off-8) |
| [off](arkts-sensorservice-sensor-off-f.md#off-9) |
| [off](arkts-sensorservice-sensor-off-f.md#off-10) |
| [off](arkts-sensorservice-sensor-off-f.md#off-11) |
| [off](arkts-sensorservice-sensor-off-f.md#off-12) |
| [off](arkts-sensorservice-sensor-off-f.md#off-13) |
| [off](arkts-sensorservice-sensor-off-f.md#off-14) |
| [off](arkts-sensorservice-sensor-off-f.md#off-15) |
| [off](arkts-sensorservice-sensor-off-f.md#off-16) |
| [off](arkts-sensorservice-sensor-off-f.md#off-17) |
| [off](arkts-sensorservice-sensor-off-f.md#off-18) |
| [off](arkts-sensorservice-sensor-off-f.md#off-19) |
| [off](arkts-sensorservice-sensor-off-f.md#off-20) |
| [off](arkts-sensorservice-sensor-off-f.md#off-21) |
| [off](arkts-sensorservice-sensor-off-f.md#off-22) |
| [off](arkts-sensorservice-sensor-off-f.md#off-23) |
| [off](arkts-sensorservice-sensor-off-f.md#off-24) |
| [off](arkts-sensorservice-sensor-off-f.md#off-25) |
| [off](arkts-sensorservice-sensor-off-f.md#off-26) |
| [off](arkts-sensorservice-sensor-off-f.md#off-27) |
| [off](arkts-sensorservice-sensor-off-f.md#off-28) |
| [off](arkts-sensorservice-sensor-off-f.md#off-29) |
| [off](arkts-sensorservice-sensor-off-f.md#off-30) |
| [off](arkts-sensorservice-sensor-off-f.md#off-31) |
| [off](arkts-sensorservice-sensor-off-f.md#off-32) |
| [off](arkts-sensorservice-sensor-off-f.md#off-33) |
| [off](arkts-sensorservice-sensor-off-f.md#off-34) |
| [off](arkts-sensorservice-sensor-off-f.md#off-35) |
| [off](arkts-sensorservice-sensor-off-f.md#off-36) |
| [off](arkts-sensorservice-sensor-off-f.md#off-37) |
| [off](arkts-sensorservice-sensor-off-f.md#off-38) |
| [off](arkts-sensorservice-sensor-off-f.md#off-39) |
| [off](arkts-sensorservice-sensor-off-f.md#off-40) |
| [off](arkts-sensorservice-sensor-off-f.md#off-41) |
| [off](arkts-sensorservice-sensor-off-f.md#off-42) |
| [off](arkts-sensorservice-sensor-off-f.md#off-43) |
| [off](arkts-sensorservice-sensor-off-f.md#off-44) |
| [off](arkts-sensorservice-sensor-off-f.md#off-45) |
| [off](arkts-sensorservice-sensor-off-f.md#off-46) |
| [off](arkts-sensorservice-sensor-off-f.md#off-47) |
| [off](arkts-sensorservice-sensor-off-f.md#off-48) |
| [off](arkts-sensorservice-sensor-off-f.md#off-49) |
| [off](arkts-sensorservice-sensor-off-f.md#off-50) |
| [off](arkts-sensorservice-sensor-off-f.md#off-51) |
| [off](arkts-sensorservice-sensor-off-f.md#off-52) |
| [off](arkts-sensorservice-sensor-off-f.md#off-53) |
| [off](arkts-sensorservice-sensor-off-f.md#off-54) |
| [off](arkts-sensorservice-sensor-off-f.md#off-55) |
| [off](arkts-sensorservice-sensor-off-f.md#off-56) |
| [off](arkts-sensorservice-sensor-off-f.md#off-57) |
| [off](arkts-sensorservice-sensor-off-f.md#off-58) |
| [off](arkts-sensorservice-sensor-off-f.md#off-59) |
| [off](arkts-sensorservice-sensor-off-f.md#off-60) |
| [off](arkts-sensorservice-sensor-off-f.md#off-61) |
| [off](arkts-sensorservice-sensor-off-f.md#off-62) |
| [off](arkts-sensorservice-sensor-off-f.md#off-63) |
| [off](arkts-sensorservice-sensor-off-f.md#off-64) |
| [off](arkts-sensorservice-sensor-off-f.md#off-65) |
| [off](arkts-sensorservice-sensor-off-f.md#off-66) |
| [off](arkts-sensorservice-sensor-off-f.md#off-67) |
| [off](arkts-sensorservice-sensor-off-f.md#off-68) |
| [on](arkts-sensorservice-sensor-on-f.md#on-2) |
| [on](arkts-sensorservice-sensor-on-f.md#on-3) |
| [on](arkts-sensorservice-sensor-on-f.md#on-4) |
| [on](arkts-sensorservice-sensor-on-f.md#on-5) |
| [on](arkts-sensorservice-sensor-on-f.md#on-6) |
| [on](arkts-sensorservice-sensor-on-f.md#on-7) |
| [on](arkts-sensorservice-sensor-on-f.md#on-8) |
| [on](arkts-sensorservice-sensor-on-f.md#on-9) |
| [on](arkts-sensorservice-sensor-on-f.md#on-10) |
| [on](arkts-sensorservice-sensor-on-f.md#on-11) |
| [on](arkts-sensorservice-sensor-on-f.md#on-12) |
| [on](arkts-sensorservice-sensor-on-f.md#on-13) |
| [on](arkts-sensorservice-sensor-on-f.md#on-14) |
| [on](arkts-sensorservice-sensor-on-f.md#on-15) |
| [on](arkts-sensorservice-sensor-on-f.md#on-16) |
| [on](arkts-sensorservice-sensor-on-f.md#on-17) |
| [on](arkts-sensorservice-sensor-on-f.md#on-18) |
| [on](arkts-sensorservice-sensor-on-f.md#on-19) |
| [on](arkts-sensorservice-sensor-on-f.md#on-20) |
| [on](arkts-sensorservice-sensor-on-f.md#on-21) |
| [on](arkts-sensorservice-sensor-on-f.md#on-22) |
| [on](arkts-sensorservice-sensor-on-f.md#on-23) |
| [on](arkts-sensorservice-sensor-on-f.md#on-24) |
| [on](arkts-sensorservice-sensor-on-f.md#on-25) |
| [on](arkts-sensorservice-sensor-on-f.md#on-26) |
| [on](arkts-sensorservice-sensor-on-f.md#on-27) |
| [on](arkts-sensorservice-sensor-on-f.md#on-28) |
| [on](arkts-sensorservice-sensor-on-f.md#on-29) |
| [on](arkts-sensorservice-sensor-on-f.md#on-30) |
| [on](arkts-sensorservice-sensor-on-f.md#on-31) |
| [on](arkts-sensorservice-sensor-on-f.md#on-32) |
| [on](arkts-sensorservice-sensor-on-f.md#on-33) |
| [on](arkts-sensorservice-sensor-on-f.md#on-34) |
| [on](arkts-sensorservice-sensor-on-f.md#on-35) |
| [on](arkts-sensorservice-sensor-on-f.md#on-36) |
| [on](arkts-sensorservice-sensor-on-f.md#on-37) |
| [on](arkts-sensorservice-sensor-on-f.md#on-38) |
| [on](arkts-sensorservice-sensor-on-f.md#on-39) |
| [on](arkts-sensorservice-sensor-on-f.md#on-40) |
| [on](arkts-sensorservice-sensor-on-f.md#on-41) |
| [on](arkts-sensorservice-sensor-on-f.md#on-42) |
| [on](arkts-sensorservice-sensor-on-f.md#on-43) |
| [on](arkts-sensorservice-sensor-on-f.md#on-44) |
| [on](arkts-sensorservice-sensor-on-f.md#on-45) |
| [once](arkts-sensorservice-sensor-once-f.md#once) |
| [once](arkts-sensorservice-sensor-once-f.md#once-1) |
| [once](arkts-sensorservice-sensor-once-f.md#once-2) |
| [once](arkts-sensorservice-sensor-once-f.md#once-3) |
| [once](arkts-sensorservice-sensor-once-f.md#once-4) |
| [once](arkts-sensorservice-sensor-once-f.md#once-5) |
| [once](arkts-sensorservice-sensor-once-f.md#once-6) |
| [once](arkts-sensorservice-sensor-once-f.md#once-7) |
| [once](arkts-sensorservice-sensor-once-f.md#once-8) |
| [once](arkts-sensorservice-sensor-once-f.md#once-9) |
| [once](arkts-sensorservice-sensor-once-f.md#once-10) |
| [once](arkts-sensorservice-sensor-once-f.md#once-11) |
| [once](arkts-sensorservice-sensor-once-f.md#once-12) |
| [once](arkts-sensorservice-sensor-once-f.md#once-13) |
| [once](arkts-sensorservice-sensor-once-f.md#once-14) |
| [once](arkts-sensorservice-sensor-once-f.md#once-15) |
| [once](arkts-sensorservice-sensor-once-f.md#once-16) |
| [once](arkts-sensorservice-sensor-once-f.md#once-17) |
| [once](arkts-sensorservice-sensor-once-f.md#once-18) |
| [once](arkts-sensorservice-sensor-once-f.md#once-19) |
| [once](arkts-sensorservice-sensor-once-f.md#once-20) |
| [once](arkts-sensorservice-sensor-once-f.md#once-21) |
| [once](arkts-sensorservice-sensor-once-f.md#once-22) |
| [once](arkts-sensorservice-sensor-once-f.md#once-23) |
| [once](arkts-sensorservice-sensor-once-f.md#once-24) |
| [once](arkts-sensorservice-sensor-once-f.md#once-25) |
| [once](arkts-sensorservice-sensor-once-f.md#once-26) |
| [once](arkts-sensorservice-sensor-once-f.md#once-27) |
| [once](arkts-sensorservice-sensor-once-f.md#once-28) |
| [once](arkts-sensorservice-sensor-once-f.md#once-29) |
| [once](arkts-sensorservice-sensor-once-f.md#once-30) |
| [once](arkts-sensorservice-sensor-once-f.md#once-31) |
| [once](arkts-sensorservice-sensor-once-f.md#once-32) |
| [once](arkts-sensorservice-sensor-once-f.md#once-33) |
| [once](arkts-sensorservice-sensor-once-f.md#once-34) |
| [once](arkts-sensorservice-sensor-once-f.md#once-35) |
| [once](arkts-sensorservice-sensor-once-f.md#once-36) |
| [once](arkts-sensorservice-sensor-once-f.md#once-37) |
| [once](arkts-sensorservice-sensor-once-f.md#once-38) |
| [once](arkts-sensorservice-sensor-once-f.md#once-39) |
| [once](arkts-sensorservice-sensor-once-f.md#once-40) |
| [once](arkts-sensorservice-sensor-once-f.md#once-41) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem-1) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off](arkts-sensorservice-sensor-off-f-sys.md#off) |
| [off](arkts-sensorservice-sensor-off-f-sys.md#off-1) |
| [off](arkts-sensorservice-sensor-off-f-sys.md#off-2) |
| [off](arkts-sensorservice-sensor-off-f-sys.md#off-3) |
| [on](arkts-sensorservice-sensor-on-f-sys.md#on) |
| [on](arkts-sensorservice-sensor-on-f-sys.md#on-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccelerometerResponse](arkts-sensorservice-sensor-accelerometerresponse-i.md) |
| [AccelerometerUncalibratedResponse](arkts-sensorservice-sensor-accelerometeruncalibratedresponse-i.md) |
| [AmbientTemperatureResponse](arkts-sensorservice-sensor-ambienttemperatureresponse-i.md) |
| [BarometerResponse](arkts-sensorservice-sensor-barometerresponse-i.md) |
| [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) |
| [FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md) |
| [GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md) |
| [GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md) |
| [GyroscopeResponse](arkts-sensorservice-sensor-gyroscoperesponse-i.md) |
| [GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md) |
| [HallResponse](arkts-sensorservice-sensor-hallresponse-i.md) |
| [HeartRateResponse](arkts-sensorservice-sensor-heartrateresponse-i.md) |
| [HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md) |
| [LightResponse](arkts-sensorservice-sensor-lightresponse-i.md) |
| [LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md) |
| [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) |
| [MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md) |
| [MagneticFieldUncalibratedResponse](arkts-sensorservice-sensor-magneticfielduncalibratedresponse-i.md) |
| [Options](arkts-sensorservice-sensor-options-i.md) |
| [OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md) |
| [PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md) |
| [PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md) |
| [ProximityResponse](arkts-sensorservice-sensor-proximityresponse-i.md) |
| [Response](arkts-sensorservice-sensor-response-i.md) |
| [RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md) |
| [RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md) |
| [Sensor](arkts-sensorservice-sensor-sensor-i.md) |
| [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) |
| [SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md) |
| [SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md) |
| [WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md) |
| [SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md) |
| [SensorId](arkts-sensorservice-sensor-sensorid-e.md) |
| [SensorType](arkts-sensorservice-sensor-sensortype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SensorId](arkts-sensorservice-sensor-sensorid-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SensorFrequency](arkts-sensorservice-sensor-sensorfrequency-t.md) |
