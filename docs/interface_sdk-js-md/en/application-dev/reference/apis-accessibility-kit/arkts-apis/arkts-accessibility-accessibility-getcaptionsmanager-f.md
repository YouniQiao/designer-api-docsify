# getCaptionsManager

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## getCaptionsManager

```TypeScript
function getCaptionsManager(): CaptionsManager
```

获取无障碍字幕配置管理实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 12

<!--Device-accessibility-function getCaptionsManager(): CaptionsManager--><!--Device-accessibility-function getCaptionsManager(): CaptionsManager-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Return value:**

| Type | Description |
| --- | --- |
| [CaptionsManager](arkts-accessibility-accessibility-captionsmanager-i.md) | 无障碍字幕配置管理。 |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();
```

