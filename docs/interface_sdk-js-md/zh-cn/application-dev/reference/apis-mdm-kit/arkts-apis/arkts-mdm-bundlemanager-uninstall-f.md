# uninstall

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## uninstall

```TypeScript
function uninstall(admin: Want, bundleName: string, userId?: number, isKeepData?: boolean): Promise<void>
```

卸载当前/指定用户下的指定包，选择是否保留包数据（由isKeepData指定）。使用Promise异步回调。调用成功后，应用被卸载，数据根据isKeepData参数保留或删除。

> **说明：**&gt;
> 当应用为不可卸载的预置应用或者通过[addDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-adddisalloweduninstallbundlessync-f.md)接口设置了不
> 允许卸载时，调用此接口卸载应用会返回401错误码。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleName | string | 是 |
| userId | number | 否 |
| isKeepData | boolean | 否 |

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
