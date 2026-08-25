# agent(Upload and Download)

The request agent api. Supports "background" and "frontend" tasks as while. Though "background" and "frontend" here do not the same with process's concept. All tasks will be executed at request manager service and recorded. Background tasks is for concurrent transfer, such as caching videos for a later play. Frontend tasks is for instant transfer, such as submitting forms for a consumption bill. Background tasks use notification to tell user tasks' status information. Frontend tasks use callback to tell caller tasks' status information. Background has some automatically restore mechanism. Frontend tasks controlled by caller. Uses `multipart/form-data` in client request for upload. A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download. More details, please see the architecture documents of the request subsystem. Only front-end mode is supported in cross-platform scenarios.

**Since:** 10

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [create(Upload and Download)](arkts-basicservices-agent-create-f.md) |
| [create(Upload and Download)](arkts-basicservices-agent-create-f.md) |
| [getTask(Upload and Download)](arkts-basicservices-agent-gettask-f.md) |
| [remove(Upload and Download)](arkts-basicservices-agent-remove-f.md) |
| [remove(Upload and Download)](arkts-basicservices-agent-remove-f.md) |
| [show(Upload and Download)](arkts-basicservices-agent-show-f.md) |
| [show(Upload and Download)](arkts-basicservices-agent-show-f.md) |
| [touch(Upload and Download)](arkts-basicservices-agent-touch-f.md) |
| [touch(Upload and Download)](arkts-basicservices-agent-touch-f.md) |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) |
| [createGroup(Upload and Download)](arkts-basicservices-agent-creategroup-f.md) |
| [attachGroup(Upload and Download)](arkts-basicservices-agent-attachgroup-f.md) |
| [deleteGroup(Upload and Download)](arkts-basicservices-agent-deletegroup-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [query(Upload and Download)](arkts-basicservices-agent-query-f-sys.md) |
| [query(Upload and Download)](arkts-basicservices-agent-query-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FileSpec(Upload and Download)](arkts-basicservices-agent-filespec-i.md) |
| [FormItem(Upload and Download)](arkts-basicservices-agent-formitem-i.md) |
| [Notification(Upload and Download)](arkts-basicservices-agent-notification-i.md) |
| [MinSpeed(Upload and Download)](arkts-basicservices-agent-minspeed-i.md) |
| [Timeout(Upload and Download)](arkts-basicservices-agent-timeout-i.md) |
| [Config(Upload and Download)](arkts-basicservices-agent-config-i.md) |
| [Progress(Upload and Download)](arkts-basicservices-agent-progress-i.md) |
| [Filter(Upload and Download)](arkts-basicservices-agent-filter-i.md) |
| [TaskInfo(Upload and Download)](arkts-basicservices-agent-taskinfo-i.md) |
| [HttpResponse(Upload and Download)](arkts-basicservices-agent-httpresponse-i.md) |
| [Task(Upload and Download)](arkts-basicservices-agent-task-i.md) |
| [GroupConfig(Upload and Download)](arkts-basicservices-agent-groupconfig-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Notification(Upload and Download)](arkts-basicservices-agent-notification-i-sys.md) |
| [Filter(Upload and Download)](arkts-basicservices-agent-filter-i-sys.md) |
| [TaskInfo(Upload and Download)](arkts-basicservices-agent-taskinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action(Upload and Download)](arkts-basicservices-agent-action-e.md) |
| [Mode(Upload and Download)](arkts-basicservices-agent-mode-e.md) |
| [Network(Upload and Download)](arkts-basicservices-agent-network-e.md) |
| [BroadcastEvent(Upload and Download)](arkts-basicservices-agent-broadcastevent-e.md) |
| [State(Upload and Download)](arkts-basicservices-agent-state-e.md) |
| [Faults(Upload and Download)](arkts-basicservices-agent-faults-e.md) |
| [WaitingReason(Upload and Download)](arkts-basicservices-agent-waitingreason-e.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [VISIBILITY_COMPLETION(Upload and Download)](arkts-basicservices-agent-con.md#visibility_completion) |
| [VISIBILITY_PROGRESS(Upload and Download)](arkts-basicservices-agent-con.md#visibility_progress) |
