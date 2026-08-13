# AreaChangeCallback

```TypeScript
declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void
```

Callback type for the component area change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void--><!--Device-unnamed-declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldValue | Area | Yes | Information before the area change, including the width, height, coordinates relative to the parent element, and position coordinates of the upper-left corner in the current window coordinate system. |
| newValue | Area | Yes | Information after the area change, including the width, height, coordinates relative to the parent element, and position coordinates of the upper-left corner in the current window coordinate system. |

