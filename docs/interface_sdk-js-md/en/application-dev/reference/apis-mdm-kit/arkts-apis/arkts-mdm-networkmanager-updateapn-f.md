# updateApn

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## updateApn

```TypeScript
function updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void
```

更新APN。适用于企业移动网络配置管理场景，例如修改APN配置参数、调整运营商设置、优化移动网络连接性能，帮助企业灵活调整移动网络配置，确保设备移动网络连接参数符合实际需求。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void--><!--Device-networkManager-function updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes | 需要更新的APN参数信息。设置后系统将使用更新后的参数修改对应APN配置，影响网络连接方式和数据传输路径。&lt;br/&gt;- apnName：APN 配置的名称标识符，可选。&lt;br/&gt;- mcc：3位数字的移动国家代码，可选。&lt;br/&gt;- mnc：2-3位数字的移动网络代码，可选。&lt;br/&gt;- APN：接入点名称，可选。&lt;br/&gt;- type：APN的服务类型，可选。&lt; br/&gt;- user：APN身份验证的用户名，可选。&lt;br/&gt;- password：APN身份验证的密码，可选。&lt;br/&gt;- proxy：普通数据连接的代理服务器地址，可选。&lt;br/&gt;- mmsproxy：彩信服务的专用代 理地址，可选。&lt;br/&gt;- authType：APN的认证协议类型，可选。 |
| apnId | string | Yes | 需要更新的APN ID。可以通过[networkManager.queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn)获取设备APN信息。 |

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
let apnId: string = "1"; // Replace it as required.
try {
  networkManager.updateApn(wantTemp, apnInfo, apnId);
  console.info(`Succeeded in updating apn.`);
} catch (err) {
  console.error(`Failed to update apn. Code: ${err.code}, message: ${err.message}`);
}
```

