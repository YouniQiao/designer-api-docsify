# TextPicker

**TextPicker** is a component that allows users to select text, images, or hybrid content through scrolling. It supports three usage modes: single-column picker, multi-column independent picker, and multi-column cascading picker. > **NOTE** > - Avoid changing the attribute data during the animation process of this component. > > - The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default > number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system > configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, > use **$r('sys.float.ohos_id_picker_show_count_landscape')**. > > - Multi-column independent pickers and multi-column cascading pickers are collectively referred to as multi-column > pickers in this document. Child Components Not supported

## TextPicker

```TypeScript
TextPicker(options?: TextPickerOptions)
```

Creates a text picker based on the specified data list.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerInterface-(options?: TextPickerOptions): TextPickerAttribute--><!--Device-TextPickerInterface-(options?: TextPickerOptions): TextPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextPickerOptions](arkts-arkui-textpickeroptions-i.md) | No | Parameters of the text picker. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [DividerOptions](arkts-arkui-divideroptions-i.md) | Define the divider configuration options. |
| [PickerBackgroundStyle](arkts-arkui-pickerbackgroundstyle-i.md) | Defines the background style configuration for selected picker items. |
| [TextCascadePickerRangeContent](arkts-arkui-textcascadepickerrangecontent-i.md) | Defines the content for multi-column picker options. |
| [TextPickerDialogOptions](arkts-arkui-textpickerdialogoptions-i.md) | Defines the TextPickerDialogOptions for Text Picker Dialog. |
| [TextPickerDialogOptionsExt](arkts-arkui-textpickerdialogoptionsext-i.md) | Defines the TextPickerDialogOptionsExt for Text Picker Dialog. |
| [TextPickerOptions](arkts-arkui-textpickeroptions-i.md) | Defines the configuration options of the text picker. |
| [TextPickerRangeContent](arkts-arkui-textpickerrangecontent-i.md) | Defines the content for single-column picker options. |
| [TextPickerResult](arkts-arkui-textpickerresult-i.md) | Defines the struct of TextPickerResult. |
| [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md) | Defines the text style options for the text picker. Inherits from PickerTextStyle. |

### Types

| Name | Description |
| --- | --- |
| [OnTextPickerChangeCallback](arkts-arkui-ontextpickerchangecallback-t.md) | Defines the **onChange** event callback signature. |
| [TextPickerEnterSelectedAreaCallback](arkts-arkui-textpickerenterselectedareacallback-t.md) | Defines the **onEnterSelectedArea** event callback signature. |
| [TextPickerScrollStopCallback](arkts-arkui-textpickerscrollstopcallback-t.md) | Defines the **onScrollStop** event callback signature. |

