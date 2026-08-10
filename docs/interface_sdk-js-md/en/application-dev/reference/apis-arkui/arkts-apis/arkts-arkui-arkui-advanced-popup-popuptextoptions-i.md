# PopupTextOptions

设置文本样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PopupTextOptions--><!--Device-unnamed-export interface PopupTextOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Popup, PopupOptions, PopupButtonOptions, PopupIconOptions, PopupTextOptions } from 'kits/@kit.ArkUI';
```

## fontColor

```TypeScript
fontColor?: ResourceColor
```

设置文本字体颜色。

默认值：`\$r('sys.color.ohos_id_color_text_secondary')`

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** $r('sys.color.ohos_id_color_text_secondary')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupTextOptions-fontColor?: ResourceColor--><!--Device-PopupTextOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: number | string | Resource
```

设置文本字体大小。

默认值：`\$r('sys.float.ohos_id_text_size_body2')` 

string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。

number：取值范围(0,+∞)。

**Type:** number \| string \| Resource

**Default:** $r('sys.float.ohos_id_text_size_body2')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupTextOptions-fontSize?: number | string | Resource--><!--Device-PopupTextOptions-fontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: number | FontWeight | string
```

设置文本字体粗细。

number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。

string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Regular

**Type:** number \| FontWeight \| string

**Default:** FontWeight.Regular

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupTextOptions-fontWeight?: number | FontWeight | string--><!--Device-PopupTextOptions-fontWeight?: number | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr
```

设置文本内容。 

**ArkTS模式：** 该接口仅适用于ArkTS-Sta。

**ArkTS-Sta起始版本：** 23

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupTextOptions-text?: ResourceStr--><!--Device-PopupTextOptions-text?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

