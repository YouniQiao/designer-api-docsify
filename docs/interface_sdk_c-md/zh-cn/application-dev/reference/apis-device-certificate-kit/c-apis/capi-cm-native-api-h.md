# cm_native_api.h

## 概述

Defines APIs for querying the list and details of different types of certificates and credentials and importing USB key certificates.

**引用文件：** <security/device_certificate/certmanager/cm_native_api.h>

**库：** libohcert_manager.z.so

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**相关模块：** [CertManager](capi-device-certificate-kit-certmanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| -- | -- |
| [int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_getukeycertificate) | 获取USB证书凭据的详情信息列表。调用完成后，需要调用OH_CertManager_FreeUkeyCertificate释放certificateList内存。 |
| [int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)](#oh_certmanager_getprivatecertificate) | 获取特定应用私有证书凭据详细信息。 |
| [int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)](#oh_certmanager_getpubliccertificate) | 获取特定用户公共证书凭据详细信息。调用完成后，需要调用OH_CertManager_FreeCredential释放certificate内存。 |
| [void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_freeukeycertificate) | 销毁证书详情信息列表。 |
| [void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)](#oh_certmanager_freecredential) | 销毁证书详情。 |
| [int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_getukeycertificatelist) | 查询USB Key证书凭据列表。调用完成后，需要调用OH_CertManager_FreeUkeyCertificate释放certificateList内存。 |
| [int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)](#oh_certmanager_importukeycert) | 导入证书到USB Key设备。 |

## 函数说明

### OH_CertManager_GetUkeyCertificate()

```c
int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

**描述：**

获取USB证书凭据的详情信息列表。调用完成后，需要调用OH_CertManager_FreeUkeyCertificate释放certificateList内存。

<!--Device-int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)--><!--Device-int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | 存放USB证书凭据的唯一标识符（字符串格式）。 |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | USB证书凭据属性信息。 |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | 获取到的USB证书凭据详情列表。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| int32_t | <ul> <li>[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) : </li> <li>**OH_CM_SUCCESS = 0**: 操作成功。</li> <li>**OH_CM_HAS_NO_PERMISSION = 201**: 权限校验失败。</li> <li>**OH_CM_CAPABILITY_NOT_SUPPORTED = 801**: 设备不支持。</li> <li>**OH_CM_PARAMETER_VALIDATION_FAILED = 17500011**: 入参校验失败。可能原因：1.参数格式错误。2.参数范围无效。</li> <li>**OH_CM_INNER_FAILURE = 17500001**: 内部错误。可能原因：1.IPC通讯失败。2.内存操作错误。3.文件操作错误。</li> <li>**OH_CM_NOT_FOUND = 17500002**: 证书不存在。</li> <li>**OH_CM_ACCESS_UKEY_SERVICE_FAILED = 17500010**: USB证书凭据访问失败。</li> </ul> |

### OH_CertManager_GetPrivateCertificate()

```c
int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**描述：**

获取特定应用私有证书凭据详细信息。

<!--Device-int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)--><!--Device-int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | 存放应用私有证书凭据的唯一标识符（字符串格式）。 |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | 获取到的应用私有凭据的详情。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| int32_t | [OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)：OH_CM_SUCCESS = 0 ：操作成功。OH_CM_HAS_NO_PERMISSION = 201 ：权限校验失败。OH_CM_PARAMETER_VALIDATION_FAILED = 17500011 ：入参校验失败。可能原因：1.参数格式错误。2.参数范围无效。OH_CM_INNER_FAILURE = 17500001 ：内部错误。可能原因：1.IPC通讯失败。2.内存操作错误。3.文件操作错误。OH_CM_NOT_FOUND = 17500002 ：证书不存在。 |

### OH_CertManager_GetPublicCertificate()

