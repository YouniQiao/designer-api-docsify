# EditModeOptions

Define edit mode options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface EditModeOptions--><!--Device-unnamed-export declare interface EditModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableGatherSelectedItemsAnimation

```TypeScript
enableGatherSelectedItemsAnimation?: boolean
```

Define whether to gather selected items in grid or list when item is long pressed for context menu.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditModeOptions-enableGatherSelectedItemsAnimation?: boolean--><!--Device-EditModeOptions-enableGatherSelectedItemsAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableTwoFingerMultiSelect

```TypeScript
enableTwoFingerMultiSelect?: boolean
```

Enable two-finger swipe multi-selection. {@code true} indicates that two-finger swiping can enter edit mode and perform multi-selection. {@code false} indicates that two-finger swiping cannot perform multi-selection.

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditModeOptions-enableTwoFingerMultiSelect?: boolean--><!--Device-EditModeOptions-enableTwoFingerMultiSelect?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onGetPreviewBadge

```TypeScript
onGetPreviewBadge?: OnGetPreviewBadgeCallback
```

Called to return whether to display the number badge or the number displayed on the badge for the context menu preview. If not set, the number of selected items within the display range will be used. Returning false means not displaying the badge. Returning true means using the number of selected items within the display range. Returning a number to include selected items outside the display range.

**Type:** [OnGetPreviewBadgeCallback](arkts-na-ongetpreviewbadgecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditModeOptions-onGetPreviewBadge?: OnGetPreviewBadgeCallback--><!--Device-EditModeOptions-onGetPreviewBadge?: OnGetPreviewBadgeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useDefaultMultiSelectStyle

```TypeScript
useDefaultMultiSelectStyle?: boolean
```

Use default multi-select style. {@code true} indicates that the check box is displayed for GridItem or ListItem after entering the multi-select state. {@code false} indicates that there is no default style after entering the multi-select state.

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditModeOptions-useDefaultMultiSelectStyle?: boolean--><!--Device-EditModeOptions-useDefaultMultiSelectStyle?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

