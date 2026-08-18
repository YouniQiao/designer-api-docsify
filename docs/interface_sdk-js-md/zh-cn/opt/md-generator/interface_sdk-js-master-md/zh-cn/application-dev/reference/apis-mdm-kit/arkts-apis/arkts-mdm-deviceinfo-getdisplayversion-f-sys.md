# getDisplayVersion（系统接口）

## 导入模块

```TypeScript
```

## getDisplayVersion

```TypeScript
function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void
```

获取设备版本号，使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getdeviceinfo)

**需要权限：** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceInfo-function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void--><!--Device-deviceInfo-function getDisplayVersion(admin: Want, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceInfo.getDisplayVersion(wantTemp, (err, result) => {
  if (err) {
    console.error(`Failed to get display version. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting display version, result : ${result}`);
});
```


## getDisplayVersion

```TypeScript
function getDisplayVersion(admin: Want): Promise<string>
```

获取设备版本号，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getdeviceinfo)

**需要权限：** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceInfo-function getDisplayVersion(admin: Want): Promise<string>--><!--Device-deviceInfo-function getDisplayVersion(admin: Want): Promise<string>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceInfo.getDisplayVersion(wantTemp).then((result) => {
  console.info(`Succeeded in getting display version, result : ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get display version. Code: ${err.code}, message: ${err.message}`);
});
```
