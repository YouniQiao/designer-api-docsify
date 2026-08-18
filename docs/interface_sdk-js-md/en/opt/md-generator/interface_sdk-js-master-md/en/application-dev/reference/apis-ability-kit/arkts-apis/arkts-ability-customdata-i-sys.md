# CustomData (System API)

When starting a modal page, you can transfer custom data to the autofill service through [reloadInModal](arkts-ability-autofillextensioncontext-c-sys.md#reloadinmodal) and obtain the data through [onFillRequest](arkts-ability-app-ability-autofillextensionability-autofillextensionability-c-sys.md#onfillrequest) of the service.

**Since:** 23

<!--Device-unnamed-export default interface CustomData--><!--Device-unnamed-export default interface CustomData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## data

```TypeScript
data: Record<string, RecordData>
```

User defined data. When the modal window of AutoFillExtension needs to be raised again, pass this parameter to the application framework.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomData-data: Record<string, RecordData>--><!--Device-CustomData-data: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.
