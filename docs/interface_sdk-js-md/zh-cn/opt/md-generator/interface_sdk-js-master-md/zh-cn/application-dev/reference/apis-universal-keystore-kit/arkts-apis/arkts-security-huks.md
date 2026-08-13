# @ohos.security.huks

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。 HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare namespace huks--><!--Device-unnamed-declare namespace huks-End-->

**系统能力：** SystemCapability.Security.Huks.Core

## 汇总

### 函数

| 名称 |
| --- |
| [abort](arkts-universalkeystore-huks-abort-f.md#abort) |
| [abort](arkts-universalkeystore-huks-abort-f.md#abort) |
| [abortSession](arkts-universalkeystore-huks-abortsession-f.md#abortSession) |
| [abortSession](arkts-universalkeystore-huks-abortsession-f.md#abortSession) |
| [anonAttestKeyItem](arkts-universalkeystore-huks-anonattestkeyitem-f.md#anonAttestKeyItem) |
| [anonAttestKeyItem](arkts-universalkeystore-huks-anonattestkeyitem-f.md#anonAttestKeyItem) |
| [anonAttestKeyItemOffline](arkts-universalkeystore-huks-anonattestkeyitemoffline-f.md#anonAttestKeyItemOffline) |
| [attestKeyItem](arkts-universalkeystore-huks-attestkeyitem-f.md#attestKeyItem) |
| [attestKeyItem](arkts-universalkeystore-huks-attestkeyitem-f.md#attestKeyItem) |
| [decapsulate](arkts-universalkeystore-huks-decapsulate-f.md#decapsulate) |
| [deleteKey](arkts-universalkeystore-huks-deletekey-f.md#deleteKey) |
| [deleteKey](arkts-universalkeystore-huks-deletekey-f.md#deleteKey) |
| [deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deleteKeyItem) |
| [deleteKeyItem](arkts-universalkeystore-huks-deletekeyitem-f.md#deleteKeyItem) |
| [encapsulate](arkts-universalkeystore-huks-encapsulate-f.md#encapsulate) |
| [exportKey](arkts-universalkeystore-huks-exportkey-f.md#exportKey) |
| [exportKey](arkts-universalkeystore-huks-exportkey-f.md#exportKey) |
| [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportKeyItem) |
| [exportKeyItem](arkts-universalkeystore-huks-exportkeyitem-f.md#exportKeyItem) |
| [finish](arkts-universalkeystore-huks-finish-f.md#finish) |
| [finish](arkts-universalkeystore-huks-finish-f.md#finish) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishSession) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishSession) |
| [finishSession](arkts-universalkeystore-huks-finishsession-f.md#finishSession) |
| [generateKey](arkts-universalkeystore-huks-generatekey-f.md#generateKey) |
| [generateKey](arkts-universalkeystore-huks-generatekey-f.md#generateKey) |
| [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md#generateKeyItem) |
| [generateKeyItem](arkts-universalkeystore-huks-generatekeyitem-f.md#generateKeyItem) |
| [getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getKeyItemProperties) |
| [getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getKeyItemProperties) |
| [getKeyProperties](arkts-universalkeystore-huks-getkeyproperties-f.md#getKeyProperties) |
| [getKeyProperties](arkts-universalkeystore-huks-getkeyproperties-f.md#getKeyProperties) |
| [getSdkVersion](arkts-universalkeystore-huks-getsdkversion-f.md#getSdkVersion) |
| [hasKeyItem](arkts-universalkeystore-huks-haskeyitem-f.md#hasKeyItem) |
| [hasKeyItem](arkts-universalkeystore-huks-haskeyitem-f.md#hasKeyItem) |
| [importKey](arkts-universalkeystore-huks-importkey-f.md#importKey) |
| [importKey](arkts-universalkeystore-huks-importkey-f.md#importKey) |
| [importKeyItem](arkts-universalkeystore-huks-importkeyitem-f.md#importKeyItem) |
| [importKeyItem](arkts-universalkeystore-huks-importkeyitem-f.md#importKeyItem) |
| [importWrappedKeyItem](arkts-universalkeystore-huks-importwrappedkeyitem-f.md#importWrappedKeyItem) |
| [importWrappedKeyItem](arkts-universalkeystore-huks-importwrappedkeyitem-f.md#importWrappedKeyItem) |
| [init](arkts-universalkeystore-huks-init-f.md#init) |
| [init](arkts-universalkeystore-huks-init-f.md#init) |
| [initSession](arkts-universalkeystore-huks-initsession-f.md#initSession) |
| [initSession](arkts-universalkeystore-huks-initsession-f.md#initSession) |
| [isKeyExist](arkts-universalkeystore-huks-iskeyexist-f.md#isKeyExist) |
| [isKeyExist](arkts-universalkeystore-huks-iskeyexist-f.md#isKeyExist) |
| [isKeyItemExist](arkts-universalkeystore-huks-iskeyitemexist-f.md#isKeyItemExist) |
| [isKeyItemExist](arkts-universalkeystore-huks-iskeyitemexist-f.md#isKeyItemExist) |
| [listAliases](arkts-universalkeystore-huks-listaliases-f.md#listAliases) |
| [unwrapKeyItem](arkts-universalkeystore-huks-unwrapkeyitem-f.md#unwrapKeyItem) |
| [update](arkts-universalkeystore-huks-update-f.md#update) |
| [update](arkts-universalkeystore-huks-update-f.md#update) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updateSession) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updateSession) |
| [updateSession](arkts-universalkeystore-huks-updatesession-f.md#updateSession) |
| [wrapKeyItem](arkts-universalkeystore-huks-wrapkeyitem-f.md#wrapKeyItem) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [anonAttestKeyItemAsUser](arkts-universalkeystore-huks-anonattestkeyitemasuser-f-sys.md#anonAttestKeyItemAsUser（系统接口）) |
| [anonAttestKeyItemOfflineAsUser](arkts-universalkeystore-huks-anonattestkeyitemofflineasuser-f-sys.md#anonAttestKeyItemOfflineAsUser（系统接口）) |
| [attestKeyItemAsUser](arkts-universalkeystore-huks-attestkeyitemasuser-f-sys.md#attestKeyItemAsUser（系统接口）) |
| [deleteKeyItemAsUser](arkts-universalkeystore-huks-deletekeyitemasuser-f-sys.md#deleteKeyItemAsUser（系统接口）) |
| [exportKeyItemAsUser](arkts-universalkeystore-huks-exportkeyitemasuser-f-sys.md#exportKeyItemAsUser（系统接口）) |
| [generateKeyItemAsUser](arkts-universalkeystore-huks-generatekeyitemasuser-f-sys.md#generateKeyItemAsUser（系统接口）) |
| [getKeyItemPropertiesAsUser](arkts-universalkeystore-huks-getkeyitempropertiesasuser-f-sys.md#getKeyItemPropertiesAsUser（系统接口）) |
| [hasKeyItemAsUser](arkts-universalkeystore-huks-haskeyitemasuser-f-sys.md#hasKeyItemAsUser（系统接口）) |
| [importKeyItemAsUser](arkts-universalkeystore-huks-importkeyitemasuser-f-sys.md#importKeyItemAsUser（系统接口）) |
| [importWrappedKeyItemAsUser](arkts-universalkeystore-huks-importwrappedkeyitemasuser-f-sys.md#importWrappedKeyItemAsUser（系统接口）) |
| [initSessionAsUser](arkts-universalkeystore-huks-initsessionasuser-f-sys.md#initSessionAsUser（系统接口）) |
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
