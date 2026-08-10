# textPicker

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [DividerOptions](arkts-arkui-textpicker-divideroptions-i.md) | 分割线的信息。 |
| [PickerBackgroundStyle](arkts-arkui-textpicker-pickerbackgroundstyle-i.md) | 选择器选中项的背景样式，包括选中项的背景颜色和边框圆角半径。 |
| [TextCascadePickerRangeContent](arkts-arkui-textpicker-textcascadepickerrangecontent-i.md) | 多列联动数据选择器的数据选项内容。 |
| [TextPickerDialogOptions](arkts-arkui-textpicker-textpickerdialogoptions-i.md) | 文本选择器弹窗的参数继承自[TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md)。  默认值： { color: \\$r('sys.color.comp_background_tertiary'), borderRadius: \\$r('sys.float.corner_radius_level12') } |
| [TextPickerDialogOptionsExt](arkts-arkui-textpicker-textpickerdialogoptionsext-i.md) | 文本选择器弹窗的参数继承自[TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md)。 |
| [TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md) | 文本选择器的参数说明。 |
| [TextPickerRangeContent](arkts-arkui-textpicker-textpickerrangecontent-i.md) | 单列数据选择器的数据选项内容。 |
| [TextPickerResult](arkts-arkui-textpicker-textpickerresult-i.md) | 文本选择器结果。 |
| [TextPickerTextStyle](arkts-arkui-textpicker-textpickertextstyle-i.md) | 文本样式选项，继承自[PickerTextStyle](arkts-arkui-common-pickertextstyle-i.md)。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [TextPickerDialogOptionsExt](arkts-arkui-textpicker-textpickerdialogoptionsext-i-sys.md) | 文本选择器弹窗的参数继承自[TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md)。 |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [OnTextPickerChangeCallback](arkts-arkui-ontextpickerchangecallback-t.md) | 滑动选中TextPicker文本内容后，触发该回调。当显示文本或图片加文本列表时，选中项的文本值为选中项中的文本值，当显示图片列表时，选中项的文本值为空。 |
| [TextPickerEnterSelectedAreaCallback](arkts-arkui-textpickerenterselectedareacallback-t.md) | 定义触发onEnterSelectedArea事件的回调类型。  在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。 |
| [TextPickerScrollStopCallback](arkts-arkui-textpickerscrollstopcallback-t.md) | 定义触发onScrollStop事件的回调类型。  当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。 |

