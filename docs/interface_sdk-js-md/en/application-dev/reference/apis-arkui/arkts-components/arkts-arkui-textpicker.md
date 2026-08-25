# TextPicker

**TextPicker** is a component that allows users to select text, images, or hybrid content through scrolling. It supports three usage modes: single-column picker, multi-column independent picker, and multi-column cascading picker.
> **NOTE**
> - Avoid changing the attribute data during the animation process of this component.>> - The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default> number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system> configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode,> use **$r('sys.float.ohos_id_picker_show_count_landscape')**.>> - Multi-column independent pickers and multi-column cascading pickers are collectively referred to as multi-column> pickers in this document.
Child Components
Not supported

## TextPicker

```TypeScript
TextPicker(options?: TextPickerOptions)
```

Creates a text picker based on the specified data list.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TextPickerOptions](arkts-arkui-textpickeroptions-i.md) | No |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnTextPickerChangeCallback](arkts-arkui-ontextpickerchangecallback-t.md) |
| [TextPickerEnterSelectedAreaCallback](arkts-arkui-textpickerenterselectedareacallback-t.md) |
| [TextPickerScrollStopCallback](arkts-arkui-textpickerscrollstopcallback-t.md) |
