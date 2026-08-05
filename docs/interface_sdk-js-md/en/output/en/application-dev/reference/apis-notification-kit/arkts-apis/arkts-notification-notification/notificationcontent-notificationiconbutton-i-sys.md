# NotificationIconButton (System API)

Describes the system notification button.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationIconButton--><!--Device-unnamed-export interface NotificationIconButton-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## hidePanel

```TypeScript
hidePanel?: boolean
```

Whether to hide the notification panel when the button is tapped. The default value is **false**. - **true**: Yes. - **false**: No.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-hidePanel?: boolean--><!--Device-NotificationIconButton-hidePanel?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## iconResource

```TypeScript
iconResource: IconType
```

Background image of a button.

**Type:** IconType

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-iconResource: IconType--><!--Device-NotificationIconButton-iconResource: IconType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## name

```TypeScript
name: string
```

Button identifier, used to distinguish multiple different buttons for the same notification. The string length cannot exceed 202 bytes, and the exceeding part will be truncated. It cannot be an empty string.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-name: string--><!--Device-NotificationIconButton-name: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## text

```TypeScript
text?: string
```

Text displayed on the button, which defaults to empty. The string length cannot exceed 202 bytes, and the exceeding part will be truncated.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-text?: string--><!--Device-NotificationIconButton-text?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

