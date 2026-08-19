# Progress

The **Progress** component represents a progress indicator that displays the progress of content loading or an operation.

## Child Components Not supported

## Progress

```TypeScript
Progress(options: ProgressOptions<Type>)
```

Creates a progress indicator.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressInterface-<Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>--><!--Device-ProgressInterface-<Type extends keyof ProgressStyleMap>(options: ProgressOptions<Type>): ProgressAttribute<Type>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ProgressOptions](arkts-arkui-progressoptions-i.md)&lt;[Type](../../apis-na/arkts-apis/arkts-na-util-type-e.md)&gt; | Yes | Options of the progress indicator, which vary by progress indicator type. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CapsuleStyleOptions](arkts-arkui-capsulestyleoptions-i.md) | Capsule style options. Inherits from [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md) and [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md) | Provides common style configuration options for the progress indicator. |
| [EclipseStyleOptions](arkts-arkui-eclipsestyleoptions-i.md) | Options of the eclipse style. The eclipse style visualizes the progress in a way similar to the moon waxing from new to full. Inherits from [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [LinearStyleOptions](arkts-arkui-linearstyleoptions-i.md) | Linear style options. Inherits from [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md) and [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [ProgressConfiguration](arkts-arkui-progressconfiguration-i.md) | Provides progress indicator configuration. Inherits from CommonConfiguration. |
| [ProgressOptions](arkts-arkui-progressoptions-i.md) | Defines progress bar options. |
| [ProgressStyleMap](arkts-arkui-progressstylemap-i.md) | Defines the mapping between progress indicators and styles. |
| [ProgressStyleOptions](arkts-arkui-progressstyleoptions-i.md) | Defines the progress bar style options. Inherits from [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [RingStyleOptions](arkts-arkui-ringstyleoptions-i.md) | Options of the ring style without scales. Inherits from [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md) and [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [ScaleRingStyleOptions](arkts-arkui-scaleringstyleoptions-i.md) | Options of the ring style with scales. Inherits from [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md). |
| [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md) | Defines the scan effect options. |

### Enums

| Name | Description |
| --- | --- |
| [ProgressStatus](arkts-arkui-progressstatus-e.md) | Current state of the progress indicator. |
| [ProgressStyle](arkts-arkui-progressstyle-e.md) | Enumerates progress indicator styles. |
| [ProgressType](arkts-arkui-progresstype-e.md) | Enumerates progress indicator types. |

