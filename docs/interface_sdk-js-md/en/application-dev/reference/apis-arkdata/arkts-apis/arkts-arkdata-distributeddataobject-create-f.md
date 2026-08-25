# create

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## create

```TypeScript
function create(context: Context, source: object): DataObject
```

Creates a distributed data object. The object properties support basic types (number, Boolean, and string) and complex types (array and nested basic types).

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| source | object | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataObject](arkts-arkdata-distributeddataobject-dataobject-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
