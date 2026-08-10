# createDistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## createDistributedObject

```TypeScript
function createDistributedObject(source: object): DistributedObject
```

创建一个分布式数据对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [distributedDataObject.create](arkts-arkdata-distributeddataobject-create-f.md#create)

<!--Device-distributedDataObject-function createDistributedObject(source: object): DistributedObject--><!--Device-distributedDataObject-function createDistributedObject(source: object): DistributedObject-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | object | Yes | 设置分布式数据对象的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DistributedObject](arkts-arkdata-distributeddataobject-distributedobject-i.md) | 创建完成的分布式数据对象。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
```

