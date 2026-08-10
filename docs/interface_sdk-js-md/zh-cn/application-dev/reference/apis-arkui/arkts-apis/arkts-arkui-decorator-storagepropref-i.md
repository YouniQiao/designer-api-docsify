# StoragePropRef

Defining StoragePropRef annotation StoragePropRef is an annotation which is mutable.Any object property modifications made through StoragePropRef are visible in the AppStorage, which is different from StorageProp.In order to prevent this, need to take a deep copy of AppStorage instance data.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare @interface StoragePropRef--><!--Device-unnamed-export declare @interface StoragePropRef-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## property

```TypeScript
property: string
```

用于标识AppStorage的属性。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StoragePropRef-property: string--><!--Device-StoragePropRef-property: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

