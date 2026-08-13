# getPreferences

## Modules to Import

```TypeScript
import { sendablePreferences } from '@kit.ArkData';
```

## getPreferences

```TypeScript
function getPreferences(context: Context, options: Options): Promise<Preferences>
```

Obtains a **Preferences** instance. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendablePreferences-function getPreferences(context: Context, options: Options): Promise<Preferences>--><!--Device-sendablePreferences-function getPreferences(context: Context, options: Options): Promise<Preferences>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Application context. |
| options | Options | Yes | Configuration options of the **Preferences** instance. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Preferences&gt; | Promise used to return the **Preferences** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [15501001](../errorcode-preferences.md#15501001-stage-model-required) | The operations is supported in stage mode only. |
| [15501002](../errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) | Invalid dataGroupId. |
| [15500000](../errorcode-preferences.md#15500000-internal-error) | Inner error. |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.getPreferences(this.context, options);
    promise.then((object: sendablePreferences.Preferences) => {
      preferences = object;
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to get preferences. code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

