# CertBlob

表示证书文件数据。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-certificateManager-export interface CertBlob--><!--Device-certificateManager-export interface CertBlob-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## certData

```TypeScript
certData: Uint8Array
```

表示证书文件数据。当certFormat传入PEM_DER，最大长度为8KB。当certFormat传入P7B，最大长度为300KB。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertBlob-certData: Uint8Array--><!--Device-CertBlob-certData: Uint8Array-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certFormat

```TypeScript
certFormat? : CertFileFormat
```

表示证书文件格式。默认值：PEM_DER。

**Type:** [CertFileFormat](arkts-devicecertificate-certificatemanager-certfileformat-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertBlob-certFormat? : CertFileFormat--><!--Device-CertBlob-certFormat? : CertFileFormat-End-->

**System capability:** SystemCapability.Security.CertificateManager

## certScope

```TypeScript
certScope? : CertScope
```

表示用户CA证书的存储位置。默认值：CURRENT_USER。

**Type:** [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CertBlob-certScope? : CertScope--><!--Device-CertBlob-certScope? : CertScope-End-->

**System capability:** SystemCapability.Security.CertificateManager

