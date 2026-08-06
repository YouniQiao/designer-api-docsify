# NavDestination

**NavDestination** is the root container of a destination page and represents the content area of the
[Navigation]{@link navigation} component.

> **NOTE**

> - Since API version 11, this component supports the safe area attribute by default, with the default attribute
> value being **expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])**. You can override
> this attribute to change the default behavior. In earlier versions, you need to use the
> [expandSafeArea]{@link common} attribute to implement the safe area feature.
>
> - The **NavDestination** component must be used in conjunction with the **Navigation** component to act as the root
> node for the navigation destination page. When used alone, it can only function as a standard container component
> and does not possess any routing-related attributes or capabilities.
>
> - If the lifecycle of an intermediate page in the routing stack changes, the lifecycle callbacks (**onWillShow**,
> **onShown**, **onHidden**, **onWillDisappear**) of the top **NavDestination** in the stack both before and after
> the navigation will be triggered last in the sequence.
>
> - If no main title or subtitle is set for **NavDestination** and there is no back button, the title bar is not
> displayed.
>
> - Avoid setting layout-related attributes such as the position and size. They may result in display issues on the
> page. For example, do not apply the [zIndex]{@link CommonMethod#zIndex} attribute to a **NavDestination**
> component. This will override the system-defined stacking order and may cause display anomalies.

## Child Components

    **NOTE**  
    
    - Allowed child component types: built-in and custom components, including rendering control types (  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, and  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_).  
    
    - Number of child components: multiple.

## NavDestination

```TypeScript
NavDestination()
```

Creates the root container for a subpage in [Navigation]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavDestinationInterface-(): NavDestinationAttribute--><!--Device-NavDestinationInterface-(): NavDestinationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

