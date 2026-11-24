# OnGetPreviewBadgeCallback

```TypeScript
declare type OnGetPreviewBadgeCallback = () => boolean | number
```

Called to obtain the number of selected items when the animation for gathering selected items upon long press is about to start.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-declare type OnGetPreviewBadgeCallback = () => boolean | number--><!--Device-unnamed-declare type OnGetPreviewBadgeCallback = () => boolean | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean &#124; number | Whether to display a badge showing the count of selected items on the menu preview image after the animation for gathering selected items upon long press is played, or the specific number to display. <br>**true**: The number of selected items in a **Grid** or **List** component will be displayed as the badge. **false**: The badge is not displayed. <br>If a number is returned, it will be displayed as the badge by default. Value range: [0, 2<sup>31</sup>-1]. If the value is out of the range, it is treated as **true**. <br>If a floating-point number is returned, it is rounded down. |
