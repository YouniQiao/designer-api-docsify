# Navigation

The **Navigation** component is the root view container for navigation. It typically functions as the root container of a page and includes a title bar, content area, and toolbar. The content area switches between the home page content (child components of **Navigation**) and non-home page content (child components of NavDestination) through routing. > **NOTE** > - Since API version 11, this component supports the safe area attribute by default, with the default attribute > value being > **expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])**. > You can override this attribute to change the default behavior. In earlier versions, you need to use the > [expandSafeArea](arkts-arkui-commonmethod-c.md#expandSafeArea) attribute to implement the safe area feature. > > - When [NavBar](arkts-arkui-navbar-t.md#NavBar) is nested within a **Navigation** component, the lifecycle of the inner > **NavDestination** component does not synchronize with the outer **NavDestination** component or the lifecycle of a > modal. > > - If the title and subTitle are not set > and hideBackButton is set to **true**, the title bar is not displayed. > > - During subpage navigation within **Navigation**, the new page actively requests focus. > > - You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

## Child Components Supported Since API version 9, it is recommended that this component be used together with the NavRouter component. Since API version 10, it is recommended that this component be used together with the [NavPathStack](arkts-arkui-navpathstack-c.md#NavPathStack) component and navDestination attribute for page routing.

## Navigation

```TypeScript
Navigation()
```

Creates a root view container for route navigation, suitable for page routing using the NavRouter component.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(): NavigationAttribute--><!--Device-NavigationInterface-(): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack)
```

Binds a navigation controller to the **Navigation** component, suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md#NavPathStack) with the navDestination attribute.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes |

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)
```

Binds a routing stack to the **Navigation** component and specifies a **NavDestination** component as the navigation page (home page) for **Navigation**. This is suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md#NavPathStack) with the navDestination attribute or the system routing table. For the usage example, see [Example 16: Using NavDestination as a Navigation Page in Navigation](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#example-16-using-navdestination-as-a-navigation-page-in-navigation).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute--><!--Device-NavigationInterface-(pathInfos: NavPathStack, homeDestination: HomePathInfo): NavigationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes |
| homeDestination | [HomePathInfo](arkts-arkui-homepathinfo-i.md) | Yes |

## Summary

- [HomePathInfo](arkts-arkui-homepathinfo-i.md)
- [MoreButtonOptions](arkts-arkui-morebuttonoptions-i.md)
- [NavContentInfo](arkts-arkui-navcontentinfo-i.md)
- [NavigationAnimatedTransition](arkts-arkui-navigationanimatedtransition-i.md)
- [NavigationCommonTitle](arkts-arkui-navigationcommontitle-i.md)
- [NavigationConfiguration](arkts-arkui-navigationconfiguration-i.md)
- [NavigationCustomTitle](arkts-arkui-navigationcustomtitle-i.md)
- [NavigationDividerStyle](arkts-arkui-navigationdividerstyle-i.md)
- [NavigationInterception](arkts-arkui-navigationinterception-i.md)
- [NavigationMenuOptions](arkts-arkui-navigationmenuoptions-i.md)
- [NavigationOptions](arkts-arkui-navigationoptions-i.md)
- [NavigationToolbarOptions](arkts-arkui-navigationtoolbaroptions-i.md)
- [NavigationTransitionProxy](arkts-arkui-navigationtransitionproxy-i.md)
- [PopInfo](arkts-arkui-popinfo-i.md)
- [PreloadOptions](arkts-arkui-preloadoptions-i.md)
- [ScrollEffectOptions](arkts-arkui-scrolleffectoptions-i.md)
- [InterceptionCallback](arkts-arkui-interceptioncallback-t.md)
- [InterceptionModeCallback](arkts-arkui-interceptionmodecallback-t.md)
- [InterceptionShowCallback](arkts-arkui-interceptionshowcallback-t.md)
- [Material](arkts-arkui-material-t.md)
- [NavBar](arkts-arkui-navbar-t.md)
- [SystemBarStyle](arkts-arkui-systembarstyle-t.md)
- [BarStyle](arkts-arkui-barstyle-e.md)
- [LaunchMode](arkts-arkui-launchmode-e.md)
- [NavBarPosition](arkts-arkui-navbarposition-e.md)
- [NavigationMode](arkts-arkui-navigationmode-e.md)
- [NavigationOperation](arkts-arkui-navigationoperation-e.md)
- [NavigationTitleMode](arkts-arkui-navigationtitlemode-e.md)
- [ScrollEffectType](arkts-arkui-scrolleffecttype-e.md)
- [ToolbarItemStatus](arkts-arkui-toolbaritemstatus-e.md)
