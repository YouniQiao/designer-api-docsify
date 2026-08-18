# setJsRawHeapTrimLevel

## Modules to Import

```TypeScript
```

## setJsRawHeapTrimLevel

```TypeScript
function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void
```

Sets the raw heap snapshot trimming level for the current process.

**Since:** 26.1.0

<!--Device-hidebug-function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void--><!--Device-hidebug-function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [JsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-jsrawheaptrimlevel-e.md) | Yes |

**Examples**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.setJsRawHeapTrimLevel(hidebug.JsRawHeapTrimLevel.TRIM_LEVEL_2);
```
