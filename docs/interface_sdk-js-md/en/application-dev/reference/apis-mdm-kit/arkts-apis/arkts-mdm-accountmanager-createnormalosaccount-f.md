# createNormalOsAccount

## Modules to Import

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## createNormalOsAccount

```TypeScript
function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>
```

创建普通系统账号。最多可以创建2个normal类型的系统账号 ([osAccount.OsAccountType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccounttype-e.md/arkts-basicservices-osaccount-osaccounttype-e.md)) 。

> **说明：**
> 
> 创建账号的流程比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。
> 
> 创建系统账号对设备的性能影响较大，此接口仅支持12GB及以上运行内存的手机、平板设备使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>--><!--Device-accountManager-function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| name | string | Yes | 系统账号名称。系统账号名称不能重复且不能为空，会报错误码9200012。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;osAccount.OsAccountInfo&gt; | Promise对象，返回创建的系统账号信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 9201003 | Failed to add an OS account. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9201040 | The number of accounts reaches the upper limit. |
| 204 | Access denied due to user access control policy. Possible causes: 1. The operation is restricted by the OS-account constraint. 2. The required privilege for the operation has not been granted. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { osAccount } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Create a normal system account. The account name needs to be passed.
accountManager.createNormalOsAccount(wantTemp, "TestAccountName").then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('Succeeded in creating normal os account, accountInfo: ' + JSON.stringify(accountInfo));
}).catch((err: BusinessError) => {
  console.error(`Failed to create normal os account: code is ${err.code}, message is ${err.message}`);
});
```

