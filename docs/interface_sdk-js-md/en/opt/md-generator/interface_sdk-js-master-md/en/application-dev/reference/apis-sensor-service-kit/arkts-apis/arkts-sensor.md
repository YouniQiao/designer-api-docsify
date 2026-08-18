# @ohos.sensor

The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides some common sensor algorithms.

**Since:** 23

<!--Device-unnamed-declare namespace sensor--><!--Device-unnamed-declare namespace sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion) |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist) |
| [getSensorListByDeviceSync](arkts-sensorservice-sensor-getsensorlistbydevicesync-f.md#getsensorlistbydevicesync) |
| [getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md#getsensorlistsync) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor) |
| [getSingleSensorByDeviceSync](arkts-sensorservice-sensor-getsinglesensorbydevicesync-f.md#getsinglesensorbydevicesync) |
| [getSingleSensorSync](arkts-sensorservice-sensor-getsinglesensorsync-f.md#getsinglesensorsync) |
| [offAccelerometerChange](arkts-sensorservice-sensor-offaccelerometerchange-f.md#offaccelerometerchange) |
| [offAccelerometerUncalibratedChange](arkts-sensorservice-sensor-offaccelerometeruncalibratedchange-f.md#offaccelerometeruncalibratedchange) |
| [offAmbientLightChange](arkts-sensorservice-sensor-offambientlightchange-f.md#offambientlightchange) |
| [offAmbientTemperatureChange](arkts-sensorservice-sensor-offambienttemperaturechange-f.md#offambienttemperaturechange) |
| [offBarometerChange](arkts-sensorservice-sensor-offbarometerchange-f.md#offbarometerchange) |
| [offFusionPressureChange](arkts-sensorservice-sensor-offfusionpressurechange-f.md#offfusionpressurechange) |
| [offGravityChange](arkts-sensorservice-sensor-offgravitychange-f.md#offgravitychange) |
| [offGyroscopeChange](arkts-sensorservice-sensor-offgyroscopechange-f.md#offgyroscopechange) |
| [offGyroscopeUncalibratedChange](arkts-sensorservice-sensor-offgyroscopeuncalibratedchange-f.md#offgyroscopeuncalibratedchange) |
| [offHallChange](arkts-sensorservice-sensor-offhallchange-f.md#offhallchange) |
| [offHeartRateChange](arkts-sensorservice-sensor-offheartratechange-f.md#offheartratechange) |
| [offHumidityChange](arkts-sensorservice-sensor-offhumiditychange-f.md#offhumiditychange) |
| [offLinearAccelerometerChange](arkts-sensorservice-sensor-offlinearaccelerometerchange-f.md#offlinearaccelerometerchange) |
| [offMagneticFieldChange](arkts-sensorservice-sensor-offmagneticfieldchange-f.md#offmagneticfieldchange) |
| [offMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-offmagneticfielduncalibratedchange-f.md#offmagneticfielduncalibratedchange) |
| [offOrientationChange](arkts-sensorservice-sensor-offorientationchange-f.md#offorientationchange) |
| [offPedometerChange](arkts-sensorservice-sensor-offpedometerchange-f.md#offpedometerchange) |
| [offPedometerDetectionChange](arkts-sensorservice-sensor-offpedometerdetectionchange-f.md#offpedometerdetectionchange) |
| [offProximityChange](arkts-sensorservice-sensor-offproximitychange-f.md#offproximitychange) |
| [offRotationVectorChange](arkts-sensorservice-sensor-offrotationvectorchange-f.md#offrotationvectorchange) |
| [offSensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md#offsensorstatuschange) |
| [offSignificantMotionChange](arkts-sensorservice-sensor-offsignificantmotionchange-f.md#offsignificantmotionchange) |
| [offWearDetectionChange](arkts-sensorservice-sensor-offweardetectionchange-f.md#offweardetectionchange) |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#offsensoridaccelerometer) |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#offsensoridaccelerometer-1) |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#offsensoridaccelerometeruncalibrated) |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#offsensoridaccelerometeruncalibrated-1) |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#offsensoridambientlight) |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#offsensoridambientlight-1) |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#offsensoridambienttemperature) |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#offsensoridambienttemperature-1) |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#offsensoridbarometer) |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#offsensoridbarometer-1) |
| [off_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-offsensoridfusionpressure-f.md#offsensoridfusionpressure) |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#offsensoridgravity) |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#offsensoridgravity-1) |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#offsensoridgyroscope) |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#offsensoridgyroscope-1) |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#offsensoridgyroscopeuncalibrated) |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#offsensoridgyroscopeuncalibrated-1) |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#offsensoridhall) |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#offsensoridhall-1) |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#offsensoridheartrate) |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#offsensoridheartrate-1) |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#offsensoridhumidity) |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#offsensoridhumidity-1) |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#offsensoridlinearaccelerometer) |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#offsensoridlinearaccelerometer-1) |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#offsensoridmagneticfield) |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#offsensoridmagneticfield-1) |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#offsensoridmagneticfielduncalibrated) |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#offsensoridmagneticfielduncalibrated-1) |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#offsensoridorientation) |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#offsensoridorientation-1) |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#offsensoridpedometer) |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#offsensoridpedometer-1) |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#offsensoridpedometerdetection) |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#offsensoridpedometerdetection-1) |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#offsensoridproximity) |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#offsensoridproximity-1) |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#offsensoridrotationvector) |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#offsensoridrotationvector-1) |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#offsensoridsignificantmotion) |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#offsensoridsignificantmotion-1) |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#offsensoridweardetection) |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#offsensoridweardetection-1) |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometer-f.md#offsensortypesensortypeidaccelerometer) |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometeruncalibrated-f.md#offsensortypesensortypeidaccelerometeruncalibrated) |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensortypesensortypeidambientlight-f.md#offsensortypesensortypeidambientlight) |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensortypesensortypeidambienttemperature-f.md#offsensortypesensortypeidambienttemperature) |
| [off_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidbarometer-f.md#offsensortypesensortypeidbarometer) |
| [off_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-offsensortypesensortypeidgravity-f.md#offsensortypesensortypeidgravity) |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscope-f.md#offsensortypesensortypeidgyroscope) |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscopeuncalibrated-f.md#offsensortypesensortypeidgyroscopeuncalibrated) |
| [off_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-offsensortypesensortypeidhall-f.md#offsensortypesensortypeidhall) |
| [off_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-offsensortypesensortypeidheartrate-f.md#offsensortypesensortypeidheartrate) |
| [off_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-offsensortypesensortypeidhumidity-f.md#offsensortypesensortypeidhumidity) |
| [off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-offsensortypesensortypeidlinearacceleration-f.md#offsensortypesensortypeidlinearacceleration) |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfield-f.md#offsensortypesensortypeidmagneticfield) |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfielduncalibrated-f.md#offsensortypesensortypeidmagneticfielduncalibrated) |
| [off_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-offsensortypesensortypeidorientation-f.md#offsensortypesensortypeidorientation) |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-offsensortypesensortypeidpedometer-f.md#offsensortypesensortypeidpedometer) |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidpedometerdetection-f.md#offsensortypesensortypeidpedometerdetection) |
| [off_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-offsensortypesensortypeidproximity-f.md#offsensortypesensortypeidproximity) |
| [off_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-offsensortypesensortypeidrotationvector-f.md#offsensortypesensortypeidrotationvector) |
| [off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensortypesensortypeidsignificantmotion-f.md#offsensortypesensortypeidsignificantmotion) |
| [off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidweardetection-f.md#offsensortypesensortypeidweardetection) |
| [off_sensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md#offsensorstatuschange) |
| [onAccelerometerChange](arkts-sensorservice-sensor-onaccelerometerchange-f.md#onaccelerometerchange) |
| [onAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onaccelerometeruncalibratedchange-f.md#onaccelerometeruncalibratedchange) |
| [onAmbientLightChange](arkts-sensorservice-sensor-onambientlightchange-f.md#onambientlightchange) |
| [onAmbientTemperatureChange](arkts-sensorservice-sensor-onambienttemperaturechange-f.md#onambienttemperaturechange) |
| [onBarometerChange](arkts-sensorservice-sensor-onbarometerchange-f.md#onbarometerchange) |
| [onFusionPressureChange](arkts-sensorservice-sensor-onfusionpressurechange-f.md#onfusionpressurechange) |
| [onGravityChange](arkts-sensorservice-sensor-ongravitychange-f.md#ongravitychange) |
| [onGyroscopeChange](arkts-sensorservice-sensor-ongyroscopechange-f.md#ongyroscopechange) |
| [onGyroscopeUncalibratedChange](arkts-sensorservice-sensor-ongyroscopeuncalibratedchange-f.md#ongyroscopeuncalibratedchange) |
| [onHallChange](arkts-sensorservice-sensor-onhallchange-f.md#onhallchange) |
| [onHeartRateChange](arkts-sensorservice-sensor-onheartratechange-f.md#onheartratechange) |
| [onHumidityChange](arkts-sensorservice-sensor-onhumiditychange-f.md#onhumiditychange) |
| [onLinearAccelerometerChange](arkts-sensorservice-sensor-onlinearaccelerometerchange-f.md#onlinearaccelerometerchange) |
| [onMagneticFieldChange](arkts-sensorservice-sensor-onmagneticfieldchange-f.md#onmagneticfieldchange) |
| [onMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-onmagneticfielduncalibratedchange-f.md#onmagneticfielduncalibratedchange) |
| [onOrientationChange](arkts-sensorservice-sensor-onorientationchange-f.md#onorientationchange) |
| [onPedometerChange](arkts-sensorservice-sensor-onpedometerchange-f.md#onpedometerchange) |
| [onPedometerDetectionChange](arkts-sensorservice-sensor-onpedometerdetectionchange-f.md#onpedometerdetectionchange) |
| [onProximityChange](arkts-sensorservice-sensor-onproximitychange-f.md#onproximitychange) |
| [onRotationVectorChange](arkts-sensorservice-sensor-onrotationvectorchange-f.md#onrotationvectorchange) |
| [onSensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md#onsensorstatuschange) |
| [onSignificantMotionChange](arkts-sensorservice-sensor-onsignificantmotionchange-f.md#onsignificantmotionchange) |
| [onWearDetectionChange](arkts-sensorservice-sensor-onweardetectionchange-f.md#onweardetectionchange) |
| [on_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-onsensoridaccelerometer-f.md#onsensoridaccelerometer) |
| [on_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridaccelerometeruncalibrated-f.md#onsensoridaccelerometeruncalibrated) |
| [on_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensoridambientlight-f.md#onsensoridambientlight) |
| [on_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensoridambienttemperature-f.md#onsensoridambienttemperature) |
| [on_SensorId.BAROMETER](arkts-sensorservice-sensor-onsensoridbarometer-f.md#onsensoridbarometer) |
| [on_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-onsensoridfusionpressure-f.md#onsensoridfusionpressure) |
| [on_SensorId.GRAVITY](arkts-sensorservice-sensor-onsensoridgravity-f.md#onsensoridgravity) |
| [on_SensorId.GYROSCOPE](arkts-sensorservice-sensor-onsensoridgyroscope-f.md#onsensoridgyroscope) |
| [on_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridgyroscopeuncalibrated-f.md#onsensoridgyroscopeuncalibrated) |
| [on_SensorId.HALL](arkts-sensorservice-sensor-onsensoridhall-f.md#onsensoridhall) |
| [on_SensorId.HEART_RATE](arkts-sensorservice-sensor-onsensoridheartrate-f.md#onsensoridheartrate) |
| [on_SensorId.HUMIDITY](arkts-sensorservice-sensor-onsensoridhumidity-f.md#onsensoridhumidity) |
| [on_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-onsensoridlinearaccelerometer-f.md#onsensoridlinearaccelerometer) |
| [on_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensoridmagneticfield-f.md#onsensoridmagneticfield) |
| [on_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridmagneticfielduncalibrated-f.md#onsensoridmagneticfielduncalibrated) |
| [on_SensorId.ORIENTATION](arkts-sensorservice-sensor-onsensoridorientation-f.md#onsensoridorientation) |
| [on_SensorId.PEDOMETER](arkts-sensorservice-sensor-onsensoridpedometer-f.md#onsensoridpedometer) |
| [on_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensoridpedometerdetection-f.md#onsensoridpedometerdetection) |
| [on_SensorId.PROXIMITY](arkts-sensorservice-sensor-onsensoridproximity-f.md#onsensoridproximity) |
| [on_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-onsensoridrotationvector-f.md#onsensoridrotationvector) |
| [on_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensoridsignificantmotion-f.md#onsensoridsignificantmotion) |
| [on_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-onsensoridweardetection-f.md#onsensoridweardetection) |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometer-f.md#onsensortypesensortypeidaccelerometer) |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometeruncalibrated-f.md#onsensortypesensortypeidaccelerometeruncalibrated) |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensortypesensortypeidambientlight-f.md#onsensortypesensortypeidambientlight) |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensortypesensortypeidambienttemperature-f.md#onsensortypesensortypeidambienttemperature) |
| [on_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidbarometer-f.md#onsensortypesensortypeidbarometer) |
| [on_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-onsensortypesensortypeidgravity-f.md#onsensortypesensortypeidgravity) |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscope-f.md#onsensortypesensortypeidgyroscope) |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscopeuncalibrated-f.md#onsensortypesensortypeidgyroscopeuncalibrated) |
| [on_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-onsensortypesensortypeidhall-f.md#onsensortypesensortypeidhall) |
| [on_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-onsensortypesensortypeidheartrate-f.md#onsensortypesensortypeidheartrate) |
| [on_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-onsensortypesensortypeidhumidity-f.md#onsensortypesensortypeidhumidity) |
| [on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-onsensortypesensortypeidlinearacceleration-f.md#onsensortypesensortypeidlinearacceleration) |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfield-f.md#onsensortypesensortypeidmagneticfield) |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfielduncalibrated-f.md#onsensortypesensortypeidmagneticfielduncalibrated) |
| [on_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-onsensortypesensortypeidorientation-f.md#onsensortypesensortypeidorientation) |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-onsensortypesensortypeidpedometer-f.md#onsensortypesensortypeidpedometer) |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidpedometerdetection-f.md#onsensortypesensortypeidpedometerdetection) |
| [on_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-onsensortypesensortypeidproximity-f.md#onsensortypesensortypeidproximity) |
| [on_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-onsensortypesensortypeidrotationvector-f.md#onsensortypesensortypeidrotationvector) |
| [on_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensortypesensortypeidsignificantmotion-f.md#onsensortypesensortypeidsignificantmotion) |
| [on_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidweardetection-f.md#onsensortypesensortypeidweardetection) |
| [on_sensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md#onsensorstatuschange) |
| [onceAccelerometerChange](arkts-sensorservice-sensor-onceaccelerometerchange-f.md#onceaccelerometerchange) |
| [onceAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onceaccelerometeruncalibratedchange-f.md#onceaccelerometeruncalibratedchange) |
| [onceAmbientLightChange](arkts-sensorservice-sensor-onceambientlightchange-f.md#onceambientlightchange) |
| [onceAmbientTemperatureChange](arkts-sensorservice-sensor-onceambienttemperaturechange-f.md#onceambienttemperaturechange) |
| [onceBarometerChange](arkts-sensorservice-sensor-oncebarometerchange-f.md#oncebarometerchange) |
| [onceGravityChange](arkts-sensorservice-sensor-oncegravitychange-f.md#oncegravitychange) |
| [onceGyroscopeChange](arkts-sensorservice-sensor-oncegyroscopechange-f.md#oncegyroscopechange) |
| [onceGyroscopeUncalibratedChange](arkts-sensorservice-sensor-oncegyroscopeuncalibratedchange-f.md#oncegyroscopeuncalibratedchange) |
| [onceHallChange](arkts-sensorservice-sensor-oncehallchange-f.md#oncehallchange) |
| [onceHeartRateChange](arkts-sensorservice-sensor-onceheartratechange-f.md#onceheartratechange) |
| [onceHumidityChange](arkts-sensorservice-sensor-oncehumiditychange-f.md#oncehumiditychange) |
| [onceLinearAccelerometerChange](arkts-sensorservice-sensor-oncelinearaccelerometerchange-f.md#oncelinearaccelerometerchange) |
| [onceMagneticFieldChange](arkts-sensorservice-sensor-oncemagneticfieldchange-f.md#oncemagneticfieldchange) |
| [onceMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-oncemagneticfielduncalibratedchange-f.md#oncemagneticfielduncalibratedchange) |
| [onceOrientationChange](arkts-sensorservice-sensor-onceorientationchange-f.md#onceorientationchange) |
| [oncePedometerChange](arkts-sensorservice-sensor-oncepedometerchange-f.md#oncepedometerchange) |
| [oncePedometerDetectionChange](arkts-sensorservice-sensor-oncepedometerdetectionchange-f.md#oncepedometerdetectionchange) |
| [onceProximityChange](arkts-sensorservice-sensor-onceproximitychange-f.md#onceproximitychange) |
| [onceRotationVectorChange](arkts-sensorservice-sensor-oncerotationvectorchange-f.md#oncerotationvectorchange) |
| [onceSignificantMotionChange](arkts-sensorservice-sensor-oncesignificantmotionchange-f.md#oncesignificantmotionchange) |
| [onceWearDetectionChange](arkts-sensorservice-sensor-onceweardetectionchange-f.md#onceweardetectionchange) |
| [once_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridaccelerometer-f.md#oncesensoridaccelerometer) |
| [once_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridaccelerometeruncalibrated-f.md#oncesensoridaccelerometeruncalibrated) |
| [once_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensoridambientlight-f.md#oncesensoridambientlight) |
| [once_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensoridambienttemperature-f.md#oncesensoridambienttemperature) |
| [once_SensorId.BAROMETER](arkts-sensorservice-sensor-oncesensoridbarometer-f.md#oncesensoridbarometer) |
| [once_SensorId.GRAVITY](arkts-sensorservice-sensor-oncesensoridgravity-f.md#oncesensoridgravity) |
| [once_SensorId.GYROSCOPE](arkts-sensorservice-sensor-oncesensoridgyroscope-f.md#oncesensoridgyroscope) |
| [once_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridgyroscopeuncalibrated-f.md#oncesensoridgyroscopeuncalibrated) |
| [once_SensorId.HALL](arkts-sensorservice-sensor-oncesensoridhall-f.md#oncesensoridhall) |
| [once_SensorId.HEART_RATE](arkts-sensorservice-sensor-oncesensoridheartrate-f.md#oncesensoridheartrate) |
| [once_SensorId.HUMIDITY](arkts-sensorservice-sensor-oncesensoridhumidity-f.md#oncesensoridhumidity) |
| [once_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridlinearaccelerometer-f.md#oncesensoridlinearaccelerometer) |
| [once_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensoridmagneticfield-f.md#oncesensoridmagneticfield) |
| [once_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridmagneticfielduncalibrated-f.md#oncesensoridmagneticfielduncalibrated) |
| [once_SensorId.ORIENTATION](arkts-sensorservice-sensor-oncesensoridorientation-f.md#oncesensoridorientation) |
| [once_SensorId.PEDOMETER](arkts-sensorservice-sensor-oncesensoridpedometer-f.md#oncesensoridpedometer) |
| [once_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensoridpedometerdetection-f.md#oncesensoridpedometerdetection) |
| [once_SensorId.PROXIMITY](arkts-sensorservice-sensor-oncesensoridproximity-f.md#oncesensoridproximity) |
| [once_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensoridrotationvector-f.md#oncesensoridrotationvector) |
| [once_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensoridsignificantmotion-f.md#oncesensoridsignificantmotion) |
| [once_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-oncesensoridweardetection-f.md#oncesensoridweardetection) |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometer-f.md#oncesensortypesensortypeidaccelerometer) |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometeruncalibrated-f.md#oncesensortypesensortypeidaccelerometeruncalibrated) |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensortypesensortypeidambientlight-f.md#oncesensortypesensortypeidambientlight) |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensortypesensortypeidambienttemperature-f.md#oncesensortypesensortypeidambienttemperature) |
| [once_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidbarometer-f.md#oncesensortypesensortypeidbarometer) |
| [once_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-oncesensortypesensortypeidgravity-f.md#oncesensortypesensortypeidgravity) |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscope-f.md#oncesensortypesensortypeidgyroscope) |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscopeuncalibrated-f.md#oncesensortypesensortypeidgyroscopeuncalibrated) |
| [once_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-oncesensortypesensortypeidhall-f.md#oncesensortypesensortypeidhall) |
| [once_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-oncesensortypesensortypeidheartrate-f.md#oncesensortypesensortypeidheartrate) |
| [once_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-oncesensortypesensortypeidhumidity-f.md#oncesensortypesensortypeidhumidity) |
| [once_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-oncesensortypesensortypeidlinearacceleration-f.md#oncesensortypesensortypeidlinearacceleration) |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfield-f.md#oncesensortypesensortypeidmagneticfield) |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfielduncalibrated-f.md#oncesensortypesensortypeidmagneticfielduncalibrated) |
| [once_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-oncesensortypesensortypeidorientation-f.md#oncesensortypesensortypeidorientation) |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometer-f.md#oncesensortypesensortypeidpedometer) |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometerdetection-f.md#oncesensortypesensortypeidpedometerdetection) |
| [once_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-oncesensortypesensortypeidproximity-f.md#oncesensortypesensortypeidproximity) |
| [once_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensortypesensortypeidrotationvector-f.md#oncesensortypesensortypeidrotationvector) |
| [once_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensortypesensortypeidsignificantmotion-f.md#oncesensortypesensortypeidsignificantmotion) |
| [once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidweardetection-f.md#oncesensortypesensortypeidweardetection) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offColorChange](arkts-sensorservice-sensor-offcolorchange-f-sys.md#offcolorchange-system-api) |
| [offSarChange](arkts-sensorservice-sensor-offsarchange-f-sys.md#offsarchange-system-api) |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#offsensoridcolor) |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#offsensoridcolor-1) |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#offsensoridsar) |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#offsensoridsar-1) |
| [onColorChange](arkts-sensorservice-sensor-oncolorchange-f-sys.md#oncolorchange-system-api) |
| [onSarChange](arkts-sensorservice-sensor-onsarchange-f-sys.md#onsarchange-system-api) |
| [on_SensorId.COLOR](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor) |
| [on_SensorId.SAR](arkts-sensorservice-sensor-onsensoridsar-f-sys.md#onsensoridsar) |
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
