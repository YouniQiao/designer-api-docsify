# Refresh

The **Refresh** component is a container that provides the pull-to-refresh feature.
> **NOTE**>> - This component is supported since API version 8. Updates will be marked with a superscript to indicate their> earliest API version.>> - Since API version 12, this component provides linkage with a vertically scrolling Swiper and> [Web](../../../reference/apis-arkui/arkui-js/js-components-basic-web.md) components. When the> loop attribute of Swiper is set to **true**, the **Refresh**> component cannot provide linkage with Swiper.>> - When the **Refresh** component is nested with a List component whose content size is smaller than> the component itself, and there are other components in between, gestures may be intercepted by the intermediate> components, preventing the pull-to-refresh effect. In such cases, set the [alwaysEnabled](arkts-arkui-edgeeffectoptions-i.md)> parameter to **true** to allow List to respond to gestures and drive the **Refresh** component> through nested scrolling for the pull-to-refresh effect. For details, see> [Example 9: Implementing Pull-to-Refresh in the Non-Full-Screen Scenario](../../../reference/apis-arkui/arkui-ts/ts-container-refresh.md#example-9-implementing-pull-to-refresh-in-the-non-full-screen-scenario).>> - The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add> custom gestures, refer to Gesture Blocking Enhancement.>> - Pull-to-refresh cannot be triggered by mouse click-and-drag operations.

## Child Components

This component supports only one child component.Since API version 11, this component's child component moves down with the pull-down gesture.

## Refresh

```TypeScript
Refresh(value: RefreshOptions)
```

Creates a **Refresh** container.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RefreshOptions](arkts-arkui-refreshoptions-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
