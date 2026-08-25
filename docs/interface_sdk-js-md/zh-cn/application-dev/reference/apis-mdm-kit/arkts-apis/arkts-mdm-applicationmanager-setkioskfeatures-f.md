# setKioskFeatures

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## setKioskFeatures

```TypeScript
function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void
```

设置Kiosk模式的特征。通过本接口可以控制在Kiosk模式下能否进入通知中心、控制中心。从API version 24开始，新增支持设置是否允许底部上滑进入最近任务栏，左滑或右滑悬停展示侧边DOCK栏。在非Kiosk模式下，本接口可以正常调用，但是不会生效，进入Kiosk模式后才会生效。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_SET_KIOSK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| features | Array&lt;[KioskFeature](arkts-mdm-applicationmanager-kioskfeature-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
