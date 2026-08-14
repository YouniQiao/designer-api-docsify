# PanelInfo

Defines the attributes of the input method panel.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface PanelInfo--><!--Device-unnamed-export interface PanelInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { PanelInfo } from 'PanelInfo';
import { PanelType } from 'PanelType';
import { PanelFlag } from 'PanelFlag';
```

## flag

```TypeScript
flag?: PanelFlag
```

State type of the input method panel. - The default value is **FLAG_FIXED**. - Currently, this parameter is used to describe the state type of the soft keyboard.

**Type:** [PanelFlag](arkts-ime-inputmethod-panel-panelflag-e.md)

**Default:** FLG_FIXED

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PanelInfo-flag?: PanelFlag--><!--Device-PanelInfo-flag?: PanelFlag-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## type

```TypeScript
type: PanelType
```

Type of the input method panel.

**Type:** [PanelType](arkts-ime-inputmethod-panel-paneltype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PanelInfo-type: PanelType--><!--Device-PanelInfo-type: PanelType-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

