# WifiEapProfile

可扩展身份验证协议配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-wifiManager-interface WifiEapProfile--><!--Device-wifiManager-interface WifiEapProfile-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## altSubjectMatch

```TypeScript
altSubjectMatch: string
```

替代主题匹配。证书验证中，除了检查证书主域名，还检查证书的主题备用名称是否匹配。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-altSubjectMatch: string--><!--Device-WifiEapProfile-altSubjectMatch: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## anonymousIdentity

```TypeScript
anonymousIdentity: string
```

匿名身份。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-anonymousIdentity: string--><!--Device-WifiEapProfile-anonymousIdentity: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## caCertAliases

```TypeScript
caCertAliases: string
```

CA 证书别名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-caCertAliases: string--><!--Device-WifiEapProfile-caCertAliases: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## caPath

```TypeScript
caPath: string
```

CA 证书路径。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-caPath: string--><!--Device-WifiEapProfile-caPath: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## certEntry

```TypeScript
certEntry: Uint8Array
```

客户端证书内容。当eapMethod为EAP_TLS时，如果该字段为空，则客户端证书别名不能为空。

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-certEntry: Uint8Array--><!--Device-WifiEapProfile-certEntry: Uint8Array-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## certPassword

```TypeScript
certPassword: string
```

CA证书密码。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-certPassword: string--><!--Device-WifiEapProfile-certPassword: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## clientCertAliases

```TypeScript
clientCertAliases: string
```

客户端证书别名。当客户端证书内容为空时，客户端证书需先调用证书管理接口安装后传入别名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-clientCertAliases: string--><!--Device-WifiEapProfile-clientCertAliases: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## domainSuffixMatch

```TypeScript
domainSuffixMatch: string
```

域后缀匹配。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-domainSuffixMatch: string--><!--Device-WifiEapProfile-domainSuffixMatch: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## eapMethod

```TypeScript
eapMethod: EapMethod
```

EAP认证方式。

**Type:** [EapMethod](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-wifimanager-eapmethod-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-eapMethod: EapMethod--><!--Device-WifiEapProfile-eapMethod: EapMethod-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## eapSubId

```TypeScript
eapSubId: number
```

SIM卡的子ID。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-eapSubId: number--><!--Device-WifiEapProfile-eapSubId: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## identity

```TypeScript
identity: string
```

身份信息。当eapMethod为TLS时，该字段不能为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-identity: string--><!--Device-WifiEapProfile-identity: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## password

```TypeScript
password: string
```

PWD类型，密码认证。无需服务器证书。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-password: string--><!--Device-WifiEapProfile-password: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## phase2Method

```TypeScript
phase2Method: Phase2Method
```

第二阶段认证方式。只有eapMethod为EAP_PEAP或EAP_TTLS时需要填写。

**Type:** [Phase2Method](../../apis-network-kit/arkts-apis/arkts-network-eap-phase2method-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-phase2Method: Phase2Method--><!--Device-WifiEapProfile-phase2Method: Phase2Method-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## plmn

```TypeScript
plmn: string
```

凭证提供商。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-plmn: string--><!--Device-WifiEapProfile-plmn: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## realm

```TypeScript
realm: string
```

通行证凭证的领域。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiEapProfile-realm: string--><!--Device-WifiEapProfile-realm: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

