# NotificationProgress

Describes the notification progress, which is used to display progress bar information in the live view.

> **NOTE：**&gt;
> The actual display effect depends on the device capabilities and the notification center UI style.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## currentValue

```TypeScript
currentValue?: int
```

Current value of the progress.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## isPercentage

```TypeScript
isPercentage?: boolean
```

Whether to display the progress as a percentage. The value defaults to **false**.  
- **true**: The progress is displayed as a percentage. - **false**: The progress is displayed as an absolute value.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## maxValue

```TypeScript
maxValue?: int
```

Maximum value of the progress.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification
