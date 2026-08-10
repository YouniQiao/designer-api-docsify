# MaximizeOptions

最大化窗口时的可选配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-window-interface MaximizeOptions--><!--Device-window-interface MaximizeOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## acrossDisplayPresentation

```TypeScript
acrossDisplayPresentation?: AcrossDisplayPresentation
```

参数控制主窗口的瀑布模式策略。该参数只能在具有折叠功能的2in1设备上正确调用。如果在其他设备类型上调用，则没有任何效果。

**Type:** [AcrossDisplayPresentation](arkts-arkui-window-acrossdisplaypresentation-e.md)

**Default:** AcrossDisplayPresentation.FOLLOW_ACROSS_DISPLAY_SETTING

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaximizeOptions-acrossDisplayPresentation?: AcrossDisplayPresentation--><!--Device-MaximizeOptions-acrossDisplayPresentation?: AcrossDisplayPresentation-End-->

**System capability:** SystemCapability.Window.SessionManager

## maximizePresentation

```TypeScript
maximizePresentation?: MaximizePresentation
```

窗口最大化时的布局。

**Type:** [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md)

**Default:** MaximizePresentation.ENTER_IMMERSIVE

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaximizeOptions-maximizePresentation?: MaximizePresentation--><!--Device-MaximizeOptions-maximizePresentation?: MaximizePresentation-End-->

**System capability:** SystemCapability.Window.SessionManager

## snapshotAnimationConfig

```TypeScript
snapshotAnimationConfig?: WindowSnapshotAnimationConfig
```

截图动效的配置。如果未指定，将使用系统默认动效。当持续时间和延迟参数都设置为0时，表示截图动效被取消。

**Type:** [WindowSnapshotAnimationConfig](arkts-arkui-window-windowsnapshotanimationconfig-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaximizeOptions-snapshotAnimationConfig?: WindowSnapshotAnimationConfig--><!--Device-MaximizeOptions-snapshotAnimationConfig?: WindowSnapshotAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

