# Navigation

The **Navigation** component is the root view container for navigation. It typically functions as the root container of a page and includes a title bar, content area, and toolbar. The content area switches between the home page content (child components of **Navigation**) and non-home page content (child components of NavDestination) through routing.
> **NOTE**
> - Since API version 11, this component supports the safe area attribute by default, with the default attribute> value being> **expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD, SafeAreaType.CUTOUT], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])**.> You can override this attribute to change the default behavior. In earlier versions, you need to use the> expandSafeArea attribute to implement the safe area feature.>> - When [NavBar](arkts-arkui-navbar-t.md) is nested within a **Navigation** component, the lifecycle of the inner> **NavDestination** component does not synchronize with the outer **NavDestination** component or the lifecycle of a> modal.>> - If the [title](arkts-arkui-navigation-attribute.md#title) and [subTitle](arkts-arkui-navigation-attribute.md#subtitle) are not set> and [hideBackButton](arkts-arkui-navigation-attribute.md#hidebackbutton) is set to **true**, the title bar is not displayed.>> - During subpage navigation within **Navigation**, the new page actively requests focus.>> - You are not advised to use stack operations in aboutToAppear, as the> page has not yet finished building at this stage, which may lead to issues such as white screens or navigation> failures.

## Child Components

Supported Since API version 9, it is recommended that this component be used together with the NavRouter component.Since API version 10, it is recommended that this component be used together with the [NavPathStack](arkts-arkui-navpathstack-c.md) component and [navDestination](arkts-arkui-navigation-attribute.md#navdestination) attribute for page routing.

## Navigation

```TypeScript
Navigation()
```

Creates a root view container for route navigation, suitable for page routing using the NavRouter component.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack)
```

Binds a navigation controller to the **Navigation** component, suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md) with the [navDestination](arkts-arkui-navigation-attribute.md#navdestination) attribute.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes |

## Navigation

```TypeScript
Navigation(pathInfos: NavPathStack, homeDestination: HomePathInfo)
```

Binds a routing stack to the **Navigation** component and specifies a **NavDestination** component as the navigation page (home page) for **Navigation**. This is suitable for page routing using [NavPathStack](arkts-arkui-navpathstack-c.md) with the [navDestination](arkts-arkui-navigation-attribute.md#navdestination) attribute or the system routing table. For the usage example, see [Example 16: Using NavDestination as a Navigation Page in Navigation](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#example-16-using-navdestination-as-a-navigation-page-in-navigation).

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathInfos | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes |
| homeDestination | [HomePathInfo](arkts-arkui-homepathinfo-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InterceptionCallback](arkts-arkui-interceptioncallback-t.md) |
| [InterceptionModeCallback](arkts-arkui-interceptionmodecallback-t.md) |
| [InterceptionShowCallback](arkts-arkui-interceptionshowcallback-t.md) |
| [NavBar](arkts-arkui-navbar-t.md) |
| [SystemBarStyle](arkts-arkui-systembarstyle-t.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
