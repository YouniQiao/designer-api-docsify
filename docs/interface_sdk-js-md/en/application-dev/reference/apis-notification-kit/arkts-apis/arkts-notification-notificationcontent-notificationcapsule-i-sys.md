# NotificationCapsule

描述通知胶囊，用于在实况窗中展示胶囊形态。

> **说明：**
> 
> 实际显示效果依赖于设备能力和通知中心UI样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationCapsule--><!--Device-unnamed-export interface NotificationCapsule-End-->

**System capability:** SystemCapability.Notification.Notification

## capsuleButtons

```TypeScript
capsuleButtons?: Array<NotificationIconButton>
```

即时任务类实况胶囊的按钮（最多支持2个）。默认为空。

**Type:** Array&lt;NotificationIconButton&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationCapsule-capsuleButtons?: Array<NotificationIconButton>--><!--Device-NotificationCapsule-capsuleButtons?: Array<NotificationIconButton>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## content

```TypeScript
content?: string
```

胶囊的拓展文本。默认为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationCapsule-content?: string--><!--Device-NotificationCapsule-content?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## time

```TypeScript
time?: int
```

即时任务类实况胶囊展示时长。默认值为0。单位：秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationCapsule-time?: int--><!--Device-NotificationCapsule-time?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

