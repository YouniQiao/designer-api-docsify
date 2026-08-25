# isDefaultApplicationSync

## Modules to Import

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## isDefaultApplicationSync

```TypeScript
function isDefaultApplicationSync(type: string): boolean
```

Checks whether this application is the default application of a system-defined application type or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md). This API returns the result synchronously.

**Since:** 10

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
