# @ohos.sensor

@ohos.sensor 模块是鸿蒙操作系统提供的传感器服务模块，属于 SensorServiceKit。该模块为开发者提供了统一的传感器数据访问能力，涵盖设备上各类物理传感器的数据订阅、查询以及传感器算法计算。 sensor 模块是传感器数据访问的统一接口，定义了设备上各类物理传感器的订阅、查询和算法计算能力。 当应用需要感知设备运动状态（如摇一摇、翻转）、检测环境条件（如自动调节屏幕亮度、测量气压估算海拔）、获取设备方向（如指南针导航）、监测健康数据（如心率计步）时，应使用本模块订阅对应传感器数据。当需要进行传感器数据相关的数学变换和计算时 ，应使用传感器算法接口。

> **说明：**

> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。订阅前可使用
> [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md)
> 接口获取该传感器的信息，获取该传感器信息成功时可正常订阅传感器，异常情况详见
> [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md)错误码说明。
> 订阅传感器数据时确保on订阅和off取消订阅成对出现。sensor模块提供传感器数据订阅与查询能力，核心使用流程如下：
1. 使用[sensor.getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md)
或[sensor.getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md)查询传感器信息，确认设备支持目标传感器。
2. 使用sensor.on接口订阅传感器数据，持续接收数据回调。
3. 使用sensor.once接口获取一次传感器数据，适用于无需持续监听的场景。
4. 使用sensor.off接口取消订阅，确保on和off成对调用。
sensor.on与sensor.once的区别：  
- sensor.on持续订阅传感器数据，通过callback反复上报，适用于需要实时监测的场景。 - sensor.once仅获取一次传感器数据，callback只触发一次后自动取消订阅，适用于单次采集的场景。 注意事项： - 订阅前建议先使用getSingleSensor确认设备支持该传感器。 - on订阅和off取消订阅必须成对出现，避免资源泄漏。 - 对于需要权限的传感器（加速度、陀螺仪、心率、计步等），须先申请相应权限。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.Sensor

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md) |
| [createQuaternion](arkts-sensorservice-sensor-createquaternion-f.md) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md) |
| [createRotationMatrix](arkts-sensorservice-sensor-createrotationmatrix-f.md) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md) |
| [getAltitude](arkts-sensorservice-sensor-getaltitude-f.md) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md) |
| [getAngleModify](arkts-sensorservice-sensor-getanglemodify-f.md) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md) |
| [getAngleVariation](arkts-sensorservice-sensor-getanglevariation-f.md) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md) |
| [getDeviceAltitude](arkts-sensorservice-sensor-getdevicealtitude-f.md) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md) |
| [getDirection](arkts-sensorservice-sensor-getdirection-f.md) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md) |
| [getGeomagneticDip](arkts-sensorservice-sensor-getgeomagneticdip-f.md) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md) |
| [getGeomagneticField](arkts-sensorservice-sensor-getgeomagneticfield-f.md) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md) |
| [getGeomagneticInfo](arkts-sensorservice-sensor-getgeomagneticinfo-f.md) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md) |
| [getInclination](arkts-sensorservice-sensor-getinclination-f.md) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md) |
| [getOrientation](arkts-sensorservice-sensor-getorientation-f.md) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md) |
| [getQuaternion](arkts-sensorservice-sensor-getquaternion-f.md) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md) |
| [getRotationMatrix](arkts-sensorservice-sensor-getrotationmatrix-f.md) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md) |
| [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md) |
| [getSensorListByDeviceSync](arkts-sensorservice-sensor-getsensorlistbydevicesync-f.md) |
| [getSensorListSync](arkts-sensorservice-sensor-getsensorlistsync-f.md) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md) |
| [getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md) |
| [getSingleSensorByDeviceSync](arkts-sensorservice-sensor-getsinglesensorbydevicesync-f.md) |
| [getSingleSensorSync](arkts-sensorservice-sensor-getsinglesensorsync-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md) |
| [off](arkts-sensorservice-sensor-off-f.md#offsensorstatuschange) |
| [offAccelerometerChange](arkts-sensorservice-sensor-offaccelerometerchange-f.md) |
| [offAccelerometerUncalibratedChange](arkts-sensorservice-sensor-offaccelerometeruncalibratedchange-f.md) |
| [offAmbientLightChange](arkts-sensorservice-sensor-offambientlightchange-f.md) |
| [offAmbientTemperatureChange](arkts-sensorservice-sensor-offambienttemperaturechange-f.md) |
| [offBarometerChange](arkts-sensorservice-sensor-offbarometerchange-f.md) |
| [offFusionPressureChange](arkts-sensorservice-sensor-offfusionpressurechange-f.md) |
| [offGravityChange](arkts-sensorservice-sensor-offgravitychange-f.md) |
| [offGyroscopeChange](arkts-sensorservice-sensor-offgyroscopechange-f.md) |
| [offGyroscopeUncalibratedChange](arkts-sensorservice-sensor-offgyroscopeuncalibratedchange-f.md) |
| [offHallChange](arkts-sensorservice-sensor-offhallchange-f.md) |
| [offHeartRateChange](arkts-sensorservice-sensor-offheartratechange-f.md) |
| [offHumidityChange](arkts-sensorservice-sensor-offhumiditychange-f.md) |
| [offLinearAccelerometerChange](arkts-sensorservice-sensor-offlinearaccelerometerchange-f.md) |
| [offMagneticFieldChange](arkts-sensorservice-sensor-offmagneticfieldchange-f.md) |
| [offMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-offmagneticfielduncalibratedchange-f.md) |
| [offOrientationChange](arkts-sensorservice-sensor-offorientationchange-f.md) |
| [offPedometerChange](arkts-sensorservice-sensor-offpedometerchange-f.md) |
| [offPedometerDetectionChange](arkts-sensorservice-sensor-offpedometerdetectionchange-f.md) |
| [offProximityChange](arkts-sensorservice-sensor-offproximitychange-f.md) |
| [offRotationVectorChange](arkts-sensorservice-sensor-offrotationvectorchange-f.md) |
| [offSensorStatusChange](arkts-sensorservice-sensor-offsensorstatuschange-f.md) |
| [offSignificantMotionChange](arkts-sensorservice-sensor-offsignificantmotionchange-f.md) |
| [offWearDetectionChange](arkts-sensorservice-sensor-offweardetectionchange-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md) |
| [on](arkts-sensorservice-sensor-on-f.md#onsensorstatuschange) |
| [onAccelerometerChange](arkts-sensorservice-sensor-onaccelerometerchange-f.md) |
| [onAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onaccelerometeruncalibratedchange-f.md) |
| [onAmbientLightChange](arkts-sensorservice-sensor-onambientlightchange-f.md) |
| [onAmbientTemperatureChange](arkts-sensorservice-sensor-onambienttemperaturechange-f.md) |
| [onBarometerChange](arkts-sensorservice-sensor-onbarometerchange-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [once](arkts-sensorservice-sensor-once-f.md) |
| [onceAccelerometerChange](arkts-sensorservice-sensor-onceaccelerometerchange-f.md) |
| [onceAccelerometerUncalibratedChange](arkts-sensorservice-sensor-onceaccelerometeruncalibratedchange-f.md) |
| [onceAmbientLightChange](arkts-sensorservice-sensor-onceambientlightchange-f.md) |
| [onceAmbientTemperatureChange](arkts-sensorservice-sensor-onceambienttemperaturechange-f.md) |
| [onceBarometerChange](arkts-sensorservice-sensor-oncebarometerchange-f.md) |
| [onceGravityChange](arkts-sensorservice-sensor-oncegravitychange-f.md) |
| [onceGyroscopeChange](arkts-sensorservice-sensor-oncegyroscopechange-f.md) |
| [onceGyroscopeUncalibratedChange](arkts-sensorservice-sensor-oncegyroscopeuncalibratedchange-f.md) |
| [onceHallChange](arkts-sensorservice-sensor-oncehallchange-f.md) |
| [onceHeartRateChange](arkts-sensorservice-sensor-onceheartratechange-f.md) |
| [onceHumidityChange](arkts-sensorservice-sensor-oncehumiditychange-f.md) |
| [onceLinearAccelerometerChange](arkts-sensorservice-sensor-oncelinearaccelerometerchange-f.md) |
| [onceMagneticFieldChange](arkts-sensorservice-sensor-oncemagneticfieldchange-f.md) |
| [onceMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-oncemagneticfielduncalibratedchange-f.md) |
| [onceOrientationChange](arkts-sensorservice-sensor-onceorientationchange-f.md) |
| [oncePedometerChange](arkts-sensorservice-sensor-oncepedometerchange-f.md) |
| [oncePedometerDetectionChange](arkts-sensorservice-sensor-oncepedometerdetectionchange-f.md) |
| [onceProximityChange](arkts-sensorservice-sensor-onceproximitychange-f.md) |
| [onceRotationVectorChange](arkts-sensorservice-sensor-oncerotationvectorchange-f.md) |
| [onceSignificantMotionChange](arkts-sensorservice-sensor-oncesignificantmotionchange-f.md) |
| [onceWearDetectionChange](arkts-sensorservice-sensor-onceweardetectionchange-f.md) |
| [onFusionPressureChange](arkts-sensorservice-sensor-onfusionpressurechange-f.md) |
| [onGravityChange](arkts-sensorservice-sensor-ongravitychange-f.md) |
| [onGyroscopeChange](arkts-sensorservice-sensor-ongyroscopechange-f.md) |
| [onGyroscopeUncalibratedChange](arkts-sensorservice-sensor-ongyroscopeuncalibratedchange-f.md) |
| [onHallChange](arkts-sensorservice-sensor-onhallchange-f.md) |
| [onHeartRateChange](arkts-sensorservice-sensor-onheartratechange-f.md) |
| [onHumidityChange](arkts-sensorservice-sensor-onhumiditychange-f.md) |
| [onLinearAccelerometerChange](arkts-sensorservice-sensor-onlinearaccelerometerchange-f.md) |
| [onMagneticFieldChange](arkts-sensorservice-sensor-onmagneticfieldchange-f.md) |
| [onMagneticFieldUncalibratedChange](arkts-sensorservice-sensor-onmagneticfielduncalibratedchange-f.md) |
| [onOrientationChange](arkts-sensorservice-sensor-onorientationchange-f.md) |
| [onPedometerChange](arkts-sensorservice-sensor-onpedometerchange-f.md) |
| [onPedometerDetectionChange](arkts-sensorservice-sensor-onpedometerdetectionchange-f.md) |
| [onProximityChange](arkts-sensorservice-sensor-onproximitychange-f.md) |
| [onRotationVectorChange](arkts-sensorservice-sensor-onrotationvectorchange-f.md) |
| [onSensorStatusChange](arkts-sensorservice-sensor-onsensorstatuschange-f.md) |
| [onSignificantMotionChange](arkts-sensorservice-sensor-onsignificantmotionchange-f.md) |
| [onWearDetectionChange](arkts-sensorservice-sensor-onweardetectionchange-f.md) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md) |
| [transformCoordinateSystem](arkts-sensorservice-sensor-transformcoordinatesystem-f.md) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md) |
| [transformRotationMatrix](arkts-sensorservice-sensor-transformrotationmatrix-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [off](arkts-sensorservice-sensor-off-f-sys.md) |
| [off](arkts-sensorservice-sensor-off-f-sys.md) |
| [off](arkts-sensorservice-sensor-off-f-sys.md) |
| [off](arkts-sensorservice-sensor-off-f-sys.md) |
| [offColorChange](arkts-sensorservice-sensor-offcolorchange-f-sys.md) |
| [offSarChange](arkts-sensorservice-sensor-offsarchange-f-sys.md) |
| [on](arkts-sensorservice-sensor-on-f-sys.md) |
| [on](arkts-sensorservice-sensor-on-f-sys.md) |
| [onColorChange](arkts-sensorservice-sensor-oncolorchange-f-sys.md) |
| [onSarChange](arkts-sensorservice-sensor-onsarchange-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md) |
| [SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md) |
| [SensorId](arkts-sensorservice-sensor-sensorid-e.md) |
| [SensorType](arkts-sensorservice-sensor-sensortype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SensorId](arkts-sensorservice-sensor-sensorid-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [SensorFrequency](arkts-sensorservice-sensor-sensorfrequency-t.md) |
