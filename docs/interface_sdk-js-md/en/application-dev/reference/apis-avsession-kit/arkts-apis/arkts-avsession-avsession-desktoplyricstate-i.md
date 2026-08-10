# DesktopLyricState

桌面歌词状态。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avSession-interface DesktopLyricState--><!--Device-avSession-interface DesktopLyricState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## isLocked

```TypeScript
isLocked: boolean
```

桌面歌词位置是否锁定。true表示已锁定，false表示未锁定。若已锁定，桌面显示歌词后，固定当前位置，不可被拖拽。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DesktopLyricState-isLocked: boolean--><!--Device-DesktopLyricState-isLocked: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

