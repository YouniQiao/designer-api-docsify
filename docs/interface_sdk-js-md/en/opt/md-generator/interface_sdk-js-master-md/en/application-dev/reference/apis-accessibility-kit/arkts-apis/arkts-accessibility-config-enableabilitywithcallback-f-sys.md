# enableAbilityWithCallback (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## enableAbilityWithCallback

```TypeScript
function enableAbilityWithCallback(
    name: string,
    capability: Array<accessibility.Capability>,
    connectCallback: ConnectCallback
  ): Promise<void>
```

Enables the auxiliary extension ability and specifies [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) to be invoked when the state of an auxiliary extension ability changes. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function enableAbilityWithCallback(    name: string,    capability: Array<accessibility.Capability>,    connectCallback: ConnectCallback  ): Promise<void>--><!--Device-config-function enableAbilityWithCallback(    name: string,    capability: Array<accessibility.Capability>,    connectCallback: ConnectCallback  ): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| capability | Array&lt;accessibility.Capability&gt; | Yes |
| connectCallback | [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) |

## Examples

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];
let connectCallback: config.ConnectCallback = {
  onDisconnect: () => {
    console.info(`Ability is disconnected.`);
  }
};

config.enableAbilityWithCallback(name, capability, connectCallback).then(() => {
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
});
```
