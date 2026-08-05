# LayoutStyle

Declare the layout style of the tab bar items.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum LayoutStyle--><!--Device-unnamed-export declare enum LayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_CENTER

```TypeScript
ALWAYS_CENTER = 0
```

If the tab content exceeds the tab bar width, the tabs are scrollable. If not, the tabs are compactly centered on the tab bar and not scrollable.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-ALWAYS_CENTER = 0--><!--Device-LayoutStyle-ALWAYS_CENTER = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_AVERAGE_SPLIT

```TypeScript
ALWAYS_AVERAGE_SPLIT = 1
```

If the tab content exceeds the tab bar width, the tabs are scrollable. If not, the tabs are not scrollable, and the width of the tab bar is evenly distributed among all tabs.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1--><!--Device-LayoutStyle-ALWAYS_AVERAGE_SPLIT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SPACE_BETWEEN_OR_CENTER

```TypeScript
SPACE_BETWEEN_OR_CENTER = 2
```

If the tab content exceeds the tab bar width, the tabs are scrollable. If the tab content exceeds half the width of the tab bar but is still within the tab bar width, the tabs are compactly centered and not scrollable.If the tab content does not exceed half the width of the tab bar, the tabs are centered within half the width of the tab bar with even spacing between them and are not scrollable.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2--><!--Device-LayoutStyle-SPACE_BETWEEN_OR_CENTER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

