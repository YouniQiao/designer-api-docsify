# Tabs

The **Tabs** component is a container component that allows users to switch between content views through tabs. Each tab page corresponds to a content view.

> **NOTE** > > - > > - Since API version 11, this component supports the safe area avoidance feature. The default value of the > [expandSafeArea]{} > **expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])**. You can override the default behavior by > rewriting this attribute. For versions earlier than API version 11, you need to manually implement safe area > avoidance together with the **expandSafeArea** attribute.

## Child Components

Only the child component TabContent and rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) and [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md) are supported. You are advised not to use custom components as child components. If **if/else** or **ForEach** is used, only **TabContent** can be used as the child component. You are advised not to use custom components as child components.

> **NOTE：**
> 
> If the child component has the **visibility** attribute set to **None** or **Hidden**, it is hidden but still takes
> up space in the layout.
> 
> When a displayed **Tabs** child component **TabContent** is hidden, it is not destroyed. For details about how to
> implement lazy loading and release on the page, see
> [Example 13](../../../reference/apis-arkui/arkui-ts/ts-container-tabs.md#example-13-implementing-lazy-loading-and-resource-release-of-pages).
> 
> 
> If height is set to **auto** for **Tabs**, the tab height can be
> automatically adjusted based on that of the child component. When width
> is set to **auto**, the tab width can be automatically adjusted based on that of the child component.

## Tabs

```TypeScript
Tabs(options?: TabsOptions)
```

Create a **Tabs** container.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TabsInterface-(options?: TabsOptions): TabsAttribute--><!--Device-TabsInterface-(options?: TabsOptions): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabsoptions-i.md) | No | Options of the **Tabs** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [DividerStyle](arkts-arkui-dividerstyle-i.md) | Describes the divider style. |

### Types

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

