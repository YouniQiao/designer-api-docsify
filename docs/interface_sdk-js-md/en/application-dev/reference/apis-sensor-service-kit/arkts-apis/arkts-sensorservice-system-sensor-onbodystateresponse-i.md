# OnBodyStateResponse

设备佩戴状态的响应对象，包含设备是否已佩戴的状态数据。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#WearDetectionResponse

<!--Device-unnamed-export interface OnBodyStateResponse--><!--Device-unnamed-export interface OnBodyStateResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## Modules to Import

```TypeScript
import { OnBodyStateResponse, subscribeAccelerometerOptions, ProximityResponse, SubscribeGyroscopeOptions, SubscribeStepCounterOptions, SubscribeDeviceOrientationOptions, HeartRateResponse, LightResponse, AccelerometerResponse, SubscribeLightOptions, DeviceOrientationResponse, SubscribeHeartRateOptions, StepCounterResponse, SubscribeCompassOptions, GetOnBodyStateOptions, SubscribeBarometerOptions, BarometerResponse, SubscribeProximityOptions, CompassResponse, GyroscopeResponse, SubscribeOnBodyStateOptions } from 'kits/@kit.SensorServiceKit';
```

## value

```TypeScript
value: boolean
```

是否已佩戴设备。取值说明：true表示已佩戴，false表示未佩戴。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#WearDetectionResponse.value

**Model restriction:** This API can be used only in the FA model.

<!--Device-OnBodyStateResponse-value: boolean--><!--Device-OnBodyStateResponse-value: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

