# PageTransitionCallback

```TypeScript
declare type PageTransitionCallback = (type: RouteType, progress: number) => void
```

Represents the callback for page transition events.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type PageTransitionCallback = (type: RouteType, progress: number) => void--><!--Device-unnamed-declare type PageTransitionCallback = (type: RouteType, progress: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [RouteType](arkts-arkui-routetype-e.md) | Yes |
| progress | number | Yes |
