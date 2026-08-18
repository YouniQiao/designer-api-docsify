# PasscodeSubmitCallback (System API)

```TypeScript
type PasscodeSubmitCallback = (passcode: Uint8Array) => void
```

Defines the callback used to submit a passcode entered by the user.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type PasscodeSubmitCallback = (passcode: Uint8Array) => void--><!--Device-companionDeviceAuth-type PasscodeSubmitCallback = (passcode: Uint8Array) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| passcode | Uint8Array | Yes |
