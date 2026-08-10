# ShowToastOptions

文本提示框的选项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions

<!--Device-prompt-interface ShowToastOptions--><!--Device-prompt-interface ShowToastOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## bottom

```TypeScript
bottom?: string | number
```

设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。

**Type:** string \| number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#bottom

<!--Device-ShowToastOptions-bottom?: string | number--><!--Device-ShowToastOptions-bottom?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#duration

<!--Device-ShowToastOptions-duration?: number--><!--Device-ShowToastOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

显示的文本信息。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#message

<!--Device-ShowToastOptions-message: string--><!--Device-ShowToastOptions-message: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

