# createDistributedObject

## createDistributedObject

```TypeScript
function createDistributedObject(source: object): DistributedObject
```

Creates a distributed data object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [distributedDataObject.create](arkts-arkdata-distributeddataobject-create-f.md#create)

<!--Device-distributedDataObject-function createDistributedObject(source: object): DistributedObject--><!--Device-distributedDataObject-function createDistributedObject(source: object): DistributedObject-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | object | Yes | Properties of the distributed data object. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Distributed data object created. |

**Example**

```TypeScript
class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
```

