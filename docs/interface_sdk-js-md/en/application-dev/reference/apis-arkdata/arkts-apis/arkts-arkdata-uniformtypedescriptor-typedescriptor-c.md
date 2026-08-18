# TypeDescriptor

Represents a class for defining a uniform data type. It provides properties and methods for describing a uniform data type and its relationship with other uniform data types.

**Since:** 23

<!--Device-uniformTypeDescriptor-class TypeDescriptor--><!--Device-uniformTypeDescriptor-class TypeDescriptor-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
```

## belongsTo

```TypeScript
belongsTo(type: string): boolean
```

Checks whether this data type belongs to the specified uniform data type.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeDescriptor-belongsTo(type: string): boolean--><!--Device-TypeDescriptor-belongsTo(type: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the data type belongs to or is the same as the specified uniform data type; returns **false** if they are not related. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

**Examples**

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.belongsTo('general.source-code');
    if(ret) {
        console.info('type general.type-script belongs to type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`belongsTo throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

## equals

```TypeScript
equals(typeDescriptor: TypeDescriptor): boolean
```

Checks whether this data type is the same as the specified uniform data type. That is, compares **typeId**s of two [TypeDescriptor](#typedescriptor) objects.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeDescriptor-equals(typeDescriptor: TypeDescriptor): boolean--><!--Device-TypeDescriptor-equals(typeDescriptor: TypeDescriptor): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typeDescriptor | [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | Yes | Uniform data type to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the type IDs are the same; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

**Examples**

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeA : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let typeB : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.python-script');
    if(!typeA.equals(typeB)) {
      console.info('typeA is not equal to typeB');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

## isHigherLevelType

```TypeScript
isHigherLevelType(type: string): boolean
```

Checks whether this data type is a higher-level type of the specified uniform data type. For example, **SOURCE_CODE** is a higher-level type of **TYPE_SCRIPT**, and **TEXT** is a higher-level type of **SOURCE_CODE** and **TYPE_SCRIPT**.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeDescriptor-isHigherLevelType(type: string): boolean--><!--Device-TypeDescriptor-isHigherLevelType(type: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the data type is a higher-level type of the specified uniform data type; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

**Examples**

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.source-code');
    let ret = typeObj.isHigherLevelType('general.type-script');
    if(ret) {
        console.info('type general.source-code is higher level type of type general.type-script');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`isHigherLevelType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

## isLowerLevelType

```TypeScript
isLowerLevelType(type: string): boolean
```

Checks whether this data type is a lower-level type of the specified uniform data type. For example, **TYPE_SCRIPT** is a lower-level type of **SOURCE_CODE**, and **TYPE_SCRIPT** and **SOURCE_CODE** are lower-level types of **TEXT**.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeDescriptor-isLowerLevelType(type: string): boolean--><!--Device-TypeDescriptor-isLowerLevelType(type: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the data type is a lower-level type of the specified uniform data type; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types; <br>3. Parameter verification failed. |

**Examples**

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.isLowerLevelType('general.source-code');
    if(ret) {
        console.info('type general.type-script is lower level type of type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(`isLowerLevelType throws an exception. code is ${error.code}, message is ${error.message} `);
}
```

