# NavRouter

The **NavRouter** component provides default processing logic for responding to clicks, eliminating the need for manual logic definition.
> **NOTE**>> This component is deprecated since API version 13. You are advised to use [NavPathStack](arkts-arkui-navpathstack-c.md) in> conjunction with the **navDestination** attribute for page routing.

## Child Components

This component must contain two child components, the second of which must be NavDestination.

> **NOTE：**&gt;
> 1. If there is only one child component, the navigation to the **NavDestination** component does not work.&gt;
> 2. If there is only the **NavDestination** child component, the navigation does not work.&gt;
> 3. If there are more than two child components, the excess child components are not displayed.&gt;
> 4. If the second child component is not **NavDestination**, the navigation does not work.

## NavRouter

```TypeScript
NavRouter()
```

Constructor.

**Since:** 9

**Deprecated since:** 13

**Substitutes:** [NavDestinationAttribute](arkts-arkui-navdestination-attribute.md#navdestinationattribute)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NavRouter

```TypeScript
NavRouter(value: RouteInfo)
```

Provides route information so that clicking the **NavRouter** component redirects the user to the specified navigation destination page.

**Since:** 10

**Deprecated since:** 13

**Substitutes:** [NavPathInfo](arkts-arkui-navpathinfo-c.md)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RouteInfo](arkts-arkui-routeinfo-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
