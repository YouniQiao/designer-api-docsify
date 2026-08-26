# @ohos.net.networkSecurity(Network Security)

The **networkSecurity** module provides the network security verification capability. Specifically, it provides APIs for applications to verify the certificates in use.

**Since:** 11

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [certVerification(Network Security)](arkts-network-networksecurity-certverification-f.md) | Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed by the user in the certificate management. This API uses a promise to return the result. |
| [certVerificationSync(Network Security)](arkts-network-networksecurity-certverificationsync-f.md) | Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed by the user in the certificate management. This API returns the result synchronously. |
| [isCleartextPermitted(Network Security)](arkts-network-networksecurity-iscleartextpermitted-f.md) | Checks whether plaintext HTTP access is allowed from the preset **network_config.json** file of the application. By default, plaintext HTTP access is allowed. |
| [isCleartextPermittedByHostName(Network Security)](arkts-network-networksecurity-iscleartextpermittedbyhostname-f.md) | Checks whether host name–based plaintext HTTP access is allowed from the preset **network_config.json** file of the application. By default, plaintext HTTP access is allowed. |
| [verifyCertChain(Network Security)](arkts-network-networksecurity-verifycertchain-f.md) | Verifies the server certificate chain and returns a sorted chain. |

### Interfaces

| Name | Description |
| --- | --- |
| [CertBlob(Network Security)](arkts-network-networksecurity-certblob-i.md) | Defines the certificate data. |

### Enums

| Name | Description |
| --- | --- |
| [CertType(Network Security)](arkts-network-networksecurity-certtype-e.md) | Enumerates certificate types. |
