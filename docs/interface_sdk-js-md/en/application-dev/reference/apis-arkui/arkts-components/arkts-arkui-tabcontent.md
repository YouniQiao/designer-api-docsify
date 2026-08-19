# TabContent

The **TabContent** component is used only in the **Tabs** component. It corresponds to the content view of a switched tab page. > **NOTE** > - By default, the clip attribute of this component is set to **true**. > If you want to extend the content area to the outside of the component, disable the **clip** attribute first.

## Child Components This component supports only one child component. > **NOTE** > > Built-in system and custom components, and rendering control types ( > [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), and > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)) are supported.

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
| [BoardStyle](arkts-arkui-boardstyle-i.md) | Represents a board style object. |
| [DrawableTabBarIndicator](arkts-arkui-drawabletabbarindicator-i.md) | Uses an image resource as the indicator. |
| [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) | Represents an indicator style object. |
| [LabelStyle](arkts-arkui-labelstyle-i.md) | Represents a style object for the label text and font. |
| [TabBarIconStyle](arkts-arkui-tabbariconstyle-i.md) | Represents a label icon style object. |
| [TabBarOptions](arkts-arkui-tabbaroptions-i.md) | Defines the options for configuring images and text content on the tabs. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element &gt; 's @since version number is higher than inner elements'. This does not affect interface usability. |

### Types

| Name | Description |
| --- | --- |
| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | Defines the input parameter object of the **drawable** attribute in the **DrawableTabBarIndicator** object. |

### Enums

| Name | Description |
| --- | --- |
| [LayoutMode](arkts-arkui-layoutmode-e.md) | Enumerates the layout modes of the images and texts on the bottom tabs. |
| [SelectedMode](arkts-arkui-selectedmode-e.md) | Enumerates the display modes of selected subtabs. |

