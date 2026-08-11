# PanelInfo

Defines the attributes of the input method panel.

**Since:** 11

<!--Device-unnamed-export interface PanelInfo--><!--Device-unnamed-export interface PanelInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from 'kits/@kit.IMEKit';
```

## flag

```TypeScript
flag?: PanelFlag
```

State type of the input method panel.

- The default value is **FLAG_FIXED**.  
- Currently, this parameter is used to describe the state type of the soft keyboard.

**Type:** [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md)

**Default:** FLG_FIXED

**Since:** 11

<!--Device-PanelInfo-flag?: PanelFlag--><!--Device-PanelInfo-flag?: PanelFlag-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## type

```TypeScript
type: PanelType
```

Type of the input method panel.

**Type:** [PanelType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md)

**Since:** 11

<!--Device-PanelInfo-type: PanelType--><!--Device-PanelInfo-type: PanelType-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework
