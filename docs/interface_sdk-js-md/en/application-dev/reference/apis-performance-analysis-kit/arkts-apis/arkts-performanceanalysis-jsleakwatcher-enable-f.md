# enable

## Modules to Import

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## enable

```TypeScript
function enable(isEnable: boolean): void
```

Enables the detection for JS object leaks. This function is disabled by default.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-jsLeakWatcher-function enable(isEnable: boolean): void--><!--Device-jsLeakWatcher-function enable(isEnable: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnable | boolean | Yes | Whether to enable **jsLeakWatcher**. **true**: yes; **false**: no. |

## Examples

```TypeScript
jsLeakWatcher.enable(true);
```

