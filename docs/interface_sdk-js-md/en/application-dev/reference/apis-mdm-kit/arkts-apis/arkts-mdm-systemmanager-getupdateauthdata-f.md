# getUpdateAuthData

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getUpdateAuthData

```TypeScript
function getUpdateAuthData(admin: Want): Promise<string>
```

获取系统更新的鉴权数据，用于校验系统更新信息。使用Promise异步回调。适用于内网升级场景，企业管理员可以通过鉴权数据验证系统更新包的合法性和完整性，防止恶意更新包，提升系统安全性。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getUpdateAuthData(admin: Want): Promise<string>--><!--Device-systemManager-function getUpdateAuthData(admin: Want): Promise<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回系统更新的鉴权数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
systemManager.getUpdateAuthData(wantTemp).then((result: string) => {
  console.info(`Succeeded in getting update auth data: ${JSON.stringify(result)}`);
}).catch((error: BusinessError) => {
  console.error(`Get update auth data failed. Code is ${error.code},message is ${error.message}`);
});
```

