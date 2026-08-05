# InputEvent

The **inputEvent** module provides the basic events reported by the device.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface InputEvent--><!--Device-unnamed-export declare interface InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## actionTime

```TypeScript
actionTime: long
```

Time when an input event is reported, in microseconds (μs) since the system starts.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-actionTime: long--><!--Device-InputEvent-actionTime: long-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## deviceId

```TypeScript
deviceId: int
```

Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-deviceId: int--><!--Device-InputEvent-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## id

```TypeScript
id: int
```

Enumerates event IDs.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-id: int--><!--Device-InputEvent-id: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## screenId

```TypeScript
screenId: int
```

Target screen ID.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-screenId: int--><!--Device-InputEvent-screenId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## windowId

```TypeScript
windowId: int
```

Target window ID.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-windowId: int--><!--Device-InputEvent-windowId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

