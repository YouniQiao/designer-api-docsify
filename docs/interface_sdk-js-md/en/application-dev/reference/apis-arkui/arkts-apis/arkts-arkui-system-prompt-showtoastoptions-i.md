# ShowToastOptions

定义ShowToast的选项。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions

<!--Device-unnamed-export interface ShowToastOptions--><!--Device-unnamed-export interface ShowToastOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ShowActionMenuOptions, Button, ShowToastOptions, ShowDialogOptions, ShowDialogSuccessResponse } from 'kits/@kit.ArkUI';
```

## bottom

```TypeScript
bottom?: string | number
```

设置弹窗边框距离屏幕底部的位置。

**Type:** string \| number

**Since:** 5

**ArkTS mode:** ArkTS-Dyn only, since version 5.

**Deprecated since:** 8

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#bottom

<!--Device-ShowToastOptions-bottom?: string | number--><!--Device-ShowToastOptions-bottom?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

默认值1500ms，建议区间：1500ms-10000ms。若小于1500ms则取默认值，最大取值为10000ms。

**Type:** number

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#duration

<!--Device-ShowToastOptions-duration?: number--><!--Device-ShowToastOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

显示的文本信息。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.promptAction/promptAction.ShowToastOptions#message

<!--Device-ShowToastOptions-message: string--><!--Device-ShowToastOptions-message: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

