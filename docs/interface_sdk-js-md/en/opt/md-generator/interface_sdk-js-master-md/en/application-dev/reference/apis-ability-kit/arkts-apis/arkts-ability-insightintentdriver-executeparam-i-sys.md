# ExecuteParam (System API)

Defines the parameter used to execute an intent call.

**Since:** 23

**Deprecated since:** -1

<!--Device-insightIntentDriver-interface ExecuteParam--><!--Device-insightIntentDriver-interface ExecuteParam-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## abilityName

```TypeScript
abilityName: string
```

Name of the ability to be called. If an intent defined by the @InsightIntentLink decorator is used to implement application redirection, this parameter can be left empty.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-abilityName: string--><!--Device-ExecuteParam-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

Name of the bundle to which the ability to be called belongs.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-bundleName: string--><!--Device-ExecuteParam-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId?: string
```

Indicates the device identifier. Obtained from [getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getAvailableDeviceListSync)

**Type:** string

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-deviceId?: string--><!--Device-ExecuteParam-deviceId?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## displayId

```TypeScript
displayId?: number
```

Physical screen ID specified during intent call. The value must be an integer. This parameter is valid only when **executeMode** is set to **UI_ABILITY_FOREGROUND**.

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-displayId?: long--><!--Device-ExecuteParam-displayId?: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode
```

Intent execution mode. If an intent defined by the @InsightIntentLink decorator is used to implement application redirection, this parameter must be filled (with any value that conforms to the definition), although it will not actually take effect.

**Type:** insightIntent.ExecuteMode

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-executeMode: insightIntent.ExecuteMode--><!--Device-ExecuteParam-executeMode: insightIntent.ExecuteMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## flags

```TypeScript
flags?: number
```

[Flags](arkts-ability-wantconstant-flags-e.md#Flags) of the URIs authorized by the intent caller to the intent executor during the call. **NOTE：**This parameter supports only **FLAG_AUTH_READ_URI_PERMISSION**, **FLAG_AUTH_WRITE_URI_PERMISSION**, and FLAG_AUTH_READ_URI_PERMISSION|

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-flags?: int--><!--Device-ExecuteParam-flags?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## insightIntentName

```TypeScript
insightIntentName: string
```

Intent name.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-insightIntentName: string--><!--Device-ExecuteParam-insightIntentName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## insightIntentParam

```TypeScript
insightIntentParam: Record<string, RecordData>
```

Indicates the insight intent param.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-insightIntentParam: Record<string, RecordData>--><!--Device-ExecuteParam-insightIntentParam: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

Name of the module to which the ability belongs.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-moduleName: string--><!--Device-ExecuteParam-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uris

```TypeScript
uris?: Array<string>
```

List of URIs authorized by the intent caller to the intent executor during the call. If an intent defined by the @InsightIntentLink decorator is used to implement application redirection, this field is mandatory. Only the first element in the array is read as the URI of [openLink](arkts-ability-uiabilitycontext-c.md#openLink).

**Type:** Array&lt;string&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-uris?: Array<string>--><!--Device-ExecuteParam-uris?: Array<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: number
```

ID of the user to which the intent belongs. **NOTE：**If the user ID of the calling application is different from the user ID of the intent, the calling application must request the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission.

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteParam-userId?: int--><!--Device-ExecuteParam-userId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.
