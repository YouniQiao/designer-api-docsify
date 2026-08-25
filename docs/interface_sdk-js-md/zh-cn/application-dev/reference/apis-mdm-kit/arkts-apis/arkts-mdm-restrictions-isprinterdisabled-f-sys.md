# isPrinterDisabled（系统接口）

## 导入模块

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## isPrinterDisabled

```TypeScript
function isPrinterDisabled(admin: Want, callback: AsyncCallback<boolean>): void
```

查询设备打印能力是否被禁用。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md)(admin: Want | null, feature: FeatureForDevice)

**需要权限：** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## isPrinterDisabled

```TypeScript
function isPrinterDisabled(admin: Want): Promise<boolean>
```

查询设备打印能力是否被禁用。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md)(admin: Want | null, feature: FeatureForDevice)

**需要权限：** ohos.permission.ENTERPRISE_RESTRICT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
