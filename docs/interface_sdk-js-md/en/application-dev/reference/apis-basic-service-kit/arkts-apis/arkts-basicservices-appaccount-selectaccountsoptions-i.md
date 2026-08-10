# SelectAccountsOptions

表示用于选择账号的选项。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appAccount-interface SelectAccountsOptions--><!--Device-appAccount-interface SelectAccountsOptions-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## allowedAccounts

```TypeScript
allowedAccounts?: Array<AppAccountInfo>
```

允许的账号数组，默认为空。

**Type:** Array&lt;AppAccountInfo&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SelectAccountsOptions-allowedAccounts?: Array<AppAccountInfo>--><!--Device-SelectAccountsOptions-allowedAccounts?: Array<AppAccountInfo>-End-->

**System capability:** SystemCapability.Account.AppAccount

## allowedOwners

```TypeScript
allowedOwners?: Array<string>
```

允许的账号所有者数组，默认为空。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SelectAccountsOptions-allowedOwners?: Array<string>--><!--Device-SelectAccountsOptions-allowedOwners?: Array<string>-End-->

**System capability:** SystemCapability.Account.AppAccount

## requiredLabels

```TypeScript
requiredLabels?: Array<string>
```

认证器的标签标识，默认为空。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SelectAccountsOptions-requiredLabels?: Array<string>--><!--Device-SelectAccountsOptions-requiredLabels?: Array<string>-End-->

**System capability:** SystemCapability.Account.AppAccount

