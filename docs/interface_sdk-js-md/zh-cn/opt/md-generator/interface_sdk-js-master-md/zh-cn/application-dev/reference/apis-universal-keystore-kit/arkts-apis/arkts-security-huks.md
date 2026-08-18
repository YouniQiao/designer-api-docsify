# @ohos.security.huks

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。 HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

**起始版本：** 8

<!--Device-unnamed-declare namespace huks--><!--Device-unnamed-declare namespace huks-End-->

**系统能力：** SystemCapability.Security.Huks.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [abort](arkts-universalkeystore-huks-abort-f.md#abort) |
| [abort](arkts-universalkeystore-huks-abort-f.md#abort) |
| [abortSession](arkts-universalkeystore-huks-abortsession-f.md#abortsession) |
| [abortSession](arkts-universalkeystore-huks-abortsession-f.md#abortsession) |
| [anonAttestKeyItem](arkts-universalkeystore-huks-anonattestkeyitem-f.md#anonattestkeyitem) |
| [anonAttestKeyItem](arkts-universalkeystore-huks-anonattestkeyitem-f.md#anonattestkeyitem) |
| [anonAttestKeyItemOffline](arkts-universalkeystore-huks-anonattestkeyitemoffline-f.md#anonattestkeyitemoffline) |
| [attestKeyItem](arkts-universalkeystore-huks-attestkeyitem-f.md#attestkeyitem) |
| [attestKeyItem](arkts-universalkeystore-huks-attestkeyitem-f.md#attestkeyitem) |
| [decapsulate](arkts-universalkeystore-huks-decapsulate-f.md#decapsulate) |
| [deleteKey](arkts-universalkeystore-huks-deletekey-f.md#deletekey) |
| [deleteKey](arkts-universalkeystore-huks-deletekey-f.md#deletekey) |
| [deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem) |
| [deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deletekeyitem) |
| [encapsulate](arkts-universalkeystore-huks-encapsulate-f.md#encapsulate) |
| [exportKey](arkts-universalkeystore-huks-exportkey-f.md#exportkey) |
| [exportKey](arkts-universalkeystore-huks-exportkey-f.md#exportkey) |
| [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem) |
| [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportkeyitem) |
| [finish](arkts-universalkeystore-huks-finish-f.md#finish) |
| [finish](arkts-universalkeystore-huks-finish-f.md#finish) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishsession) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishsession) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishsession) |
| [generateKey](arkts-universalkeystore-huks-generatekey-f.md#generatekey) |
| [generateKey](arkts-universalkeystore-huks-generatekey-f.md#generatekey) |
| [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md#generatekeyitem) |
| [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md#generatekeyitem) |
| [getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getkeyitemproperties) |
| [getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getkeyitemproperties) |
| [getKeyProperties](arkts-universalkeystore-huks-getkeyproperties-f.md#getkeyproperties) |
| [getKeyProperties](arkts-universalkeystore-huks-getkeyproperties-f.md#getkeyproperties) |
| [getSdkVersion](arkts-universalkeystore-huks-getsdkversion-f.md#getsdkversion) |
| [hasKeyItem](arkts-universalkeystore-huks-haskeyitem-f.md#haskeyitem) |
| [hasKeyItem](arkts-universalkeystore-huks-haskeyitem-f.md#haskeyitem) |
| [importKey](arkts-universalkeystore-huks-importkey-f.md#importkey) |
| [importKey](arkts-universalkeystore-huks-importkey-f.md#importkey) |
| [importKeyItem](arkts-universalkeystore-huks-importkeyitem-f.md#importkeyitem) |
| [importKeyItem](arkts-universalkeystore-huks-importkeyitem-f.md#importkeyitem) |
| [importWrappedKeyItem](arkts-universalkeystore-huks-importwrappedkeyitem-f.md#importwrappedkeyitem) |
| [importWrappedKeyItem](arkts-universalkeystore-huks-importwrappedkeyitem-f.md#importwrappedkeyitem) |
| [init](arkts-universalkeystore-huks-init-f.md#init) |
| [init](arkts-universalkeystore-huks-init-f.md#init) |
| [initSession](arkts-universalkeystore-huks-initsession-f.md#initsession) |
| [initSession](arkts-universalkeystore-huks-initsession-f.md#initsession) |
| [isKeyExist](arkts-universalkeystore-huks-iskeyexist-f.md#iskeyexist) |
| [isKeyExist](arkts-universalkeystore-huks-iskeyexist-f.md#iskeyexist) |
| [isKeyItemExist](arkts-universalkeystore-huks-iskeyitemexist-f.md#iskeyitemexist) |
| [isKeyItemExist](arkts-universalkeystore-huks-iskeyitemexist-f.md#iskeyitemexist) |
| [listAliases](arkts-universalkeystore-huks-listaliases-f.md#listaliases) |
| [unwrapKeyItem](arkts-universalkeystore-huks-unwrapkeyitem-f.md#unwrapkeyitem) |
| [update](arkts-universalkeystore-huks-update-f.md#update) |
| [update](arkts-universalkeystore-huks-update-f.md#update) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession) |
| [wrapKeyItem](arkts-universalkeystore-huks-wrapkeyitem-f.md#wrapkeyitem) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [anonAttestKeyItemAsUser](arkts-universalkeystore-huks-anonattestkeyitemasuser-f-sys.md#anonattestkeyitemasuser系统接口) |
| [anonAttestKeyItemOfflineAsUser](arkts-universalkeystore-huks-anonattestkeyitemofflineasuser-f-sys.md#anonattestkeyitemofflineasuser系统接口) |
| [attestKeyItemAsUser](arkts-universalkeystore-huks-attestkeyitemasuser-f-sys.md#attestkeyitemasuser系统接口) |
| [deleteKeyItemAsUser](arkts-universalkeystore-huks-deletekeyitemasuser-f-sys.md#deletekeyitemasuser系统接口) |
| [exportKeyItemAsUser](arkts-universalkeystore-huks-exportkeyitemasuser-f-sys.md#exportkeyitemasuser系统接口) |
| [generateKeyItemAsUser](arkts-universalkeystore-huks-generatekeyitemasuser-f-sys.md#generatekeyitemasuser系统接口) |
| [getKeyItemPropertiesAsUser](arkts-universalkeystore-huks-getkeyitempropertiesasuser-f-sys.md#getkeyitempropertiesasuser系统接口) |
| [hasKeyItemAsUser](arkts-universalkeystore-huks-haskeyitemasuser-f-sys.md#haskeyitemasuser系统接口) |
| [importKeyItemAsUser](arkts-universalkeystore-huks-importkeyitemasuser-f-sys.md#importkeyitemasuser系统接口) |
| [importWrappedKeyItemAsUser](arkts-universalkeystore-huks-importwrappedkeyitemasuser-f-sys.md#importwrappedkeyitemasuser系统接口) |
| [initSessionAsUser](arkts-universalkeystore-huks-initsessionasuser-f-sys.md#initsessionasuser系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [HuksHandle](arkts-universalkeystore-huks-hukshandle-i.md) |
| [HuksListAliasesReturnResult](arkts-universalkeystore-huks-hukslistaliasesreturnresult-i.md) |
| [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) |
| [HuksParam](arkts-universalkeystore-huks-huksparam-i.md) |
| [HuksResult](arkts-universalkeystore-huks-huksresult-i.md) |
| [HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md) |
| [HuksSessionHandle](arkts-universalkeystore-huks-hukssessionhandle-i.md) |

### 枚举

| 名称 |
| --- |
| [HuksAuthAccessType](arkts-universalkeystore-huks-huksauthaccesstype-e.md) |
| [HuksAuthStorageLevel](arkts-universalkeystore-huks-huksauthstoragelevel-e.md) |
| [HuksChallengePosition](arkts-universalkeystore-huks-hukschallengeposition-e.md) |
| [HuksChallengeType](arkts-universalkeystore-huks-hukschallengetype-e.md) |
| [HuksCipherMode](arkts-universalkeystore-huks-huksciphermode-e.md) |
| [HuksErrorCode](arkts-universalkeystore-huks-hukserrorcode-e.md) |
| [HuksExceptionErrCode](arkts-universalkeystore-huks-huksexceptionerrcode-e.md) |
| [HuksImportKeyType](arkts-universalkeystore-huks-huksimportkeytype-e.md) |
| [HuksKeyAlg](arkts-universalkeystore-huks-hukskeyalg-e.md) |
| [HuksKeyClassType](arkts-universalkeystore-huks-hukskeyclasstype-e.md) |
| [HuksKeyDigest](arkts-universalkeystore-huks-hukskeydigest-e.md) |
| [HuksKeyFlag](arkts-universalkeystore-huks-hukskeyflag-e.md) |
| [HuksKeyGenerateType](arkts-universalkeystore-huks-hukskeygeneratetype-e.md) |
| [HuksKeyPadding](arkts-universalkeystore-huks-hukskeypadding-e.md) |
| [HuksKeyPurpose](arkts-universalkeystore-huks-hukskeypurpose-e.md) |
| [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md) |
| [HuksKeySize](arkts-universalkeystore-huks-hukskeysize-e.md) |
| [HuksKeyStorageType](arkts-universalkeystore-huks-hukskeystoragetype-e.md) |
| [HuksKeyWrapType](arkts-universalkeystore-huks-hukskeywraptype-e.md) |
| [HuksRsaPssSaltLenType](arkts-universalkeystore-huks-huksrsapsssaltlentype-e.md) |
| [HuksSecureSignType](arkts-universalkeystore-huks-hukssecuresigntype-e.md) |
| [HuksSendType](arkts-universalkeystore-huks-hukssendtype-e.md) |
| [HuksTag](arkts-universalkeystore-huks-hukstag-e.md) |
| [HuksTagType](arkts-universalkeystore-huks-hukstagtype-e.md) |
| [HuksUnwrapSuite](arkts-universalkeystore-huks-huksunwrapsuite-e.md) |
| [HuksUserAuthMode](arkts-universalkeystore-huks-huksuserauthmode-e.md) |
| [HuksUserAuthType](arkts-universalkeystore-huks-huksuserauthtype-e.md) |
