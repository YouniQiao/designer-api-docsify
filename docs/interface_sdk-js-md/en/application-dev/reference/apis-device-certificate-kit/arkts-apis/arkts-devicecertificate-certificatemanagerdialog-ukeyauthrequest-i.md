# UkeyAuthRequest

USB key PIN authentication request.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-certificateManagerDialog-export interface UkeyAuthRequest--><!--Device-certificateManagerDialog-export interface UkeyAuthRequest-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

## keyUri

```TypeScript
keyUri: string
```

Unique identifier of the USB Key credential. The value contains up to 256 bytes.The value of this parameter can be obtained from the CertReference returned by invoking the  
[openAuthorizeDialog]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ interface.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UkeyAuthRequest-keyUri: string--><!--Device-UkeyAuthRequest-keyUri: string-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

