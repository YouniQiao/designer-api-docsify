# setPolicySync

## setPolicySync

```TypeScript
function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void
```

为指定的浏览器设置浏览器子策略，适用于企业统一管理员工浏览器行为的场景。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-browser-function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void--><!--Device-browser-function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| appId | string | 是 |
| policyName | string | 是 |
| policyValue | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 此处参数appId的赋值应替换为开发者自己指定的浏览器的应用ID
let appId: string = 'com.example.******_******/******5t5CoBM=';
// 浏览器策略名称
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
// 浏览器策略值
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setPolicySync(wantTemp, appId, policyName, policyValue);
  console.info('Succeeded in setting browser policies.');
} catch (err) {
  console.error(`Failed to set browser policies. Code is ${err.code}, message is ${err.message}`);
}
```
