# UIPickerComponent

The **UIPickerComponent** container is used to implement user selection operations. It supports single selection from a limited set of options and can be applied to various scenarios such as time selection, date selection, region selection, and status selection. Its display effect is a three-dimensional wheel style, supporting customizable options including text type, image type, and text-image combination type. NOTE - The height of the **UIPickerComponent** container options is fixed at 40 vp, and a maximum of seven options can be displayed. Due to the three-dimensional wheel display effect, options other than the selected one will be rotated at different angles, so the actual visible height will be less than 40 vp. - It is recommended that the height of the **UIPickerComponent** container be set to 200 vp. When the set height is greater than or equal to this recommended value, all 7 options can be fully displayed. Otherwise, the display area will be cropped from the top and bottom edges towards the center, and the number of displayed options will be reduced accordingly, always keeping the selected item vertically centered. - When the **UIPickerComponent** container's width is not set, the maximum width of the visible child components in the current view is taken as the container width. You are advised to set the width of the **UIPickerComponent** container or set the same width for each child component to avoid dynamic changes in container width during sliding, which affects the display effect. - The alignment mode of child components in the **UIPickerComponent** container is fixed to center alignment, and cannot be changed via the align attribute. - Currently, the **UIPickerComponent** container does not support wearables. - This component supports WithTheme since API version 26.0.0. Child Components - Multiple child components are supported. - Supported child component types: Text, Image, Row, and SymbolGlyph - Supported rendering control types: [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) and [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md) NOTE - When the Row **container** is used as a child component, the **Row** container can contain only the **Text**, **Image**, and **SymbolGlyph** basic components. Including other container components may affect the display effect or cause sliding functionality abnormalities. - When counting the number of child components, the **Row** container and its child components are counted as one child component. - When the child component is **Text**, **Image**, or **SymbolGlyph**, the height attribute does not take effect and is fixed at 40 vp. - When the child component is a **Row** container, its height attribute does not take effect and is fixed at 40 vp. The height attribute of the child components in the **Row** container takes effect. The final display effect is determined by the **Row** container. - The text-image combination option requires that the **Row** container contain the **Text** and **Image** components. When using the text-image combination option, you are advised to set the image's height to 40 vp or below to avoid cropping when images are large. - The **fontSize** attribute of all text components (including the **Text** components in the **Row** container) in the **UIPickerComponent** container is 20 fp by default. User settings will override the default value, and abnormal values will be processed according to the result of handling the text component's fontSize. You are advised to set the **fontSize** attribute to a unified value or not to set it to ensure a good display effect.

## UIPickerComponent

```TypeScript
UIPickerComponent(options?: UIPickerComponentOptions)
```

Creates a **UIPickerComponent** container, whose selected item is determined by the **selectedIndex** attribute in the **options** parameter.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentInterface-(options?: UIPickerComponentOptions): UIPickerComponentAttribute--><!--Device-UIPickerComponentInterface-(options?: UIPickerComponentOptions): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UIPickerComponentOptions](arkts-arkui-uipickercomponentoptions-i.md) | No | Parameters of the **UIPickerComponent** container. If the parameter is left empty, the component is a placeholder but the content is empty. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PickerIndicatorStyle](arkts-arkui-pickerindicatorstyle-i.md) | Sets parameters of the selected item indicator style. |
| [UIPickerComponentOptions](arkts-arkui-uipickercomponentoptions-i.md) | Describes the parameters of the **UIPickerComponent** container. |

### Types

| Name | Description |
| --- | --- |
| [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) | Defines the callback types for the [onChange](arkts-arkui-uipickercomponent-attribute.md#onchange) and [onScrollStop](arkts-arkui-uipickercomponent-attribute.md#onscrollstop) events. Value range: an integer in the range of [0, Number of child components – 1]. |

### Enums

| Name | Description |
| --- | --- |
| [PickerIndicatorType](arkts-arkui-pickerindicatortype-e.md) | Enumerates the types of the selected item indicator. |

