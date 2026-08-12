# deletePreferences

## Modules to Import

```TypeScript
import { sendablePreferences } from '@kit.ArkData';
```

## deletePreferences

```TypeScript
function deletePreferences(context: Context, options: Options): Promise<void>
```

Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding persistent file, the persistent file is also deleted. This API uses a promise to return the result.Avoid using a deleted **Preferences** instance to perform data operations, which may cause data inconsistency.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendablePreferences-function deletePreferences(context: Context, options: Options): Promise<void>--><!--Device-sendablePreferences-function deletePreferences(context: Context, options: Options): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Application context. |
| options | Options | Yes | Configuration options of the **Preferences** instance. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [15501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501001-stage-model-required) | The operations is supported in stage mode only. |
| [15500010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500010-failed-to-delete-the-user-preference-persistence-file) | Failed to delete the user preferences persistence file. |
| [15501002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) | Invalid dataGroupId. |
| [15500000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-internal-error) | Inner error. |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.deletePreferences(this.context, options);
    promise.then(() => {
      console.info("Succeeded in deleting preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete preferences. code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

