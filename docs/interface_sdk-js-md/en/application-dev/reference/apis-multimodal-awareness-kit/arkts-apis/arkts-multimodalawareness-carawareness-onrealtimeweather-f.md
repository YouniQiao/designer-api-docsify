# onRealTimeWeather

## Modules to Import

```TypeScript
import { carAwareness } from '@kit.MultimodalAwarenessKit';
```

## onRealTimeWeather

```TypeScript
function onRealTimeWeather(callback: Callback<RealTimeWeatherInfo>): void
```

Enables real-time weather awareness and subscribes to real-time weather awareness results. If the capability is not supported, no callback will be triggered. You can obtain the supported capabilities by calling the getAllCapacityList method.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Required permissions:** ohos.permission.vehicle.MMA_WEATHER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RealTimeWeatherInfo](arkts-multimodalawareness-carawareness-realtimeweatherinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [34000001](../errorcode-onScreen.md#34000001-service-exception) |
| [34000002](../errorcode-onScreen.md#34000002-unsupported-application-or-page) |
