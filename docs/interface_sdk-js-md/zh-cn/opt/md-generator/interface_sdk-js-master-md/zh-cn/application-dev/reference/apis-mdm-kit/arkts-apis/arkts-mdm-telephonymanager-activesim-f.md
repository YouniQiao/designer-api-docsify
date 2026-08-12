# activeSim

## activeSim

```TypeScript
function activeSim(admin: Want, slotId: number): void
```

启用指定卡槽的SIM卡。设备已经插入SIM卡但是并未启用的场景，可以通过该接口启用SIM卡，无需用户手动启用。SIM卡启用后可以使用该SIM卡进行通信。该接口需要插入SIM卡并关闭飞行模式才能成功调用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-telephonyManager-function activeSim(admin: Want, slotId: number): void--><!--Device-telephonyManager-function activeSim(admin: Want, slotId: number): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| slotId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [9201017](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201017-启用sim或停用sim卡失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [203](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 设置要启用的卡槽ID
let slotId: number = 0;
try {
  // 启用指定卡槽的SIM卡
  telephonyManager.activeSim(wantTemp, slotId);
  console.info(`success to active SIM`);
} catch (err) {
  console.error(`Failed to active SIM. Code: ${err.code}, message: ${err.message}`);
}
```
