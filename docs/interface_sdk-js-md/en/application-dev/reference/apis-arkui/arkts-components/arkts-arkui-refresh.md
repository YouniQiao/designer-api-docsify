# Refresh

The **Refresh** component is a container that provides the pull-to-refresh feature. > **NOTE** > > - This component is supported since API version 8. Updates will be marked with a superscript to indicate their > earliest API version. > > - Since API version 12, this component provides linkage with a vertically scrolling Swiper and > [Web](../../../reference/apis-arkui/arkui-js/js-components-basic-web.md) components. When the > loop attribute of Swiper is set to **true**, the **Refresh** > component cannot provide linkage with Swiper. > > - When the **Refresh** component is nested with a List component whose content size is smaller than > the component itself, and there are other components in between, gestures may be intercepted by the intermediate > components, preventing the pull-to-refresh effect. In such cases, set the alwaysEnabled > parameter to **true** to allow List to respond to gestures and drive the **Refresh** component > through nested scrolling for the pull-to-refresh effect. For details, see > [Example 9: Implementing Pull-to-Refresh in the Non-Full-Screen Scenario](../../../reference/apis-arkui/arkui-ts/ts-container-refresh.md#example-9-implementing-pull-to-refresh-in-the-non-full-screen-scenario). > > - The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add > custom gestures, refer to Gesture Blocking Enhancement. > > - Pull-to-refresh cannot be triggered by mouse click-and-drag operations.

## Child Components This component supports only one child component. Since API version 11, this component's child component moves down with the pull-down gesture.

## Refresh

```TypeScript
Refresh(value: RefreshOptions)
```

Creates a **Refresh** container.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RefreshInterface-(value: RefreshOptions): RefreshAttribute--><!--Device-RefreshInterface-(value: RefreshOptions): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RefreshOptions](arkts-arkui-refreshoptions-i.md) | Yes | Parameters of the **Refresh** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RefreshOptions](arkts-arkui-refreshoptions-i.md) | Defines the options of the **Refresh** component. > **Supplementary Notes** > > - If neither **builder** nor **refreshingContent** is set, the pull-down displacement effect is implemented by > adjusting the translate attribute of the child component. > During the pull-down process, the > onAreaChange event of the child > component is not triggered, and any changes made to the > translate attribute of the child component do not take > effect. > > - When **builder** or **refreshingContent** is set, the pull-down displacement effect is implemented by adjusting > the position of the child component relative to the **Refresh** component. During the pull-down process, the > onAreaChange event of the child > component can be triggered. However, if the position attribute is set for the child > component, the position of the child component relative to the **Refresh** component is fixed, preventing the child > component from moving down with the pull gesture. > > - If the width and height of a custom component set by **builder** are not specified, its dimensions will adapt to > the child components. If the width is specified but the height is not, the height of the component is automatically > adjusted according to the pull-down distance. If a custom component set by **refreshingContent** does not have a > specified height, its height will also adapt to the pull-down distance. In such cases, as the pull-down distance > increases, the height of the custom component will increase accordingly. When the custom component's height is set > to a fixed value or reaches its maximum height limit, further increases in the pull-down distance will cause the > spacing between the custom component and the top boundary of the **Refresh** component to widen. |

### Enums

| Name | Description |
| --- | --- |
| [RefreshStatus](arkts-arkui-refreshstatus-e.md) | Enumerates the states of a refresh operation. |

