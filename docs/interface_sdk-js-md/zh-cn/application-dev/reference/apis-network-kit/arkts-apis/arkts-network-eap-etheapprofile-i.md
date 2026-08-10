# EthEapProfile

Eth EAP profile.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-eap-interface EthEapProfile--><!--Device-eap-interface EthEapProfile-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## altSubjectMatch

```TypeScript
altSubjectMatch: string
```

Alternate subject match

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-altSubjectMatch: string--><!--Device-EthEapProfile-altSubjectMatch: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## anonymousIdentity

```TypeScript
anonymousIdentity: string
```

Anonymous identity

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-anonymousIdentity: string--><!--Device-EthEapProfile-anonymousIdentity: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## caCertAliases

```TypeScript
caCertAliases: string
```

CA certificate alias

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-caCertAliases: string--><!--Device-EthEapProfile-caCertAliases: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## caPath

```TypeScript
caPath: string
```

CA certificate path

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-caPath: string--><!--Device-EthEapProfile-caPath: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## certEntry

```TypeScript
certEntry: Uint8Array
```

content of user's certificate

**类型：** Uint8Array

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-certEntry: Uint8Array--><!--Device-EthEapProfile-certEntry: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## certPassword

```TypeScript
certPassword: string
```

Password of user's certificate

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-certPassword: string--><!--Device-EthEapProfile-certPassword: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## clientCertAliases

```TypeScript
clientCertAliases: string
```

Client certificate alias

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-clientCertAliases: string--><!--Device-EthEapProfile-clientCertAliases: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## domainSuffixMatch

```TypeScript
domainSuffixMatch: string
```

Domain suffix match

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-domainSuffixMatch: string--><!--Device-EthEapProfile-domainSuffixMatch: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## eapMethod

```TypeScript
eapMethod: EapMethod
```

EAP authentication method

**类型：** [EapMethod](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-wifimanager-eapmethod-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-eapMethod: EapMethod--><!--Device-EthEapProfile-eapMethod: EapMethod-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## eapSubId

```TypeScript
eapSubId: number
```

Sub ID of the SIM card

**类型：** number

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-eapSubId: number--><!--Device-EthEapProfile-eapSubId: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## identity

```TypeScript
identity: string
```

The identity

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-identity: string--><!--Device-EthEapProfile-identity: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## password

```TypeScript
password: string
```

Password

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-password: string--><!--Device-EthEapProfile-password: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## phase2Method

```TypeScript
phase2Method: Phase2Method
```

Phase 2 authentication method

**类型：** [Phase2Method](arkts-network-eap-phase2method-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-phase2Method: Phase2Method--><!--Device-EthEapProfile-phase2Method: Phase2Method-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## plmn

```TypeScript
plmn: string
```

Public Land Mobile Network of the provider of Passpoint credential

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-plmn: string--><!--Device-EthEapProfile-plmn: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

## realm

```TypeScript
realm: string
```

Realm for Passpoint credential

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-EthEapProfile-realm: string--><!--Device-EthEapProfile-realm: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

