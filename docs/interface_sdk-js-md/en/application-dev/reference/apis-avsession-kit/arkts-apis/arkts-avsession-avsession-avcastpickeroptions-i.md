# AVCastPickerOptions

拉起的投播组件包含的配置属性。

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

当pickerStyle设置为STYLE_MENU时，可以设置弹出菜单的位置。

**Type:** [MenuPosition](arkts-avsession-avsession-menuposition-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-AVCastPickerOptions-menuPosition?: MenuPosition--><!--Device-AVCastPickerOptions-menuPosition?: MenuPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
pickerStyle?: AVCastPickerStyle
```

设置组件样式。

**Type:** [AVCastPickerStyle](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstyle-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-AVCastPickerOptions-pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPickerOptions-pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
sessionType?: AVSessionType
```

会话类型，默认值为audio。

当前仅支持的会话类型有audio和video。如果传入voice_call或video_call，将默认按照传入audio处理。

**Type:** [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerOptions-sessionType?: AVSessionType--><!--Device-AVCastPickerOptions-sessionType?: AVSessionType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

