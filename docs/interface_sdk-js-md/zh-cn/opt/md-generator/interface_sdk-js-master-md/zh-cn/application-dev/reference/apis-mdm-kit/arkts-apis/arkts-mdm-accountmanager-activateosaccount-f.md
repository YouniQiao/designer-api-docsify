# activateOsAccount

## activateOsAccount

```TypeScript
function activateOsAccount(admin: Want, accountId: number): Promise<void>
```

切换系统账号。当前仅支持手机、平板设备使用，只能在[createNormalOsAccount](arkts-mdm-accountmanager-createnormalosaccount-f.md#createnormalosaccount)创建的普通系统账号和默认系统账号 (ID为100) 之间切换。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-accountManager-function activateOsAccount(admin: Want, accountId: number): Promise<void>--><!--Device-accountManager-function activateOsAccount(admin: Want, accountId: number): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9201046](../errorcode-enterpriseDeviceManager.md#9201046-已登录系统账号数量达到上限) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9201041](../errorcode-enterpriseDeviceManager.md#9201041-系统账号类型受限) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { osAccount } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 创建普通系统账号
accountManager.createNormalOsAccount(wantTemp, "TestAccountName").then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('Succeeded in creating normal os account, accountInfo: ' + JSON.stringify(accountInfo));
  // 根据系统账号ID切换账号
  let accountId: number = accountInfo.localId;
  return accountManager.activateOsAccount(wantTemp, accountId);
}).then(() => {
  console.info('Succeeded in activating os account');
}).catch((err: BusinessError) => {
  console.error(`Failed to create and activate normal os account: code is ${err.code}, message is ${err.message}`);
});
```
