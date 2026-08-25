# getUniformDataTypeByFilenameExtension

## Modules to Import

```TypeScript
import { uniformTypeDescriptor } from 'kits/@kit.ArkData';
```

## getUniformDataTypeByFilenameExtension

```TypeScript
function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string
```

Obtains the uniform data type ID based on the given file name extension and data type. If there are multiple uniform data type IDs matching the conditions, the first one is returned.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filenameExtension | string | Yes |
| [belongsTo](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
