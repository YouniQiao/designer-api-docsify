# CreateAccountImplicitlyOptions

Defines the options for implicitly creating an application account.

**Since:** 23

<!--Device-appAccount-interface CreateAccountImplicitlyOptions--><!--Device-appAccount-interface CreateAccountImplicitlyOptions-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from '@kit.BasicServicesKit';
```

## authType

```TypeScript
authType?: string
```

Authentication type.

**Type:** string

**Since:** 23

<!--Device-CreateAccountImplicitlyOptions-authType?: string--><!--Device-CreateAccountImplicitlyOptions-authType?: string-End-->

**System capability:** SystemCapability.Account.AppAccount

## parameters

```TypeScript
parameters?: Record<string, RecordData>
```

Custom parameter object. By default, no value is passed in.

**Type:** Record&lt;string, [RecordData](arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

<!--Device-CreateAccountImplicitlyOptions-parameters?: Record<string, RecordData>--><!--Device-CreateAccountImplicitlyOptions-parameters?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Account.AppAccount

## requiredLabels

```TypeScript
requiredLabels?: Array<string>
```

Required labels. By default, no value is passed in.

**Type:** Array&lt;string&gt;

**Since:** 23

<!--Device-CreateAccountImplicitlyOptions-requiredLabels?: Array<string>--><!--Device-CreateAccountImplicitlyOptions-requiredLabels?: Array<string>-End-->

**System capability:** SystemCapability.Account.AppAccount

