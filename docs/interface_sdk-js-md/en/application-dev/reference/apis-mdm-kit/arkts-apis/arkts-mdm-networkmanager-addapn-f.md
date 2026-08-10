# addApn

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## addApn

```TypeScript
function addApn(admin: Want, apnInfo: Record<string, string>): void
```

添加APN（Access Point Name，接入点名称）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function addApn(admin: Want, apnInfo: Record<string, string>): void--><!--Device-networkManager-function addApn(admin: Want, apnInfo: Record<string, string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes | 需要添加的APN参数信息。设置后系统将使用这些参数配置移动数据网络的接入点，影响网络连接方式和数据传输路径。&lt;br/&gt;- apnName： APN配置的名称标识符，必选。&lt;br/&gt;- mcc：3位数字的移动国家代码，必选。&lt;br/&gt;- mnc：2-3位数字的移动网络代码，必选。&lt;br/&gt;- apn：接入点名称，必选。&lt;br/&gt;- type：APN的服务类型，可 选。&lt;br/&gt;- user：APN身份验证的用户名，可选。&lt;br/&gt;- password：APN身份验证的密码，可选。&lt;br/&gt;- proxy：普通数据连接的代理服务器地址，可选。&lt;br/&gt;- mmsproxy：彩信服务的 专用代理地址，可选。&lt;br/&gt;- authType：APN的认证协议类型，可选。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  // Replace with actual values.
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  networkManager.addApn(wantTemp, apnInfo);
  console.info(`Succeeded in adding apn.`);
} catch (err) {
  console.error(`Failed to add apn. Code: ${err.code}, message: ${err.message}`);
}
```

