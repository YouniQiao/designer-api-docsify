# addDisallowedRunningBundlesSync

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addDisallowedRunningBundlesSync

```TypeScript
function addDisallowedRunningBundlesSync(
    admin: Want,
    appIds: Array<string>,
    accountId?: number
  ): void
```

添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。从API version 21开始，如果应用运行允许名单 [addAllowedRunningBundles](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md)非空，就不能再通过本接口添加应用运行禁止名单，否则会报9200010冲突错误 码。

> **说明：**&gt;
> 若指定应用正在运行，将其加入禁止名单后，系统将立即终止该应用进程。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| appIds | Array & lt;string & gt; | 是 |
| accountId | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
