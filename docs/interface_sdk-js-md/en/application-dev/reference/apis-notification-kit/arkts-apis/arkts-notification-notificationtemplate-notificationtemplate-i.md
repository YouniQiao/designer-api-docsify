# NotificationTemplate

通知模板。用于指定通知所使用的模板类型。

> **说明：**
> 
> 提供预定义模板支持。允许应用开发者使用系统预定义的通知模板，只需提供模板名称和相应的数据，系统会自动渲染出符合规范的通知样式。
> 使用场景：当前仅支持上传下载场景。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationTemplate--><!--Device-unnamed-export interface NotificationTemplate-End-->

**System capability:** SystemCapability.Notification.Notification

## data

```TypeScript
data: Record<string, Object>
```

模板数据。

- title: 表示下载标题。必填字段，值为字符串类型。  
- fileName: 表示下载文件名。必填字段，值为字符串类型。  
- progressValue: 表示下载进度，值为数值类型。建议取值范围为0~100，  
 表示百分比进度。当`progressValue`取值小于或等于0时，进度为0； 当其取值大于或等于100时，进度环消失，代表下载完成。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-NotificationTemplate-data: Record<string, Object>--><!--Device-NotificationTemplate-data: Record<string, Object>-End-->

**System capability:** SystemCapability.Notification.Notification

## name

```TypeScript
name: string
```

模板名称。当前仅支持表示下载进度的进度条通知模板，取值为'downloadTemplate'。字符串长度不超过202字节，超出部分会被截断。不可为空字符串。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-NotificationTemplate-name: string--><!--Device-NotificationTemplate-name: string-End-->

**System capability:** SystemCapability.Notification.Notification

