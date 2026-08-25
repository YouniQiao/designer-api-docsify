# StoragePropRef

Defining StoragePropRef annotation StoragePropRef is an annotation which is mutable. Any object property modifications made through StoragePropRef are visible in the AppStorage, which is different from StorageProp. In order to prevent this, need to take a deep copy of AppStorage instance data.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## property

```TypeScript
property: string
```

The give property in AppStorage.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