```c
int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**描述：**

获取特定用户公共证书凭据详细信息。调用完成后，需要调用OH_CertManager_FreeCredential释放certificate内存。

<!--Device-int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)--><!--Device-int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | 存放用户公共证书凭据的唯一标识符（字符串格式）。 |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | 获取到的用户公共证书凭据的详情。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| int32_t | <ul> <li>[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) ： </li> <li>OH_CM_SUCCESS = 0 ：操作成功。</li> <li>OH_CM_HAS_NO_PERMISSION = 201 ：权限校验失败。</li> <li>OH_CM_PARAMETER_VALIDATION_FAILED = 17500011 ：入参校验失败。可能原因：1.参数格式错误。2.参数范围无效。</li> <li>OH_CM_INNER_FAILURE = 17500001 ：内部错误。可能原因：1.IPC通讯失败。2.内存操作错误。3.文件操作错误。</li> <li>OH_CM_NOT_FOUND = 17500002 ：证书不存在。</li> <li>OH_CM_NO_AUTHORIZATION =  17500005 ：应用未经用户授权。</li> </ul> |

### OH_CertManager_FreeUkeyCertificate()

```c
void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)
```

**描述：**

销毁证书详情信息列表。

<!--Device-void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)--><!--Device-void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | 待销毁的证书凭据详细列表。 |

### OH_CertManager_FreeCredential()

```c
void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)
```

**描述：**

销毁证书详情。

<!--Device-void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)--><!--Device-void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | 待销毁的证书凭据详情。 |

### OH_CertManager_GetUkeyCertificateList()

```c
int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

**描述：**

查询USB Key证书凭据列表。调用完成后，需要调用OH_CertManager_FreeUkeyCertificate释放certificateList内存。

<!--Device-int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)--><!--Device-int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**起始版本：** 26.1.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *ukeyProvider | [入参] USB Key设备提供商名称。 |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | [入参] USB证书凭据属性信息。 |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | [出参] 获取到的USB证书凭据列表。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| int32_t | 证书管理的错误码，错误码定义请参考[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)。<ul> <li>[OH_CM_SUCCESS](capi-cm-native-type-h.md#oh_cm_errorcode): 操作成功。</li> <li>[OH_CM_HAS_NO_PERMISSION](capi-cm-native-type-h.md#oh_cm_errorcode): 权限校验失败。</li> <li>[OH_CM_CAPABILITY_NOT_SUPPORTED](capi-cm-native-type-h.md#oh_cm_errorcode): 设备不支持。</li> <li>[OH_CM_INNER_FAILURE](capi-cm-native-type-h.md#oh_cm_errorcode): 内部错误。可能原因：<br>1.IPC通讯失败。<br>2.内存操作错误。<br>3.文件操作错误。</li> <li>[OH_CM_ACCESS_UKEY_SERVICE_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): USB证书凭据访问失败。</li> <li>[OH_CM_PARAMETER_VALIDATION_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): 入参校验失败。可能原因：<br>1.参数格式错误。<br>2.参数范围无效。</li> </ul> |

### OH_CertManager_ImportUkeyCert()

```c
int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)
```

**描述：**

导入证书到USB Key设备。

<!--Device-int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)--><!--Device-int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**起始版本：** 26.1.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | [入参] 存放USB证书凭据的唯一标识符（字符串格式）。 |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *cert | [入参] 待导入的证书文件。 |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | [入参] USB证书凭据属性信息。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| int32_t | 证书管理的错误码，错误码定义请参考[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)。<ul> <li>[OH_CM_SUCCESS](capi-cm-native-type-h.md#oh_cm_errorcode): 操作成功。</li> <li>[OH_CM_HAS_NO_PERMISSION](capi-cm-native-type-h.md#oh_cm_errorcode): 权限校验失败。</li> <li>[OH_CM_CAPABILITY_NOT_SUPPORTED](capi-cm-native-type-h.md#oh_cm_errorcode): 设备不支持。</li> <li>[OH_CM_INNER_FAILURE](capi-cm-native-type-h.md#oh_cm_errorcode): 内部错误。可能原因：<br>1.IPC通讯失败。<br>2.内存操作错误。<br>3.文件操作错误。</li> <li>[OH_CM_NOT_FOUND](capi-cm-native-type-h.md#oh_cm_errorcode): keyUri指定的证书凭据不存在。</li> <li>[OH_CM_ACCESS_UKEY_SERVICE_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): USB证书凭据访问失败。</li> <li>[OH_CM_PARAMETER_VALIDATION_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): 入参校验失败。可能原因：<br>1.参数格式错误。<br>2.参数范围无效。</li> </ul> |


