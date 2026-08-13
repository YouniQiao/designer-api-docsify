# dump

## Modules to Import

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## dump

```TypeScript
function dump(filePath: string): Array<string>
```

Dumps the list of leaked objects and VM memory snapshot.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>--><!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Path for storing exported information files. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Export result. The file name extension is **.jsleaklist** for the list of leaked objects and **.heapsnapshot** for the VM memory snapshot. &lt;br&gt;Note: If the dump is successful, the path of the leaked object list file and the VM memory snapshot path are returned. Otherwise, an empty array is returned. |

## Examples

```TypeScript
let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```

