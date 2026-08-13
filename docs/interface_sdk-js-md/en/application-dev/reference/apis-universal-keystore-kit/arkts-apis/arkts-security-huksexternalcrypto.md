# @ohos.security.huksExternalCrypto(External Key Management)

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace huksExternalCrypto--><!--Device-unnamed-declare namespace huksExternalCrypto-End-->

**System capability:** SystemCapability.Security.Huks.CryptoExtension

## Modules to Import

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [clearUkeyPinAuthState](arkts-universalkeystore-huksexternalcrypto-clearukeypinauthstate-f.md#clearUkeyPinAuthState) | Clear the PIN auth state of the specified resource ID. |
| [closeResource](arkts-universalkeystore-huksexternalcrypto-closeresource-f.md#closeResource) | Close the resource with a specific resource ID. |
| [getErrorInfo](arkts-universalkeystore-huksexternalcrypto-geterrorinfo-f.md#getErrorInfo) | Get the detailed error information. |
| [getProperty](arkts-universalkeystore-huksexternalcrypto-getproperty-f.md#getProperty) | Obtains a property value. This API uses a promise to return the result. The **propertyId** indicates the ID of the property to be queried. Currently, only the SKF API names defined in GMT 0016-2023 can be used as property IDs. The supported IDs are as follows: - SKF_EnumDev - SKF_GetDevInfo - SKF_EnumApplication - SKF_EnumContainer |
| [getResourceId](arkts-universalkeystore-huksexternalcrypto-getresourceid-f.md#getResourceId) | Obtain the resource ID of the provider. |
| [getUkeyPinAuthState](arkts-universalkeystore-huksexternalcrypto-getukeypinauthstate-f.md#getUkeyPinAuthState) | Obtains the PIN authentication state. This API uses a promise to return the result. |
| [openResource](arkts-universalkeystore-huksexternalcrypto-openresource-f.md#openResource) | Open resource by specific resource ID. NOTE: The opened resource must be closed using closeResource. |
| [registerProvider](arkts-universalkeystore-huksexternalcrypto-registerprovider-f.md#registerProvider) | Registers a specified external Provider. This API uses a promise to return the result. |
| [setProperty](arkts-universalkeystore-huksexternalcrypto-setproperty-f.md#setProperty) | The set-type operations of the external crypto extension support calling custom interfaces. However, the custom interface must be registered with the provider. |
| [unregisterProvider](arkts-universalkeystore-huksexternalcrypto-unregisterprovider-f.md#unregisterProvider) | Unregisters a specified external Provider. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [authUkeyPin](arkts-universalkeystore-huksexternalcrypto-authukeypin-f-sys.md#authUkeyPin) | Authenticates a UKey PIN. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md) | Defines the type of the param array used for calling the API. |
| [HuksExternalErrorInfo](arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | Defines detailed error information. |

### Enums

| Name | Description |
| --- | --- |
| [HuksExternalCryptoTag](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotag-e.md) | Enumerates the tags used to invoke parameters. |
| [HuksExternalCryptoTagType](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotagtype-e.md) | Enumerates the external encrypted data types. |
| [HuksExternalPinAuthState](arkts-universalkeystore-huksexternalcrypto-huksexternalpinauthstate-e.md) | Enumerates the Ukey PIN authentication states. |

