# agent

The request agent api. Supports "background" and "frontend" tasks as while. Though "background" and "frontend" here do not the same with process's concept. All tasks will be executed at request manager service and recorded. Background tasks is for concurrent transfer, such as caching videos for a later play. Frontend tasks is for instant transfer, such as submitting forms for a consumption bill. Background tasks use notification to tell user tasks' status information. Frontend tasks use callback to tell caller tasks' status information. Background has some automatically restore mechanism. Frontend tasks controlled by caller. Uses `multipart/form-data` in client request for upload. A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download. More details, please see the architecture documents of the request subsystem. Only front-end mode is supported in cross-platform scenarios.

**Since:** 23

<!--Device-request-namespace agent--><!--Device-request-namespace agent-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [create](arkts-basicservices-agent-create-f.md#create) |
| [create](arkts-basicservices-agent-create-f.md#create) |
| [getTask](arkts-basicservices-agent-gettask-f.md#gettask) |
| [remove](arkts-basicservices-agent-remove-f.md#remove) |
| [remove](arkts-basicservices-agent-remove-f.md#remove) |
| [show](arkts-basicservices-agent-show-f.md#show) |
| [show](arkts-basicservices-agent-show-f.md#show) |
| [touch](arkts-basicservices-agent-touch-f.md#touch) |
| [touch](arkts-basicservices-agent-touch-f.md#touch) |
| [search](arkts-basicservices-agent-search-f.md#search) |
| [search](arkts-basicservices-agent-search-f.md#search) |
| [search](arkts-basicservices-agent-search-f.md#search) |
| [createGroup](arkts-basicservices-agent-creategroup-f.md#creategroup) |
| [attachGroup](arkts-basicservices-agent-attachgroup-f.md#attachgroup) |
| [deleteGroup](arkts-basicservices-agent-deletegroup-f.md#deletegroup) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [query](arkts-basicservices-agent-query-f-sys.md#query-system-api) |
| [query](arkts-basicservices-agent-query-f-sys.md#query-system-api) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Notification](arkts-basicservices-agent-notification-i-sys.md) |
| [Filter](arkts-basicservices-agent-filter-i-sys.md) |
| [TaskInfo](arkts-basicservices-agent-taskinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action](arkts-basicservices-agent-action-e.md) |
| [Mode](arkts-basicservices-agent-mode-e.md) |
| [Network](arkts-basicservices-agent-network-e.md) |
| [BroadcastEvent](arkts-basicservices-agent-broadcastevent-e.md) |
| [State](arkts-basicservices-agent-state-e.md) |
| [Faults](arkts-basicservices-agent-faults-e.md) |
| [WaitingReason](arkts-basicservices-agent-waitingreason-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [VISIBILITY_COMPLETION](arkts-basicservices-agent-con.md#visibilitycompletion) |
| [VISIBILITY_PROGRESS](arkts-basicservices-agent-con.md#visibilityprogress) |
