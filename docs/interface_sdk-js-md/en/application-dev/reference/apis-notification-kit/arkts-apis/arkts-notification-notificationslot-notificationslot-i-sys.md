# NotificationSlot

描述通知渠道，不同通知渠道对应的通知提醒方式不同。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationSlot--><!--Device-unnamed-export interface NotificationSlot-End-->

**System capability:** SystemCapability.Notification.Notification

## authorizedStatus

```TypeScript
readonly authorizedStatus?: int
```

授权状态。

- 0：表示已授权。   
- 1：表示待授权。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-readonly authorizedStatus?: int--><!--Device-NotificationSlot-readonly authorizedStatus?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reminderMode

```TypeScript
readonly reminderMode?: int
```

通知提醒模式。

- bit0：铃声提示。0表示关闭，1表示开启。   
- bit1：锁屏。0表示关闭，1表示开启。   
- bit2：横幅。0表示关闭，1表示开启。   
- bit3：亮屏。0表示关闭，1表示开启。   
- bit4：振动。0表示关闭，1表示开启。   
- bit5：状态栏通知图标。0表示关闭，1表示开启。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationSlot-readonly reminderMode?: int--><!--Device-NotificationSlot-readonly reminderMode?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

