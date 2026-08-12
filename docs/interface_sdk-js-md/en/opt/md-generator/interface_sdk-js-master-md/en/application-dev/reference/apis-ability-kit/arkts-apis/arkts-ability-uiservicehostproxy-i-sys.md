# UIServiceHostProxy (System API)

UIServiceHostProxy functions as a proxy to send data from the  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#UIServiceExtensionAbility) server to the client.

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
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#UIServiceExtensionAbility)server to the client.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { common, UIServiceExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[UiServiceExtensionAbility] ';

export default class MyUiServiceExtensionAbility extends UIServiceExtensionAbility {
  // Process data sending.
  onData(proxy: common.UIServiceHostProxy, data: Record<string, Object>) {
    console.info(TAG + `onData ${JSON.stringify(data)}`);
    // Define the data to be sent.
    let formData: Record<string, string> = {
      'proxyData': 'proxyData'
    };
    try {
      // Send data to the UIServiceExtensionAbility server.
      proxy.sendData(formData);
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`${TAG} sendData failed, err code: ${code}, err msg: ${msg}.`);
    }
  }
}
```
