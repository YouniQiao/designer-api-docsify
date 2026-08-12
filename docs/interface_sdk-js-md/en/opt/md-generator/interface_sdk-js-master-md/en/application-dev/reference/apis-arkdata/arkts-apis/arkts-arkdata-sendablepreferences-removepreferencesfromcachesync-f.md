# removePreferencesFromCacheSync

## Modules to Import

```TypeScript
import { sendablePreferences } from '@kit.ArkData';
```

## removePreferencesFromCacheSync

```TypeScript
function removePreferencesFromCacheSync(context: Context, options: Options): void
```

Removes a **Preferences** instance from the cache. This API returns the result synchronously.After an application calls [getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md#getPreferences) for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls   
[getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md#getPreferences) again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendablePreferences-function removePreferencesFromCacheSync(context: Context, options: Options): void--><!--Device-sendablePreferences-function removePreferencesFromCacheSync(context: Context, options: Options): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [15501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501001-stage-model-required) |
| [15501002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) |
| [15500000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-internal-error) |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    sendablePreferences.removePreferencesFromCacheSync(this.context, options);
  }
}
```
