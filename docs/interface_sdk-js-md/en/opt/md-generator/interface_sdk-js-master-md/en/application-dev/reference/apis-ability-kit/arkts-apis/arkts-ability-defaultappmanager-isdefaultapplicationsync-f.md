# isDefaultApplicationSync

## Modules to Import

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## isDefaultApplicationSync

```TypeScript
function isDefaultApplicationSync(type: string): boolean
```

Checks whether this application is the default application of a system-defined application type or a  
[uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md/arkts-data-uniformtypedescriptor.md). This API returns the result synchronously.

**Since:** 10

<!--Device-defaultAppManager-function isDefaultApplicationSync(type: string): boolean--><!--Device-defaultAppManager-function isDefaultApplicationSync(type: string): boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';

try {
  let data = defaultAppManager.isDefaultApplicationSync(defaultAppManager.ApplicationType.BROWSER)
  console.info('Operation successful. IsDefaultApplicationSync ? ' + JSON.stringify(data));
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
}
```
