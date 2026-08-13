# getManagedBrowserPolicy

## Modules to Import

```TypeScript
import { browser } from '@kit.MDMKit';
```

## getManagedBrowserPolicy

```TypeScript
function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer
```

Obtains the policy of a specified browser based on the application bundle name. This API is applicable to scenarios where the current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise device administrator application and verifying whether a policy has taken effect.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer--><!--Device-browser-function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |

## Examples

```TypeScript
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.testbrowser';

try {
  let buffer: ArrayBuffer = browser.getManagedBrowserPolicy(wantTemp, bundleName);
  let intBuffer: Uint8Array = new Uint8Array(buffer);
  let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
  let stringData: string = decoder.decodeToString(intBuffer);
  console.info(`Succeeded in getting managed browser policy, result : ${stringData}`);
} catch(err) {
  console.error(`Failed to get managed browser policy. Code is ${err.code}, message is ${err.message}`);
}
```
