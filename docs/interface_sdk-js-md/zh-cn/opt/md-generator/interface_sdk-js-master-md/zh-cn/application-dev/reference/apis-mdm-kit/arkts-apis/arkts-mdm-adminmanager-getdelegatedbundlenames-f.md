# getDelegatedBundleNames

## getDelegatedBundleNames

```TypeScript
function getDelegatedBundleNames(admin: Want, policy: string): Array<string>
```

查询可以访问某个委托策略的被委托应用，输出被委托应用列表。

**起始版本：** 14

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-adminManager-function getDelegatedBundleNames(admin: Want, policy: string): Array<string>--><!--Device-adminManager-function getDelegatedBundleNames(admin: Want, policy: string): Array<string>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| policy | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let bundleNames: Array<string> = adminManager.getDelegatedBundleNames(admin, "disabled_hdc");
  console.info(`Succeeded in getting delegated bundles.${JSON.stringify(bundleNames)}`);
} catch (err) {
  console.error(`Failed to get delegated bundles. Code: ${err.code}, message: ${err.message}`);
}
```
