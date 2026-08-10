# ActionMenuOptions

操作菜单的选项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ActionMenuOptions

<!--Device-prompt-interface ActionMenuOptions--><!--Device-prompt-interface ActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## buttons

```TypeScript
buttons: [Button, Button?, Button?, Button?, Button?, Button?]
```

菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。

**Type:** [Button, Button?, Button?, Button?, Button?, Button?]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ActionMenuOptions#buttons

<!--Device-ActionMenuOptions-buttons: [Button, Button?, Button?, Button?, Button?, Button?]--><!--Device-ActionMenuOptions-buttons: [Button, Button?, Button?, Button?, Button?, Button?]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string
```

标题文本。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction.ActionMenuOptions#title

<!--Device-ActionMenuOptions-title?: string--><!--Device-ActionMenuOptions-title?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

