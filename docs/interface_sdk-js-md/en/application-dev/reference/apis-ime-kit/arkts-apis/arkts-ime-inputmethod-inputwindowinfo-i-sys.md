# InputWindowInfo

Information of input window.

**Since:** 23

<!--Device-inputMethod-export interface InputWindowInfo--><!--Device-inputMethod-export interface InputWindowInfo-End-->

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

## userId

```TypeScript
userId?: int
```

Indicates the ID of the user whose input window is shown.

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputWindowInfo-userId?: int--><!--Device-InputWindowInfo-userId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

