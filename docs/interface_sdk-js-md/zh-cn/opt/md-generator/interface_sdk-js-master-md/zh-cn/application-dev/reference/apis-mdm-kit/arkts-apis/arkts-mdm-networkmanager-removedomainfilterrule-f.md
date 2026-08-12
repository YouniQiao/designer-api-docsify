# removeDomainFilterRule

## removeDomainFilterRule

```TypeScript
function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void
```

移除设备域名过滤规则。适用于企业网络安全策略调整场景，例如取消某些域名访问限制、调整域名过滤策略、清理过时或无效的规则、解决误拦截问题，帮助企业灵活调整域名访问策略，确保网络访问控制策略符合实际需求。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md#LogType)。

移除规则后如果不存在[Action](arkts-mdm-networkmanager-action-e.md#Action)为ALLOW规则后，会将  
[addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#addDomainFilterRule)添加的默认DENY规则清空。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-networkManager-function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void--><!--Device-networkManager-function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| domainFilterRule | [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let domainFilterRule: networkManager.DomainFilterRule = {
  // 需根据实际情况进行替换
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1,
  "logType": networkManager.LogType.NFLOG
};

// 移除指定的规则
try {
  networkManager.removeDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in removing domain filter rules');
} catch (err) {
  console.error(`Failed to remove domain filter rules. Code: ${err.code}, message: ${err.message}`);
}

// 清空IP协议版本为IPv4的所有规则
try {
  networkManager.removeDomainFilterRule(wantTemp);
  console.info('Succeeded in removing all domain filter rules');
} catch (err) {
  console.error(`Failed to remove all domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```
