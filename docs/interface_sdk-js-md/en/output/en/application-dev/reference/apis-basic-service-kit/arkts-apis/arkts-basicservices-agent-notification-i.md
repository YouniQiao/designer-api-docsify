# Notification

Describes the custom information of the notification bar.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-agent-interface Notification--><!--Device-agent-interface Notification-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## text

```TypeScript
text?: string
```

Custom body text, with a maximum of 3072 bytes. The default text is used if this parameter is not set.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-Notification-text?: string--><!--Device-Notification-text?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## title

```TypeScript
title?: string
```

Custom title, with a maximum of 1024 bytes. The default title is used if this parameter is not set.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-Notification-title?: string--><!--Device-Notification-title?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## visibility

```TypeScript
visibility?: int
```

Task visibility mode for the notification bar, which is determined by bitwise operations on the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The options are as follows: - Only the completion notification is displayed. The parameter is **VISIBILITY\_COMPLETION** or **1**. The corresponding notification is displayed after the task is complete or fails. - Only the progress notification is displayed when the task is in progress. The parameter is **VISIBILITY\_PROGRESS** or **2**. Completion notification is not displayed when the download task is complete or fails. - The progress notification and completion notification are displayed. The parameter is VISIBILITY\_COMPLETION | VISIBILITY\_PROGRESS or **3**. The progress notification is displayed when the task is in progress. When the download task is complete or fails, the completion notification is displayed as well. If this parameter is not set, the **gauge** field is used for determination. If there is no **gauge** field, only the completion notification is displayed. The value should be an integer.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Notification-visibility?: int--><!--Device-Notification-visibility?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

Notification parameter, which is used to implement redirection after a task notification is tapped. The default value is empty.

**Type:** WantAgent

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Notification-wantAgent?: WantAgent--><!--Device-Notification-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

