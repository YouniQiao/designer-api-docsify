# updateConfiguration (System API)

## Modules to Import

```TypeScript
```

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

Updates the configuration. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
import abilityManager from '@ohos.application.abilityManager';
import { Configuration } from '@ohos.application.Configuration';

let config: Configuration = {
  language: 'chinese' 
};

abilityManager.updateConfiguration(config, () => {
    console.info('------------ updateConfiguration -----------');
});
```

```TypeScript
import abilityManager from '@ohos.application.abilityManager';
import { Configuration } from '@ohos.application.Configuration';
import { BusinessError } from '@ohos.base';

let config: Configuration = {
  language: 'chinese' 
};

abilityManager.updateConfiguration(config).then(() => {
  console.info('updateConfiguration success');
}).catch((err: BusinessError) => {
  console.error('updateConfiguration fail');
});
```


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

Updates the configuration. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

See [updateConfiguration](#updateconfiguration)
