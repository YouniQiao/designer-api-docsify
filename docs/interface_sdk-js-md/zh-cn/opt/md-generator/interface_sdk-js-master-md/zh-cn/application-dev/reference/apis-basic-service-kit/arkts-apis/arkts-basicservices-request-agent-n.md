# agent

The request agent api.Supports "background" and "frontend" tasks as while.Though "background" and "frontend" here do not the same with process's concept.All tasks will be executed at request manager service and recorded.Background tasks is for concurrent transfer, such as caching videos for a later play.Frontend tasks is for instant transfer, such as submitting forms for a consumption bill.Background tasks use notification to tell user tasks' status information.Frontend tasks use callback to tell caller tasks' status information.Background has some automatically restore mechanism.Frontend tasks controlled by caller.Uses `multipart/form-data` in client request for upload.A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download.More details, please see the architecture documents of the request subsystem.Only front-end mode is supported in cross-platform scenarios.

**起始版本：** 10

<!--Device-request-namespace agent--><!--Device-request-namespace agent-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## 汇总

### 函数

| 名称 |
| --- |
| [create](arkts-basicservices-agent-create-f.md#create) |
| [create](arkts-basicservices-agent-create-f.md#create-1) |
| [getTask](arkts-basicservices-agent-gettask-f.md#gettask) |
| [remove](arkts-basicservices-agent-remove-f.md#remove) |
| [remove](arkts-basicservices-agent-remove-f.md#remove-1) |
| [show](arkts-basicservices-agent-show-f.md#show) |
| [show](arkts-basicservices-agent-show-f.md#show-1) |
| [touch](arkts-basicservices-agent-touch-f.md#touch) |
| [touch](arkts-basicservices-agent-touch-f.md#touch-1) |
| [search](arkts-basicservices-agent-search-f.md#search) |
| [search](arkts-basicservices-agent-search-f.md#search-1) |
| [search](arkts-basicservices-agent-search-f.md#search-2) |
| [createGroup](arkts-basicservices-agent-creategroup-f.md#creategroup) |
| [attachGroup](arkts-basicservices-agent-attachgroup-f.md#attachgroup) |
| [deleteGroup](arkts-basicservices-agent-deletegroup-f.md#deletegroup) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [query](arkts-basicservices-agent-query-f-sys.md#query) |
| [query](arkts-basicservices-agent-query-f-sys.md#query-1) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [FileSpec](arkts-basicservices-agent-filespec-i.md) |
| [FormItem](arkts-basicservices-agent-formitem-i.md) |
| [Notification](arkts-basicservices-agent-notification-i.md) |
| [MinSpeed](arkts-basicservices-agent-minspeed-i.md) |
| [Timeout](arkts-basicservices-agent-timeout-i.md) |
| [Config](arkts-basicservices-agent-config-i.md) |
| [Progress](arkts-basicservices-agent-progress-i.md) |
| [Filter](arkts-basicservices-agent-filter-i.md) |
| [TaskInfo](arkts-basicservices-agent-taskinfo-i.md) |
| [HttpResponse](arkts-basicservices-agent-httpresponse-i.md) |
| [Task](arkts-basicservices-agent-task-i.md) |
| [GroupConfig](arkts-basicservices-agent-groupconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Notification](arkts-basicservices-agent-notification-i-sys.md) |
| [Filter](arkts-basicservices-agent-filter-i-sys.md) |
| [TaskInfo](arkts-basicservices-agent-taskinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Action](arkts-basicservices-agent-action-e.md) |
| [Mode](arkts-basicservices-agent-mode-e.md) |
| [Network](arkts-basicservices-agent-network-e.md) |
| [BroadcastEvent](arkts-basicservices-agent-broadcastevent-e.md) |
| [State](arkts-basicservices-agent-state-e.md) |
| [Faults](arkts-basicservices-agent-faults-e.md) |
| [WaitingReason](arkts-basicservices-agent-waitingreason-e.md) |

### 常量

| 名称 |
| --- |
| [VISIBILITY_COMPLETION](arkts-basicservices-agent-con.md#visibility_completion) |
| [VISIBILITY_PROGRESS](arkts-basicservices-agent-con.md#visibility_progress) |
