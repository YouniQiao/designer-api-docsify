# InterruptForceType

Enumerates the types of force that causes audio interruption.

The force type is obtained when an [InterruptEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is received.

This type specifies whether audio interruption is forcibly performed by the system. The operation information (such as audio pause or stop) can be obtained through [InterruptHint]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. For details about the audio interruption policy, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-enum InterruptForceType--><!--Device-audio-enum InterruptForceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## INTERRUPT_FORCE

```TypeScript
INTERRUPT_FORCE = 0
```

The operation is forcibly performed by the system.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterruptForceType-INTERRUPT_FORCE = 0--><!--Device-InterruptForceType-INTERRUPT_FORCE = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## INTERRUPT_SHARE

```TypeScript
INTERRUPT_SHARE = 1
```

The operation will not be performed by the system. [InterruptHint]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is used to provide recommended operations for the application, and the application can determine the next processing mode.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterruptForceType-INTERRUPT_SHARE = 1--><!--Device-InterruptForceType-INTERRUPT_SHARE = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

