# addAllowedDistributeAbilityConnBundles

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addAllowedDistributeAbilityConnBundles

```TypeScript
function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void
```

为指定用户下的特定分布式业务添加允许跨设备的应用名单。即名单中的应用可以不受 [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)的限制， 通过使用该特定分布式业务跨设备传输数据。当前支持的分布式业务类型有：[协同业务](arkts-mdm-applicationmanager-servicetype-e.md)。

> **说明：**&gt;
> 1.如果要设置允许使用特定分布式业务的应用名单，在调用本接口前必须已经通过
> [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)接口
> 禁用了向其他设备传输数据的设备间单向传输数据的能力，否则会抛出错误码9201043。

> 2.当向其他设备传输数据的设备间单向传输数据的能力被解除禁用时，通过本接口设置的允许使用特定分布式业务的应用名单会被同步清除。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| appIdentifiers | Array & lt;string & gt; | 是 |
| serviceType | [ServiceType](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-servicetype-e.md) | 是 |
| accountId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201043](../errorcode-enterpriseDeviceManager.md#9201043-api调用的前置条件未满足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
