# operateDevice

## operateDevice

```TypeScript
function operateDevice(admin: Want, operate: string, addition?: string): void
```

允许管理员对设备执行恢复出厂设置、重启、关机、锁屏等操作，例如在企业设备管理场景下，管理员可远程控制员工设备执行恢复出厂设置、重启、关机或锁屏等操作。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_OPERATE_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceControl-function operateDevice(admin: Want, operate: string, addition?: string): void--><!--Device-deviceControl-function operateDevice(admin: Want, operate: string, addition?: string): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| operate | string | 是 |
| [addition](../../apis-test-kit/arkts-apis/arkts-test-uitest-inputtextmode-i.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  deviceControl.operateDevice(wantTemp, 'resetFactory');
} catch (err) {
  console.error(`Failed to reset factory. Code is ${err.code}, message is ${err.message}`);
}
```


## operateDevice

```TypeScript
function operateDevice(admin: Want, operation: Operation, addition?: string): void
```

允许管理员操作设备，例如在企业设备管理场景下，管理员可远程控制员工设备执行磁盘擦除、恢复出厂设置、重启、关机、锁屏、锁定设备或解锁设备等操作。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_OPERATE_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceControl-function operateDevice(admin: Want, operation: Operation, addition?: string): void--><!--Device-deviceControl-function operateDevice(admin: Want, operation: Operation, addition?: string): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| operation | [Operation](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-operation-e.md) | 是 |
| [addition](../../apis-test-kit/arkts-apis/arkts-test-uitest-inputtextmode-i.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| 9201048 |
| [9200010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let filePath: string = '/test.png';

try {
  // 参数需根据实际情况进行替换
  deviceControl.operateDevice(wantTemp, deviceControl.Operation.DISK_ERASURE, filePath);
} catch (err) {
  console.error(`Failed to disk erase. Code is ${err.code}, message is ${err.message}`);
}
```
