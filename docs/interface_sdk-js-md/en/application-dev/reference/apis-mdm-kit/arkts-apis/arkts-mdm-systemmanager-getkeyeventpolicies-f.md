# getKeyEventPolicies

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>
```

获取按键事件处理策略。适用于需要查询当前按键事件处理策略配置的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>--><!--Device-systemManager-function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;KeyEventPolicy&gt; | 返回当前配置的按键事件策略列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |


## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>
```

获取按键事件处理策略。适用于需要查询当前按键事件处理策略配置的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>--><!--Device-systemManager-function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;KeyEventPolicy&gt; | 返回当前配置的按键事件策略列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let result: Array<systemManager.KeyEventPolicy> = [];
try {
  result = systemManager.getKeyEventPolicies(wantTemp);
  console.info('Succeeded in getting key event policies.');
} catch (err) {
  console.error(`Failed to get key event policies. Code is ${err.code}, message is ${err.message}`);
}
```

