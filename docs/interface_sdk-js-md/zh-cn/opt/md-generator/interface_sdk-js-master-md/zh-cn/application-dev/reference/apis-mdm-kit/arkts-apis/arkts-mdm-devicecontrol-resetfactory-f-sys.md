# resetFactory（系统接口）

## resetFactory

```TypeScript
function resetFactory(admin: Want, callback: AsyncCallback<void>): void
```

使设备恢复出厂设置。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operateDevice)(admin: Want, operation: Operation, addition?: string)

**需要权限：** ohos.permission.ENTERPRISE_RESET_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceControl-function resetFactory(admin: Want, callback: AsyncCallback<void>): void--><!--Device-deviceControl-function resetFactory(admin: Want, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceControl.resetFactory(wantTemp, (err) => {
  if (err) {
    console.error(`Failed to reset factory. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in resetting factory');
})
```


## resetFactory

```TypeScript
function resetFactory(admin: Want): Promise<void>
```

使设备恢复出厂设置。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operateDevice)(admin: Want, operation: Operation, addition?: string)

**需要权限：** ohos.permission.ENTERPRISE_RESET_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceControl-function resetFactory(admin: Want): Promise<void>--><!--Device-deviceControl-function resetFactory(admin: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

deviceControl.resetFactory(wantTemp).then(() => {
}).catch((err: BusinessError) => {
  console.error(`Failed to reset factory. Code is ${err.code}, message is ${err.message}`);
})
```
