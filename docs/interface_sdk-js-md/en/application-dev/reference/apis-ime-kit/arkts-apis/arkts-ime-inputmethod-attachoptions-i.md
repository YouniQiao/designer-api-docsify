# AttachOptions

Defines additional options for binding an input method.

**Since:** 23

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import inputMethod from '@kit.IMEKit';
import inputMethodEngine from '@kit.IMEKitEngine';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKitList';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit.Panel';
import { InputMethodExtraConfig } from '@kit.IMEKit.ExtraConfig';
import inputMethodSystemPanelManager from '@kit.IMEKitSystemPanelManager';
```

## requestKeyboardReason

```TypeScript
requestKeyboardReason?: RequestKeyboardReason
```

Reason for requesting the keyboard.

**Type:** RequestKeyboardReason

**Default:** RequestKeyboardReason.NONE

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## showKeyboard

```TypeScript
showKeyboard?: boolean
```

Whether to start the input method keyboard after the self-drawing component is attached to the input method.   
- **true** means to start the input method keyboard.   
- **false** means not to start the input method keyboard.

**Type:** boolean

**Default:** true

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework
