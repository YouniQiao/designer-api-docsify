# ScrollOnScrollCallback

```TypeScript
export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void
```

Represents the callback triggered when the \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ component scrolls. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If the \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_onScrollFrameBegin\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ event and \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_scrollBy\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ method are used to implement nested scrolling, set the \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_edgeEffect\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ attribute of the scrollable child component to \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_None\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_. For example, if a \_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_ is nested in the \_\_\_HTML\_TAG\_DESC\_USD\_16\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_17\_\_\_ component, \_\_\_HTML\_TAG\_DESC\_USD\_18\_\_\_edgeEffect\_\_\_HTML\_TAG\_DESC\_USD\_19\_\_\_ of the \_\_\_HTML\_TAG\_DESC\_USD\_20\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_21\_\_\_ must be set to \_\_\_HTML\_TAG\_DESC\_USD\_22\_\_\_EdgeEffect.None\_\_\_HTML\_TAG\_DESC\_USD\_23\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_24\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void--><!--Device-unnamed-export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xOffset | double | Yes | Horizontal offset per frame during scrolling. A positive offset indicates scrolling to the left, and a negative offset indicates scrolling to the right. \_\_\_HTML\_TAG\_USD\_0\_\_\_Unit: vp.  |
| yOffset | double | Yes | Vertical offset per frame during scrolling. A positive offset indicates scrolling upward, and a negative offset indicates scrolling downward. \_\_\_HTML\_TAG\_USD\_0\_\_\_Unit: vp.  |
| scrollState | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Current scrolling state.  |

