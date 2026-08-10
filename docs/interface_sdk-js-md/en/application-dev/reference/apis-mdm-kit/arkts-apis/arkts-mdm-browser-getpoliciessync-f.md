# getPoliciesSync

## Modules to Import

```TypeScript
import { browser } from 'kits/@kit.MDMKit';
```

## getPoliciesSync

```TypeScript
function getPoliciesSync(admin: Want, appId: string): string
```

通过appid获取指定浏览器设置的策略，适用于查询当前浏览器策略配置的场景，例如在企业设备管理应用中展示策略详情、验证策略是否生效等。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function getPoliciesSync(admin: Want, appId: string): string--><!--Device-browser-function getPoliciesSync(admin: Want, appId: string): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appId | string | Yes | 应用ID，用于指定浏览器。详情信息可参考 [什么是appId](../../../quick-start/common-problem-of-application.md#什么是appid)。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 浏览器策略。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9200001 | The application is not an administrator application of the device. |


## getPoliciesSync

```TypeScript
function getPoliciesSync(admin: Want | null, appId: string): string
```

通过appid获取指定浏览器设置的策略，适用于查询当前浏览器策略配置的场景，例如在企业设备管理应用中展示策略详情、验证策略是否生效等。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-browser-function getPoliciesSync(admin: Want | null, appId: string): string--><!--Device-browser-function getPoliciesSync(admin: Want | null, appId: string): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |
| appId | string | Yes | 应用ID，用于指定浏览器。详情信息可参考 [什么是appId](../../../quick-start/common-problem-of-application.md#什么是appid)。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 浏览器策略。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9200001 | The application is not an administrator application of the device. |

## Examples

```TypeScript
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace the value of appId with the specified application ID of the browser.
let appId: string = 'com.example.******_******/******5t5CoBM=';

try {
  let result: string = browser.getPoliciesSync(wantTemp, appId);
  console.info(`Succeeded in getting browser policies, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get browser policies. Code is ${err.code}, message is ${err.message}`);
}
```

