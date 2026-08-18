# registerPasscodePromptCallback (System API)

## Modules to Import

```TypeScript
```

## registerPasscodePromptCallback

```TypeScript
function registerPasscodePromptCallback(callback: PasscodePromptCallback): void
```

Registers the callback invoked when the framework needs a companion device passcode. If a callback has already been registered, the new one replaces it.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-function registerPasscodePromptCallback(callback: PasscodePromptCallback): void--><!--Device-companionDeviceAuth-function registerPasscodePromptCallback(callback: PasscodePromptCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PasscodePromptCallback](arkts-userauthentication-companiondeviceauth-passcodepromptcallback-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32600001](../errorcode-useriam.md#32600001-system-service-not-working-properly) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
