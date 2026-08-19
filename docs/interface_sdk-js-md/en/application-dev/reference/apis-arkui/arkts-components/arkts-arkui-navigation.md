# Navigation

The **Navigation** component is the root view container for navigation. It typically functions as the root container of a page and includes a title bar, content area, and toolbar. The content area switches between the home page content (child components of **Navigation**) and non-home page content (child components of NavDestination) through routing. > **NOTE** > - Since API version 11, this component supports the safe area attribute by default, with the default attribute > value being > **expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])**. > You can override this attribute to change the default behavior. In earlier versions, you need to use the > expandSafeArea attribute to implement the safe area feature. > > - When [NavBar](arkts-arkui-navbar-t.md) is nested within a **Navigation** component, the lifecycle of the inner > **NavDestination** component does not synchronize with the outer **NavDestination** component or the lifecycle of a > modal. > > - If the title and subTitle are not set > and hideBackButton is set to **true**, the title bar is not displayed. > > - During subpage navigation within **Navigation**, the new page actively requests focus. > > - You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

## Child Components Supported Since API version 9, it is recommended that this component be used together with the NavRouter component. Since API version 10, it is recommended that this component be used together with the [NavPathStack](arkts-arkui-navpathstack-c.md) component and navDestination attribute for page routing.

## Navigation

```TypeScript
Navigation()
```

Creates a root view container for route navigation, suitable for page routing using the NavRouter component.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(): NavigationAttribute--><!--Device-NavigationInterface-(): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack)
```

Binds a navigation controller to the **Navigation** component, suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md) with the navDestination attribute.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes | Navigation controller object. |

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)
```

Binds a routing stack to the **Navigation** component and specifies a **NavDestination** component as the navigation page (home page) for **Navigation**. This is suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md) with the navDestination attribute or the system routing table. For the usage example, see [Example 16: Using NavDestination as a Navigation Page in Navigation](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#example-16-using-navdestination-as-a-navigation-page-in-navigation).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes | Information about the routing stack. |
| homeDestination | [HomePathInfo](arkts-arkui-homepathinfo-i.md) | Yes | Home page **NavDestination** information. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [HomePathInfo](arkts-arkui-homepathinfo-i.md) | Defines the home page **NavDestination** information. |
| [MoreButtonOptions](arkts-arkui-morebuttonoptions-i.md) | Defines the options for the more button menu. |
| [NavContentInfo](arkts-arkui-navcontentinfo-i.md) | Provides the destination information. |
| [NavigationAnimatedTransition](arkts-arkui-navigationanimatedtransition-i.md) | Defines the custom transition animation protocol. You need to implement this protocol to define the redirection animation of the navigation route. |
| [NavigationCommonTitle](arkts-arkui-navigationcommontitle-i.md) | Defines a general title for the **Navigation** component. |
| [NavigationConfiguration](arkts-arkui-navigationconfiguration-i.md) | Navigation configuration options. |
| [NavigationCustomTitle](arkts-arkui-navigationcustomtitle-i.md) | Defines a custom title for the **Navigation** component. |
| [NavigationDividerStyle](arkts-arkui-navigationdividerstyle-i.md) | Color of the navigation divider and the upper and lower margins of the **Navigation** component. |
| [NavigationInterception](arkts-arkui-navigationinterception-i.md) | Describes the object to be intercepted during navigation redirection. |
| [NavigationMenuOptions](arkts-arkui-navigationmenuoptions-i.md) | Defines options for menu items in the upper right corner of the page. |
| [NavigationOptions](arkts-arkui-navigationoptions-i.md) | Defines the routing stack operation options. |
| [NavigationToolbarOptions](arkts-arkui-navigationtoolbaroptions-i.md) | Defines the toolbar options. |
| [NavigationTransitionProxy](arkts-arkui-navigationtransitionproxy-i.md) | Implements a custom transition animation proxy. |
| [PopInfo](arkts-arkui-popinfo-i.md) | Provides the callback information returned when a page is popped out of the routing stack. |
| [PreloadOptions](arkts-arkui-preloadoptions-i.md) | Indicates options for preloading a page. |
| [ScrollEffectOptions](arkts-arkui-scrolleffectoptions-i.md) | Defines the scroll effect options for the title bar. |

### Types

| Name | Description |
| --- | --- |
| [InterceptionCallback](arkts-arkui-interceptioncallback-t.md) | Defines the callback triggered before a navigation page is redirected. |
| [InterceptionModeCallback](arkts-arkui-interceptionmodecallback-t.md) | Implements an interception callback invoked when the display mode of the **Navigation** component switches between single-column and split-column. |
| [InterceptionShowCallback](arkts-arkui-interceptionshowcallback-t.md) | Represents the interception callback invoked before and after page redirection. |
| [Material](arkts-arkui-material-t.md) | Import the Material type for Navigation. |
| [NavBar](arkts-arkui-navbar-t.md) | Defines the name of the navigation home page. |
| [SystemBarStyle](arkts-arkui-systembarstyle-t.md) | Describes the properties of the status bar. These properties are valid for the page-level status bar. |

### Enums

| Name | Description |
| --- | --- |
| [BarStyle](arkts-arkui-barstyle-e.md) | Enumerates the layout styles of the title bar and toolbar. Note that this API is not supported for the toolbar in **NavDestination**. |
| [LaunchMode](arkts-arkui-launchmode-e.md) | Enumerates the operation modes for the routing stack. |
| [NavBarPosition](arkts-arkui-navbarposition-e.md) | Position of the navigation page. |
| [NavigationMode](arkts-arkui-navigationmode-e.md) | Display mode of the navigation page. When **Navigation** is displayed in split-column mode, a divider is displayed between the navigation page and the content area. &gt; **NOTE：**&gt; &gt; For simplicity, **calcNavBarWidth** is defined as follows: Component width �C minContentWidth �C Divider width (1 px) **Table 1** Relationship between actual navBarWidth and the developer-defined value | Developer-defined navBarWidth| calcNavBarWidth Value| Actual navBarWidth| | --- | --- | --- | | navBarWidth &lt; minNavBarWidth | NA | minNavBarWidth | | navBarWidth &gt; maxNavBarWidth | calcNavBarWidth &gt; maxNavBarWidth | maxNavBarWidth | | navBarWidth &gt; maxNavBarWidth | calcNavBarWidth &lt; minNavBarWidth | minNavBarWidth | | navBarWidth &gt; maxNavBarWidth | minNavBarWidth �� calcNavBarWidth �� maxNavBarWidth | calcNavBarWidth | | minNavBarWidth �� navBarWidth �� maxNavBarWidth | calcNavBarWidth �� minNavBarWidth | minNavBarWidth | | minNavBarWidth �� navBarWidth �� maxNavBarWidth | minNavBarWidth &lt; calcNavBarWidth &lt;= navBarWidth | calcNavBarWidth | | minNavBarWidth �� navBarWidth �� maxNavBarWidth | calcNavBarWidth &gt; navBarWidth | navBarWidth | |
| [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Enumerates the page redirection types. |
| [NavigationTitleMode](arkts-arkui-navigationtitlemode-e.md) | Enumerates the display modes of the title bar. |
| [ScrollEffectType](arkts-arkui-scrolleffecttype-e.md) | Enumerates the scroll effect types. |
| [ToolbarItemStatus](arkts-arkui-toolbaritemstatus-e.md) | Enumerates the toolbar item states. |

