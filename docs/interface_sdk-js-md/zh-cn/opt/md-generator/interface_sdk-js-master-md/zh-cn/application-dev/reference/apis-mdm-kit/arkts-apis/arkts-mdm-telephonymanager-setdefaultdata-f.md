# setDefaultData

## setDefaultData

```TypeScript
function setDefaultData(admin: Want, slotId: number): void
```

设置指定卡槽的SIM卡为默认数据流量卡，设备将使用指定卡槽的SIM卡流量上网。例如，企业可在双卡设备管理场景中，为员工设备指定默认的数据流量卡以统一管理流量使用。该接口需要插入SIM卡并关闭飞行模式才能成功调用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-telephonyManager-function setDefaultData(admin: Want, slotId: number): void--><!--Device-telephonyManager-function setDefaultData(admin: Want, slotId: number): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| slotId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201020](../errorcode-enterpriseDeviceManager.md#9201020-设置默认数据流量卡失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [203](../../errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 设置要作为默认数据流量卡的卡槽ID
let slotId: number = 0;
try {
  // 设置指定卡槽为默认数据流量卡
  telephonyManager.setDefaultData(wantTemp, slotId);
  console.info(`success to set default data SIM ID`);
} catch (err) {
  console.error(`Failed to set default data. Code: ${err.code}, message: ${err.message}`);
}
```
