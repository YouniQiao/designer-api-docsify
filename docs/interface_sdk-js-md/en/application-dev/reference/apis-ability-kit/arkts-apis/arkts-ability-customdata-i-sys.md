# CustomData (System API)

拉起模态页面时，开发者可通过[reloadInModal](arkts-ability-autofillextensioncontext-c-sys.md#reloadinmodal)接口将自定义数据传递给自动填充服务，并可通过自动填充服务的  
[onFillRequest](./../@ohos.app.ability.AutoFillExtensionAbility:AutoFillExtensionAbility.onFillRequest)获取到该数据。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface CustomData--><!--Device-unnamed-export default interface CustomData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## data

```TypeScript
data: Record<string, Object>
```

拉起模态页面时传递的自定义数据，该数据为Record类型。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomData-data: Record<string, Object>--><!--Device-CustomData-data: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

