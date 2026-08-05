# OnAdsEventAdsStartedHandle

```TypeScript
type OnAdsEventAdsStartedHandle = (adsId: string, duration: int) => void
```

Describes the callback function of the ad content playback start event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnAdsEventAdsStartedHandle = (adsId: string, duration: int) => void--><!--Device-media-type OnAdsEventAdsStartedHandle = (adsId: string, duration: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adsId | string | Yes | ID of the ad resource that is being played.  |
| duration | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Playing duration of the advertisement, in milliseconds. \_\_\_HTML\_TAG\_USD\_0\_\_\_The value should be an integer.  |

