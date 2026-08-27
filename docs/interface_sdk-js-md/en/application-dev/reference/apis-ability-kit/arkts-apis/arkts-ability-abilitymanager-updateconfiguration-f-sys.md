# updateConfiguration (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

Updates the configuration. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | New configuration. You only need to configure the items to be updated. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined**. Otherwise, **err** is an error object. You can perform error handling or other custom processing. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { abilityManager, Configuration, ConfigurationConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const config: Configuration = {
  language: 'Zh-Hans',                 // Simplified Chinese
  colorMode: ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT,         // Light theme.
  direction: ConfigurationConstant.Direction.DIRECTION_VERTICAL,       // Vertical direction.
  screenDensity: ConfigurationConstant.ScreenDensity.SCREEN_DENSITY_SDPI,  // The screen pixel density is sdpi.
  displayId: 1,                        // The application is displayed on the display with ID 1.
  hasPointerDevice: true,              // A pointer device is connected.
};

try {
  abilityManager.updateConfiguration(config, (err: BusinessError) => {
    if (err) {
      console.error(`updateConfiguration fail, err: ${JSON.stringify(err)}`);
    } else {
      console.info('updateConfiguration success.');
    }
  });
} catch (paramError) {
  let code: number = (paramError as BusinessError).code;
  let message: string = (paramError as BusinessError).message;
  console.error(`error.code: ${code}, error.message: ${message}`);
}
```


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

Updates the configuration. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | New configuration. You only need to configure the items to be updated. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. You can perform error handling or other custom processing. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { abilityManager, Configuration, ConfigurationConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const config: Configuration = {
  language: 'Zh-Hans',                 // Simplified Chinese
  colorMode: ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT,         // Light theme.
  direction: ConfigurationConstant.Direction.DIRECTION_VERTICAL,       // Vertical direction.
  screenDensity: ConfigurationConstant.ScreenDensity.SCREEN_DENSITY_SDPI,  // The screen pixel density is sdpi.
  displayId: 1,                        // The application is displayed on the display with ID 1.
  hasPointerDevice: true,              // A pointer device is connected.
};

try {
  abilityManager.updateConfiguration(config).then(() => {
    console.info('updateConfiguration success.');
  }).catch((err: BusinessError) => {
    console.error(`updateConfiguration fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code: number = (paramError as BusinessError).code;
  let message: string = (paramError as BusinessError).message;
  console.error(`error.code: ${code}, error.message: ${message}`);
}
```
