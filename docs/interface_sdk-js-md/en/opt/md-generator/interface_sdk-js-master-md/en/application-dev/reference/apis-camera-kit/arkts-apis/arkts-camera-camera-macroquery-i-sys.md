# MacroQuery (System API)

MacroQuery provides the API to check the support for macro photography.

**Since:** 23

<!--Device-camera-interface MacroQuery--><!--Device-camera-interface MacroQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## isMacroSupported

```TypeScript
isMacroSupported(): boolean
```

Checks whether macro photography is supported in the current state. This API must be called after [commitConfig](arkts-camera-camera-session-i.md#commitconfig).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MacroQuery-isMacroSupported(): boolean--><!--Device-MacroQuery-isMacroSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
