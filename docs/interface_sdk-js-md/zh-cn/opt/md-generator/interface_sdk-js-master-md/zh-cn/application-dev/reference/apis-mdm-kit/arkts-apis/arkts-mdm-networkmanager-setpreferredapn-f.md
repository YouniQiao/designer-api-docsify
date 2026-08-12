# setPreferredApn

## setPreferredApn

```TypeScript
function setPreferredApn(admin: Want, apnId: string): void
```

设置优选APN。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-networkManager-function setPreferredApn(admin: Want, apnId: string): void--><!--Device-networkManager-function setPreferredApn(admin: Want, apnId: string): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| apnId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; // 需根据实际情况进行替换
try {
  networkManager.setPreferredApn(wantTemp, apnId);
  console.info(`Succeeded in setting preferred apn.`);
} catch (err) {
  console.error(`Failed to set preferred apn. Code: ${err.code}, message: ${err.message}`);
}
```
