# Macro

**Macro** inherits from [MacroQuery](arkts-camera-camera-macroquery-i.md).

It provides the API to enable macro photography.

**Inheritance/Implementation:** Macro extends [MacroQuery](arkts-camera-camera-macroquery-i.md)

**Since:** 19

<!--Device-camera-interface Macro extends MacroQuery--><!--Device-camera-interface Macro extends MacroQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## enableMacro

```TypeScript
enableMacro(enabled: boolean): void
```

Enables or disables macro photography.

> **NOTE：**
> 
> Before calling this API, call [isMacroSupported](arkts-camera-camera-macroquery-i.md#ismacrosupported) to check whether the
> current device supports macro photography.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Macro-enableMacro(enabled: boolean): void--><!--Device-Macro-enableMacro(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
