# getCfgDirListSync (System API)

## Modules to Import

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgDirListSync

```TypeScript
function getCfgDirListSync(): Array<string>
```

Obtains a list of configuration level directories, in ascending order of priority.

**Since:** 23

<!--Device-configPolicy-function getCfgDirListSync(): Array<string>--><!--Device-configPolicy-function getCfgDirListSync(): Array<string>-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Obtains the list of configuration level directories. This API returns the result synchronously. |

**Examples**

```TypeScript
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

try {
  let result: Array<string> = configPolicy.getCfgDirListSync();
  console.info('result is ' + result);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error('error:' + code + ', ' + message);
}
```

