# PopupButtonOptions

PopupButtonOptions定义按钮的相关属性和事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PopupButtonOptions--><!--Device-unnamed-export interface PopupButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Popup, PopupOptions, PopupButtonOptions, PopupIconOptions, PopupTextOptions } from 'kits/@kit.ArkUI';
```

## action

```TypeScript
action?: VoidCallback
```

设置按钮click回调。 

默认不执行任何操作。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-action?: VoidCallback--><!--Device-PopupButtonOptions-action?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

设置按钮文本字体颜色。

默认值：`\$r('sys.color.ohos_id_color_text_primary_activated')`

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

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

设置按钮文本字体大小。 

默认值：`\$r('sys.float.ohos_id_text_size_button2')`

string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。

设置值为异常值时取默认值。

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

设置按钮内容。 

**ArkTS模式：** 该接口仅适用于ArkTS-Sta。 

**ArkTS-Sta起始版本：** 23

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupButtonOptions-text?: ResourceStr--><!--Device-PopupButtonOptions-text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

