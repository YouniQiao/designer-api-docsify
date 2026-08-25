# install

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

安装指定路径下的应用包。使用Promise异步回调。此接口只能安装分发类型为enterprise_mdm（MDM应用）和enterprise_normal（普通企业应用）类型的应用，可以通过 [getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md)接口查询应用自身的 BundleInfo，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。自API版本26.0.0起，建议使用 [installForResult](arkts-mdm-bundlemanager-installforresult-f.md)，以获取更详细的错误码返回值。

> **说明：**&gt;
> 该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-企业应用安装失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
