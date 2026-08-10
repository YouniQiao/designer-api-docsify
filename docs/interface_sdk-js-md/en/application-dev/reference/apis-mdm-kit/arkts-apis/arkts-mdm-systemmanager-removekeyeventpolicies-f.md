# removeKeyEventPolicies

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## removeKeyEventPolicies

```TypeScript
function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void
```

删除按键事件处理策略。删除成功后，系统将恢复对指定按键事件的默认处理行为。适用于需要恢复按键默认行为的场景，帮助企业管理员灵活调整设备按键响应策略，满足不同业务场景的需求。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void--><!--Device-systemManager-function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| keyCodes | Array&lt;KeyCode&gt; | Yes | 按键编码。支持一次删除多条按键策略，删除不支持按键时返回9200012错误码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
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

let keyCodes: Array<systemManager.KeyCode> = [
  systemManager.KeyCode.POWER, systemManager.KeyCode.VOLUME_UP,
];

try {
  systemManager.removeKeyEventPolicies(wantTemp, keyCodes);
  console.info('Succeeded in removing key event policies.');
} catch (err) {
  console.error(`Failed to remove key event policies. Code is ${err.code}, message is ${err.message}`);
}
```

