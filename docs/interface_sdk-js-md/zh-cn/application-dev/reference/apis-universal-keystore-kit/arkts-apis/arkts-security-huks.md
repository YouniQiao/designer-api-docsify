# @ohos.security.huks(Universal Keystore)

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

**起始版本：** 8

**系统能力：** SystemCapability.Security.Huks.Core

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [abort(Universal Keystore)](arkts-universalkeystore-huks-abort-f.md) |
| [abort(Universal Keystore)](arkts-universalkeystore-huks-abort-f.md) |
| [abortSession(Universal Keystore)](arkts-universalkeystore-huks-abortsession-f.md) |
| [abortSession(Universal Keystore)](arkts-universalkeystore-huks-abortsession-f.md) |
| [anonAttestKeyItem(Universal Keystore)](arkts-universalkeystore-huks-anonattestkeyitem-f.md) |
| [anonAttestKeyItem(Universal Keystore)](arkts-universalkeystore-huks-anonattestkeyitem-f.md) |
| [anonAttestKeyItemOffline(Universal Keystore)](arkts-universalkeystore-huks-anonattestkeyitemoffline-f.md) |
| [attestKeyItem(Universal Keystore)](arkts-universalkeystore-huks-attestkeyitem-f.md) |
| [attestKeyItem(Universal Keystore)](arkts-universalkeystore-huks-attestkeyitem-f.md) |
| [decapsulate(Universal Keystore)](arkts-universalkeystore-huks-decapsulate-f.md) |
| [deleteKey(Universal Keystore)](arkts-universalkeystore-huks-deletekey-f.md) |
| [deleteKey(Universal Keystore)](arkts-universalkeystore-huks-deletekey-f.md) |
| [deleteKeyItem(Universal Keystore)](arkts-universalkeystore-huks-deletekeyitem-f.md) |
| [deleteKeyItem(Universal Keystore)](arkts-universalkeystore-huks-deletekeyitem-f.md) |
| [encapsulate(Universal Keystore)](arkts-universalkeystore-huks-encapsulate-f.md) |
| [exportKey(Universal Keystore)](arkts-universalkeystore-huks-exportkey-f.md) |
| [exportKey(Universal Keystore)](arkts-universalkeystore-huks-exportkey-f.md) |
| [exportKeyItem(Universal Keystore)](arkts-universalkeystore-huks-exportkeyitem-f.md) |
| [exportKeyItem(Universal Keystore)](arkts-universalkeystore-huks-exportkeyitem-f.md) |
| [finish(Universal Keystore)](arkts-universalkeystore-huks-finish-f.md) |
| [finish(Universal Keystore)](arkts-universalkeystore-huks-finish-f.md) |
| [finishSession(Universal Keystore)](arkts-universalkeystore-huks-finishsession-f.md) |
| [finishSession(Universal Keystore)](arkts-universalkeystore-huks-finishsession-f.md) |
| [finishSession(Universal Keystore)](arkts-universalkeystore-huks-finishsession-f.md) |
| [generateKey(Universal Keystore)](arkts-universalkeystore-huks-generatekey-f.md) |
| [generateKey(Universal Keystore)](arkts-universalkeystore-huks-generatekey-f.md) |
| [generateKeyItem(Universal Keystore)](arkts-universalkeystore-huks-generatekeyitem-f.md) |
| [generateKeyItem(Universal Keystore)](arkts-universalkeystore-huks-generatekeyitem-f.md) |
| [getKeyItemProperties(Universal Keystore)](arkts-universalkeystore-huks-getkeyitemproperties-f.md) |
| [getKeyItemProperties(Universal Keystore)](arkts-universalkeystore-huks-getkeyitemproperties-f.md) |
| [getKeyProperties(Universal Keystore)](arkts-universalkeystore-huks-getkeyproperties-f.md) |
| [getKeyProperties(Universal Keystore)](arkts-universalkeystore-huks-getkeyproperties-f.md) |
| [getSdkVersion(Universal Keystore)](arkts-universalkeystore-huks-getsdkversion-f.md) |
| [hasKeyItem(Universal Keystore)](arkts-universalkeystore-huks-haskeyitem-f.md) |
| [hasKeyItem(Universal Keystore)](arkts-universalkeystore-huks-haskeyitem-f.md) |
| [importKey(Universal Keystore)](arkts-universalkeystore-huks-importkey-f.md) |
| [importKey(Universal Keystore)](arkts-universalkeystore-huks-importkey-f.md) |
| [importKeyItem(Universal Keystore)](arkts-universalkeystore-huks-importkeyitem-f.md) |
| [importKeyItem(Universal Keystore)](arkts-universalkeystore-huks-importkeyitem-f.md) |
| [importWrappedKeyItem(Universal Keystore)](arkts-universalkeystore-huks-importwrappedkeyitem-f.md) |
| [importWrappedKeyItem(Universal Keystore)](arkts-universalkeystore-huks-importwrappedkeyitem-f.md) |
| [init(Universal Keystore)](arkts-universalkeystore-huks-init-f.md) |
| [init(Universal Keystore)](arkts-universalkeystore-huks-init-f.md) |
| [initSession(Universal Keystore)](arkts-universalkeystore-huks-initsession-f.md) |
| [initSession(Universal Keystore)](arkts-universalkeystore-huks-initsession-f.md) |
| [isKeyExist(Universal Keystore)](arkts-universalkeystore-huks-iskeyexist-f.md) |
| [isKeyExist(Universal Keystore)](arkts-universalkeystore-huks-iskeyexist-f.md) |
| [isKeyItemExist(Universal Keystore)](arkts-universalkeystore-huks-iskeyitemexist-f.md) |
| [isKeyItemExist(Universal Keystore)](arkts-universalkeystore-huks-iskeyitemexist-f.md) |
| [listAliases(Universal Keystore)](arkts-universalkeystore-huks-listaliases-f.md) |
| [unwrapKeyItem(Universal Keystore)](arkts-universalkeystore-huks-unwrapkeyitem-f.md) |
| [update(Universal Keystore)](arkts-universalkeystore-huks-update-f.md) |
| [update(Universal Keystore)](arkts-universalkeystore-huks-update-f.md) |
| [updateSession(Universal Keystore)](arkts-universalkeystore-huks-updatesession-f.md) |
| [updateSession(Universal Keystore)](arkts-universalkeystore-huks-updatesession-f.md) |
| [updateSession(Universal Keystore)](arkts-universalkeystore-huks-updatesession-f.md) |
| [wrapKeyItem(Universal Keystore)](arkts-universalkeystore-huks-wrapkeyitem-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [anonAttestKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-anonattestkeyitemasuser-f-sys.md) |
| [anonAttestKeyItemOfflineAsUser(Universal Keystore)](arkts-universalkeystore-huks-anonattestkeyitemofflineasuser-f-sys.md) |
| [attestKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-attestkeyitemasuser-f-sys.md) |
| [deleteKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-deletekeyitemasuser-f-sys.md) |
| [exportKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-exportkeyitemasuser-f-sys.md) |
| [generateKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-generatekeyitemasuser-f-sys.md) |
| [getKeyItemPropertiesAsUser(Universal Keystore)](arkts-universalkeystore-huks-getkeyitempropertiesasuser-f-sys.md) |
| [hasKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-haskeyitemasuser-f-sys.md) |
| [importKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-importkeyitemasuser-f-sys.md) |
| [importWrappedKeyItemAsUser(Universal Keystore)](arkts-universalkeystore-huks-importwrappedkeyitemasuser-f-sys.md) |
| [initSessionAsUser(Universal Keystore)](arkts-universalkeystore-huks-initsessionasuser-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [HuksHandle(Universal Keystore)](arkts-universalkeystore-huks-hukshandle-i.md) |
| [HuksListAliasesReturnResult(Universal Keystore)](arkts-universalkeystore-huks-hukslistaliasesreturnresult-i.md) |
| [HuksOptions(Universal Keystore)](arkts-universalkeystore-huks-huksoptions-i.md) |
| [HuksParam(Universal Keystore)](arkts-universalkeystore-huks-huksparam-i.md) |
| [HuksResult(Universal Keystore)](arkts-universalkeystore-huks-huksresult-i.md) |
| [HuksReturnResult(Universal Keystore)](arkts-universalkeystore-huks-huksreturnresult-i.md) |
| [HuksSessionHandle(Universal Keystore)](arkts-universalkeystore-huks-hukssessionhandle-i.md) |

### 枚举

| 名称 |
| --- |
| [HuksAuthAccessType(Universal Keystore)](arkts-universalkeystore-huks-huksauthaccesstype-e.md) |
| [HuksAuthStorageLevel(Universal Keystore)](arkts-universalkeystore-huks-huksauthstoragelevel-e.md) |
| [HuksChallengePosition(Universal Keystore)](arkts-universalkeystore-huks-hukschallengeposition-e.md) |
| [HuksChallengeType(Universal Keystore)](arkts-universalkeystore-huks-hukschallengetype-e.md) |
| [HuksCipherMode(Universal Keystore)](arkts-universalkeystore-huks-huksciphermode-e.md) |
| [HuksErrorCode(Universal Keystore)](arkts-universalkeystore-huks-hukserrorcode-e.md) |
| [HuksExceptionErrCode(Universal Keystore)](arkts-universalkeystore-huks-huksexceptionerrcode-e.md) |
| [HuksImportKeyType(Universal Keystore)](arkts-universalkeystore-huks-huksimportkeytype-e.md) |
| [HuksKeyAlg(Universal Keystore)](arkts-universalkeystore-huks-hukskeyalg-e.md) |
| [HuksKeyClassType(Universal Keystore)](arkts-universalkeystore-huks-hukskeyclasstype-e.md) |
| [HuksKeyDigest(Universal Keystore)](arkts-universalkeystore-huks-hukskeydigest-e.md) |
| [HuksKeyFlag(Universal Keystore)](arkts-universalkeystore-huks-hukskeyflag-e.md) |
| [HuksKeyGenerateType(Universal Keystore)](arkts-universalkeystore-huks-hukskeygeneratetype-e.md) |
| [HuksKeyPadding(Universal Keystore)](arkts-universalkeystore-huks-hukskeypadding-e.md) |
| [HuksKeyPurpose(Universal Keystore)](arkts-universalkeystore-huks-hukskeypurpose-e.md) |
| [HuksKeySecurityLevel(Universal Keystore)](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md) |
| [HuksKeySize(Universal Keystore)](arkts-universalkeystore-huks-hukskeysize-e.md) |
| [HuksKeyStorageType(Universal Keystore)](arkts-universalkeystore-huks-hukskeystoragetype-e.md) |
| [HuksKeyWrapType(Universal Keystore)](arkts-universalkeystore-huks-hukskeywraptype-e.md) |
| [HuksRsaPssSaltLenType(Universal Keystore)](arkts-universalkeystore-huks-huksrsapsssaltlentype-e.md) |
| [HuksSecureSignType(Universal Keystore)](arkts-universalkeystore-huks-hukssecuresigntype-e.md) |
| [HuksSendType(Universal Keystore)](arkts-universalkeystore-huks-hukssendtype-e.md) |
| [HuksTag(Universal Keystore)](arkts-universalkeystore-huks-hukstag-e.md) |
| [HuksTagType(Universal Keystore)](arkts-universalkeystore-huks-hukstagtype-e.md) |
| [HuksUnwrapSuite(Universal Keystore)](arkts-universalkeystore-huks-huksunwrapsuite-e.md) |
| [HuksUserAuthMode(Universal Keystore)](arkts-universalkeystore-huks-huksuserauthmode-e.md) |
| [HuksUserAuthType(Universal Keystore)](arkts-universalkeystore-huks-huksuserauthtype-e.md) |
