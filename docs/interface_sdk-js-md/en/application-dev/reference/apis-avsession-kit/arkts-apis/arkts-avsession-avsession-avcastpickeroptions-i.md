# AVCastPickerOptions

An option to make different picker usage

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCastPickerOptions--><!--Device-avSession-interface AVCastPickerOptions-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## menuPosition

```TypeScript
menuPosition?: MenuPosition
```

Set the popup menu position if pickerstyple is set to STYLE_MENU.

**Type:** [MenuPosition](arkts-avsession-avsession-menuposition-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-AVCastPickerOptions-menuPosition?: MenuPosition--><!--Device-AVCastPickerOptions-menuPosition?: MenuPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
pickerStyle?: AVCastPickerStyle
```

Set the picker style.

**Type:** [AVCastPickerStyle](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstyle-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-AVCastPickerOptions-pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPickerOptions-pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
sessionType?: AVSessionType
```

Indicates current session type to show different picker ui.If not set, default value is 'audio'.

**Type:** [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerOptions-sessionType?: AVSessionType--><!--Device-AVCastPickerOptions-sessionType?: AVSessionType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

