# @ohos.enterprise.accountManager(账号管理)

本模块提供设备账号管理能力，包括禁止创建本地账号等。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [activateOsAccount(账号管理)](arkts-mdm-accountmanager-activateosaccount-f.md) |
| [addOsAccountAsync(账号管理)](arkts-mdm-accountmanager-addosaccountasync-f.md) |
| [createNormalOsAccount(账号管理)](arkts-mdm-accountmanager-createnormalosaccount-f.md) |
| [disallowOsAccountAddition(账号管理)](arkts-mdm-accountmanager-disallowosaccountaddition-f.md) |
| [getDomainAccountPolicy(账号管理)](arkts-mdm-accountmanager-getdomainaccountpolicy-f.md) |
| [isOsAccountAdditionDisallowed(账号管理)](arkts-mdm-accountmanager-isosaccountadditiondisallowed-f.md) |
| [isOsAccountAdditionDisallowed(账号管理)](arkts-mdm-accountmanager-isosaccountadditiondisallowed-f.md) |
| [removeOsAccount(账号管理)](arkts-mdm-accountmanager-removeosaccount-f.md) |
| [setDomainAccountPolicy(账号管理)](arkts-mdm-accountmanager-setdomainaccountpolicy-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addOsAccount(账号管理)](arkts-mdm-accountmanager-addosaccount-f-sys.md) |
| [disallowAddLocalAccount(账号管理)](arkts-mdm-accountmanager-disallowaddlocalaccount-f-sys.md) |
| [disallowAddLocalAccount(账号管理)](arkts-mdm-accountmanager-disallowaddlocalaccount-f-sys.md) |
| [disallowAddOsAccountByUser(账号管理)](arkts-mdm-accountmanager-disallowaddosaccountbyuser-f-sys.md) |
| [isAddOsAccountByUserDisallowed(账号管理)](arkts-mdm-accountmanager-isaddosaccountbyuserdisallowed-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [DomainAccountPolicy(账号管理)](arkts-mdm-accountmanager-domainaccountpolicy-i.md) |
