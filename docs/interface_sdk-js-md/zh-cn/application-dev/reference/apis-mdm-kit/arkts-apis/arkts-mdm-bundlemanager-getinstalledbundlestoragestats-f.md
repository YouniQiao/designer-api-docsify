# getInstalledBundleStorageStats

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## getInstalledBundleStorageStats

```TypeScript
function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>
```

获取设备指定用户下已安装应用的存储占用信息。使用Promise异步回调。

> **说明：**&gt;
> 1.仅能获取已安装应用的存储占用信息。&gt;
> 2.bundleNames参数为empty或全部传入未安装的应用包名，会抛出9200012错误码。&gt;
> 3.bundleNames参数传递的包名部分应用已安装，部分应用未安装时，接口返回正常，已安装的应用返回实际的存储占用信息，未安装的应用存储占用信息为0。&gt;
> 4.该接口支持跨用户查询，比如可以在100用户下，查询101用户下的某些应用的存储占用信息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_GET_ALL_BUNDLE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleNames | Array & lt;string & gt; | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[BundleStorageStats](arkts-mdm-bundlemanager-bundlestoragestats-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
