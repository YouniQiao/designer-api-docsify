# getPreferencesSync

## Modules to Import

```TypeScript
import { sendablePreferences } from '@kit.ArkData';
```

## getPreferencesSync

```TypeScript
function getPreferencesSync(context: Context, options: Options): Preferences
```

Obtains a **Preferences** instance. This API returns the result synchronously.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-sendablePreferences-function getPreferencesSync(context: Context, options: Options): Preferences--><!--Device-sendablePreferences-function getPreferencesSync(context: Context, options: Options): Preferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Preferences](arkts-arkdata-preferences-preferences-i.md) |

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

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    preferences = sendablePreferences.getPreferencesSync(this.context, options);
  }
}
```
