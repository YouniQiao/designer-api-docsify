# addKeepAliveApps

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addKeepAliveApps

```TypeScript
function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void
```

添加保活应用名单，添加后将自动保活应用进程。在开机和应用被杀死后，由系统主动拉起应用进程。通过本接口添加至保活名单的应用，禁止用户在设备上手动取消保活，但可通过 [removeKeepAliveApps](arkts-mdm-applicationmanager-removekeepaliveapps-f.md)接口将应用从保活名单中移除。如果将应用添加至应用禁止运行名单[addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md)，就不能将应用添 加至保活应用名单，否则会报9200010冲突错误码。如果需要在Phone/Tablet设备使用类似功能，可以调用[addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md)或者 [addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md)接口，具体功能请参考相关文档。

**起始版本：** 14

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleNames | Array & lt;string & gt; | 是 |
| accountId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [9201005](../errorcode-enterpriseDeviceManager.md#9201005-添加保活应用失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## addKeepAliveApps

```TypeScript
function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void
```

添加保活应用名单，并设置是否禁止用户手动取消保活，添加后将自动保活应用进程。在开机和应用被杀死后，由系统主动拉起应用进程。通过本接口、[addKeepAliveApps](#addkeepaliveapps)接口均可添加保活应用名单，两个接口的设置可同时生效。同一用户下，保活应用名单最多支持包含5个应 用。例如：若当前名单中已有3个应用，则最多还能通过本接口为当前用户添加2个应用。如果通过[addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md)接口将应用添加至应用禁止运行名单，就不能 将应用添加至保活应用名单，否则会报9200010冲突错误码。如果需要在Phone/Tablet设备使用类似功能，可以调用[addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md)或者 [addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md)接口，具体功能请参考相关文档。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleNames | Array & lt;string & gt; | 是 |
| accountId | number | 是 |
| disallowModify | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [9201005](../errorcode-enterpriseDeviceManager.md#9201005-添加保活应用失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
