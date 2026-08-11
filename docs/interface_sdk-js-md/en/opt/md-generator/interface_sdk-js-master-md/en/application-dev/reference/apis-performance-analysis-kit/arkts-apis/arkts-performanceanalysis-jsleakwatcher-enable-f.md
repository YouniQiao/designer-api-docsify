# enable

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## enable

```TypeScript
function enable(isEnable: boolean): void
```

Enables the detection for JS object leaks. This function is disabled by default.

**Since:** 12

<!--Device-jsLeakWatcher-function enable(isEnable: boolean): void--><!--Device-jsLeakWatcher-function enable(isEnable: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnable | boolean | Yes |

## Examples

```TypeScript
jsLeakWatcher.enable(true);
```
