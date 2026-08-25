# addAllowedDistributeAbilityConnBundles

## 导入模块

```TypeScript
import { applicationManager } from '@kit.MDMKit';
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

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

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

**示例**

```TypeScript
import { applicationManager, restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

// 如果要在100用户下，禁止设备上除了指定应用以外的其他应用向其他设备传输数据，需要执行两个步骤：
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let accountId: number = 100;

// 步骤1. 禁用100用户下的设备间单向传输数据能力（若之前已经设置过设备间单向传输数据能力的禁用，此处无需重复设置）
try {
  restrictions.setDisallowedPolicyForAccount(wantTemp, restrictions.FeatureForAccount.DISTRIBUTED_TRANSMISSION_OUTGOING, true, accountId);
  console.info('Succeeded in setting distributedTransmissionOutgoing disabled');
} catch (err) {
  console.error(`Failed to set distributedTransmissionOutgoing disabled. Code is ${err.code}, message is ${err.message}`);
}

// 步骤2. 设置100用户下允许使用某种分布式业务（例如协同业务）的应用名单
try {
  // 需根据实际情况进行替换
  let appIdentifiers: Array<string> = ['6917****3569'];
  applicationManager.addAllowedDistributeAbilityConnBundles(wantTemp, appIdentifiers,
    applicationManager.ServiceType.COLLABORATION_SERVICE, accountId);
  console.info('Succeeded in adding allowed distribute ability conn bundles.');
} catch (err) {
  console.error(`Failed to add allowed distribute ability conn bundles. Code: ${err.code}, message: ${err.message}`);
}
// 执行以上两个步骤后，在100用户下，仅应用6917****3569可以通过协同业务向其他设备传输数据，其他应用无法向其他设备传输数据。
// 注意：禁用某用户下的设备间单向传输数据能力后，是否需要添加允许使用协同业务的应用名单，应根据实际业务需求判断。
```
