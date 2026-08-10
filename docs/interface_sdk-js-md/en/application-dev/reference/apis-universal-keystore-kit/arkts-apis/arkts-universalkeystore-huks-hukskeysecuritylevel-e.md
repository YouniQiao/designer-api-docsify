# HuksKeySecurityLevel

表示密钥安全级别的枚举。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-huks-export enum HuksKeySecurityLevel--><!--Device-huks-export enum HuksKeySecurityLevel-End-->

**System capability:** SystemCapability.Security.Huks.Core

## HUKS_KEY_SECURITY_LEVEL_TEE

```TypeScript
HUKS_KEY_SECURITY_LEVEL_TEE = 0
```

密钥在可信执行环境中生成并使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HuksKeySecurityLevel-HUKS_KEY_SECURITY_LEVEL_TEE = 0--><!--Device-HuksKeySecurityLevel-HUKS_KEY_SECURITY_LEVEL_TEE = 0-End-->

**System capability:** SystemCapability.Security.Huks.Core

## HUKS_KEY_SECURITY_LEVEL_SE

```TypeScript
HUKS_KEY_SECURITY_LEVEL_SE = 1
```

密钥在安全环境中生成并使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_SE_KEY

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HuksKeySecurityLevel-HUKS_KEY_SECURITY_LEVEL_SE = 1--><!--Device-HuksKeySecurityLevel-HUKS_KEY_SECURITY_LEVEL_SE = 1-End-->

**System capability:** SystemCapability.Security.Huks.Core

