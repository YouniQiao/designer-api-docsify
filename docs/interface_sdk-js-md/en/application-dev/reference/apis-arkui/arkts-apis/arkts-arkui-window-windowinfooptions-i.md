# WindowInfoOptions

窗口布局信息过滤选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-window-interface WindowInfoOptions--><!--Device-window-interface WindowInfoOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## excludeSystemWindows

```TypeScript
excludeSystemWindows?: boolean
```

是否排除系统窗口。true表示需要排除，false表示不排除，默认为false。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WindowInfoOptions-excludeSystemWindows?: boolean--><!--Device-WindowInfoOptions-excludeSystemWindows?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## foregroundAboveWindow

```TypeScript
foregroundAboveWindow?: int
```

需要过滤掉的不高于此窗口层级的窗口的ID。表示只返回层级高于这个窗口的窗口信息。默认值是0，表示忽略本选项；如果值小于0，返回1300016错误码；如果指定的窗口不存在，则与设置为0等价。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WindowInfoOptions-foregroundAboveWindow?: int--><!--Device-WindowInfoOptions-foregroundAboveWindow?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## foregroundBelowWindow

```TypeScript
foregroundBelowWindow?: int
```

需要过滤掉的不低于此窗口层级的窗口的ID。表示只返回层级低于这个窗口的窗口信息。默认值是0，表示忽略本选项；如果值小于0，返回1300016错误码；如果指定的窗口不存在，则与设置为0等价。若同时指定foregroundBelowWindow和foregroundAboveWindow，且两者都是有效的窗口ID，但foregroundBelowWindow指定的窗口的层级未高于foregroundAboveWindow指定的窗口，则返回空数组。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WindowInfoOptions-foregroundBelowWindow?: int--><!--Device-WindowInfoOptions-foregroundBelowWindow?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

