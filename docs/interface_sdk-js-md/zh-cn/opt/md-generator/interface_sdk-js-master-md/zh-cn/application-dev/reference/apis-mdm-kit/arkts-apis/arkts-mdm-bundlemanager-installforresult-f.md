# installForResult

## installForResult

```TypeScript
function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

安装指定路径下的应用包，并返回安装结果。使用Promise异步回调。

此接口只能安装分发类型为enterprise_mdm（MDM应用）和enterprise_normal（普通企业应用）类型的应用，可以通过  
[getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md/arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself)接口查询应用自身的  
[BundleInfo](arkts-mdm-bundlemanager-bundleinfo-i.md)，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。

> **说明：**
> 
> 该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>--><!--Device-bundleManager-function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| hapFilePaths | Array&lt;string&gt; | 是 |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9201036](../errorcode-enterpriseDeviceManager.md#9201036-数据代理uri错误导致应用安装失败) |
| [9201037](../errorcode-enterpriseDeviceManager.md#9201037-数据代理权限配置错误导致应用安装失败) |
| [9201038](../errorcode-enterpriseDeviceManager.md#9201038-代码签名验证失败导致应用安装失败) |
| [9201039](../errorcode-enterpriseDeviceManager.md#9201039-企业设备验证失败导致应用安装失败) |
| [9201032](../errorcode-enterpriseDeviceManager.md#9201032-指定用户id不存在) |
| [9201033](../errorcode-enterpriseDeviceManager.md#9201033-overlay检查失败导致应用安装失败) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-企业应用安装失败) |
| [9201034](../errorcode-enterpriseDeviceManager.md#9201034-hsp缺少必需权限导致应用安装失败) |
| [9201035](../errorcode-enterpriseDeviceManager.md#9201035-跨应用共享库安装不被允许导致应用安装失败) |
| [9201028](../errorcode-enterpriseDeviceManager.md#9201028-isolationmode配置不支持导致应用安装失败) |
| [9201029](../errorcode-enterpriseDeviceManager.md#9201029-hap版本过低导致应用安装失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9201030](../errorcode-enterpriseDeviceManager.md#9201030-versioncode不大于当前版本导致应用安装失败) |
| [9201031](../errorcode-enterpriseDeviceManager.md#9201031-依赖模块不存在导致应用安装失败) |
| [9201024](../errorcode-enterpriseDeviceManager.md#9201024-hap解析失败导致应用安装失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9201025](../errorcode-enterpriseDeviceManager.md#9201025-hap签名验证失败导致应用安装失败) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201026](../errorcode-enterpriseDeviceManager.md#9201026-hap路径无效或文件过大导致应用安装失败) |
| [9201027](../errorcode-enterpriseDeviceManager.md#9201027-hap配置信息不一致导致安装失败) |
| [9201022](../errorcode-enterpriseDeviceManager.md#9201022-系统磁盘空间不足导致应用安装失败) |
| [9201023](../errorcode-enterpriseDeviceManager.md#9201023-企业设备管理禁止安装导致应用安装失败) |
