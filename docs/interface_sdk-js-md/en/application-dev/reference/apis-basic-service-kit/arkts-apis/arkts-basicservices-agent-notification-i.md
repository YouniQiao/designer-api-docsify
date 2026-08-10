# Notification

通知栏自定义信息。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-agent-interface Notification--><!--Device-agent-interface Notification-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## text

```TypeScript
text?: string
```

通知栏自定义正文。若不设置则使用默认显示方式。text长度上限为3072B。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-Notification-text?: string--><!--Device-Notification-text?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## title

```TypeScript
title?: string
```

通知栏自定义标题。若不设置则使用默认显示方式。title长度上限为1024B。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-Notification-title?: string--><!--Device-Notification-title?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## visibility

```TypeScript
visibility?: int
```

设置任务的通知栏显示方式，通过[VISIBILITY常量](../../../reference/apis-basic-services-kit/js-apis-request.md#常量-1)的位运算方式决定显示方式，任务通知的显示方式，包括如下几种：

- 仅显示完成通知，参数为VISIBILITY_COMPLETION或1，任务完成/失败后展示对应通知。  
- 仅显示进度通知，参数为VISIBILITY_PROGRESS或2，任务在进行中显示进度通知，当任务下载成功/失败后会直接退出进度通知，不会显示完成通知。  
- 显示进度通知/完成通知，参数为VISIBILITY_COMPLETION | VISIBILITY_PROGRESS或3，任务在进行中显示进度通知，当任务下载成功/失败后会退出进度通知，并显示完成通知。

若不设置该参数，则根据gauge字段来判断；若无gauge字段，则仅显示完成通知。

The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Notification-visibility?: int--><!--Device-Notification-visibility?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

通知参数，用于实现点击任务通知后跳转的功能。默认值为空。

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Notification-wantAgent?: WantAgent--><!--Device-Notification-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

