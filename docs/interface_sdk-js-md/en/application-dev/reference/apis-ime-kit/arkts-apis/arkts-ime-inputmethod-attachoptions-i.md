# AttachOptions

绑定输入法的附加选项。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-inputMethod-export interface AttachOptions--><!--Device-inputMethod-export interface AttachOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## requestKeyboardReason

```TypeScript
requestKeyboardReason?: RequestKeyboardReason
```

请求键盘输入的原因。

**Type:** [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md)

**Default:** RequestKeyboardReason.NONE

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason--><!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## showKeyboard

```TypeScript
showKeyboard?: boolean
```

绑定输入法成功后，是否拉起输入法键盘。

- true表示拉起。  
- false表示不拉起。

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttachOptions-showKeyboard?: boolean--><!--Device-AttachOptions-showKeyboard?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

