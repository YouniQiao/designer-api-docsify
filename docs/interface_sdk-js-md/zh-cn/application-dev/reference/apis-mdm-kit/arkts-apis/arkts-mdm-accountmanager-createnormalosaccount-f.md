# createNormalOsAccount

## 导入模块

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## createNormalOsAccount

```TypeScript
function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>
```

创建普通系统账号。最多可以创建2个normal类型的系统账号 ([osAccount.OsAccountType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccounttype-e.md)) 。

> **说明：**&gt;
> 创建账号的流程比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。&gt;
> 创建系统账号对设备的性能影响较大，此接口仅支持12GB及以上运行内存的手机、平板设备使用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;osAccount.OsAccountInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201003](../errorcode-enterpriseDeviceManager.md#9201003-创建账号失败) |
| [9201040](../errorcode-enterpriseDeviceManager.md#9201040-系统账号数量已达到最大限制) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
