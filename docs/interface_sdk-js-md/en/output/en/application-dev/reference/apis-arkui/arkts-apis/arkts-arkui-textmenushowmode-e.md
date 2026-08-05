# TextMenuShowMode

Enumerates the text menu display modes.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

<!--Device-unnamed-declare enum TextMenuShowMode--><!--Device-unnamed-declare enum TextMenuShowMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

The menu is displayed in the current window.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

<!--Device-TextMenuShowMode-DEFAULT = 0--><!--Device-TextMenuShowMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PREFER_WINDOW

```TypeScript
PREFER_WINDOW = 1
```

The menu is preferentially displayed in a separate window. If a separate window is not supported, the menu is displayed in the current window. **NOTE** Displaying the text selection menu in a separate window is not supported for window types other than the app main window, app sub-window, system modal window, and system desktop window. Displaying the text selection menu in a separate window is not supported in the previewer. Displaying the text selection menu in a separate window is not supported in [UIExtension]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. When a text component is displayed in a child window of [Popup]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [Dialog]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, or [Menu]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, the corresponding text selection menu cannot be displayed in a separate window. When **autoFill** is available for **TextInput** or **TextArea**, the corresponding text selection menu cannot be displayed in a separate window.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 16.

<!--Device-TextMenuShowMode-PREFER_WINDOW = 1--><!--Device-TextMenuShowMode-PREFER_WINDOW = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

