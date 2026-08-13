# getDisallowedNearLinkProtocols

## getDisallowedNearLinkProtocols

```TypeScript
function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>
```

获取指定用户下禁用的星闪协议名单。适用于需要查询用户当前星闪协议访问限制的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**起始版本：** 20

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-systemManager-function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>--><!--Device-systemManager-function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[NearLinkProtocol](arkts-mdm-systemmanager-nearlinkprotocol-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let accountId: number = 100;

try {
  let result: systemManager.NearLinkProtocol[] = systemManager.getDisallowedNearLinkProtocols(wantTemp, accountId);
  console.info(`Succeeded in querying the disabled Starlink protocol list for the specified user: ${result}`);
} catch (err) {
  console.error(`Failed to query the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
}
```
