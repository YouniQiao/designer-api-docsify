# NotificationProgress

Describes the notification progress, which is used to display progress bar information in the live view.
    **NOTE**  
    
    The actual display effect depends on the device capabilities and the notification center UI style.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationProgress--><!--Device-unnamed-export interface NotificationProgress-End-->

**System capability:** SystemCapability.Notification.Notification

## currentValue

```TypeScript
currentValue?: int
```

Current value of the progress.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-currentValue?: int--><!--Device-NotificationProgress-currentValue?: int-End-->

**System capability:** SystemCapability.Notification.Notification

## isPercentage

```TypeScript
isPercentage?: boolean
```

Whether to display the progress as a percentage. The value defaults to **false**.

- **true**: The progress is displayed as a percentage.  
- **false**: The progress is displayed as an absolute value.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-isPercentage?: boolean--><!--Device-NotificationProgress-isPercentage?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## maxValue

```TypeScript
maxValue?: int
```

Maximum value of the progress.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-maxValue?: int--><!--Device-NotificationProgress-maxValue?: int-End-->

**System capability:** SystemCapability.Notification.Notification

