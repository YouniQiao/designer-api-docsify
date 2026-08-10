# NotificationFlags

描述通知标志位。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationFlags--><!--Device-unnamed-export interface NotificationFlags-End-->

**System capability:** SystemCapability.Notification.Notification

## reminderFlags

```TypeScript
readonly reminderFlags?: long
```

是否启用输入信息提示功能。

- bit0：铃声提示。0表示关闭，1表示开启。   
- bit1：锁屏。0表示关闭，1表示开启。   
- bit2：横幅。0表示关闭，1表示开启。   
- bit3：亮屏。0表示关闭，1表示开启。   
- bit4：振动。0表示关闭，1表示开启。   
- bit5：状态栏通知图标。0表示关闭，1表示开启。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationFlags-readonly reminderFlags?: long--><!--Device-NotificationFlags-readonly reminderFlags?: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

