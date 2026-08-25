# install（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

安装指定路径下的应用包。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [install](arkts-mdm-bundlemanager-install-f.md)(admin: Want, hapFilePaths: Array&lt;string&gt;, installParam?: InstallParam)

**需要权限：** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| hapFilePaths | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-企业应用安装失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

安装指定路径下的指定安装参数的应用包。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [install](arkts-mdm-bundlemanager-install-f.md)(admin: Want, hapFilePaths: Array&lt;string&gt;, installParam?: InstallParam)

**需要权限：** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| hapFilePaths | Array & lt;string & gt; | 是 |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-企业应用安装失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
