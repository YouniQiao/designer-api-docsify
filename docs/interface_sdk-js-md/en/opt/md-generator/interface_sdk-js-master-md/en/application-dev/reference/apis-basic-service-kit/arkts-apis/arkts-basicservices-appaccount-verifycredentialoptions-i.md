# VerifyCredentialOptions

Represents the options for verifying the user credential.

**Since:** 23

<!--Device-appAccount-interface VerifyCredentialOptions--><!--Device-appAccount-interface VerifyCredentialOptions-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
```

## credential

```TypeScript
credential?: string
```

Credential value. The custom value, the value cannot exceed 1024 characters. By default, no value is passed in.

**Type:** string

**Since:** 23

<!--Device-VerifyCredentialOptions-credential?: string--><!--Device-VerifyCredentialOptions-credential?: string-End-->

**System capability:** SystemCapability.Account.AppAccount

## credentialType

```TypeScript
credentialType?: string
```

Credential type. The custom type, the value cannot exceed 1024 characters. By default, no value is passed in.

**Type:** string

**Since:** 23

<!--Device-VerifyCredentialOptions-credentialType?: string--><!--Device-VerifyCredentialOptions-credentialType?: string-End-->

**System capability:** SystemCapability.Account.AppAccount

## parameters

```TypeScript
parameters?: Record<string, RecordData>
```

Custom parameter object. By default, no value is passed in.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

<!--Device-VerifyCredentialOptions-parameters?: Record<string, RecordData>--><!--Device-VerifyCredentialOptions-parameters?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Account.AppAccount
