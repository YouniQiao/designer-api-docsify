# getTypeDescriptor

## Modules to Import

```TypeScript
import { uniformTypeDescriptor } from 'uniformTypeDescriptor';
```

## getTypeDescriptor

```TypeScript
function getTypeDescriptor(typeId: string): TypeDescriptor
```

Obtains the **TypeDescriptor** object based on the uniform data type ID.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor--><!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typeId | string | Yes | [Uniform data type ID]. |

**Return value:**

| Type | Description |
| --- | --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | TypeDescriptor** object obtained. If the uniform data type does not exist, **null** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

## Examples

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('com.adobe.photoshop-image');
    if (typeObj) {
        let typeId = typeObj.typeId;
        let belongingToTypes = typeObj.belongingToTypes;
        let description = typeObj.description;
        let referenceURL = typeObj.referenceURL;
        let iconFile = typeObj.iconFile;
        let filenameExtensions = typeObj.filenameExtensions;
        let mimeTypes = typeObj.mimeTypes;
        console.info(`typeId: ${typeId}, belongingToTypes: ${belongingToTypes}, description: ${description}, referenceURL: ${referenceURL}, iconFile: ${iconFile}, filenameExtensions: ${filenameExtensions}, mimeTypes: ${mimeTypes}`);
    } else {
        console.info('type com.adobe.photoshop-image does not exist');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`getTypeDescriptor throws an exception. code is ${error.code}, message is ${error.message} `);
}
```


## getTypeDescriptor

```TypeScript
function getTypeDescriptor(typeId: string): TypeDescriptor | null
```

Queries and returns the uniform type descriptor by the given uniform data type ID.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor | null--><!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor | null-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typeId | string | Yes | Uniform data type ID. |

**Return value:**

| Type | Description |
| --- | --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | Returns the uniform type descriptor corresponding to the uniform data type ID or null if the uniform data type does not exist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

