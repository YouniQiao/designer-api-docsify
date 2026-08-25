# VerifyCredentialOptions

Represents the options for verifying the user credential.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from '@kit.BasicServicesKit';
```

## credential

```TypeScript
credential?: string
```

Credential value. The custom value, the value cannot exceed 1024 characters. By default, no value is passed in.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.AppAccount

## credentialType

```TypeScript
credentialType?: string
```

Credential type. The custom type, the value cannot exceed 1024 characters. By default, no value is passed in.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.AppAccount

## parameters

```TypeScript
parameters?: Record<string, Object>
```

Custom parameter object. By default, no value is passed in.

**Type:** Record&lt;string, Object&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Account.AppAccount
