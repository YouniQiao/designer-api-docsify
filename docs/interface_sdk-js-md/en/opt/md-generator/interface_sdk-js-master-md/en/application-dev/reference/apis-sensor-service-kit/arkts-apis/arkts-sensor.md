# @ohos.sensor

The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides some common sensor algorithms.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sensor--><!--Device-unnamed-declare namespace sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createQuaternion) |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createQuaternion) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createRotationMatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createRotationMatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createRotationMatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createRotationMatrix) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getAltitude) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getAltitude) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getAngleModify) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getAngleModify) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getAngleVariation) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getAngleVariation) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getDeviceAltitude) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getDirection) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getDirection) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getGeomagneticDip) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getGeomagneticDip) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getGeomagneticField) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getGeomagneticField) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getGeomagneticInfo) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getGeomagneticInfo) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getInclination) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getInclination) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getOrientation) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getOrientation) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getQuaternion) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getQuaternion) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getRotationMatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getRotationMatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getRotationMatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getRotationMatrix) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getSensorList) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getSensorList) |
| [getSensorListByDeviceSync](arkts-sensorservice-sensor-getsensorlistbydevicesync-f.md#getSensorListByDeviceSync) |
| [getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md#getSensorListSync) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getSingleSensor) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getSingleSensor) |
| [getSingleSensorByDeviceSync](arkts-sensorservice-sensor-getsinglesensorbydevicesync-f.md#getSingleSensorByDeviceSync) |
| [getSingleSensorSync](arkts-sensorservice-sensor-getsinglesensorsync-f.md#getSingleSensorSync) |
| [offAccelerometerChange](arkts-sensorservice-sensor-offaccelerometerchange-f.md#offAccelerometerChange) |
| [offAccelerometerUncalibratedChange](arkts-sensorservice-sensor-offaccelerometeruncalibratedchange-f.md#offAccelerometerUncalibratedChange) |
| [offAmbientLightChange](arkts-sensorservice-sensor-offambientlightchange-f.md#offAmbientLightChange) |
| [offAmbientTemperatureChange](arkts-sensorservice-sensor-offambienttemperaturechange-f.md#offAmbientTemperatureChange) |
| [offBarometerChange](arkts-sensorservice-sensor-offbarometerchange-f.md#offBarometerChange) |
| [offFusionPressureChange](arkts-sensorservice-sensor-offfusionpressurechange-f.md#offFusionPressureChange) |
| [offGravityChange](arkts-sensorservice-sensor-offgravitychange-f.md#offGravityChange) |
| [offGyroscopeChange](arkts-sensorservice-sensor-offgyroscopechange-f.md#offGyroscopeChange) |
| [offGyroscopeUncalibratedChange](arkts-sensorservice-sensor-offgyroscopeuncalibratedchange-f.md#offGyroscopeUncalibratedChange) |
| [offHallChange](arkts-sensorservice-sensor-offhallchange-f.md#offHallChange) |
| [offHeartRateChange](arkts-sensorservice-sensor-offheartratechange-f.md#offHeartRateChange) |
| [offHumidityChange](arkts-sensorservice-sensor-offhumiditychange-f.md#offHumidityChange) |
| [offLinearAccelerometerChange](arkts-sensorservice-sensor-offlinearaccelerometerchange-f.md#offLinearAccelerometerChange) |
| [offMagneticFieldChange](arkts-sensorservice-sensor-offmagneticfieldchange-f.md#offMagneticFieldChange) |
| [offMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-offmagneticfielduncalibratedchange-f.md#offMagneticFieldUncalibratedChange) |
| [offOrientationChange](arkts-sensorservice-sensor-offorientationchange-f.md#offOrientationChange) |
| [offPedometerChange](arkts-sensorservice-sensor-offpedometerchange-f.md#offPedometerChange) |
| [offPedometerDetectionChange](arkts-sensorservice-sensor-offpedometerdetectionchange-f.md#offPedometerDetectionChange) |
| [offProximityChange](arkts-sensorservice-sensor-offproximitychange-f.md#offProximityChange) |
| [offRotationVectorChange](arkts-sensorservice-sensor-offrotationvectorchange-f.md#offRotationVectorChange) |
| [offSensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md#offSensorStatusChange) |
| [offSignificantMotionChange](arkts-sensorservice-sensor-offsignificantmotionchange-f.md#offSignificantMotionChange) |
| [offWearDetectionChange](arkts-sensorservice-sensor-offweardetectionchange-f.md#offWearDetectionChange) |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#off_SensorId.ACCELEROMETER) |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#off_SensorId.ACCELEROMETER) |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#off_SensorId.ACCELEROMETER_UNCALIBRATED) |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#off_SensorId.ACCELEROMETER_UNCALIBRATED) |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#off_SensorId.AMBIENT_LIGHT) |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#off_SensorId.AMBIENT_LIGHT) |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#off_SensorId.AMBIENT_TEMPERATURE) |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#off_SensorId.AMBIENT_TEMPERATURE) |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#off_SensorId.BAROMETER) |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#off_SensorId.BAROMETER) |
| [off_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-offsensoridfusionpressure-f.md#off_SensorId.FUSION_PRESSURE) |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#off_SensorId.GRAVITY) |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#off_SensorId.GRAVITY) |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#off_SensorId.GYROSCOPE) |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#off_SensorId.GYROSCOPE) |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#off_SensorId.GYROSCOPE_UNCALIBRATED) |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#off_SensorId.GYROSCOPE_UNCALIBRATED) |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#off_SensorId.HALL) |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#off_SensorId.HALL) |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#off_SensorId.HEART_RATE) |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#off_SensorId.HEART_RATE) |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#off_SensorId.HUMIDITY) |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#off_SensorId.HUMIDITY) |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#off_SensorId.LINEAR_ACCELEROMETER) |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#off_SensorId.LINEAR_ACCELEROMETER) |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#off_SensorId.MAGNETIC_FIELD) |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#off_SensorId.MAGNETIC_FIELD) |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#off_SensorId.MAGNETIC_FIELD_UNCALIBRATED) |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#off_SensorId.MAGNETIC_FIELD_UNCALIBRATED) |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#off_SensorId.ORIENTATION) |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#off_SensorId.ORIENTATION) |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#off_SensorId.PEDOMETER) |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#off_SensorId.PEDOMETER) |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#off_SensorId.PEDOMETER_DETECTION) |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#off_SensorId.PEDOMETER_DETECTION) |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#off_SensorId.PROXIMITY) |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#off_SensorId.PROXIMITY) |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#off_SensorId.ROTATION_VECTOR) |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#off_SensorId.ROTATION_VECTOR) |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#off_SensorId.SIGNIFICANT_MOTION) |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#off_SensorId.SIGNIFICANT_MOTION) |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#off_SensorId.WEAR_DETECTION) |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#off_SensorId.WEAR_DETECTION) |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometer-f.md#off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER) |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometeruncalibrated-f.md#off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED) |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensortypesensortypeidambientlight-f.md#off_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT) |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensortypesensortypeidambienttemperature-f.md#off_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE) |
| [off_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidbarometer-f.md#off_SensorType.SENSOR_TYPE_ID_BAROMETER) |
| [off_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-offsensortypesensortypeidgravity-f.md#off_SensorType.SENSOR_TYPE_ID_GRAVITY) |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscope-f.md#off_SensorType.SENSOR_TYPE_ID_GYROSCOPE) |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscopeuncalibrated-f.md#off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED) |
| [off_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-offsensortypesensortypeidhall-f.md#off_SensorType.SENSOR_TYPE_ID_HALL) |
| [off_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-offsensortypesensortypeidheartrate-f.md#off_SensorType.SENSOR_TYPE_ID_HEART_RATE) |
| [off_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-offsensortypesensortypeidhumidity-f.md#off_SensorType.SENSOR_TYPE_ID_HUMIDITY) |
| [off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-offsensortypesensortypeidlinearacceleration-f.md#off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION) |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfield-f.md#off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD) |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfielduncalibrated-f.md#off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED) |
| [off_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-offsensortypesensortypeidorientation-f.md#off_SensorType.SENSOR_TYPE_ID_ORIENTATION) |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-offsensortypesensortypeidpedometer-f.md#off_SensorType.SENSOR_TYPE_ID_PEDOMETER) |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidpedometerdetection-f.md#off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION) |
| [off_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-offsensortypesensortypeidproximity-f.md#off_SensorType.SENSOR_TYPE_ID_PROXIMITY) |
| [off_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-offsensortypesensortypeidrotationvector-f.md#off_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR) |
| [off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensortypesensortypeidsignificantmotion-f.md#off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION) |
| [off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidweardetection-f.md#off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION) |
| [off_sensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md) |
| [onAccelerometerChange](arkts-sensorservice-sensor-onaccelerometerchange-f.md#onAccelerometerChange) |
| [onAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onaccelerometeruncalibratedchange-f.md#onAccelerometerUncalibratedChange) |
| [onAmbientLightChange](arkts-sensorservice-sensor-onambientlightchange-f.md#onAmbientLightChange) |
| [onAmbientTemperatureChange](arkts-sensorservice-sensor-onambienttemperaturechange-f.md#onAmbientTemperatureChange) |
| [onBarometerChange](arkts-sensorservice-sensor-onbarometerchange-f.md#onBarometerChange) |
| [onFusionPressureChange](arkts-sensorservice-sensor-onfusionpressurechange-f.md#onFusionPressureChange) |
| [onGravityChange](arkts-sensorservice-sensor-ongravitychange-f.md#onGravityChange) |
| [onGyroscopeChange](arkts-sensorservice-sensor-ongyroscopechange-f.md#onGyroscopeChange) |
| [onGyroscopeUncalibratedChange](arkts-sensorservice-sensor-ongyroscopeuncalibratedchange-f.md#onGyroscopeUncalibratedChange) |
| [onHallChange](arkts-sensorservice-sensor-onhallchange-f.md#onHallChange) |
| [onHeartRateChange](arkts-sensorservice-sensor-onheartratechange-f.md#onHeartRateChange) |
| [onHumidityChange](arkts-sensorservice-sensor-onhumiditychange-f.md#onHumidityChange) |
| [onLinearAccelerometerChange](arkts-sensorservice-sensor-onlinearaccelerometerchange-f.md#onLinearAccelerometerChange) |
| [onMagneticFieldChange](arkts-sensorservice-sensor-onmagneticfieldchange-f.md#onMagneticFieldChange) |
| [onMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-onmagneticfielduncalibratedchange-f.md#onMagneticFieldUncalibratedChange) |
| [onOrientationChange](arkts-sensorservice-sensor-onorientationchange-f.md#onOrientationChange) |
| [onPedometerChange](arkts-sensorservice-sensor-onpedometerchange-f.md#onPedometerChange) |
| [onPedometerDetectionChange](arkts-sensorservice-sensor-onpedometerdetectionchange-f.md#onPedometerDetectionChange) |
| [onProximityChange](arkts-sensorservice-sensor-onproximitychange-f.md#onProximityChange) |
| [onRotationVectorChange](arkts-sensorservice-sensor-onrotationvectorchange-f.md#onRotationVectorChange) |
| [onSensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md#onSensorStatusChange) |
| [onSignificantMotionChange](arkts-sensorservice-sensor-onsignificantmotionchange-f.md#onSignificantMotionChange) |
| [onWearDetectionChange](arkts-sensorservice-sensor-onweardetectionchange-f.md#onWearDetectionChange) |
| [on_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-onsensoridaccelerometer-f.md#on_SensorId.ACCELEROMETER) |
| [on_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridaccelerometeruncalibrated-f.md#on_SensorId.ACCELEROMETER_UNCALIBRATED) |
| [on_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensoridambientlight-f.md#on_SensorId.AMBIENT_LIGHT) |
| [on_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensoridambienttemperature-f.md#on_SensorId.AMBIENT_TEMPERATURE) |
| [on_SensorId.BAROMETER](arkts-sensorservice-sensor-onsensoridbarometer-f.md#on_SensorId.BAROMETER) |
| [on_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-onsensoridfusionpressure-f.md#on_SensorId.FUSION_PRESSURE) |
| [on_SensorId.GRAVITY](arkts-sensorservice-sensor-onsensoridgravity-f.md#on_SensorId.GRAVITY) |
| [on_SensorId.GYROSCOPE](arkts-sensorservice-sensor-onsensoridgyroscope-f.md#on_SensorId.GYROSCOPE) |
| [on_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridgyroscopeuncalibrated-f.md#on_SensorId.GYROSCOPE_UNCALIBRATED) |
| [on_SensorId.HALL](arkts-sensorservice-sensor-onsensoridhall-f.md#on_SensorId.HALL) |
| [on_SensorId.HEART_RATE](arkts-sensorservice-sensor-onsensoridheartrate-f.md#on_SensorId.HEART_RATE) |
| [on_SensorId.HUMIDITY](arkts-sensorservice-sensor-onsensoridhumidity-f.md#on_SensorId.HUMIDITY) |
| [on_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-onsensoridlinearaccelerometer-f.md#on_SensorId.LINEAR_ACCELEROMETER) |
| [on_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensoridmagneticfield-f.md#on_SensorId.MAGNETIC_FIELD) |
| [on_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridmagneticfielduncalibrated-f.md#on_SensorId.MAGNETIC_FIELD_UNCALIBRATED) |
| [on_SensorId.ORIENTATION](arkts-sensorservice-sensor-onsensoridorientation-f.md#on_SensorId.ORIENTATION) |
| [on_SensorId.PEDOMETER](arkts-sensorservice-sensor-onsensoridpedometer-f.md#on_SensorId.PEDOMETER) |
| [on_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensoridpedometerdetection-f.md#on_SensorId.PEDOMETER_DETECTION) |
| [on_SensorId.PROXIMITY](arkts-sensorservice-sensor-onsensoridproximity-f.md#on_SensorId.PROXIMITY) |
| [on_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-onsensoridrotationvector-f.md#on_SensorId.ROTATION_VECTOR) |
| [on_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensoridsignificantmotion-f.md#on_SensorId.SIGNIFICANT_MOTION) |
| [on_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-onsensoridweardetection-f.md#on_SensorId.WEAR_DETECTION) |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometer-f.md#on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER) |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometeruncalibrated-f.md#on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED) |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensortypesensortypeidambientlight-f.md#on_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT) |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensortypesensortypeidambienttemperature-f.md#on_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE) |
| [on_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidbarometer-f.md#on_SensorType.SENSOR_TYPE_ID_BAROMETER) |
| [on_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-onsensortypesensortypeidgravity-f.md#on_SensorType.SENSOR_TYPE_ID_GRAVITY) |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscope-f.md#on_SensorType.SENSOR_TYPE_ID_GYROSCOPE) |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscopeuncalibrated-f.md#on_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED) |
| [on_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-onsensortypesensortypeidhall-f.md#on_SensorType.SENSOR_TYPE_ID_HALL) |
| [on_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-onsensortypesensortypeidheartrate-f.md#on_SensorType.SENSOR_TYPE_ID_HEART_RATE) |
| [on_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-onsensortypesensortypeidhumidity-f.md#on_SensorType.SENSOR_TYPE_ID_HUMIDITY) |
| [on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-onsensortypesensortypeidlinearacceleration-f.md#on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION) |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfield-f.md#on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD) |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfielduncalibrated-f.md#on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED) |
| [on_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-onsensortypesensortypeidorientation-f.md#on_SensorType.SENSOR_TYPE_ID_ORIENTATION) |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-onsensortypesensortypeidpedometer-f.md#on_SensorType.SENSOR_TYPE_ID_PEDOMETER) |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidpedometerdetection-f.md#on_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION) |
| [on_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-onsensortypesensortypeidproximity-f.md#on_SensorType.SENSOR_TYPE_ID_PROXIMITY) |
| [on_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-onsensortypesensortypeidrotationvector-f.md#on_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR) |
| [on_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensortypesensortypeidsignificantmotion-f.md#on_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION) |
| [on_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidweardetection-f.md#on_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION) |
| [on_sensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md) |
| [onceAccelerometerChange](arkts-sensorservice-sensor-onceaccelerometerchange-f.md#onceAccelerometerChange) |
| [onceAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onceaccelerometeruncalibratedchange-f.md#onceAccelerometerUncalibratedChange) |
| [onceAmbientLightChange](arkts-sensorservice-sensor-onceambientlightchange-f.md#onceAmbientLightChange) |
| [onceAmbientTemperatureChange](arkts-sensorservice-sensor-onceambienttemperaturechange-f.md#onceAmbientTemperatureChange) |
| [onceBarometerChange](arkts-sensorservice-sensor-oncebarometerchange-f.md#onceBarometerChange) |
| [onceGravityChange](arkts-sensorservice-sensor-oncegravitychange-f.md#onceGravityChange) |
| [onceGyroscopeChange](arkts-sensorservice-sensor-oncegyroscopechange-f.md#onceGyroscopeChange) |
| [onceGyroscopeUncalibratedChange](arkts-sensorservice-sensor-oncegyroscopeuncalibratedchange-f.md#onceGyroscopeUncalibratedChange) |
| [onceHallChange](arkts-sensorservice-sensor-oncehallchange-f.md#onceHallChange) |
| [onceHeartRateChange](arkts-sensorservice-sensor-onceheartratechange-f.md#onceHeartRateChange) |
| [onceHumidityChange](arkts-sensorservice-sensor-oncehumiditychange-f.md#onceHumidityChange) |
| [onceLinearAccelerometerChange](arkts-sensorservice-sensor-oncelinearaccelerometerchange-f.md#onceLinearAccelerometerChange) |
| [onceMagneticFieldChange](arkts-sensorservice-sensor-oncemagneticfieldchange-f.md#onceMagneticFieldChange) |
| [onceMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-oncemagneticfielduncalibratedchange-f.md#onceMagneticFieldUncalibratedChange) |
| [onceOrientationChange](arkts-sensorservice-sensor-onceorientationchange-f.md#onceOrientationChange) |
| [oncePedometerChange](arkts-sensorservice-sensor-oncepedometerchange-f.md#oncePedometerChange) |
| [oncePedometerDetectionChange](arkts-sensorservice-sensor-oncepedometerdetectionchange-f.md#oncePedometerDetectionChange) |
| [onceProximityChange](arkts-sensorservice-sensor-onceproximitychange-f.md#onceProximityChange) |
| [onceRotationVectorChange](arkts-sensorservice-sensor-oncerotationvectorchange-f.md#onceRotationVectorChange) |
| [onceSignificantMotionChange](arkts-sensorservice-sensor-oncesignificantmotionchange-f.md#onceSignificantMotionChange) |
| [onceWearDetectionChange](arkts-sensorservice-sensor-onceweardetectionchange-f.md#onceWearDetectionChange) |
| [once_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridaccelerometer-f.md#once_SensorId.ACCELEROMETER) |
| [once_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridaccelerometeruncalibrated-f.md#once_SensorId.ACCELEROMETER_UNCALIBRATED) |
| [once_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensoridambientlight-f.md#once_SensorId.AMBIENT_LIGHT) |
| [once_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensoridambienttemperature-f.md#once_SensorId.AMBIENT_TEMPERATURE) |
| [once_SensorId.BAROMETER](arkts-sensorservice-sensor-oncesensoridbarometer-f.md#once_SensorId.BAROMETER) |
| [once_SensorId.GRAVITY](arkts-sensorservice-sensor-oncesensoridgravity-f.md#once_SensorId.GRAVITY) |
| [once_SensorId.GYROSCOPE](arkts-sensorservice-sensor-oncesensoridgyroscope-f.md#once_SensorId.GYROSCOPE) |
| [once_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridgyroscopeuncalibrated-f.md#once_SensorId.GYROSCOPE_UNCALIBRATED) |
| [once_SensorId.HALL](arkts-sensorservice-sensor-oncesensoridhall-f.md#once_SensorId.HALL) |
| [once_SensorId.HEART_RATE](arkts-sensorservice-sensor-oncesensoridheartrate-f.md#once_SensorId.HEART_RATE) |
| [once_SensorId.HUMIDITY](arkts-sensorservice-sensor-oncesensoridhumidity-f.md#once_SensorId.HUMIDITY) |
| [once_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridlinearaccelerometer-f.md#once_SensorId.LINEAR_ACCELEROMETER) |
| [once_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensoridmagneticfield-f.md#once_SensorId.MAGNETIC_FIELD) |
| [once_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridmagneticfielduncalibrated-f.md#once_SensorId.MAGNETIC_FIELD_UNCALIBRATED) |
| [once_SensorId.ORIENTATION](arkts-sensorservice-sensor-oncesensoridorientation-f.md#once_SensorId.ORIENTATION) |
| [once_SensorId.PEDOMETER](arkts-sensorservice-sensor-oncesensoridpedometer-f.md#once_SensorId.PEDOMETER) |
| [once_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensoridpedometerdetection-f.md#once_SensorId.PEDOMETER_DETECTION) |
| [once_SensorId.PROXIMITY](arkts-sensorservice-sensor-oncesensoridproximity-f.md#once_SensorId.PROXIMITY) |
| [once_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensoridrotationvector-f.md#once_SensorId.ROTATION_VECTOR) |
| [once_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensoridsignificantmotion-f.md#once_SensorId.SIGNIFICANT_MOTION) |
| [once_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-oncesensoridweardetection-f.md#once_SensorId.WEAR_DETECTION) |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometer-f.md#once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER) |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometeruncalibrated-f.md#once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED) |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensortypesensortypeidambientlight-f.md#once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT) |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensortypesensortypeidambienttemperature-f.md#once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE) |
| [once_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidbarometer-f.md#once_SensorType.SENSOR_TYPE_ID_BAROMETER) |
| [once_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-oncesensortypesensortypeidgravity-f.md#once_SensorType.SENSOR_TYPE_ID_GRAVITY) |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscope-f.md#once_SensorType.SENSOR_TYPE_ID_GYROSCOPE) |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscopeuncalibrated-f.md#once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED) |
| [once_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-oncesensortypesensortypeidhall-f.md#once_SensorType.SENSOR_TYPE_ID_HALL) |
| [once_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-oncesensortypesensortypeidheartrate-f.md#once_SensorType.SENSOR_TYPE_ID_HEART_RATE) |
| [once_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-oncesensortypesensortypeidhumidity-f.md#once_SensorType.SENSOR_TYPE_ID_HUMIDITY) |
| [once_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-oncesensortypesensortypeidlinearacceleration-f.md#once_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION) |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfield-f.md#once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD) |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfielduncalibrated-f.md#once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED) |
| [once_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-oncesensortypesensortypeidorientation-f.md#once_SensorType.SENSOR_TYPE_ID_ORIENTATION) |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometer-f.md#once_SensorType.SENSOR_TYPE_ID_PEDOMETER) |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometerdetection-f.md#once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION) |
| [once_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-oncesensortypesensortypeidproximity-f.md#once_SensorType.SENSOR_TYPE_ID_PROXIMITY) |
| [once_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensortypesensortypeidrotationvector-f.md#once_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR) |
| [once_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensortypesensortypeidsignificantmotion-f.md#once_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION) |
| [once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidweardetection-f.md#once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformCoordinateSystem) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformCoordinateSystem) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformRotationMatrix) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformRotationMatrix) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offColorChange](arkts-sensorservice-sensor-offcolorchange-f-sys.md#offColorChange-(System-API)) |
| [offSarChange](arkts-sensorservice-sensor-offsarchange-f-sys.md#offSarChange-(System-API)) |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR) |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#off_SensorId.COLOR) |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#off_SensorId.SAR) |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#off_SensorId.SAR) |
| [onColorChange](arkts-sensorservice-sensor-oncolorchange-f-sys.md#onColorChange-(System-API)) |
| [onSarChange](arkts-sensorservice-sensor-onsarchange-f-sys.md#onSarChange-(System-API)) |
| [on_SensorId.COLOR](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_SensorId.COLOR) |
| [on_SensorId.SAR](arkts-sensorservice-sensor-onsensoridsar-f-sys.md#on_SensorId.SAR) |
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
