# @ohos.security.huksExternalCrypto(External Key Management)

模块提供外部密钥管理扩展功能的注册与注销，PIN码认证与认证状态获取等。

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为22。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

## 导入模块

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [clearUkeyPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-clearukeypinauthstate-f.md) |
| [closeResource(External Key Management)](arkts-universalkeystore-huksexternalcrypto-closeresource-f.md) |
| [getErrorInfo(External Key Management)](arkts-universalkeystore-huksexternalcrypto-geterrorinfo-f.md) |
| [getProperty(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getproperty-f.md) |
| [getResourceId(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getresourceid-f.md) |
| [getUkeyPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getukeypinauthstate-f.md) |
| [openResource(External Key Management)](arkts-universalkeystore-huksexternalcrypto-openresource-f.md) |
| [registerProvider(External Key Management)](arkts-universalkeystore-huksexternalcrypto-registerprovider-f.md) |
| [setProperty(External Key Management)](arkts-universalkeystore-huksexternalcrypto-setproperty-f.md) |
| [unregisterProvider(External Key Management)](arkts-universalkeystore-huksexternalcrypto-unregisterprovider-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [authUkeyPin(External Key Management)](arkts-universalkeystore-huksexternalcrypto-authukeypin-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [HuksExternalCryptoParam(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md) |
| [HuksExternalErrorInfo(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [HuksExternalCryptoTag(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotag-e.md) |
| [HuksExternalCryptoTagType(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotagtype-e.md) |
| [HuksExternalPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalpinauthstate-e.md) |
