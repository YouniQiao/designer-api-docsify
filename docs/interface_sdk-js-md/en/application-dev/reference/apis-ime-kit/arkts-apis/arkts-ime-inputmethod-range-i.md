# Range

@brief Describes the range of the selected text.

**Since:** 23

<!--Device-inputMethod-export interface Range--><!--Device-inputMethod-export interface Range-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## end

```TypeScript
end: int
```

@brief Index of the last selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length. The **end** value must be greater than the **start** value.

**Type:** int

**Since:** 23

<!--Device-Range-end: int--><!--Device-Range-end: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## start

```TypeScript
start: int
```

@brief Index of the first selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length.

**Type:** int

**Since:** 23

<!--Device-Range-start: int--><!--Device-Range-start: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

