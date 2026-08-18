# NavDestination

**NavDestination** is the root container of a destination page and represents the content area of the Navigation component. > **NOTE** > - Since API version 11, this component supports the safe area attribute by default, with the default attribute > value being **expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])**. You can override > this attribute to change the default behavior. In earlier versions, you need to use the > expandSafeArea attribute to implement the safe area feature. > > - The **NavDestination** component must be used in conjunction with the **Navigation** component to act as the root > node for the navigation destination page. When used alone, it can only function as a standard container component > and does not possess any routing-related attributes or capabilities. > > - If the lifecycle of an intermediate page in the routing stack changes, the lifecycle callbacks (**onWillShow**, > **onShown**, **onHidden**, **onWillDisappear**) of the top **NavDestination** in the stack both before and after > the navigation will be triggered last in the sequence. > > - If no main title or subtitle is set for **NavDestination** and there is no back button, the title bar is not > displayed. > > - Avoid setting layout-related attributes such as the position and size. They may result in display issues on the > page. For example, do not apply the zIndex attribute to a **NavDestination** > component. This will override the system-defined stacking order and may cause display anomalies.

## Child Components > **NOTE** > > - Allowed child component types: built-in and custom components, including rendering control types ( > [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), and > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)). > > - Number of child components: multiple.

## NavDestination

```TypeScript
NavDestination()
```

Creates the root container for a subpage in Navigation.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavDestinationInterface-(): NavDestinationAttribute--><!--Device-NavDestinationInterface-(): NavDestinationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [NavDestinationCommonTitle](arkts-arkui-navdestinationcommontitle-i.md) | Defines a general title for the **NavDestination** component. |
| [NavDestinationContext](arkts-arkui-navdestinationcontext-i.md) | Defines the context information for the **NavDestination** component. |
| [NavDestinationCustomTitle](arkts-arkui-navdestinationcustomtitle-i.md) | Defines a custom title for the **NavDestination** component. |
| [NavDestinationTransition](arkts-arkui-navdestinationtransition-i.md) | Defines a custom transition animation for the **NavDestination** component. |
| [NestedScrollInfo](arkts-arkui-nestedscrollinfo-i.md) | Provides the information about the nested scrollable containers. |
| [RouteMapConfig](arkts-arkui-routemapconfig-i.md) | Defines the routing configuration. |

### Types

| Name | Description |
| --- | --- |
| [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) | Defines the delegate function for custom transition animations of the **NavDestination** component. |
| [Orientation](arkts-arkui-orientation-t.md) | Defines an instance object of the Orientation type. |
| [RestoreStateCallback](arkts-arkui-restorestatecallback-t.md) | Custom page state restore callback. |
| [SaveStateCallback](arkts-arkui-savestatecallback-t.md) | Custom page state save callback. |

### Enums

| Name | Description |
| --- | --- |
| [NavDestinationActiveReason](arkts-arkui-navdestinationactivereason-e.md) | Enumerates reasons for the activation state changes of the **NavDestination** component. |
| [NavDestinationMode](arkts-arkui-navdestinationmode-e.md) | Mode of the **NavDestination** component. |
| [NavigationSystemTransitionType](arkts-arkui-navigationsystemtransitiontype-e.md) | Type of the system transition animation. > **NOTE：**> System transition animations for the title bar and content area can be configured separately. > The system transition animation of the title bar is only available for the push and pop animations of navigation > destination pages in STANDARD mode, with the following constraints: > When **NONE** or **TITLE** is set, no system transition animation is displayed. When **CONTENT** or **DEFAULT** is > set, the system transition animation is displayed by default. |
| [VisibilityChangeReason](arkts-arkui-visibilitychangereason-e.md) | Enumerates reasons for **NavDestination** visibility changes. |

