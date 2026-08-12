# PopupButtonOptions

Defines the popup button options

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PopupButtonOptions--><!--Device-unnamed-export interface PopupButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Popup, PopupOptions, PopupButtonOptions, PopupIconOptions, PopupTextOptions } from '@kit.ArkUI';
```

## action

```TypeScript
action?: VoidCallback
```

Set the button callback.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-action?: VoidCallback--><!--Device-PopupButtonOptions-action?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

Set the button font color.

**Type:** ResourceColor

**Default:** $r('sys.color.ohos_id_color_text_primary_activated')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-fontColor?: ResourceColor--><!--Device-PopupButtonOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: number | string | Resource
```

Set the button font size.

**Type:** number \| string \| Resource

**Default:** $r('sys.float.ohos_id_text_size_button2')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-fontSize?: number | string | Resource--><!--Device-PopupButtonOptions-fontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

Set the button display content.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-text?: ResourceStr--><!--Device-PopupButtonOptions-text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

