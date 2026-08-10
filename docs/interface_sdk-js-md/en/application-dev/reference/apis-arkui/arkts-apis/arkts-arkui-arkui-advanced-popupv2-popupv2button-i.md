# PopupV2Button

PopupV2Button定义按钮的相关属性和事件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface PopupV2Button--><!--Device-unnamed-export interface PopupV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PopupV2Button, PopupV2, PopupV2InitInfo } from 'kits/@kit.ArkUI';
```

## action

```TypeScript
action?: VoidCallback
```

设置按钮点击回调。

默认不执行任何操作。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2Button-action?: VoidCallback--><!--Device-PopupV2Button-action?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonTextModifier

```TypeScript
buttonTextModifier?: TextModifier
```

设置按钮文本属性，如设置文本颜色、字体大小等。默认值：undefined，值为undefined时，默认使用系统按钮文本属性。

**Type:** TextModifier

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2Button-buttonTextModifier?: TextModifier--><!--Device-PopupV2Button-buttonTextModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: ResourceStr
```

设置按钮内容。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupV2Button-text: ResourceStr--><!--Device-PopupV2Button-text: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

