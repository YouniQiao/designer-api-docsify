# StoragePropRef

Defining StoragePropRef annotation StoragePropRef is an annotation which is mutable.Any object property modifications made through StoragePropRef are visible in the AppStorage, which is different from StorageProp.In order to prevent this, need to take a deep copy of AppStorage instance data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare @interface StoragePropRef--><!--Device-unnamed-export declare @interface StoragePropRef-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## property

```TypeScript
property: string
```

The give property in AppStorage.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StoragePropRef-property: string--><!--Device-StoragePropRef-property: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

