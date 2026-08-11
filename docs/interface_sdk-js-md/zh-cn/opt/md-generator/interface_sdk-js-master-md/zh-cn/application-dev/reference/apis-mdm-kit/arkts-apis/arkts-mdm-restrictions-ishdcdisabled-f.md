# isHdcDisabled

## isHdcDisabled

```TypeScript
function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void
```

查询HDC是否被禁用。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin:

**需要权限：** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void--><!--Device-restrictions-function isHdcDisabled(admin: Want, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.isHdcDisabled(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to query is hdc disabled or not. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying is hdc disabled : ${result}`);
})
```


## isHdcDisabled

```TypeScript
function isHdcDisabled(admin: Want): Promise<boolean>
```

查询HDC是否被禁用。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin:

**需要权限：** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function isHdcDisabled(admin: Want): Promise<boolean>--><!--Device-restrictions-function isHdcDisabled(admin: Want): Promise<boolean>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

restrictions.isHdcDisabled(wantTemp).then((result) => {
  console.info(`Succeeded in querying is hdc disabled : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query is hdc disabled or not. Code is ${err.code}, message is ${err.message}`);
})
```
