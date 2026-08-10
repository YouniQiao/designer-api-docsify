# AttachOptions

绑定输入法时的附加选项。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-export interface AttachOptions--><!--Device-inputMethodEngine-export interface AttachOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## isSimpleKeyboardEnabled

```TypeScript
isSimpleKeyboardEnabled?: boolean
```

是否使能简单键盘，该属性由编辑框应用设置，true表示使能简单键盘，false表示不使能简单键盘。

如果没有设置或设置非法值，则默认不使能简单键盘。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AttachOptions-isSimpleKeyboardEnabled?: boolean--><!--Device-AttachOptions-isSimpleKeyboardEnabled?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## requestKeyboardReason

```TypeScript
requestKeyboardReason?: RequestKeyboardReason
```

该属性由编辑框应用设置，如果没有设置或设置非法值，则默认没有特定的原因触发键盘请求。

**Type:** [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason--><!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

