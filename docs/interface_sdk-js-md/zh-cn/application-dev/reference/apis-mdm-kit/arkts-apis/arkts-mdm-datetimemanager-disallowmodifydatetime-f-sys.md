# disallowModifyDateTime（系统接口）

## 导入模块

```TypeScript
import { dateTimeManager } from 'kits/@kit.MDMKit';
```

## disallowModifyDateTime

```TypeScript
function disallowModifyDateTime(admin: Want, disallow: boolean, callback: AsyncCallback<void>): void
```

禁止设备修改系统时间。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**需要权限：** ohos.permission.ENTERPRISE_SET_DATETIME

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| disallow | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## disallowModifyDateTime

```TypeScript
function disallowModifyDateTime(admin: Want, disallow: boolean): Promise<void>
```

禁止设备修改系统时间。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**需要权限：** ohos.permission.ENTERPRISE_SET_DATETIME

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| disallow | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
