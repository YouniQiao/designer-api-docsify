# NotificationProgress

描述通知进度，用于在实况窗中展示进度条信息。

> **说明：**
> 
> 实际显示效果依赖于设备能力和通知中心UI样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationProgress--><!--Device-unnamed-export interface NotificationProgress-End-->

**System capability:** SystemCapability.Notification.Notification

## currentValue

```TypeScript
currentValue?: int
```

进度当前值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-currentValue?: int--><!--Device-NotificationProgress-currentValue?: int-End-->

**System capability:** SystemCapability.Notification.Notification

## isPercentage

```TypeScript
isPercentage?: boolean
```

是否按百分比展示进度。默认为false。

- true：进度以百分比形式展示。  
- false：进度以绝对值形式展示。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-isPercentage?: boolean--><!--Device-NotificationProgress-isPercentage?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## maxValue

```TypeScript
maxValue?: int
```

进度最大值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationProgress-maxValue?: int--><!--Device-NotificationProgress-maxValue?: int-End-->

**System capability:** SystemCapability.Notification.Notification

