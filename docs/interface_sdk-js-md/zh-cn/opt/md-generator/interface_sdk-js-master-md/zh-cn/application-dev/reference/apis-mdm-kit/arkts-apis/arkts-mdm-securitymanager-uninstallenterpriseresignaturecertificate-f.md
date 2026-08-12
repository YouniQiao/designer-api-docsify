# uninstallEnterpriseReSignatureCertificate

## uninstallEnterpriseReSignatureCertificate

```TypeScript
function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void
```

卸载企业应用重签名证书。卸载企业重签名证书后，使用该证书签名的应用在设备重启前正常运行，设备重启后无法运行。

使用场景：

1.安装新证书：调用[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installEnterpriseReSignatureCertificate)接口安装新证书后，经新证书重签名的应用可正常运行。如果旧签名证书对应的应用为超级设备管理应用，需先取消激活后才能卸载证书，否则卸载证书后该应用无法卸载且无法运行。

2.恢复误删证书：调用[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installEnterpriseReSignatureCertificate)接口重新安装误删除的证书后，已重签名的应用可正常运行，不受影响。

> **注意：**
> 
> 删除证书常见证书过期和证书泄露场景，建议开发者在实现该功能时，强提示管理员谨慎删除证书，并确保删除证书前加载新的重签名证书，并完成所有应用更新切换到新的重签名证书，否则重启后历史安装的应用将无法运行。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-securityManager-function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: int): void--><!--Device-securityManager-function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: int): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| certificateAlias | string | 是 |
| accountId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [9201008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201008-企业重签名证书不存在) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let certificateAlias: string = 'test.cer';
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  securityManager.uninstallEnterpriseReSignatureCertificate(
    wantTemp, certificateAlias, accountId);
  console.info('Success to uninstall enterprise re signature certificate.');
} catch (err) {
  console.error(`Failed to uninstall enterprise re signature certificate.
    Code: ${err.code}, message: ${err.message}`);
};
```
