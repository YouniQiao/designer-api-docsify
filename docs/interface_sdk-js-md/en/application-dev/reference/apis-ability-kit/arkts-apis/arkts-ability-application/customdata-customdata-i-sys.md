# CustomData (System API)

When starting a modal page, you can transfer custom data to the autofill service through  
[reloadInModal]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and obtain the data through  
[onFillRequest]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ of the service.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface CustomData--><!--Device-unnamed-export default interface CustomData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## data

```TypeScript
data: Record<string, Object>
```

Custom data transferred for starting the modal page. The data is of the Record type.

**Type:** Record&lt;string, Object&gt;

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomData-data: Record<string, Object>--><!--Device-CustomData-data: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

