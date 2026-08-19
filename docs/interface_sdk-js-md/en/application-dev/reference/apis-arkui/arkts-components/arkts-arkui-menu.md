# Menu

The **Menu** component is a vertical list of items presented to the user. > **NOTE** > > - This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate > their > > - The **Menu** component must be used together with the > bindMenu or > bindContextMenu > method. It does not work when used alone.

## Child Components This component contains the MenuItem and MenuItemGroup child components.

## Menu

```TypeScript
Menu()
```

Creates a fixed container for a menu. This API does not have any parameters. &gt; **NOTE：**&gt; &gt; - Rules for calculating the width of menus and menu items: &gt; &gt; &gt; &gt; - During the layout, the width of each menu item is expected to be the same. If a child component has its &gt; width set, the size calculation rule prevails. &gt; &gt; &gt; &gt; - If no width is set for the **Menu** component, it applies a default two-column width to the **MenuItem** &gt; and **MenuItemGroup** child components. If a menu item's content area exceeds the two-column width, the &gt; **Menu** component automatically expands the menu item's content area. &gt; &gt; &gt; &gt; - When an explicit width is set for the **Menu** component, its child components **MenuItem** and &gt; **MenuItemGroup** adopt a fixed width (equal to the **Menu** component's configured width minus the padding). &gt; &gt; &gt; &gt; - The minimum width is 64 vp. &gt; &gt; - Universal attributes unsupported by **Menu**: outline attributes and the &gt; shadow attribute

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuInterface-(): MenuAttribute--><!--Device-MenuInterface-(): MenuAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Enums

| Name | Description |
| --- | --- |
| [SubMenuExpandingMode](arkts-arkui-submenuexpandingmode-e.md) | Enumerates the submenu expanding modes. |

