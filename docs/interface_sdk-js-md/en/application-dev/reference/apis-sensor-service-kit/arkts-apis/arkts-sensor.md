# @ohos.sensor

The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides some common sensor algorithms.

**Since:** 23

<!--Device-unnamed-declare namespace sensor--><!--Device-unnamed-declare namespace sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion) | Converts a rotation vector into a quaternion. This API uses an asynchronous callback to return the result. |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md#createquaternion) | Converts a rotation vector into a quaternion. This API uses a promise to return the result. |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) | Converts a rotation vector into a rotation matrix. This API uses an asynchronous callback to return the result. |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) | Converts a rotation vector into a rotation matrix. This API uses a promise to return the result. |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) | Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous callback to return the result. |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md#createrotationmatrix) | Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the result. |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude) | Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current atmospheric pressure. This API uses an asynchronous callback to return the result. |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md#getaltitude) | Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current atmospheric pressure. This API uses a promise to return the result. |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify) | Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the result. |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md#getanglemodify) | Obtains the angle change between two rotation matrices. This API uses a promise to return the result. |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation) | Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the result. |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md#getanglevariation) | Obtains the angle change between two rotation matrices. This API uses a promise to return the result. |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude) | Obtains the altitude based on the atmospheric pressure. This API uses an asynchronous callback to return the result. |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md#getdevicealtitude) | Obtains the altitude based on the atmospheric pressure. This API uses a promise to return the result. |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection) | Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the result. |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md#getdirection) | Obtains the device direction based on the rotation matrix. This API uses a promise to return the result. |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip) | Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result. |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md#getgeomagneticdip) | Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result. |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield) | Obtains the geomagnetic field of a geographic location. This API uses an asynchronous callback to return the result. |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md#getgeomagneticfield) | Obtains the geomagnetic field of a geographic location. This API uses a promise to return the result. |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo) | Obtains the geomagnetic field of a geographic location at a certain time. This API uses an asynchronous callback to return the result. |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md#getgeomagneticinfo) | Obtains the geomagnetic field of a geographic location at a certain time. This API uses a promise to return the result. |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination) | Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result. |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md#getinclination) | Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result. |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation) | Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the result. |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md#getorientation) | Obtains the device direction based on the rotation matrix. This API uses a promise to return the result. |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion) | Obtains the quaternion from a rotation vector. This API uses an asynchronous callback to return the result. |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md#getquaternion) | Obtains the quaternion from a rotation vector. This API uses a promise to return the result. |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) | Obtains the rotation matrix from a rotation vector. This API uses an asynchronous callback to return the result. |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) | Obtains the rotation matrix from a rotation vector. This API uses a promise to return the result. |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) | Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous callback to return the result. |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md#getrotationmatrix) | Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the result. |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist) | Obtains information about all sensors on the device. This API uses an asynchronous callback to return the result. |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md#getsensorlist) | Obtains information about all sensors on the device. This API uses a promise to return the result. |
| [getSensorListByDeviceSync](arkts-sensorservice-sensor-getsensorlistbydevicesync-f.md#getsensorlistbydevicesync) | Obtains the information about all sensors on the device. |
| [getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md#getsensorlistsync) | Obtains information about all sensors on the device. This API returns the result synchronously. |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor) | Obtains information about the sensor of a specific type. This API uses an asynchronous callback to return the result. |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor) | Obtains information about the sensor of a specific type. This API uses a promise to return the result. |
| [getSingleSensorByDeviceSync](arkts-sensorservice-sensor-getsinglesensorbydevicesync-f.md#getsinglesensorbydevicesync) | Obtains information about the sensor of a specific type. |
| [getSingleSensorSync](arkts-sensorservice-sensor-getsinglesensorsync-f.md#getsinglesensorsync) | Obtains information about the sensor of a specific type. This API returns the result synchronously. |
| [offAccelerometerChange](arkts-sensorservice-sensor-offaccelerometerchange-f.md#offaccelerometerchange) | Unsubscribe to accelerometer sensor data, {@code SensorId.ACCELEROMETER}. |
| [offAccelerometerUncalibratedChange](arkts-sensorservice-sensor-offaccelerometeruncalibratedchange-f.md#offaccelerometeruncalibratedchange) | Unsubscribe to uncalibrated accelerometer sensor data, {@code SensorId.ACCELEROMETER_UNCALIBRATED}. |
| [offAmbientLightChange](arkts-sensorservice-sensor-offambientlightchange-f.md#offambientlightchange) | Unsubscribe to ambient light sensor data, {@code SensorId.AMBIENT_LIGHT}. |
| [offAmbientTemperatureChange](arkts-sensorservice-sensor-offambienttemperaturechange-f.md#offambienttemperaturechange) | Unsubscribe to ambient temperature sensor data， {@code SensorId.AMBIENT_TEMPERATURE}. |
| [offBarometerChange](arkts-sensorservice-sensor-offbarometerchange-f.md#offbarometerchange) | Unsubscribe to barometer sensor data, {@code SensorId.BAROMETER}. |
| [offFusionPressureChange](arkts-sensorservice-sensor-offfusionpressurechange-f.md#offfusionpressurechange) | Unsubscribe to fusion pressure sensor data, {@code SensorId.FUSION_PRESSURE}. |
| [offGravityChange](arkts-sensorservice-sensor-offgravitychange-f.md#offgravitychange) | Unsubscribe to gravity sensor data, {@code SensorId.GRAVITY}. |
| [offGyroscopeChange](arkts-sensorservice-sensor-offgyroscopechange-f.md#offgyroscopechange) | Unsubscribe to gyroscope sensor data, {@code SensorId.GYROSCOPE}. |
| [offGyroscopeUncalibratedChange](arkts-sensorservice-sensor-offgyroscopeuncalibratedchange-f.md#offgyroscopeuncalibratedchange) | Unsubscribe to uncalibrated gyroscope sensor data, {@code SensorId.GYROSCOPE_UNCALIBRATED}. |
| [offHallChange](arkts-sensorservice-sensor-offhallchange-f.md#offhallchange) | Unsubscribe to hall sensor data, {@code SensorId.HALL}. |
| [offHeartRateChange](arkts-sensorservice-sensor-offheartratechange-f.md#offheartratechange) | Unsubscribe to heart rate sensor data, {@code SensorId.HEART_RATE}. |
| [offHumidityChange](arkts-sensorservice-sensor-offhumiditychange-f.md#offhumiditychange) | Unsubscribe to humidity sensor data, {@code SensorId.HUMIDITY}. |
| [offLinearAccelerometerChange](arkts-sensorservice-sensor-offlinearaccelerometerchange-f.md#offlinearaccelerometerchange) | Unsubscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}. |
| [offMagneticFieldChange](arkts-sensorservice-sensor-offmagneticfieldchange-f.md#offmagneticfieldchange) | Unsubscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}. |
| [offMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-offmagneticfielduncalibratedchange-f.md#offmagneticfielduncalibratedchange) | Unsubscribe to uncalibrated magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}. |
| [offOrientationChange](arkts-sensorservice-sensor-offorientationchange-f.md#offorientationchange) | Unsubscribe to orientation sensor data, {@code SensorId.ORIENTATION}. |
| [offPedometerChange](arkts-sensorservice-sensor-offpedometerchange-f.md#offpedometerchange) | Unsubscribe to pedometer sensor data, {@code SensorId.PEDOMETER}. |
| [offPedometerDetectionChange](arkts-sensorservice-sensor-offpedometerdetectionchange-f.md#offpedometerdetectionchange) | Unsubscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}. |
| [offProximityChange](arkts-sensorservice-sensor-offproximitychange-f.md#offproximitychange) | Unsubscribe to proximity sensor data, {@code SensorId.PROXIMITY}. |
| [offRotationVectorChange](arkts-sensorservice-sensor-offrotationvectorchange-f.md#offrotationvectorchange) | Unsubscribe to rotation vector sensor data, {@code SensorId.ROTATION_VECTOR}. |
| [offSensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md#offsensorstatuschange) | Stop listening on device status changes. |
| [offSignificantMotionChange](arkts-sensorservice-sensor-offsignificantmotionchange-f.md#offsignificantmotionchange) | Unsubscribe to significant motion sensor data, {@code SensorId.SIGNIFICANT_MOTION}. |
| [offWearDetectionChange](arkts-sensorservice-sensor-offweardetectionchange-f.md#offweardetectionchange) | Unsubscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}. |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#offsensoridaccelerometer) | Unsubscribes from data of the acceleration sensor. |
| [off_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-offsensoridaccelerometer-f.md#offsensoridaccelerometer-1) | Unsubscribes from data of the acceleration sensor. |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#offsensoridaccelerometeruncalibrated) | Unsubscribes from data of the uncalibrated acceleration sensor. |
| [off_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridaccelerometeruncalibrated-f.md#offsensoridaccelerometeruncalibrated-1) | Unsubscribes from data of the uncalibrated acceleration sensor. |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#offsensoridambientlight) | Unsubscribes from data of the ambient light sensor. |
| [off_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensoridambientlight-f.md#offsensoridambientlight-1) | Unsubscribes from data of the ambient light sensor. |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#offsensoridambienttemperature) | Unsubscribes from data of the ambient temperature sensor. |
| [off_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensoridambienttemperature-f.md#offsensoridambienttemperature-1) | Unsubscribes from data of the ambient temperature sensor. |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#offsensoridbarometer) | Unsubscribes from data of the barometer sensor. |
| [off_SensorId.BAROMETER](arkts-sensorservice-sensor-offsensoridbarometer-f.md#offsensoridbarometer-1) | Unsubscribes from data of the barometer sensor. |
| [off_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-offsensoridfusionpressure-f.md#offsensoridfusionpressure) | Unsubscribes from the fused pressure sensor data. |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#offsensoridgravity) | Unsubscribes from data of the gravity sensor. |
| [off_SensorId.GRAVITY](arkts-sensorservice-sensor-offsensoridgravity-f.md#offsensoridgravity-1) | Unsubscribes from data of the gravity sensor. |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#offsensoridgyroscope) | Unsubscribes from data of the gyroscope sensor. |
| [off_SensorId.GYROSCOPE](arkts-sensorservice-sensor-offsensoridgyroscope-f.md#offsensoridgyroscope-1) | Unsubscribes from data of the gyroscope sensor. |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#offsensoridgyroscopeuncalibrated) | Unsubscribes from data of the uncalibrated gyroscope sensor. |
| [off_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridgyroscopeuncalibrated-f.md#offsensoridgyroscopeuncalibrated-1) | Unsubscribes from data of the uncalibrated gyroscope sensor. |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#offsensoridhall) | Unsubscribes from data of the Hall effect sensor. |
| [off_SensorId.HALL](arkts-sensorservice-sensor-offsensoridhall-f.md#offsensoridhall-1) | Unsubscribes from data of the Hall effect sensor. |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#offsensoridheartrate) | Unsubscribes from data of the heart rate sensor. |
| [off_SensorId.HEART_RATE](arkts-sensorservice-sensor-offsensoridheartrate-f.md#offsensoridheartrate-1) | Unsubscribes from data of the heart rate sensor. |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#offsensoridhumidity) | Unsubscribes from data of the humidity sensor. |
| [off_SensorId.HUMIDITY](arkts-sensorservice-sensor-offsensoridhumidity-f.md#offsensoridhumidity-1) | Unsubscribes from data of the humidity sensor. |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#offsensoridlinearaccelerometer) | Unsubscribes from data of the linear acceleration sensor. |
| [off_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-offsensoridlinearaccelerometer-f.md#offsensoridlinearaccelerometer-1) | Unsubscribes from data of the linear acceleration sensor. |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#offsensoridmagneticfield) | Unsubscribes from data of the magnetic field sensor. |
| [off_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensoridmagneticfield-f.md#offsensoridmagneticfield-1) | Unsubscribes from data of the magnetic field sensor. |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#offsensoridmagneticfielduncalibrated) | Unsubscribes from data of the uncalibrated magnetic field sensor. |
| [off_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensoridmagneticfielduncalibrated-f.md#offsensoridmagneticfielduncalibrated-1) | Unsubscribes from data of the uncalibrated magnetic field sensor. |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#offsensoridorientation) | Unsubscribes from data of the orientation sensor. |
| [off_SensorId.ORIENTATION](arkts-sensorservice-sensor-offsensoridorientation-f.md#offsensoridorientation-1) | Unsubscribes from data of the orientation sensor. |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#offsensoridpedometer) | Unsubscribes from data of the pedometer sensor. |
| [off_SensorId.PEDOMETER](arkts-sensorservice-sensor-offsensoridpedometer-f.md#offsensoridpedometer-1) | Unsubscribes from data of the pedometer sensor. |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#offsensoridpedometerdetection) | Unsubscribes from data of the pedometer detection sensor. |
| [off_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensoridpedometerdetection-f.md#offsensoridpedometerdetection-1) | Unsubscribes from data of the pedometer detection sensor. |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#offsensoridproximity) | Unsubscribes from data of the proximity sensor. |
| [off_SensorId.PROXIMITY](arkts-sensorservice-sensor-offsensoridproximity-f.md#offsensoridproximity-1) | Unsubscribes from data of the proximity sensor. |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#offsensoridrotationvector) | Unsubscribes from data of the rotation vector sensor. |
| [off_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-offsensoridrotationvector-f.md#offsensoridrotationvector-1) | Unsubscribes from data of the rotation vector sensor. |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#offsensoridsignificantmotion) | Unsubscribes from valid motion sensor data. |
| [off_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensoridsignificantmotion-f.md#offsensoridsignificantmotion-1) | Unsubscribes from valid motion sensor data. |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#offsensoridweardetection) | Unsubscribes from data of the wear detection sensor. |
| [off_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-offsensoridweardetection-f.md#offsensoridweardetection-1) | Unsubscribes from data of the wear detection sensor. |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometer-f.md#offsensortypesensortypeidaccelerometer) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidaccelerometeruncalibrated-f.md#offsensortypesensortypeidaccelerometeruncalibrated) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-offsensortypesensortypeidambientlight-f.md#offsensortypesensortypeidambientlight) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-offsensortypesensortypeidambienttemperature-f.md#offsensortypesensortypeidambienttemperature) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-offsensortypesensortypeidbarometer-f.md#offsensortypesensortypeidbarometer) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-offsensortypesensortypeidgravity-f.md#offsensortypesensortypeidgravity) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscope-f.md#offsensortypesensortypeidgyroscope) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidgyroscopeuncalibrated-f.md#offsensortypesensortypeidgyroscopeuncalibrated) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-offsensortypesensortypeidhall-f.md#offsensortypesensortypeidhall) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-offsensortypesensortypeidheartrate-f.md#offsensortypesensortypeidheartrate) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-offsensortypesensortypeidhumidity-f.md#offsensortypesensortypeidhumidity) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-offsensortypesensortypeidlinearacceleration-f.md#offsensortypesensortypeidlinearacceleration) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfield-f.md#offsensortypesensortypeidmagneticfield) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-offsensortypesensortypeidmagneticfielduncalibrated-f.md#offsensortypesensortypeidmagneticfielduncalibrated) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-offsensortypesensortypeidorientation-f.md#offsensortypesensortypeidorientation) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-offsensortypesensortypeidpedometer-f.md#offsensortypesensortypeidpedometer) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidpedometerdetection-f.md#offsensortypesensortypeidpedometerdetection) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-offsensortypesensortypeidproximity-f.md#offsensortypesensortypeidproximity) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-offsensortypesensortypeidrotationvector-f.md#offsensortypesensortypeidrotationvector) | Unsubscribes from sensor data changes. |
| [off_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-offsensortypesensortypeidsignificantmotion-f.md#offsensortypesensortypeidsignificantmotion) | Unsubscribes from valid motion sensor data. |
| [off_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-offsensortypesensortypeidweardetection-f.md#offsensortypesensortypeidweardetection) | Unsubscribes from sensor data changes. |
| [off_sensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md#offsensorstatuschange) | Disables listening for sensor status changes. |
| [onAccelerometerChange](arkts-sensorservice-sensor-onaccelerometerchange-f.md#onaccelerometerchange) | Subscribe to accelerometer sensor data, {@code SensorId.ACCELEROMETER}. |
| [onAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onaccelerometeruncalibratedchange-f.md#onaccelerometeruncalibratedchange) | Subscribe to uncalibrated accelerometer sensor data, {@code SensorId.ACCELEROMETER_UNCALIBRATED}. |
| [onAmbientLightChange](arkts-sensorservice-sensor-onambientlightchange-f.md#onambientlightchange) | Subscribe to ambient light sensor data, {@code SensorId.AMBIENT_LIGHT}. |
| [onAmbientTemperatureChange](arkts-sensorservice-sensor-onambienttemperaturechange-f.md#onambienttemperaturechange) | Subscribe to ambient temperature sensor data, {@code SensorId.AMBIENT_TEMPERATURE}. |
| [onBarometerChange](arkts-sensorservice-sensor-onbarometerchange-f.md#onbarometerchange) | Subscribe to barometer sensor data, {@code SensorId.BAROMETER}. |
| [onFusionPressureChange](arkts-sensorservice-sensor-onfusionpressurechange-f.md#onfusionpressurechange) | Subscribe to fusion pressure sensor data, {@code SensorId.FUSION_PRESSURE}. |
| [onGravityChange](arkts-sensorservice-sensor-ongravitychange-f.md#ongravitychange) | Subscribe to gravity sensor data, {@code SensorId.GRAVITY}. |
| [onGyroscopeChange](arkts-sensorservice-sensor-ongyroscopechange-f.md#ongyroscopechange) | Subscribe to gyroscope sensor data, {@code SensorId.GYROSCOPE}. |
| [onGyroscopeUncalibratedChange](arkts-sensorservice-sensor-ongyroscopeuncalibratedchange-f.md#ongyroscopeuncalibratedchange) | Subscribe to uncalibrated gyroscope sensor data, {@code SensorId.GYROSCOPE_UNCALIBRATED}. |
| [onHallChange](arkts-sensorservice-sensor-onhallchange-f.md#onhallchange) | Subscribe to hall sensor data, {@code SensorId.HALL}. |
| [onHeartRateChange](arkts-sensorservice-sensor-onheartratechange-f.md#onheartratechange) | Subscribe to heart rate sensor data, {@code SensorId.HEART_RATE}. |
| [onHumidityChange](arkts-sensorservice-sensor-onhumiditychange-f.md#onhumiditychange) | Subscribe to humidity sensor data, {@code SensorId.HUMIDITY}. |
| [onLinearAccelerometerChange](arkts-sensorservice-sensor-onlinearaccelerometerchange-f.md#onlinearaccelerometerchange) | Subscribe to linear acceleration sensor data, {@code SensorId.LINEAR_ACCELEROMETER}. |
| [onMagneticFieldChange](arkts-sensorservice-sensor-onmagneticfieldchange-f.md#onmagneticfieldchange) | Subscribe to magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD}. |
| [onMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-onmagneticfielduncalibratedchange-f.md#onmagneticfielduncalibratedchange) | Subscribe to uncalibrated magnetic field sensor data, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}. |
| [onOrientationChange](arkts-sensorservice-sensor-onorientationchange-f.md#onorientationchange) | Subscribe to orientation sensor data, {@code SensorId.ORIENTATION}. |
| [onPedometerChange](arkts-sensorservice-sensor-onpedometerchange-f.md#onpedometerchange) | Subscribe to pedometer sensor data, {@code SensorId.PEDOMETER}. |
| [onPedometerDetectionChange](arkts-sensorservice-sensor-onpedometerdetectionchange-f.md#onpedometerdetectionchange) | Subscribe to pedometer detection sensor data, {@code SensorId.PEDOMETER_DETECTION}. |
| [onProximityChange](arkts-sensorservice-sensor-onproximitychange-f.md#onproximitychange) | Subscribe to proximity sensor data, {@code SensorId.PROXIMITY}. |
| [onRotationVectorChange](arkts-sensorservice-sensor-onrotationvectorchange-f.md#onrotationvectorchange) | Subscribe to rotation vector sensor data, {@code SensorId.ROTATION_VECTOR}. |
| [onSensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md#onsensorstatuschange) | Start listening on device status changes. |
| [onSignificantMotionChange](arkts-sensorservice-sensor-onsignificantmotionchange-f.md#onsignificantmotionchange) | Subscribe to significant motion sensor data, {@code SensorId.SIGNIFICANT_MOTION}. |
| [onWearDetectionChange](arkts-sensorservice-sensor-onweardetectionchange-f.md#onweardetectionchange) | Subscribe to wear detection sensor data, {@code SensorId.WEAR_DETECTION}. |
| [on_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-onsensoridaccelerometer-f.md#onsensoridaccelerometer) | Subscribes to data of the acceleration sensor. |
| [on_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridaccelerometeruncalibrated-f.md#onsensoridaccelerometeruncalibrated) | Subscribes to data of the uncalibrated acceleration sensor. |
| [on_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensoridambientlight-f.md#onsensoridambientlight) | Subscribes to data of the ambient light sensor. |
| [on_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensoridambienttemperature-f.md#onsensoridambienttemperature) | Subscribes to data of the ambient temperature sensor. |
| [on_SensorId.BAROMETER](arkts-sensorservice-sensor-onsensoridbarometer-f.md#onsensoridbarometer) | Subscribes to data of the barometer sensor. |
| [on_SensorId.FUSION_PRESSURE](arkts-sensorservice-sensor-onsensoridfusionpressure-f.md#onsensoridfusionpressure) | Subscribes to the fused pressure sensor data. |
| [on_SensorId.GRAVITY](arkts-sensorservice-sensor-onsensoridgravity-f.md#onsensoridgravity) | Subscribes to data of the gravity sensor. |
| [on_SensorId.GYROSCOPE](arkts-sensorservice-sensor-onsensoridgyroscope-f.md#onsensoridgyroscope) | Subscribes to data of the gyroscope sensor. |
| [on_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridgyroscopeuncalibrated-f.md#onsensoridgyroscopeuncalibrated) | Subscribes to data of the uncalibrated gyroscope sensor. |
| [on_SensorId.HALL](arkts-sensorservice-sensor-onsensoridhall-f.md#onsensoridhall) | Subscribes to data of the Hall effect sensor. |
| [on_SensorId.HEART_RATE](arkts-sensorservice-sensor-onsensoridheartrate-f.md#onsensoridheartrate) | Subscribes to data of the heart rate sensor. |
| [on_SensorId.HUMIDITY](arkts-sensorservice-sensor-onsensoridhumidity-f.md#onsensoridhumidity) | Subscribes to data of the humidity sensor. |
| [on_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-onsensoridlinearaccelerometer-f.md#onsensoridlinearaccelerometer) | Subscribes to data of the linear acceleration sensor. |
| [on_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensoridmagneticfield-f.md#onsensoridmagneticfield) | Subscribes to data of the magnetic field sensor. |
| [on_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensoridmagneticfielduncalibrated-f.md#onsensoridmagneticfielduncalibrated) | Subscribes to data of the uncalibrated magnetic field sensor. |
| [on_SensorId.ORIENTATION](arkts-sensorservice-sensor-onsensoridorientation-f.md#onsensoridorientation) | Subscribes to data of the orientation sensor. > **NOTE：**> > Applications or services invoking this API can prompt users to use figure-8 calibration to improve the accuracy > of the direction sensor. The sensor has a theoretical error of ±5 degrees, but the specific precision may vary > depending on different driver implementations and algorithmic designs. |
| [on_SensorId.PEDOMETER](arkts-sensorservice-sensor-onsensoridpedometer-f.md#onsensoridpedometer) | Subscribes to data of the pedometer sensor. The step counter sensor's data reporting is subject to some delay, and the delay is determined by specific product implementations. |
| [on_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensoridpedometerdetection-f.md#onsensoridpedometerdetection) | Subscribes to data of the pedometer detection sensor. |
| [on_SensorId.PROXIMITY](arkts-sensorservice-sensor-onsensoridproximity-f.md#onsensoridproximity) | Subscribes to data of the proximity sensor. |
| [on_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-onsensoridrotationvector-f.md#onsensoridrotationvector) | Subscribes to data of the rotation vector sensor. |
| [on_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensoridsignificantmotion-f.md#onsensoridsignificantmotion) | Subscribes to the significant motion sensor data. |
| [on_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-onsensoridweardetection-f.md#onsensoridweardetection) | Subscribes to data of the wear detection sensor. |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometer-f.md#onsensortypesensortypeidaccelerometer) | Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidaccelerometeruncalibrated-f.md#onsensortypesensortypeidaccelerometeruncalibrated) | Subscribes to data changes of the uncalibrated acceleration sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-onsensortypesensortypeidambientlight-f.md#onsensortypesensortypeidambientlight) | Subscribes to data changes of the ambient light sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-onsensortypesensortypeidambienttemperature-f.md#onsensortypesensortypeidambienttemperature) | Subscribes to data changes of the ambient temperature sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-onsensortypesensortypeidbarometer-f.md#onsensortypesensortypeidbarometer) | Subscribes to data changes of the barometer sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-onsensortypesensortypeidgravity-f.md#onsensortypesensortypeidgravity) | Subscribes to data changes of the gravity sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscope-f.md#onsensortypesensortypeidgyroscope) | Subscribes to data changes of the gyroscope sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidgyroscopeuncalibrated-f.md#onsensortypesensortypeidgyroscopeuncalibrated) | Subscribes to data changes of the uncalibrated gyroscope sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-onsensortypesensortypeidhall-f.md#onsensortypesensortypeidhall) | Subscribes to data changes of the Hall effect sensor. If this API is called multiple times for the same application , the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-onsensortypesensortypeidheartrate-f.md#onsensortypesensortypeidheartrate) | Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-onsensortypesensortypeidhumidity-f.md#onsensortypesensortypeidhumidity) | Subscribes to data changes of the humidity sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-onsensortypesensortypeidlinearacceleration-f.md#onsensortypesensortypeidlinearacceleration) | Subscribes to data changes of the linear acceleration sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfield-f.md#onsensortypesensortypeidmagneticfield) | Subscribes to data changes of the magnetic field sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-onsensortypesensortypeidmagneticfielduncalibrated-f.md#onsensortypesensortypeidmagneticfielduncalibrated) | Subscribes to data changes of the uncalibrated magnetic field sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-onsensortypesensortypeidorientation-f.md#onsensortypesensortypeidorientation) | Subscribes to data changes of the orientation sensor. If this API is called multiple times for the same application , the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-onsensortypesensortypeidpedometer-f.md#onsensortypesensortypeidpedometer) | Subscribes to data changes of the pedometer sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidpedometerdetection-f.md#onsensortypesensortypeidpedometerdetection) | Subscribes to data changes of the pedometer detection sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-onsensortypesensortypeidproximity-f.md#onsensortypesensortypeidproximity) | Subscribes to data changes of the proximity sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-onsensortypesensortypeidrotationvector-f.md#onsensortypesensortypeidrotationvector) | Subscribes to data changes of the rotation vector sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-onsensortypesensortypeidsignificantmotion-f.md#onsensortypesensortypeidsignificantmotion) | Subscribes to data changes of the significant motion sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-onsensortypesensortypeidweardetection-f.md#onsensortypesensortypeidweardetection) | Subscribes to data changes of the wear detection sensor. If this API is called multiple times for the same application, the last call takes effect. |
| [on_sensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md#onsensorstatuschange) | Enables listening for sensor status changes. This API asynchronously returns the result through a callback. |
| [onceAccelerometerChange](arkts-sensorservice-sensor-onceaccelerometerchange-f.md#onceaccelerometerchange) | Subscribe to accelerometer sensor data once, {@code SensorId.ACCELEROMETER}. |
| [onceAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onceaccelerometeruncalibratedchange-f.md#onceaccelerometeruncalibratedchange) | Subscribe to uncalibrated accelerometer sensor data once, {@code SensorId.ACCELEROMETER_UNCALIBRATED}. |
| [onceAmbientLightChange](arkts-sensorservice-sensor-onceambientlightchange-f.md#onceambientlightchange) | Subscribe to ambient light sensor data once, {@code SensorId.AMBIENT_LIGHT}. |
| [onceAmbientTemperatureChange](arkts-sensorservice-sensor-onceambienttemperaturechange-f.md#onceambienttemperaturechange) | Subscribe to ambient temperature sensor data once, {@code SensorId.AMBIENT_TEMPERATURE}. |
| [onceBarometerChange](arkts-sensorservice-sensor-oncebarometerchange-f.md#oncebarometerchange) | Subscribe to barometer sensor data once, {@code SensorId.BAROMETER}. |
| [onceGravityChange](arkts-sensorservice-sensor-oncegravitychange-f.md#oncegravitychange) | Subscribe to gravity sensor data once, {@code SensorId.GRAVITY}. |
| [onceGyroscopeChange](arkts-sensorservice-sensor-oncegyroscopechange-f.md#oncegyroscopechange) | Subscribe to gyroscope sensor data once, {@code SensorId.GYROSCOPE}. |
| [onceGyroscopeUncalibratedChange](arkts-sensorservice-sensor-oncegyroscopeuncalibratedchange-f.md#oncegyroscopeuncalibratedchange) | Subscribe to uncalibrated gyroscope sensor data once, {@code SensorId.GYROSCOPE_UNCALIBRATED}. |
| [onceHallChange](arkts-sensorservice-sensor-oncehallchange-f.md#oncehallchange) | Subscribe to hall sensor data once, {@code SensorId.HALL}. |
| [onceHeartRateChange](arkts-sensorservice-sensor-onceheartratechange-f.md#onceheartratechange) | Subscribe to heart rate sensor data once, {@code SensorId.HEART_RATE}. |
| [onceHumidityChange](arkts-sensorservice-sensor-oncehumiditychange-f.md#oncehumiditychange) | Subscribe to humidity sensor data once, {@code SensorId.HUMIDITY}. |
| [onceLinearAccelerometerChange](arkts-sensorservice-sensor-oncelinearaccelerometerchange-f.md#oncelinearaccelerometerchange) | Subscribe to linear acceleration sensor data once, {@code SensorId.LINEAR_ACCELEROMETER}. |
| [onceMagneticFieldChange](arkts-sensorservice-sensor-oncemagneticfieldchange-f.md#oncemagneticfieldchange) | Subscribe to magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD}. |
| [onceMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-oncemagneticfielduncalibratedchange-f.md#oncemagneticfielduncalibratedchange) | Subscribe to uncalibrated magnetic field sensor data once, {@code SensorId.MAGNETIC_FIELD_UNCALIBRATED}. |
| [onceOrientationChange](arkts-sensorservice-sensor-onceorientationchange-f.md#onceorientationchange) | Subscribe to orientation sensor data once, {@code SensorId.ORIENTATION}. |
| [oncePedometerChange](arkts-sensorservice-sensor-oncepedometerchange-f.md#oncepedometerchange) | Subscribe to pedometer sensor data once, {@code SensorId.PEDOMETER}. |
| [oncePedometerDetectionChange](arkts-sensorservice-sensor-oncepedometerdetectionchange-f.md#oncepedometerdetectionchange) | Subscribe to pedometer detection sensor data once, {@code SensorId.PEDOMETER_DETECTION}. |
| [onceProximityChange](arkts-sensorservice-sensor-onceproximitychange-f.md#onceproximitychange) | Subscribe to proximity sensor data once, {@code SensorId.PROXIMITY}. |
| [onceRotationVectorChange](arkts-sensorservice-sensor-oncerotationvectorchange-f.md#oncerotationvectorchange) | Subscribe to rotation vector sensor data once, {@code SensorId.ROTATION_VECTOR}. |
| [onceSignificantMotionChange](arkts-sensorservice-sensor-oncesignificantmotionchange-f.md#oncesignificantmotionchange) | Subscribe to significant motion sensor data once, {@code SensorId.SIGNIFICANT_MOTION}. |
| [onceWearDetectionChange](arkts-sensorservice-sensor-onceweardetectionchange-f.md#onceweardetectionchange) | Subscribe to wear detection sensor data once, {@code SensorId.WEAR_DETECTION}. |
| [once_SensorId.ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridaccelerometer-f.md#oncesensoridaccelerometer) | Obtains data of the acceleration sensor once. |
| [once_SensorId.ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridaccelerometeruncalibrated-f.md#oncesensoridaccelerometeruncalibrated) | Obtains data of the uncalibrated acceleration sensor once. |
| [once_SensorId.AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensoridambientlight-f.md#oncesensoridambientlight) | Obtains data of the ambient light sensor once. |
| [once_SensorId.AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensoridambienttemperature-f.md#oncesensoridambienttemperature) | Obtains data of the temperature sensor once. |
| [once_SensorId.BAROMETER](arkts-sensorservice-sensor-oncesensoridbarometer-f.md#oncesensoridbarometer) | Obtains data of the barometer sensor once. |
| [once_SensorId.GRAVITY](arkts-sensorservice-sensor-oncesensoridgravity-f.md#oncesensoridgravity) | Obtains data of the gravity sensor once. |
| [once_SensorId.GYROSCOPE](arkts-sensorservice-sensor-oncesensoridgyroscope-f.md#oncesensoridgyroscope) | Obtains data of the gyroscope sensor once. |
| [once_SensorId.GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridgyroscopeuncalibrated-f.md#oncesensoridgyroscopeuncalibrated) | Obtains data of the uncalibrated gyroscope sensor once. |
| [once_SensorId.HALL](arkts-sensorservice-sensor-oncesensoridhall-f.md#oncesensoridhall) | Obtains data of the Hall effect sensor once. |
| [once_SensorId.HEART_RATE](arkts-sensorservice-sensor-oncesensoridheartrate-f.md#oncesensoridheartrate) | Obtains data of the heart rate sensor once. |
| [once_SensorId.HUMIDITY](arkts-sensorservice-sensor-oncesensoridhumidity-f.md#oncesensoridhumidity) | Obtains data of the humidity sensor once. |
| [once_SensorId.LINEAR_ACCELEROMETER](arkts-sensorservice-sensor-oncesensoridlinearaccelerometer-f.md#oncesensoridlinearaccelerometer) | Obtains data of the linear acceleration sensor once. |
| [once_SensorId.MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensoridmagneticfield-f.md#oncesensoridmagneticfield) | Obtains data of the magnetic field sensor once. |
| [once_SensorId.MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensoridmagneticfielduncalibrated-f.md#oncesensoridmagneticfielduncalibrated) | Obtains data of the uncalibrated magnetic field sensor once. |
| [once_SensorId.ORIENTATION](arkts-sensorservice-sensor-oncesensoridorientation-f.md#oncesensoridorientation) | Obtains data of the orientation sensor once. |
| [once_SensorId.PEDOMETER](arkts-sensorservice-sensor-oncesensoridpedometer-f.md#oncesensoridpedometer) | Obtains data of the pedometer sensor once. The step counter sensor's data reporting is subject to some delay, and the delay is determined by specific product implementations. |
| [once_SensorId.PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensoridpedometerdetection-f.md#oncesensoridpedometerdetection) | Obtains data of the pedometer sensor once. |
| [once_SensorId.PROXIMITY](arkts-sensorservice-sensor-oncesensoridproximity-f.md#oncesensoridproximity) | Obtains data of the proximity sensor once. |
| [once_SensorId.ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensoridrotationvector-f.md#oncesensoridrotationvector) | Obtains data of the rotation vector sensor once. |
| [once_SensorId.SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensoridsignificantmotion-f.md#oncesensoridsignificantmotion) | Obtains the significant motion sensor data once. |
| [once_SensorId.WEAR_DETECTION](arkts-sensorservice-sensor-oncesensoridweardetection-f.md#oncesensoridweardetection) | Obtains data of the wear detection sensor once. |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometer-f.md#oncesensortypesensortypeidaccelerometer) | Subscribes to only one data change of the acceleration sensor. |
| [once_SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidaccelerometeruncalibrated-f.md#oncesensortypesensortypeidaccelerometeruncalibrated) | Subscribes to only one data change of the uncalibrated acceleration sensor. |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT](arkts-sensorservice-sensor-oncesensortypesensortypeidambientlight-f.md#oncesensortypesensortypeidambientlight) | Subscribes to only one data change of the ambient light sensor. |
| [once_SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE](arkts-sensorservice-sensor-oncesensortypesensortypeidambienttemperature-f.md#oncesensortypesensortypeidambienttemperature) | Subscribes to only one data change of the ambient temperature sensor. |
| [once_SensorType.SENSOR_TYPE_ID_BAROMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidbarometer-f.md#oncesensortypesensortypeidbarometer) | Subscribes to only one data change of the barometer sensor. |
| [once_SensorType.SENSOR_TYPE_ID_GRAVITY](arkts-sensorservice-sensor-oncesensortypesensortypeidgravity-f.md#oncesensortypesensortypeidgravity) | Subscribes to only one data change of the gravity sensor. |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscope-f.md#oncesensortypesensortypeidgyroscope) | Subscribes to only one data change of the gyroscope sensor. |
| [once_SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidgyroscopeuncalibrated-f.md#oncesensortypesensortypeidgyroscopeuncalibrated) | Subscribes to only one data change of the uncalibrated gyroscope sensor. |
| [once_SensorType.SENSOR_TYPE_ID_HALL](arkts-sensorservice-sensor-oncesensortypesensortypeidhall-f.md#oncesensortypesensortypeidhall) | Subscribes to only one data change of the Hall effect sensor. |
| [once_SensorType.SENSOR_TYPE_ID_HEART_RATE](arkts-sensorservice-sensor-oncesensortypesensortypeidheartrate-f.md#oncesensortypesensortypeidheartrate) | Subscribes to only one data change of the heart rate sensor. |
| [once_SensorType.SENSOR_TYPE_ID_HUMIDITY](arkts-sensorservice-sensor-oncesensortypesensortypeidhumidity-f.md#oncesensortypesensortypeidhumidity) | Subscribes to only one data change of the humidity sensor. |
| [once_SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION](arkts-sensorservice-sensor-oncesensortypesensortypeidlinearacceleration-f.md#oncesensortypesensortypeidlinearacceleration) | Subscribes to only one data change of the linear acceleration sensor. |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfield-f.md#oncesensortypesensortypeidmagneticfield) | Subscribes to only one data change of the magnetic field sensor. |
| [once_SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED](arkts-sensorservice-sensor-oncesensortypesensortypeidmagneticfielduncalibrated-f.md#oncesensortypesensortypeidmagneticfielduncalibrated) | Subscribes to only one data change of the uncalibrated magnetic field sensor. |
| [once_SensorType.SENSOR_TYPE_ID_ORIENTATION](arkts-sensorservice-sensor-oncesensortypesensortypeidorientation-f.md#oncesensortypesensortypeidorientation) | Subscribes to only one data change of the orientation sensor. |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometer-f.md#oncesensortypesensortypeidpedometer) | Subscribes to only one data change of the pedometer sensor. |
| [once_SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidpedometerdetection-f.md#oncesensortypesensortypeidpedometerdetection) | Subscribes to only one data change of the pedometer detection sensor. |
| [once_SensorType.SENSOR_TYPE_ID_PROXIMITY](arkts-sensorservice-sensor-oncesensortypesensortypeidproximity-f.md#oncesensortypesensortypeidproximity) | Subscribes to only one data change of the proximity sensor. |
| [once_SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR](arkts-sensorservice-sensor-oncesensortypesensortypeidrotationvector-f.md#oncesensortypesensortypeidrotationvector) | Subscribes to only one data change of the rotation vector sensor. |
| [once_SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION](arkts-sensorservice-sensor-oncesensortypesensortypeidsignificantmotion-f.md#oncesensortypesensortypeidsignificantmotion) | Subscribes to only one data change of the significant motion sensor. |
| [once_SensorType.SENSOR_TYPE_ID_WEAR_DETECTION](arkts-sensorservice-sensor-oncesensortypesensortypeidweardetection-f.md#oncesensortypesensortypeidweardetection) | Subscribes to only one data change of the wear detection sensor. |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem) | Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses an asynchronous callback to return the result. |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md#transformcoordinatesystem) | Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses a promise to return the result. |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix) | Transforms a rotation vector based on the coordinate system. This API uses an asynchronous callback to return the result. |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md#transformrotationmatrix) | Transforms a rotation vector based on the coordinate system. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [offColorChange](arkts-sensorservice-sensor-offcolorchange-f-sys.md#offcolorchange) | Unsubscribe to color sensor data, {@code SensorId.COLOR}. |
| [offSarChange](arkts-sensorservice-sensor-offsarchange-f-sys.md#offsarchange) | Unsubscribe to sar sensor data, {@code SensorId.SAR}. |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#offsensoridcolor) | Unsubscribes from data of the color sensor. |
| [off_SensorId.COLOR](arkts-sensorservice-sensor-offsensoridcolor-f-sys.md#offsensoridcolor-1) | Unsubscribes from data of the color sensor. |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#offsensoridsar) | Unsubscribes from data of the SAR sensor. |
| [off_SensorId.SAR](arkts-sensorservice-sensor-offsensoridsar-f-sys.md#offsensoridsar-1) | Unsubscribes from data of the SAR sensor. |
| [onColorChange](arkts-sensorservice-sensor-oncolorchange-f-sys.md#oncolorchange) | Subscribe to color sensor data, {@code SensorId.COLOR}. |
| [onSarChange](arkts-sensorservice-sensor-onsarchange-f-sys.md#onsarchange) | Subscribe to SAR sensor data, {@code SensorId.SAR}. |
| [on_SensorId.COLOR](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#onsensoridcolor) | Subscribes to data of the color sensor. |
| [on_SensorId.SAR](arkts-sensorservice-sensor-onsensoridsar-f-sys.md#onsensoridsar) | Subscribes to data of the Sodium Adsorption Ratio (SAR) sensor. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AccelerometerResponse](arkts-sensorservice-sensor-accelerometerresponse-i.md) | Describes the acceleration sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [AccelerometerUncalibratedResponse](arkts-sensorservice-sensor-accelerometeruncalibratedresponse-i.md) | Describes the uncalibrated acceleration sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [AmbientTemperatureResponse](arkts-sensorservice-sensor-ambienttemperatureresponse-i.md) | Describes the ambient temperature sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [BarometerResponse](arkts-sensorservice-sensor-barometerresponse-i.md) | Describes the barometer sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) | Describes the coordinate options. |
| [FusionPressureResponse](arkts-sensorservice-sensor-fusionpressureresponse-i.md) | Describes the fusion pressure sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [GeomagneticResponse](arkts-sensorservice-sensor-geomagneticresponse-i.md) | Describes a geomagnetic response object. |
| [GravityResponse](arkts-sensorservice-sensor-gravityresponse-i.md) | Describes the gravity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [GyroscopeResponse](arkts-sensorservice-sensor-gyroscoperesponse-i.md) | Describes the gyroscope sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [GyroscopeUncalibratedResponse](arkts-sensorservice-sensor-gyroscopeuncalibratedresponse-i.md) | Describes the uncalibrated gyroscope sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [HallResponse](arkts-sensorservice-sensor-hallresponse-i.md) | Describes the Hall effect sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [HeartRateResponse](arkts-sensorservice-sensor-heartrateresponse-i.md) | Describes the heart rate sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [HumidityResponse](arkts-sensorservice-sensor-humidityresponse-i.md) | Describes the humidity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [LightResponse](arkts-sensorservice-sensor-lightresponse-i.md) | Describes the ambient light sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [LinearAccelerometerResponse](arkts-sensorservice-sensor-linearaccelerometerresponse-i.md) | Describes the linear acceleration sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [LocationOptions](arkts-sensorservice-sensor-locationoptions-i.md) | Describes the geographical location. |
| [MagneticFieldResponse](arkts-sensorservice-sensor-magneticfieldresponse-i.md) | Describes the magnetic field sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [MagneticFieldUncalibratedResponse](arkts-sensorservice-sensor-magneticfielduncalibratedresponse-i.md) | Describes the uncalibrated magnetic field sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [Options](arkts-sensorservice-sensor-options-i.md) | Describes the sensor data reporting frequency. |
| [OrientationResponse](arkts-sensorservice-sensor-orientationresponse-i.md) | Describes the orientation sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [PedometerDetectionResponse](arkts-sensorservice-sensor-pedometerdetectionresponse-i.md) | Describes the pedometer detection sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [PedometerResponse](arkts-sensorservice-sensor-pedometerresponse-i.md) | Describes the pedometer sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [ProximityResponse](arkts-sensorservice-sensor-proximityresponse-i.md) | Describes the proximity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [Response](arkts-sensorservice-sensor-response-i.md) | Describes the timestamp of the sensor data. |
| [RotationMatrixResponse](arkts-sensorservice-sensor-rotationmatrixresponse-i.md) | Describes the response for setting the rotation matrix. |
| [RotationVectorResponse](arkts-sensorservice-sensor-rotationvectorresponse-i.md) | Describes the rotation vector sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [Sensor](arkts-sensorservice-sensor-sensor-i.md) | Describes the sensor information. |
| [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md) | Defines sensor parameters, including **deviceId** and **sensorIndex**. |
| [SensorStatusEvent](arkts-sensorservice-sensor-sensorstatusevent-i.md) | Defines a device status change event. |
| [SignificantMotionResponse](arkts-sensorservice-sensor-significantmotionresponse-i.md) | Describes the significant motion sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [WearDetectionResponse](arkts-sensorservice-sensor-weardetectionresponse-i.md) | Describes the wear detection sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md) | Describes the color sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
| [SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md) | Describes the SAR sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response). |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md) | Enumerates the accuracy levels of sensor data. |
| [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | Enumerates the sensor types. |
| [SensorType](arkts-sensorservice-sensor-sensortype-e.md) | Enumerates the sensor types. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [SensorId](arkts-sensorservice-sensor-sensorid-e-sys.md) | Enumerates the sensor types. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [SensorFrequency](arkts-sensorservice-sensor-sensorfrequency-t.md) | Defines the reporting frequency mode of the sensor. |

