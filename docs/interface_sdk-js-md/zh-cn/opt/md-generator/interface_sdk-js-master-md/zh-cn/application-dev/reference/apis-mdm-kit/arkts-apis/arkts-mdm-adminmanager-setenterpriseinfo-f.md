# setEnterpriseInfo

## setEnterpriseInfo

```TypeScript
function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo, callback: AsyncCallback<void>): void
```

设置设备管理应用的企业信息。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.SET_ENTERPRISE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-adminManager-function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo, callback: AsyncCallback<void>): void--><!--Device-adminManager-function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| enterpriseInfo | [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |

## 示例

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let enterpriseInfo: adminManager.EnterpriseInfo = {
  // 需根据实际情况进行替换
  name: 'enterprise name',
  description: 'enterprise description'
};

adminManager.setEnterpriseInfo(wantTemp, enterpriseInfo, (err) => {
  if (err) {
    console.error(`Failed to set enterprise info. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting enterprise info');
});
```


## setEnterpriseInfo

```TypeScript
function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo): Promise<void>
```

设置设备管理应用的企业信息。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.SET_ENTERPRISE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-adminManager-function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo): Promise<void>--><!--Device-adminManager-function setEnterpriseInfo(admin: Want, enterpriseInfo: EnterpriseInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| enterpriseInfo | [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |

## 示例

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let enterpriseInfo: adminManager.EnterpriseInfo = {
  // 需根据实际情况进行替换
  name: 'enterprise name',
  description: 'enterprise description'
};

adminManager.setEnterpriseInfo(wantTemp, enterpriseInfo).catch((err: BusinessError) => {
  console.error(`Failed to set enterprise info. Code: ${err.code}, message: ${err.message}`);
});
```
