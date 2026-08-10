# @ohos.net.networkSecurity

Provides networkSecurity related APIs.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace networkSecurity--><!--Device-unnamed-declare namespace networkSecurity-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [certVerification](arkts-network-networksecurity-certverification-f.md#certverification) | Certificate verification to the server. |
| [certVerificationSync](arkts-network-networksecurity-certverificationsync-f.md#certverificationsync) | Certificate verification to the server. |
| [isCleartextPermitted](arkts-network-networksecurity-iscleartextpermitted-f.md#iscleartextpermitted) | Checks whether the Cleartext traffic is permitted.To invoke this method, you must have the {@code ohos.permission.INTERNET} permission. |
| [isCleartextPermittedByHostName](arkts-network-networksecurity-iscleartextpermittedbyhostname-f.md#iscleartextpermittedbyhostname) | Checks whether the Cleartext traffic for a specified hostname is permitted.To invoke this method, you must have the {@code ohos.permission.INTERNET} permission. |
| [verifyCertChain](arkts-network-networksecurity-verifycertchain-f.md#verifycertchain) | Verifies the server certificate chain and returns a sorted chain. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [CertBlob](arkts-network-networksecurity-certblob-i.md) | Define the certificate content. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [CertType](arkts-network-networksecurity-certtype-e.md) | Defines the certificate type. |

