# OnAdsEventLoadingErrorHandle

```TypeScript
type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void
```

Describes the callback function for the ad media resource loading error event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void--><!--Device-media-type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adsId | string | Yes | ID of the advertisement resource that fails to be loaded. |
| reason | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md) | Yes | Indicates the reason of the loading failure. |

