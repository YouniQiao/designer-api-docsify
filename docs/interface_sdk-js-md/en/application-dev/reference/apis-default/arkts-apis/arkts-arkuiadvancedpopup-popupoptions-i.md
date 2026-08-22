# PopupOptions

Defines the popup options. @interface PopupOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PopupOptions--><!--Device-unnamed-export interface PopupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## buttons

```TypeScript
buttons?: [
    PopupButtonOptions | undefined,
    PopupButtonOptions | undefined
  ]
```

The buttons of Popup. Setting undefined means that the button will not be displayed.

**Type:** [     PopupButtonOptions \| undefined,     PopupButtonOptions \| undefined   ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-buttons?: [    PopupButtonOptions | undefined,    PopupButtonOptions | undefined  ]--><!--Device-PopupOptions-buttons?: [    PopupButtonOptions | undefined,    PopupButtonOptions | undefined  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Direction
```

Indicates the attribute of the current popup direction.

**Type:** Direction

**Default:** Direction.Auto

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-direction?: Direction--><!--Device-PopupOptions-direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: PopupIconOptions
```

The icon of Popup.

**Type:** [PopupIconOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedpopup-popupiconoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-icon?: PopupIconOptions--><!--Device-PopupOptions-icon?: PopupIconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxWidth

```TypeScript
maxWidth?: Dimension
```

Set the max width of the popup.

**Type:** Dimension

**Default:** 400.0_vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-maxWidth?: Dimension--><!--Device-PopupOptions-maxWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: PopupTextOptions
```

The message of Popup.

**Type:** [PopupTextOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedpopup-popuptextoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-message?: PopupTextOptions--><!--Device-PopupOptions-message?: PopupTextOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClose

```TypeScript
onClose?: VoidCallback
```

The close button callback of Popup.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onClose?: VoidCallback--><!--Device-PopupOptions-onClose?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showClose

```TypeScript
showClose?: boolean | Resource
```

The show close of Popup.

**Type:** boolean \| Resource

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-showClose?: boolean | Resource--><!--Device-PopupOptions-showClose?: boolean | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: PopupTextOptions
```

The title of Popup.

**Type:** [PopupTextOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedpopup-popuptextoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-title?: PopupTextOptions--><!--Device-PopupOptions-title?: PopupTextOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

