# WindowSnapshotConfiguration

主窗口截图的配置项。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-window-interface WindowSnapshotConfiguration--><!--Device-window-interface WindowSnapshotConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## useCache

```TypeScript
useCache?: boolean
```

是否使用主窗口的已有截图。默认值为true。 true表示使用主窗口的已有截图，若主窗口无保存的截图，则使用主窗口的最新截图。false表示使用主窗口的最新截图。

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-WindowSnapshotConfiguration-useCache?: boolean--><!--Device-WindowSnapshotConfiguration-useCache?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

