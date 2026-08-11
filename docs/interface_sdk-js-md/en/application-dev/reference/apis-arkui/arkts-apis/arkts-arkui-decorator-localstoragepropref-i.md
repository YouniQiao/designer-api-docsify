# LocalStoragePropRef

Defining LocalStoragePropRef annotation LocalStoragePropRef is an annotation which is mutable.Any object property modifications made through LocalStoragePropRef are visible in the LocalStorage, which is different from LocalStorageProp.In order to prevent this, need to take a deep copy of LocalStorage data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare @interface LocalStoragePropRef--><!--Device-unnamed-export declare @interface LocalStoragePropRef-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## property

```TypeScript
property: string
```

The give property in LocalStorage.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStoragePropRef-property: string--><!--Device-LocalStoragePropRef-property: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

