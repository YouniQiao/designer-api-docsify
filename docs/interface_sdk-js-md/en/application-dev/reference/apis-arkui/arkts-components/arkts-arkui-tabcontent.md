# TabContent

The **TabContent** component is used only in the **Tabs** component. It corresponds to the content view of a switched tab page.

> **NOTE**

> - By default, the clip attribute of this component is set to **true**. > If you want to extend the content area to the outside of the component, disable the **clip** attribute first.

## Child Components

This component supports only one child component.

> **NOTE：**
> 
> Built-in system and custom components, and rendering control types (
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md),
> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), and
> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)) are supported.

## TabContent

```TypeScript
TabContent()
```

Creates the **TabContent** component, which represents the content associated with a specific tab.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TabContentInterface-(): TabContentAttribute--><!--Device-TabContentInterface-(): TabContentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) | Represents an indicator style object. |
| [LabelStyle](arkts-arkui-labelstyle-i.md) | Represents a style object for the label text and font. |

### Types

| Name | Description |
| --- | --- |
| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | Defines the input parameter object of the **drawable** attribute in the **DrawableTabBarIndicator** object. |

### Enums

| Name | Description |
| --- | --- |

