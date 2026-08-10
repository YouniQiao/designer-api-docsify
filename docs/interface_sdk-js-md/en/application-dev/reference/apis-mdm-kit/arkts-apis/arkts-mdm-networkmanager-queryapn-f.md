# queryApn

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## queryApn

```TypeScript
function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>
```

查询符合特定APN信息的APN ID。适用于企业移动网络配置审计场景，例如查找特定配置的APN、验证APN配置是否存在、为APN管理操作提供APN ID参数，帮助企业查找和管理APN配置，为APN的更新和删除操作提供必要的参数信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>--><!--Device-networkManager-function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes | APN的查询条件。设置后系统将根据这些条件筛选匹配的APN配置，返回符合条件的APN ID列表。&lt;br/&gt;- apnName：APN配置的名称 标识符，可选。&lt;br/&gt;- mcc：3位数字的移动国家代码，可选。&lt;br/&gt;- mnc：2-3位数字的移动网络代码，可选。&lt;br/&gt;- apn：接入点名称，可选。&lt;br/&gt;- type：APN的服务类型，可选。&lt;br/&gt;- user：APN身份验证的用户名，可选。&lt;br/&gt;- proxy：普通数据连接的代理服务器地址，可选。&lt;br/&gt;- mmsproxy：彩信服务的专用代理地址，可选。&lt;br/&gt;- authType：APN的认证协议类型，可 选。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 满足要求的APN ID。 |

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
  let queryResult: Array<string> = networkManager.queryApn(wantTemp, apnInfo);
  console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
} catch (err) {
  console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
}
```


## queryApn

```TypeScript
function queryApn(admin: Want, apnId: string): Record<string, string>
```

查询特定APN的APN参数信息。适用于企业移动网络配置审计场景，例如检查特定APN的配置参数、验证APN配置是否正确、审计移动网络接入点配置，帮助企业审核和验证APN配置，确保移动网络配置符合要求。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function queryApn(admin: Want, apnId: string): Record<string, string>--><!--Device-networkManager-function queryApn(admin: Want, apnId: string): Record<string, string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnId | string | Yes | 指定的APN ID。设置后将查询该APN ID对应的详细参数配置信息。可以通过 [networkManager.queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn)获取设备信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | 指定APN ID的APN参数信息。&lt;br/&gt;- apnName：APN配置的名称标识符。&lt;br/&gt;- mcc：3位数字的移动国家代码。&lt;br/&gt;- mnc：2 -3位数字的移动网络代码。&lt;br/&gt;- apn：接入点名称。&lt;br/&gt;- type：APN的服务类型。&lt;br/&gt;- user：APN身份验证的用户名。&lt;br/&gt;- proxy：普通数据连接的代理服务器地址。&lt;br/&gt;- mmsproxy：彩信服务的专用代理地址。&lt;br/&gt;- authType：APN的认证协议类型。 |

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
let apnId: string = "1"; // Replace it as required.
try {
  let queryResult: Record<string, string> = networkManager.queryApn(wantTemp, apnId);
  console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
} catch (err) {
  console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
}
```

