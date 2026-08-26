# Range

Describes the range of the selected text.

**Since:** 10

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

## end

```TypeScript
end: number
```

Index of the last selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length. The **end** value must be greater than the **start** value.

**Type:** number

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## start

```TypeScript
start: number
```

Index of the first selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length.

**Type:** number

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework
