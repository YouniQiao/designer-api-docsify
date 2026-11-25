# cm_native_api.h

## Overview

Defines APIs for querying the list and details of different types of certificates and credentials and importing USB key certificates.

**File to Include**: <security/device_certificate/certmanager/cm_native_api.h>

**Library**: libohcert_manager.z.so

**System capability**: SystemCapability.Security.CertificateManager

**Since**: 22

**Related module**: [CertManager](capi-device-certificate-kit-certmanager.md)

## Summary

### Functions

| Name | Description |
| -- | -- |
| [int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_getukeycertificate) | Obtains the detail list of USB certificate credentials. After the call is complete, call OH_CertManager_FreeUkeyCertificate to release the certificateList memory. |
| [int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)](#oh_certmanager_getprivatecertificate) | Obtains the details of a private certificate credential of a specific application. After the call is complete, call OH_CertManager_FreeCredential to release the certificate memory. |
| [int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)](#oh_certmanager_getpubliccertificate) | Obtains the details of a public certificate credential of a specific user. After the call is complete, call OH_CertManager_FreeCredential to release the certificate memory. |
| [void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_freeukeycertificate) | Destroys the certificate detail list. |
| [void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)](#oh_certmanager_freecredential) | Destroys the certificate details. |
| [int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)](#oh_certmanager_getukeycertificatelist) | This interface is used to query the USB key certificate credential list. After the call is complete, call OH_CertManager_FreeUkeyCertificate to release the certificateList memory. |
| [int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)](#oh_certmanager_importukeycert) | Import the certificate to the USB key device. |

## Function description

### OH_CertManager_GetUkeyCertificate()

```c
int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

**Description**

Obtains the detail list of USB certificate credentials. After the call is complete, call OH_CertManager_FreeUkeyCertificate to release the certificateList memory.

<!--Device-int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)--><!--Device-int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Required permission**: ohos.permission.ACCESS_CERT_MANAGER

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | Pointer to the URI that stores the USB certificate credentials, in string format. |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | Pointer to the property information of the USB certificate credential. |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | Pointer to the USB certificate credential detail list obtained. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul> <li>[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) : </li> <li>**OH_CM_SUCCESS = 0**: Operation successful.</li> <li>**OH_CM_HAS_NO_PERMISSION = 201**: Permission verification failed.</li> <li>**OH_CM_CAPABILITY_NOT_SUPPORTED = 801**: The device is not supported.</li> <li>**OH_CM_PARAMETER_VALIDATION_FAILED = 17500011**: Input parameter verification failed. Possible causes: 1. Incorrect parameter format. 2. Invalid parameter value range.</li> <li>**OH_CM_INNER_FAILURE = 17500001**: Internal error. Possible causes: 1. IPC failure. 2. Memory operation error. 3. File operation error.</li> <li>**OH_CM_NOT_FOUND = 17500002**: The certificate does not exist.</li> <li>**OH_CM_ACCESS_UKEY_SERVICE_FAILED = 17500010**: Failed to access the USB certificate credential.</li> </ul> |

### OH_CertManager_GetPrivateCertificate()

```c
int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**Description**

Obtains the details of a private certificate credential of a specific application. After the call is complete, call OH_CertManager_FreeCredential to release the certificate memory.

<!--Device-int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)--><!--Device-int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Required permission**: ohos.permission.ACCESS_CERT_MANAGER

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | Pointer to the URI that stores the application's private certificate credentials, in string format. |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | Pointer to the details of the application's private credentials obtained. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul> <li>[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) : </li> <li>**OH_CM_SUCCESS = 0**: Operation successful.</li> <li>**OH_CM_HAS_NO_PERMISSION = 201**: Permission verification failed.</li> <li>**OH_CM_PARAMETER_VALIDATION_FAILED = 17500011**: Input parameter verification failed. Possible causes: 1. Incorrect parameter format. 2. Invalid parameter value range.</li> <li>**OH_CM_INNER_FAILURE = 17500001**: Internal error. Possible causes: 1. IPC failure. 2. Memory operation error. 3. File operation error.</li> <li>**OH_CM_NOT_FOUND = 17500002**: The certificate does not exist.</li> </ul> |

### OH_CertManager_GetPublicCertificate()

```c
int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**Description**

Obtains the details of a public certificate credential of a specific user. After the call is complete, call OH_CertManager_FreeCredential to release the certificate memory.

<!--Device-int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)--><!--Device-int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Required permission**: ohos.permission.ACCESS_CERT_MANAGER

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | Pointer to the URI that stores the user's public certificate credentials, in string format. |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | Pointer to the details of the user's public certificate credential obtained. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul> <li>[OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) : </li> <li>**OH_CM_SUCCESS = 0**: Operation successful.</li> <li>**OH_CM_HAS_NO_PERMISSION = 201**: Permission verification failed.</li> <li>**OH_CM_PARAMETER_VALIDATION_FAILED = 17500011**: Input parameter verification failed. Possible causes: 1. Incorrect parameter format. 2. Invalid parameter value range.</li> <li>**OH_CM_INNER_FAILURE = 17500001**: Internal error. Possible causes: 1. IPC failure. 2. Memory operation error. 3. File operation error.</li> <li>**OH_CM_NOT_FOUND = 17500002**: The certificate does not exist.</li> <li>**OH_CM_NO_AUTHORIZATION = 17500005**: The application is not authorized.</li> </ul> |

### OH_CertManager_FreeUkeyCertificate()

```c
void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)
```

**Description**

Destroys the certificate detail list.

<!--Device-void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)--><!--Device-void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | Pointer to the certificate credential detail list to be destroyed. |

### OH_CertManager_FreeCredential()

```c
void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)
```

**Description**

Destroys the certificate details.

<!--Device-void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)--><!--Device-void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_CM_Credential](capi-certmanagertype-oh-cm-credential.md) *certificate | Pointer to the certificate credential details to be destroyed. |

### OH_CertManager_GetUkeyCertificateList()

```c
int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

**Description**

This interface is used to query the USB key certificate credential list. After the call is complete, call OH_CertManager_FreeUkeyCertificate to release the certificateList memory.

<!--Device-int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)--><!--Device-int32_t OH_CertManager_GetUkeyCertificateList(const OH_CM_Blob *ukeyProvider, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Required permission**: ohos.permission.ACCESS_CERT_MANAGER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *ukeyProvider | [Input parameter] USB key vendor name. |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | [Input parameter] USB certificate credential attribute information. |
| [OH_CM_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) *certificateList | [Output parameter] Obtained USB certificate credential list. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | Certificate management error code. For the definition of the error code, see [OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode).<ul> <li>[OH_CM_SUCCESS](capi-cm-native-type-h.md#oh_cm_errorcode): Operation succeeded. </li> <li>[OH_CM_HAS_NO_PERMISSION](capi-cm-native-type-h.md#oh_cm_errorcode): Permission verification failed. </li> <li>[OH_CM_CAPABILITY_NOT_SUPPORTED](capi-cm-native-type-h.md#oh_cm_errorcode): The device does not support this function. </li> <li>\_\_LINK\_\_4_: Internal error. Possible causes: <br>1. The IPC communication fails. <br>2. Memory operation error. <br>3. File operation error. </li> <li>[OH_CM_ACCESS_UKEY_SERVICE_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): Failed to access the USB certificate credentials. </li> <li>[OH_CM_PARAMETER_VALIDATION_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): Input parameter validation failed. Possible causes: <br>1. The parameter format is incorrect. <br>2. The parameter range is invalid. </li> </ul> |

### OH_CertManager_ImportUkeyCert()

```c
int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)
```

**Description**

Import the certificate to the USB key device.

<!--Device-int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)--><!--Device-int32_t OH_CertManager_ImportUkeyCert(const OH_CM_Blob *keyUri, const OH_CM_Blob *cert, const OH_CM_UkeyInfo *ukeyInfo)-End-->

**System capability**: SystemCapability.Security.CertificateManager

**Required permission**: ohos.permission.ACCESS_CERT_MANAGER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *keyUri | [Input parameter] Unique identifier of the USB certificate (character string format). |
| [const OH_CM_Blob](capi-certmanagertype-oh-cm-blob.md) *cert | [Input parameter] Certificate file to be imported. |
| [const OH_CM_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) *ukeyInfo | [Input parameter] USB certificate credential attribute information. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | Certificate management error code. For details about the error code definition, see [OH_CM_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode).<ul> <li>[OH_CM_SUCCESS](capi-cm-native-type-h.md#oh_cm_errorcode): Operation succeeded. </li> <li>[OH_CM_HAS_NO_PERMISSION](capi-cm-native-type-h.md#oh_cm_errorcode): Permission verification failed. </li> <li>[OH_CM_CAPABILITY_NOT_SUPPORTED](capi-cm-native-type-h.md#oh_cm_errorcode): The device does not support this function. </li> <li>\_\_LINK\_\_4_: Internal error. Possible causes: <br>1. The IPC communication fails. <br>2. Memory operation error. <br>3. File operation error. </li> <li>[OH_CM_NOT_FOUND](capi-cm-native-type-h.md#oh_cm_errorcode): The certificate credential specified by keyUri does not exist. </li> <li>[OH_CM_ACCESS_UKEY_SERVICE_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): Failed to access the USB certificate credentials. </li> <li>[OH_CM_PARAMETER_VALIDATION_FAILED](capi-cm-native-type-h.md#oh_cm_errorcode): Input parameter validation failed. Possible causes: <br>1. The parameter format is incorrect. <br>2. The parameter range is invalid. </li> </ul> |


