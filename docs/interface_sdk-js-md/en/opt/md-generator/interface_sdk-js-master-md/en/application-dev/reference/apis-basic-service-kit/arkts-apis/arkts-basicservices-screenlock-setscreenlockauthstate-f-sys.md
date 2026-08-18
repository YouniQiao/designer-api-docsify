# setScreenLockAuthState (System API)

## Modules to Import

```TypeScript
```

## setScreenLockAuthState

```TypeScript
function setScreenLockAuthState(state: AuthState, userId: number, authToken: Uint8Array): Promise<boolean>
```

Set the screen lock authentication state for os account local userId.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function setScreenLockAuthState(state: AuthState, userId: int, authToken: Uint8Array): Promise<boolean>--><!--Device-screenLock-function setScreenLockAuthState(state: AuthState, userId: int, authToken: Uint8Array): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [AuthState](arkts-basicservices-screenlock-authstate-e-sys.md) | Yes |
| userId | number | Yes |
| authToken | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |
