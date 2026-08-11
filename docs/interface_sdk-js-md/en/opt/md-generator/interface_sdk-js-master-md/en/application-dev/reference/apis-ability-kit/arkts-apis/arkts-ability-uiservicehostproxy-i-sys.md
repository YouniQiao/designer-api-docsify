# UIServiceHostProxy (System API)

UIServiceHostProxy functions as a proxy to send data from the  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md) server to the client.

> **NOTE：**
> 
> - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Since:** 14

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceHostProxy-sendData(data: Record<string, Object>): void--><!--Device-UIServiceHostProxy-sendData(data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
