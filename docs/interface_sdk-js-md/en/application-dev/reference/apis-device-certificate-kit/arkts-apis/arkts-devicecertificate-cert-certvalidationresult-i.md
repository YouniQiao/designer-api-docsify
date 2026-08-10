# CertValidationResult

证书验证的结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cert-interface CertValidationResult--><!--Device-cert-interface CertValidationResult-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## certChain

```TypeScript
readonly certChain: Array<X509Cert>
```

验证后的证书链。验证成功时返回完整的证书链，从终端实体证书到信任锚点。可用于后续的证书信息查询或其他验证操作。

**Type:** Array&lt;X509Cert&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationResult-readonly certChain: Array<X509Cert>--><!--Device-CertValidationResult-readonly certChain: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

