# getInputMethodSetting

## Modules to Import

```TypeScript
import inputMethod from '@kit.IMEKit';
import inputMethodEngine from '@kit.IMEKitEngine';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKitList';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit.Panel';
import { InputMethodExtraConfig } from '@kit.IMEKit.ExtraConfig';
import inputMethodSystemPanelManager from '@kit.IMEKitSystemPanelManager';
```

## getInputMethodSetting

```TypeScript
function getInputMethodSetting(): InputMethodSetting
```

Obtains an [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSetting](arkts-ime-inputmethod-getsetting-f.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | InputMethodSetting** instance. |

**Examples**

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();
```
