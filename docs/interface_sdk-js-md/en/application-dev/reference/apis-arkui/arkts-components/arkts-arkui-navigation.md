# Navigation

The **Navigation** component is the root view container for navigation. It typically functions as the root container
of a page and includes a title bar, content area, and toolbar. The content area switches between the home page
content (child components of **Navigation**) and non-home page content (child components of
[NavDestination]{@link nav_destination}) through routing.

> **NOTE**

> - Since API version 11, this component supports the safe area attribute by default, with the default attribute
> value being
> **expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP,
 SafeAreaEdge.BOTTOM])**.
> You can override this attribute to change the default behavior. In earlier versions, you need to use the
> [expandSafeArea]{@link CommonMethod#expandSafeArea} attribute to implement the safe area feature.
>
> - When [NavBar]{@link NavBar} is nested within a **Navigation** component, the lifecycle of the inner
> **NavDestination** component does not synchronize with the outer **NavDestination** component or the lifecycle of a
> [modal]{@link common}.
>
> - If the [title]{@link NavigationAttribute#title} and [subTitle]{@link NavigationAttribute#subTitle} are not set
> and [hideBackButton]{@link NavigationAttribute#hideBackButton} is set to **true**, the title bar is not displayed.
>
> - During subpage navigation within **Navigation**, the new page actively requests focus.
>
> - You are not advised to use stack operations in [aboutToAppear]{@link BaseCustomComponent#aboutToAppear}, as the
> page has not yet finished building at this stage, which may lead to issues such as white screens or navigation
> failures.

## Child Components

Supported

Since API version 9, it is recommended that this component be used together with the [NavRouter]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_component.

Since API version 10, it is recommended that this component be used together with the  
[NavPathStack]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ component and [navDestination]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute for page routing.

## Navigation

```TypeScript
Navigation()
```

Creates a root view container for route navigation, suitable for page routing using the  
[NavRouter]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ component.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(): NavigationAttribute--><!--Device-NavigationInterface-(): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack)
```

Binds a navigation controller to the **Navigation** component, suitable for page routing using  
[NavPathStack]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ with the [navDestination]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ attribute.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Navigation controller object.  |

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)
```

Binds a routing stack to the **Navigation** component and specifies a **NavDestination** component as the navigation page (home page) for **Navigation**. This is suitable for page routing using  
[NavPathStack]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ with the [navDestination]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute or the system routing table. For the usage example, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the routing stack.  |
| homeDestination | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Home page **NavDestination** information.  |

## Summary

