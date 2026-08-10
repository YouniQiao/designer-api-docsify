# NotificationIconButton (System API)

描述系统通知按钮。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationIconButton--><!--Device-unnamed-export interface NotificationIconButton-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## hidePanel

```TypeScript
hidePanel?: boolean
```

点击按钮时，是否隐藏通知中心。默认为false。

- true：是。  
- false：否。

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

按钮的背景图。

**Type:** [IconType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-composelistitem-icontype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-iconResource: IconType--><!--Device-NotificationIconButton-iconResource: IconType-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## name

```TypeScript
name: string
```

按钮标识，用于区分同一通知的多个不同按钮。字符串长度不超过202字节，超出部分会被截断。不可为空字符串。

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

按钮展示的信息。默认为空。字符串长度不超过202字节，超出部分会被截断。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationIconButton-text?: string--><!--Device-NotificationIconButton-text?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

