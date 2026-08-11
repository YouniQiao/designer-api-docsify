# startEthEap

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## startEthEap

```TypeScript
function startEthEap(netId: number, profile: EthEapProfile): void
```

Set the specified network interface parameters.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function startEthEap(netId: number, profile: EthEapProfile): void--><!--Device-eap-function startEthEap(netId: number, profile: EthEapProfile): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netId | number | Yes |
| profile | [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33200010](../errorcode-net-eap.md#33200010-invalid-eap-status) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200003](../errorcode-net-eap.md#33200003-invalid-eth-eap-configuration) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
| [33200001](../errorcode-net-eap.md#33200001-invalid-netid) |

## Examples

```TypeScript
import {eap} from '@kit.NetworkKit';
let netId = 100;
let profile: eap.EthEapProfile = {
  eapMethod: eap.EapMethod.EAP_TTLS,
  phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
  identity: "identity",
  anonymousIdentity: "anonymousIdentity",
  password: "password",
  caCertAliases: "caCertAliases",
  caPath: "caPath",
  clientCertAliases: "clientCertAliases",
  certEntry: new Uint8Array([5,6,7,8,9,10]),
  certPassword: "certPassword",
  altSubjectMatch: "altSubjectMatch",
  domainSuffixMatch: "domainSuffixMatch",
  realm: "realm",
  plmn: "plmn",
  eapSubId: 1
};
    
try {
  eap.startEthEap(netId, profile);
  console.info('startEthEap success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
