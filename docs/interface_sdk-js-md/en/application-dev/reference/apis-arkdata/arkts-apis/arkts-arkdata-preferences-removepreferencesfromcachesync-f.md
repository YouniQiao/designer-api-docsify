# removePreferencesFromCacheSync

## Modules to Import

```TypeScript
import { preferences } from '@kit.ArkData';
```

## removePreferencesFromCacheSync

```TypeScript
function removePreferencesFromCacheSync(context: Context, name: string): void
```

Removes a **Preferences** instance from the cache. This API returns the result synchronously.After an application calls   
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls   
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency. Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.If [GSKV](../../../database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the number of data cache pages that are not written to the disk.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-preferences-function removePreferencesFromCacheSync(context: Context, name: string): void--><!--Device-preferences-function removePreferencesFromCacheSync(context: Context, name: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Application context.&lt;br&gt;For details about the application context of the FA model, see [Context](./app/context).&lt;br&gt;For details about the application context of the stage model, see [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#Context). |
| name | string | Yes | Name of the **Preferences** instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [15500000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

## Examples

FA model:

```TypeScript
// Obtain the context.
import { featureAbility } from '@kit.AbilityKit';
let context = featureAbility.getContext();
preferences.removePreferencesFromCacheSync(context, 'myStore');
```

Stage model:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.removePreferencesFromCacheSync(this.context, 'myStore');
  }
}
```


## removePreferencesFromCacheSync

```TypeScript
function removePreferencesFromCacheSync(context: Context, options: Options): void
```

Removes a **Preferences** instance from the cache. This API returns the result synchronously.After an application calls   
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls   
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency. Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.If [GSKV](../../../database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the number of data cache pages that are not written to the disk.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-preferences-function removePreferencesFromCacheSync(context: Context, options: Options): void--><!--Device-preferences-function removePreferencesFromCacheSync(context: Context, options: Options): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Application context.&lt;br&gt;For details about the application context of the FA model, see [Context](./app/context).&lt;br&gt;For details about the application context of the stage model, see [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#Context). |
| options | Options | Yes | Configuration options of the **Preferences** instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [15501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501001-stage-model-required) | The operations is supported in stage mode only. |
| [15501002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) | Invalid dataGroupId. |
| [15500000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-internal-error) | Inner error.<br>**Applicable version:** 11 and later |

## Examples

FA model:

```TypeScript
// Obtain the context.
import { featureAbility } from '@kit.AbilityKit';
let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
preferences.removePreferencesFromCacheSync(context, options);
```

Stage model:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.removePreferencesFromCacheSync(this.context, options);
  }
}
```

