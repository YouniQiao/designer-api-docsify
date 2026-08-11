# dump

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## dump

```TypeScript
function dump(filePath: string): Array<string>
```

Dumps the list of leaked objects and VM memory snapshot.

**Since:** 12

<!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>--><!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |

## Examples

```TypeScript
let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```
