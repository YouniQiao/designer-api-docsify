# WifiEapConfig

Wi-Fi EAP config.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-wifiManager-interface WifiEapConfig--><!--Device-wifiManager-interface WifiEapConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## altSubjectMatch

```TypeScript
altSubjectMatch: string
```

Alternate subject match

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-altSubjectMatch: string--><!--Device-WifiEapConfig-altSubjectMatch: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## anonymousIdentity

```TypeScript
anonymousIdentity: string
```

Anonymous identity

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-anonymousIdentity: string--><!--Device-WifiEapConfig-anonymousIdentity: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## caCertAlias

```TypeScript
caCertAlias: string
```

CA certificate alias

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-caCertAlias: string--><!--Device-WifiEapConfig-caCertAlias: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## caPath

```TypeScript
caPath: string
```

CA certificate path

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-caPath: string--><!--Device-WifiEapConfig-caPath: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## certEntry

```TypeScript
certEntry: Uint8Array
```

content of user's certificate

**类型：** Uint8Array

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-certEntry: Uint8Array--><!--Device-WifiEapConfig-certEntry: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## certPassword

```TypeScript
certPassword: string
```

Password of user's certificate

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-certPassword: string--><!--Device-WifiEapConfig-certPassword: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## clientCertAlias

```TypeScript
clientCertAlias: string
```

Client certificate alias

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-clientCertAlias: string--><!--Device-WifiEapConfig-clientCertAlias: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## domainSuffixMatch

```TypeScript
domainSuffixMatch: string
```

Domain suffix match

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-domainSuffixMatch: string--><!--Device-WifiEapConfig-domainSuffixMatch: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## eapMethod

```TypeScript
eapMethod: EapMethod
```

EAP authentication method

**类型：** [EapMethod](arkts-connectivity-wifimanager-eapmethod-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-eapMethod: EapMethod--><!--Device-WifiEapConfig-eapMethod: EapMethod-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## eapSubId

```TypeScript
eapSubId: int
```

Sub ID of the SIM card

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-eapSubId: int--><!--Device-WifiEapConfig-eapSubId: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## identity

```TypeScript
identity: string
```

The identity

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-identity: string--><!--Device-WifiEapConfig-identity: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## password

```TypeScript
password: string
```

Password

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-password: string--><!--Device-WifiEapConfig-password: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## phase2Method

```TypeScript
phase2Method: Phase2Method
```

Phase 2 authentication method

**类型：** [Phase2Method](../../apis-network-kit/arkts-apis/arkts-network-eap-phase2method-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-phase2Method: Phase2Method--><!--Device-WifiEapConfig-phase2Method: Phase2Method-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## plmn

```TypeScript
plmn: string
```

Public Land Mobile Network of the provider of Passpoint credential

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-plmn: string--><!--Device-WifiEapConfig-plmn: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## realm

```TypeScript
realm: string
```

Realm for Passpoint credential

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiEapConfig-realm: string--><!--Device-WifiEapConfig-realm: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

