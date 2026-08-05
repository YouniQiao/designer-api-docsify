# SubscribeLightOptions

Defines the type of data to return for a subscription to data changes of the ambient light sensor.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor.SensorId#AMBIENT_LIGHT

<!--Device-unnamed-export interface SubscribeLightOptions--><!--Device-unnamed-export interface SubscribeLightOptions-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Callback invoked when an API call fails.

**Type:** (data: string, code: number) =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeLightOptions-fail?: (data: string, code: number) => void--><!--Device-SubscribeLightOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

## success

```TypeScript
success: (data: LightResponse) => void
```

Callback invoked when the ambient light sensor data changes.

**Type:** (data: LightResponse) =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.sensor/sensor#on

**Model restriction:** This API can be used only in the FA model.

<!--Device-SubscribeLightOptions-success: (data: LightResponse) => void--><!--Device-SubscribeLightOptions-success: (data: LightResponse) => void-End-->

**System capability:** SystemCapability.Sensors.Sensor.Lite

