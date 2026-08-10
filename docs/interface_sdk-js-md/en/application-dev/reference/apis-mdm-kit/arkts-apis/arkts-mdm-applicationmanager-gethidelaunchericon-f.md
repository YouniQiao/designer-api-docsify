# getHideLauncherIcon

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## getHideLauncherIcon

```TypeScript
function getHideLauncherIcon(admin: Want | null): Array<string>
```

查询当前用户下隐藏桌面应用图标名单。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getHideLauncherIcon(admin: Want | null): Array<string>--><!--Device-applicationManager-function getHideLauncherIcon(admin: Want | null): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。&lt;br/&gt;当设备存在多个MDM应用时，传入 admin查询对应admin设置的策略。传入null时查询整机实际生效的策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回当前用户下的隐藏桌面应用图标名单。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let bundleNames: Array<string> = applicationManager.getHideLauncherIcon(wantTemp);
  console.info('Succeeded in getting hide launcher icon.');
} catch (err) {
  console.error(`Failed to get hide launcher icon. Code is ${err.code}, message is ${err.message}`);
}
```

