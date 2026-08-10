# CertBlob

证书信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.enterprise.securityManager:securityManager.CertBlob](arkts-mdm-securitymanager-certblob-i.md)

<!--Device-deviceSettings-export interface CertBlob--><!--Device-deviceSettings-export interface CertBlob-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## alias

```TypeScript
alias: string
```

证书别名，别名长度小于40个字符。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** @ohos.enterprise.securityManager:securityManager.alias

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertBlob-alias: string--><!--Device-CertBlob-alias: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## inData

```TypeScript
inData: Uint8Array
```

证书的二进制内容。

**Type:** Uint8Array

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** @ohos.enterprise.securityManager:securityManager.inData

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertBlob-inData: Uint8Array--><!--Device-CertBlob-inData: Uint8Array-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

