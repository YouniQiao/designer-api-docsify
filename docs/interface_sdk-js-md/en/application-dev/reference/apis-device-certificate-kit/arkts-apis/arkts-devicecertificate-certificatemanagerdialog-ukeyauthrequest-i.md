# UkeyAuthRequest

USB Key PIN码认证请求。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-certificateManagerDialog-export interface UkeyAuthRequest--><!--Device-certificateManagerDialog-export interface UkeyAuthRequest-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## keyUri

```TypeScript
keyUri: string
```

表示USB Key证书凭据的唯一标识符，长度限制256字节以内。该参数值可通过调用[openAuthorizeDialog](arkts-devicecertificate-certificatemanagerdialog-openauthorizedialog-f.md#openauthorizedialog)接口返回的CertReference中获取。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UkeyAuthRequest-keyUri: string--><!--Device-UkeyAuthRequest-keyUri: string-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

