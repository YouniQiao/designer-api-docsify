# getCfgDirListSync (System API)

## Modules to Import

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
```

## getCfgDirListSync

```TypeScript
function getCfgDirListSync(): Array<string>
```

Obtains a list of configuration level directories, in ascending order of priority.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-configPolicy-function getCfgDirListSync(): Array<string>--><!--Device-configPolicy-function getCfgDirListSync(): Array<string>-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Obtains the list of configuration level directories. This API returns the result synchronously. |

