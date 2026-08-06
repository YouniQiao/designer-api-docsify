# Menu

The **Menu** component is a vertical list of items presented to the user.

> **NOTE**
>
> - This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate 
> their 
>
> - The **Menu** component must be used together with the 
> [bindMenu]{@link CommonMethod#bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions)} or 
> [bindContextMenu]{@link CommonMethod#bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions)}
> method. It does not work when used alone.

## Child Components

This component contains the [MenuItem]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and [MenuItemGroup]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ child components.

## Menu

```TypeScript
Menu()
```

Creates a fixed container for a menu. This API does not have any parameters.
    **NOTE**  
    
    - Rules for calculating the width of menus and menu items:  
        
        - During the layout, the width of each menu item is expected to be the same. If a child component has its  
    width set, the [size calculation rule]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ prevails.  
        
        - If no width is set for the **Menu** component, it applies a default two-column width to the **MenuItem**  
    and **MenuItemGroup** child components. If a menu item's content area exceeds the two-column width, the  
    **Menu** component automatically expands the menu item's content area.  
        
        - When an explicit width is set for the **Menu** component, its child components **MenuItem** and  
    **MenuItemGroup** adopt a fixed width (equal to the **Menu** component's configured width minus the padding).  
        
        - The minimum width is 64 vp.  
    
    - Universal attributes unsupported by **Menu**: [outline]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ attributes and the  
    [shadow]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuInterface-(): MenuAttribute--><!--Device-MenuInterface-(): MenuAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

