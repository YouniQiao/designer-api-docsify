# AuthorizationManager (System API)

Defines the OS account authorization manager class.

**Since:** 24

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## acquireAuthorization

```TypeScript
acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>
```

Acquires an authorization for the current process.

**Since:** 24

**Required permissions:** ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |
| options | [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AcquireAuthorizationResult](arkts-basicservices-osaccount-acquireauthorizationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## hasAuthorization

```TypeScript
hasAuthorization(privilege: string): Promise<boolean>
```

Checks whether the current process has specified authorization.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## releaseAuthorization

```TypeScript
releaseAuthorization(privilege: string): Promise<void>
```

Releases the specified authorization for the current process.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
