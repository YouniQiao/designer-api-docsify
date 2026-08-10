# Macro

Macro继承自[MacroQuery](arkts-camera-camera-macroquery-i.md)。

提供使能微距能力的接口。

**Inheritance/Implementation:** Macro extends [MacroQuery](arkts-camera-camera-macroquery-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

使能当前的微距能力。

> **说明：**
> 
> 使用该接口前，需要先通过[isMacroSupported](arkts-camera-camera-macroquery-i.md#ismacrosupported)接口查询当前设备是否支持微距能力。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Macro-enableMacro(enabled: boolean): void--><!--Device-Macro-enableMacro(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 是否开启微距能力。true表示开启微距能力，false表示关闭微距能力。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed.<br>**Applicable version:** 12 and later |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**Applicable version:** 11 - 18 |

