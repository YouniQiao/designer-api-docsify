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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendablePreferences-function deletePreferences(context: Context, options: Options): Promise<void>--><!--Device-sendablePreferences-function deletePreferences(context: Context, options: Options): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [15501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501001-stage-model-required) |
| [15500010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500010-failed-to-delete-the-user-preference-persistence-file) |
| [15501002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) |
| [15500000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-internal-error) |

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
