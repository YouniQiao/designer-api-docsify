# UIServiceHostProxy (System API)

UIServiceHostProxy functions as a proxy to send data from the  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md) server to the client.

> **NOTE：**
> 
> - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface UIServiceHostProxy--><!--Device-unnamed-export default interface UIServiceHostProxy-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## sendData

```TypeScript
sendData(data: Record<string, Object>): void
```

Sends data from the  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)server to the client.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceHostProxy-sendData(data: Record<string, Object>): void--><!--Device-UIServiceHostProxy-sendData(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes | Data to be sent to the [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md) client. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

## sendData

```TypeScript
sendData(data: Record<string, RecordData>): void
```

Sends data from the  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)server to the client.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceHostProxy-sendData(data: Record<string, RecordData>): void--><!--Device-UIServiceHostProxy-sendData(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | Data to be sent to the [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md) client. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

