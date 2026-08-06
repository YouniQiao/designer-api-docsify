# AccessibilityFocusCallback

```TypeScript
export type AccessibilityFocusCallback = (isFocus: boolean) => void
```

Defines the callback type used in accessibility focus. The value of isFocus indicates whether the current component is focused

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type AccessibilityFocusCallback = (isFocus: boolean) => void--><!--Device-unnamed-export type AccessibilityFocusCallback = (isFocus: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isFocus | boolean | Yes | if component is focused,isFocus will be true. else isFocus is false.  |

