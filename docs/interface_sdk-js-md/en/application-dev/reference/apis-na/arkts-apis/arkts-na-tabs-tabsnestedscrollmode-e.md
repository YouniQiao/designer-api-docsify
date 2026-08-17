# TabsNestedScrollMode

Tabs nested scroll nested mode

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export declare enum TabsNestedScrollMode--><!--Device-unnamed-export declare enum TabsNestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_ONLY

```TypeScript
SELF_ONLY = 0
```

The scrolling is contained within the Tabs component, and no scroll chaining occurs, that is, the parent container does not scroll when the component scrolling reaches the boundary.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsNestedScrollMode-SELF_ONLY = 0--><!--Device-TabsNestedScrollMode-SELF_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_FIRST

```TypeScript
SELF_FIRST = 1
```

The Tabs component scrolls first, and when it hits the boundary, the parent container scrolls.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsNestedScrollMode-SELF_FIRST = 1--><!--Device-TabsNestedScrollMode-SELF_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

