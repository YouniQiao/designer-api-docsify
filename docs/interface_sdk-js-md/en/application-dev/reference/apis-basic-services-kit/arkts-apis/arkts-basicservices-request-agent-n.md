# agent(Upload and Download)

The request agent api. Supports "background" and "frontend" tasks as while. Though "background" and "frontend" here do not the same with process's concept. All tasks will be executed at request manager service and recorded. Background tasks is for concurrent transfer, such as caching videos for a later play. Frontend tasks is for instant transfer, such as submitting forms for a consumption bill. Background tasks use notification to tell user tasks' status information. Frontend tasks use callback to tell caller tasks' status information. Background has some automatically restore mechanism. Frontend tasks controlled by caller. Uses `multipart/form-data` in client request for upload. A `Content-Disposition: attachment; filename=&lt;filename&gt;` response from server leads to download. More details, please see the architecture documents of the request subsystem. Only front-end mode is supported in cross-platform scenarios.

**Since:** 10

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import request from '@kit.BasicServicesKit';
import cacheDownload from '@kit.BasicServicesKit.cacheDownload';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [create(Upload and Download)](arkts-basicservices-agent-create-f.md) | Creates an upload or download task and adds it to the queue. This API uses an asynchronous callback to return the result. HTTP/HTTPS is supported. |
| [create(Upload and Download)](arkts-basicservices-agent-create-f.md) | Creates an upload or download task and adds it to the queue. This API uses a promise to return the result. HTTP/ HTTPS is supported. |
| [getTask(Upload and Download)](arkts-basicservices-agent-gettask-f.md) | Obtains task information based on the task ID. This API uses a promise to return the result. |
| [remove(Upload and Download)](arkts-basicservices-agent-remove-f.md) | Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses an asynchronous callback to return the result. After this API is called, the **task** object and its callback function are released. |
| [remove(Upload and Download)](arkts-basicservices-agent-remove-f.md) | Removes a specified task of the invoker. If the task is being executed, the task is forced to stop. This API uses a promise to return the result. After this API is called, the **task** object and its callback function are released. |
| [show(Upload and Download)](arkts-basicservices-agent-show-f.md) | Queries the task details based on the task ID. This API uses an asynchronous callback to return the result. |
| [show(Upload and Download)](arkts-basicservices-agent-show-f.md) | Queries the task details based on the task ID. This API uses a promise to return the result. |
| [touch(Upload and Download)](arkts-basicservices-agent-touch-f.md) | Queries the task details based on the task ID and token. This API uses an asynchronous callback to return the result. |
| [touch(Upload and Download)](arkts-basicservices-agent-touch-f.md) | Queries the task details based on the task ID and token. This API uses a promise to return the result. |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) | Searches for task IDs based on [Filter](arkts-basicservices-agent-filter-i.md). The IDs of all tasks from the invoking time to 24 hours ago are searched. This API uses an asynchronous callback to return the result. |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) | Searches for task IDs based on [Filter](arkts-basicservices-agent-filter-i.md). This API uses an asynchronous callback to return the result. |
| [search(Upload and Download)](arkts-basicservices-agent-search-f.md) | Searches for task IDs based on [Filter](arkts-basicservices-agent-filter-i.md). This API uses a promise to return the result. |
| [createGroup(Upload and Download)](arkts-basicservices-agent-creategroup-f.md) | Creates a group based on [GroupConfig](arkts-basicservices-agent-groupconfig-i.md). This API uses a promise to return the result. |
| [attachGroup(Upload and Download)](arkts-basicservices-agent-attachgroup-f.md) | Attaches multiple download task IDs to a specified group ID. This API uses a promise to return the result.If any task ID does not meet the attachment conditions, all tasks in the list will not be added to the group. |
| [deleteGroup(Upload and Download)](arkts-basicservices-agent-deletegroup-f.md) | Deletes a specified group. No task ID can be added to the group. This API uses a promise to return the result.When all tasks in a group are succeeded, failed, or removed and the group is deleted, the completion and failure notifications of this group are displayed. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [query(Upload and Download)](arkts-basicservices-agent-query-f-sys.md) | Queries specified task details. Creates a group based on GroupConfig |
| [query(Upload and Download)](arkts-basicservices-agent-query-f-sys.md) | Queries specified task details. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [FileSpec(Upload and Download)](arkts-basicservices-agent-filespec-i.md) | Provides the file information of a table item. |
| [FormItem(Upload and Download)](arkts-basicservices-agent-formitem-i.md) | Describes the form item of a task. |
| [Notification(Upload and Download)](arkts-basicservices-agent-notification-i.md) | Describes the custom information of the notification bar. |
| [MinSpeed(Upload and Download)](arkts-basicservices-agent-minspeed-i.md) | Defines the minimum speed of a task. If the task speed is lower than the preset value for a specified period of time, the task fails. The failure cause is [LOW_SPEED](arkts-basicservices-agent-faults-e.md). |
| [Timeout(Upload and Download)](arkts-basicservices-agent-timeout-i.md) | Defines the timeout configuration of a task. The task waiting duration is not counted. For details about the waiting reasons, see [WaitingReason&lt;sup&gt;20+&lt;/sup&gt;](arkts-basicservices-agent-waitingreason-e.md). |
| [Config(Upload and Download)](arkts-basicservices-agent-config-i.md) | Provides the configuration information of an upload or download task. |
| [Progress(Upload and Download)](arkts-basicservices-agent-progress-i.md) | Describes the data structure of the task progress. |
| [Filter(Upload and Download)](arkts-basicservices-agent-filter-i.md) | Defines the filter criteria. |
| [TaskInfo(Upload and Download)](arkts-basicservices-agent-taskinfo-i.md) | Defines the data structure of the task information for query. The fields available vary depending on the query type. |
| [HttpResponse(Upload and Download)](arkts-basicservices-agent-httpresponse-i.md) | Describes the data structure of the task response header. |
| [Task(Upload and Download)](arkts-basicservices-agent-task-i.md) | Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through [request.agent.create](arkts-basicservices-agent-create-f.md) or from a callback through [request.agent.create](arkts-basicservices-agent-create-f.md). |
| [GroupConfig(Upload and Download)](arkts-basicservices-agent-groupconfig-i.md) | Describes group configuration options for download tasks. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [Notification(Upload and Download)](arkts-basicservices-agent-notification-i-sys.md) | Describes the custom information of the notification bar. |
| [Filter(Upload and Download)](arkts-basicservices-agent-filter-i-sys.md) | Defines the filter criteria. |
| [TaskInfo(Upload and Download)](arkts-basicservices-agent-taskinfo-i-sys.md) | Defines the data structure of the task information for query. The fields available vary depending on the query type. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [Action(Upload and Download)](arkts-basicservices-agent-action-e.md) | Defines action options. |
| [Mode(Upload and Download)](arkts-basicservices-agent-mode-e.md) | Defines mode options.After foreground tasks of an application are switched to the background for a period of time, background tasks are not affected but foreground tasks will fail or pause. |
| [Network(Upload and Download)](arkts-basicservices-agent-network-e.md) | Defines network options.If the network does not meet the preset conditions, the tasks that have not been executed will await for execution, and the tasks that are being executed will fail or pause. |
| [BroadcastEvent(Upload and Download)](arkts-basicservices-agent-broadcastevent-e.md) | Defines a custom system event. You can use a common event API to obtain the event.The upload and download SA has the **ohos.permission.SEND_TASK_COMPLETE_EVENT** permission. You can configure the level-2 configuration file to which the metadata of an event points to intercept other event senders.Use the **CommonEventData** type to transmit data related to common events. The members in **CommonEventData** are different from those described in [CommonEventData](arkts-basicservices-commoneventdata-commoneventdata-i.md). Specifically, **CommonEventData.code** indicates the task status, which is **0x40 COMPLETE** or **0x41 FAILED**, and **CommonEventData.data** indicates the task ID.<!--Del-->For details about how to obtain the event configuration and configure the level-2 configuration file, see [Subscribing to Common Events in Static Mode (for System Applications Only)](../../../basic-services/common-event/common-event-static-subscription-sys.md).<!--DelEnd--> |
| [State(Upload and Download)](arkts-basicservices-agent-state-e.md) | Defines the current task status. |
| [Faults(Upload and Download)](arkts-basicservices-agent-faults-e.md) | Defines the cause of a task failure. |
| [WaitingReason(Upload and Download)](arkts-basicservices-agent-waitingreason-e.md) | Enumerates the reasons why a task is waiting. |

### Constants

| Name | Description |
| --- | --- |
| [VISIBILITY_COMPLETION(Upload and Download)](arkts-basicservices-agent-con.md#visibility_completion) | ([Notification](arkts-basicservices-agent-notification-i.md) visibility type) Displays completion notifications. |
| [VISIBILITY_PROGRESS(Upload and Download)](arkts-basicservices-agent-con.md#visibility_progress) | ([Notification](arkts-basicservices-agent-notification-i.md) visibility type) Displays progress notifications. |
