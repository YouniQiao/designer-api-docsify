# removePreferencesFromCache

## Modules to Import

```TypeScript
import { sendablePreferences } from 'kits/@kit.ArkData';
```

## removePreferencesFromCache

```TypeScript
function removePreferencesFromCache(context: Context, options: Options): Promise<void>
```

Removes a **Preferences** instance from the cache. This API uses a promise to return the result. After an application calls [getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md) for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls [getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md) again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| options | [Options](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [15500000](../errorcode-preferences.md#15500000-internal-error) |
| [15501001](../errorcode-preferences.md#15501001-stage-model-required) |
| [15501002](../errorcode-preferences.md#15501002-invalid-datagroupid-parameter-in-options) |
