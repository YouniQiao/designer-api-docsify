# TextMenuShowMode

```TypeScript
declare enum TextMenuShowMode
```

Enumerates the text menu display modes.

**Since:** 16

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

Displayed in the current window.

**Since:** 16

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PREFER_WINDOW

```TypeScript
PREFER_WINDOW = 1
```

Preferentially displayed in a separate window. If a separate window is not supported, it is displayed in the current window.

**NOTE:** 

Except for app main windows, app subwindows, system modal windows, and system desktop windows, other types of windows do not support displaying the text selection menu in a separate window.

The previewer does not support displaying the text selection menu in a separate window.

[UIExtension](arkts-arkui-arkui-uiextension.md) does not support displaying the text selection menu in a separate window.

When a text component is already displayed in a subwindow-type [Popup](arkts-arkui-arkui-advanced-popup.md), [Dialog](arkts-arkui-arkui-advanced-dialog.md), [Toast](../../../ui/arkts-create-toast.md), or [Menu](../arkts-components/arkts-arkui-menu-comp.md#menu), the corresponding text selection menu cannot be displayed in a separate window.

When TextInput and TextArea support triggering AutoFill, the corresponding text selection menu cannot be displayed in a separate window.

**Since:** 16

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
