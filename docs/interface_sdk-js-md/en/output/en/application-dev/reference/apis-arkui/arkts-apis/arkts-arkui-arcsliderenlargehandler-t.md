# ArcSliderEnlargeHandler

```TypeScript
declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void
```

Defines the callback invoked to notify the application when the arc slider is enlarged or reduced.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void--><!--Device-unnamed-declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnlarged | boolean | Yes | Whether the arc slider is enlarged.\_\_\_HTML\_TAG\_USD\_0\_\_\_**false**: The arc slider is in a reduced state.\_\_\_HTML\_TAG\_USD\_1\_\_\_**true**: The arc slider is in an enlarged state.  |

