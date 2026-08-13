# OnAdsEventLoadingErrorHandle

```TypeScript
type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void
```

Describes the callback function for the ad media resource loading error event.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void--><!--Device-media-type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adsId | string | Yes |
| reason | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md) | Yes |
