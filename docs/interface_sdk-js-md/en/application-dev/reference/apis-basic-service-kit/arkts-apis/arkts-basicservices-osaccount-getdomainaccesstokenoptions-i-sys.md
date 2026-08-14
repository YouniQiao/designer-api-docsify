# GetDomainAccessTokenOptions (System API)

Defines the options for obtaining a domain access token.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-interface GetDomainAccessTokenOptions--><!--Device-osAccount-interface GetDomainAccessTokenOptions-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'osAccount';
```

## businessParams

```TypeScript
businessParams: Record<string, RecordData>
```

Indicates the business parameters.

**Type:** Record&lt;string, [RecordData](arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-GetDomainAccessTokenOptions-businessParams: Record<string, RecordData>--><!--Device-GetDomainAccessTokenOptions-businessParams: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## callerUid

```TypeScript
callerUid: int
```

Unique identifier of the caller.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-GetDomainAccessTokenOptions-callerUid: int--><!--Device-GetDomainAccessTokenOptions-callerUid: int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## domainAccountInfo

```TypeScript
domainAccountInfo: DomainAccountInfo
```

Domain account information.

**Type:** [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-GetDomainAccessTokenOptions-domainAccountInfo: DomainAccountInfo--><!--Device-GetDomainAccessTokenOptions-domainAccountInfo: DomainAccountInfo-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## domainAccountToken

```TypeScript
domainAccountToken: Uint8Array
```

Token of the domain account.

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-GetDomainAccessTokenOptions-domainAccountToken: Uint8Array--><!--Device-GetDomainAccessTokenOptions-domainAccountToken: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

