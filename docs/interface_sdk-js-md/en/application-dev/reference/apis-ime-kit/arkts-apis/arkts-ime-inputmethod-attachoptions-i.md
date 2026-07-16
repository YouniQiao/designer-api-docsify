# AttachOptions

Attach options.

**Since:** 23

<!--Device-inputMethod-export interface AttachOptions--><!--Device-inputMethod-export interface AttachOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## requestKeyboardReason

```TypeScript
requestKeyboardReason?: RequestKeyboardReason
```

The reason for request keyboard.

**Type:** RequestKeyboardReason

**Default:** RequestKeyboardReason.NONE

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason--><!--Device-AttachOptions-requestKeyboardReason?: RequestKeyboardReason-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## showKeyboard

```TypeScript
showKeyboard?: boolean
```

Whether to show the keyboard when attaching.

**Type:** boolean

**Default:** true

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttachOptions-showKeyboard?: boolean--><!--Device-AttachOptions-showKeyboard?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

