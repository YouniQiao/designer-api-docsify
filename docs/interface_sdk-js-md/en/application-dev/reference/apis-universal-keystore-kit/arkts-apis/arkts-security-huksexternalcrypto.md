# @ohos.security.huksExternalCrypto(External Key Management)

Provides the functionalities such as registration and deregistration of external key management extension, PIN authentication, and acquisition of authentication state.

**Since:** 22

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
| [clearUkeyPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-clearukeypinauthstate-f.md) | Clear the PIN auth state of the specified resource ID. |
| [closeResource(External Key Management)](arkts-universalkeystore-huksexternalcrypto-closeresource-f.md) | Close the resource with a specific resource ID. |
| [getErrorInfo(External Key Management)](arkts-universalkeystore-huksexternalcrypto-geterrorinfo-f.md) | Get the detailed error information. |
| [getProperty(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getproperty-f.md) | Obtains a property value. This API uses a promise to return the result. The **propertyId** indicates the ID of the property to be queried. Currently, only the SKF API names defined in GMT 0016-2023 can be used as property IDs. The supported IDs are as follows: - SKF_EnumDev - SKF_GetDevInfo - SKF_EnumApplication - SKF_EnumContainer |
| [getResourceId(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getresourceid-f.md) | Obtain the resource ID of the provider. |
| [getUkeyPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-getukeypinauthstate-f.md) | Obtains the PIN authentication state. This API uses a promise to return the result. |
| [openResource(External Key Management)](arkts-universalkeystore-huksexternalcrypto-openresource-f.md) | Open resource by specific resource ID. NOTE: The opened resource must be closed using closeResource. |
| [registerProvider(External Key Management)](arkts-universalkeystore-huksexternalcrypto-registerprovider-f.md) | Registers a specified external Provider. This API uses a promise to return the result. |
| [setProperty(External Key Management)](arkts-universalkeystore-huksexternalcrypto-setproperty-f.md) | The set-type operations of the external crypto extension support calling custom interfaces. However, the custom interface must be registered with the provider. |
| [unregisterProvider(External Key Management)](arkts-universalkeystore-huksexternalcrypto-unregisterprovider-f.md) | Unregisters a specified external Provider. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [authUkeyPin(External Key Management)](arkts-universalkeystore-huksexternalcrypto-authukeypin-f-sys.md) | Authenticates a UKey PIN. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [HuksExternalCryptoParam(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md) | Defines the type of the param array used for calling the API. |
| [HuksExternalErrorInfo(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | Defines detailed error information. |

### Enums

| Name | Description |
| --- | --- |
| [HuksExternalCryptoTag(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotag-e.md) | Enumerates the tags used to invoke parameters. |
| [HuksExternalCryptoTagType(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptotagtype-e.md) | Enumerates the external encrypted data types. |
| [HuksExternalPinAuthState(External Key Management)](arkts-universalkeystore-huksexternalcrypto-huksexternalpinauthstate-e.md) | Enumerates the Ukey PIN authentication states. |

