# agent(上传下载)

The request agent api. Supports "background" and "frontend" tasks as while. Though "background" and "frontend" here do not the same with process's concept. All tasks will be executed at request manager service and recorded. Background tasks is for concurrent transfer, such as caching videos for a later play. Frontend tasks is for instant transfer, such as submitting forms for a consumption bill. Background tasks use notification to tell user tasks' status information. Frontend tasks use callback to tell caller tasks' status information. Background has some automatically restore mechanism. Frontend tasks controlled by caller. Uses `multipart/form-data` in client request for upload. A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download. More details, please see the architecture documents of the request subsystem. Only front-end mode is supported in cross-platform scenarios.

**起始版本：** 10

**系统能力：** SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create(上传下载)](arkts-basicservices-agent-create-f.md) |
| [create(上传下载)](arkts-basicservices-agent-create-f.md) |
| [getTask(上传下载)](arkts-basicservices-agent-gettask-f.md) |
| [remove(上传下载)](arkts-basicservices-agent-remove-f.md) |
| [remove(上传下载)](arkts-basicservices-agent-remove-f.md) |
| [show(上传下载)](arkts-basicservices-agent-show-f.md) |
| [show(上传下载)](arkts-basicservices-agent-show-f.md) |
| [touch(上传下载)](arkts-basicservices-agent-touch-f.md) |
| [touch(上传下载)](arkts-basicservices-agent-touch-f.md) |
| [search(上传下载)](arkts-basicservices-agent-search-f.md) |
| [search(上传下载)](arkts-basicservices-agent-search-f.md) |
| [search(上传下载)](arkts-basicservices-agent-search-f.md) |
| [createGroup(上传下载)](arkts-basicservices-agent-creategroup-f.md) |
| [attachGroup(上传下载)](arkts-basicservices-agent-attachgroup-f.md) |
| [deleteGroup(上传下载)](arkts-basicservices-agent-deletegroup-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [query(上传下载)](arkts-basicservices-agent-query-f-sys.md) |
| [query(上传下载)](arkts-basicservices-agent-query-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [FileSpec(上传下载)](arkts-basicservices-agent-filespec-i.md) |
| [FormItem(上传下载)](arkts-basicservices-agent-formitem-i.md) |
| [Notification(上传下载)](arkts-basicservices-agent-notification-i.md) |
| [MinSpeed(上传下载)](arkts-basicservices-agent-minspeed-i.md) |
| [Timeout(上传下载)](arkts-basicservices-agent-timeout-i.md) |
| [Config(上传下载)](arkts-basicservices-agent-config-i.md) |
| [Progress(上传下载)](arkts-basicservices-agent-progress-i.md) |
| [Filter(上传下载)](arkts-basicservices-agent-filter-i.md) |
| [TaskInfo(上传下载)](arkts-basicservices-agent-taskinfo-i.md) |
| [HttpResponse(上传下载)](arkts-basicservices-agent-httpresponse-i.md) |
| [Task(上传下载)](arkts-basicservices-agent-task-i.md) |
| [GroupConfig(上传下载)](arkts-basicservices-agent-groupconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Notification(上传下载)](arkts-basicservices-agent-notification-i-sys.md) |
| [Filter(上传下载)](arkts-basicservices-agent-filter-i-sys.md) |
| [TaskInfo(上传下载)](arkts-basicservices-agent-taskinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Action(上传下载)](arkts-basicservices-agent-action-e.md) |
| [Mode(上传下载)](arkts-basicservices-agent-mode-e.md) |
| [Network(上传下载)](arkts-basicservices-agent-network-e.md) |
| [BroadcastEvent(上传下载)](arkts-basicservices-agent-broadcastevent-e.md) |
| [State(上传下载)](arkts-basicservices-agent-state-e.md) |
| [Faults(上传下载)](arkts-basicservices-agent-faults-e.md) |
| [WaitingReason(上传下载)](arkts-basicservices-agent-waitingreason-e.md) |

### 常量

| 名称 |
| --- |
| [VISIBILITY_COMPLETION(上传下载)](arkts-basicservices-agent-con.md#visibility_completion) |
| [VISIBILITY_PROGRESS(上传下载)](arkts-basicservices-agent-con.md#visibility_progress) |
