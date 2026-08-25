# finishLogCollected

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## finishLogCollected

```TypeScript
function finishLogCollected(admin: Want): void
```

删除本MDM应用在当前用户下收集到的设备日志。

> **说明：**&gt;
> 在应用调用[startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md)开始收集日志后，收到
> [EnterpriseAdminExtensionAbility.onLogCollected](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onlogcollected)
> 回调时，建议立即拷贝或者处理日志，并调用此接口删除收集到的日志。&gt;
> 若不调本接口，设备日志会占用系统存储空间，不影响下一次调用[startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md)启动日志收集任务。

**起始版本：** 23

**需要权限：** ohos.permission.ENTERPRISE_READ_LOG

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
