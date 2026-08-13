# SideBarContainer

The **SideBarContainer** component contains a sidebar and content area as its child components. The sidebar is the first child component and can be shown or hidden as needed. The content area is the second child component. > **NOTE** > The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate > their

## Child Components Supported > **NOTE** > > - Allowed child component types: built-in and custom components, excluding rendering control types ( > [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), and > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)). > > - This component must contain two child components. > > - If there are three or more child components, only the first and second child components are displayed. If there > is only one child component, the sidebar is displayed, and the content area is blank. > > - The focus navigation is performed in the content area and then in the sidebar of the **SideBarContainer** > component.

## SideBarContainer

```TypeScript
SideBarContainer(type?: SideBarContainerType)
```

Creates a sidebar container.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SideBarContainerInterface-(type?: SideBarContainerType): SideBarContainerAttribute--><!--Device-SideBarContainerInterface-(type?: SideBarContainerType): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebarcontainertype-e.md) | No |

## Summary

- [ButtonIconOptions](arkts-arkui-buttoniconoptions-i.md)
- [ButtonStyle](arkts-arkui-buttonstyle-i.md)
- [SideBarContainerType](arkts-arkui-sidebarcontainertype-e.md)
- [SideBarPosition](arkts-arkui-sidebarposition-e.md)
