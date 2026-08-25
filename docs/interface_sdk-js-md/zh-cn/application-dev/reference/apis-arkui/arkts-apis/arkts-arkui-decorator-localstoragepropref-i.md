# LocalStoragePropRef

Defining LocalStoragePropRef annotation LocalStoragePropRef is an annotation which is mutable. Any object property modifications made through LocalStoragePropRef are visible in the LocalStorage, which is different from LocalStorageProp. In order to prevent this, need to take a deep copy of LocalStorage data.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## property

```TypeScript
property: string
```

用于标识LocalStorage的属性。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
