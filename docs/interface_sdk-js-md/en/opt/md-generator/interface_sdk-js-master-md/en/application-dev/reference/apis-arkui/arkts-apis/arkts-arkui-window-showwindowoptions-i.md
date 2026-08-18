# ShowWindowOptions

Describes the parameters for displaying a child window or system window.

**Since:** 23

<!--Device-window-interface ShowWindowOptions--><!--Device-window-interface ShowWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
```

## focusOnShow

```TypeScript
focusOnShow?: boolean
```

Whether the window automatically gains focus when [showWindow()](arkts-arkui-window-window-i.md#showwindow) is called. The default value is **true**. This parameter does not take effect for the main window, modal window, and dialog boxes.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ShowWindowOptions-focusOnShow?: boolean--><!--Device-ShowWindowOptions-focusOnShow?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager
