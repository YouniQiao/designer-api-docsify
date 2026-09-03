# type_def.h

## Overview

Declares common types.

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](capi-ffrt.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ffrt_function_header_t](capi-ffrt-ffrt-function-header-t.md) | ffrt_function_header_t | Defines a task executor, used to define the task execution and destruction callbacks.The exec callback is invoked when the task is scheduled, and the destroy callbackis invoked after the task completes to release task-related resources. Together theymanage the full lifecycle of an FFRT task. |
| [ffrt_dependence_t](capi-ffrt-ffrt-dependence-t.md) | ffrt_dependence_t | Defines the dependency data structure used to describe a single dependency between tasks. |
| [ffrt_deps_t](capi-ffrt-ffrt-deps-t.md) | ffrt_deps_t | Defines the dependency structure, used to hold a list of dependencies for a task. |
| [ffrt_task_attr_t](capi-ffrt-ffrt-task-attr-t.md) | ffrt_task_attr_t | Defines the task attribute structure used to store task attribute information. |
| [ffrt_queue_attr_t](capi-ffrt-ffrt-queue-attr-t.md) | ffrt_queue_attr_t | Defines the queue attribute structure used to store queue attribute information. |
| [ffrt_condattr_t](capi-ffrt-ffrt-condattr-t.md) | ffrt_condattr_t | Defines the condition variable attribute structure used to store condition variable attribute information. |
| [ffrt_mutexattr_t](capi-ffrt-ffrt-mutexattr-t.md) | ffrt_mutexattr_t | Defines the mutex attribute structure used to store mutex attribute information. |
| [ffrt_rwlockattr_t](capi-ffrt-ffrt-rwlockattr-t.md) | ffrt_rwlockattr_t | Defines the rwlock attribute structure used to store rwlock attribute information. |
| [ffrt_mutex_t](capi-ffrt-ffrt-mutex-t.md) | ffrt_mutex_t | Defines the mutex structure used to store internal data of the mutex. |
| [ffrt_rwlock_t](capi-ffrt-ffrt-rwlock-t.md) | ffrt_rwlock_t | Defines the rwlock structure used to store internal data of the rwlock. |
| [ffrt_cond_t](capi-ffrt-ffrt-cond-t.md) | ffrt_cond_t | Defines the condition variable structure used to store internal data of the condition variable. |
| [ffrt_fiber_t](capi-ffrt-ffrt-fiber-t.md) | ffrt_fiber_t | Defines the fiber structure used to store fiber execution context. |
| [ffrt_task_handle_t](capi-ffrt-ffrt-task-handle-t.md) | ffrt_task_handle_t | Defines the task handle, which identifies different tasks. |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ffrt_queue_priority_t](#ffrt_queue_priority_t) | ffrt_queue_priority_t | Enumerates the task priority types used by concurrent queues to order task dispatch. |
| [ffrt_qos_default_t](#ffrt_qos_default_t) | ffrt_qos_default_t | Enumerates the task QoS types. |
| [ffrt_storage_size_t](#ffrt_storage_size_t) | ffrt_storage_size_t | Defines the storage size of multiple types of structs, in bytes. |
| [ffrt_function_kind_t](#ffrt_function_kind_t) | ffrt_function_kind_t | Enumerates the task types, distinguishing general concurrent tasks from queue-scheduled tasks. |
| [ffrt_dependence_type_t](#ffrt_dependence_type_t) | ffrt_dependence_type_t | Enumerates the dependency types.Specifies how tasks depend on each other (data readiness or task completion). |
| [ffrt_error_t](#ffrt_error_t) | ffrt_error_t | Enumerates the error codes returned by FFRT APIs. |
| [ffrt_mutex_type](#ffrt_mutex_type) | ffrt_mutex_type | Enumerates the mutex types. |
| [qos_default](#qos_default) | - | Enumerates the task QoS types.Each enumerator mirrors the corresponding enumerator in [ffrt_qos_default_t](capi-type-def-h.md#ffrt_qos_default_t). |

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef void (\*ffrt_function_t)(void*)](#ffrt_function_t) | ffrt_function_t | Defines the task function pointer type.The function pointer defines the entry point of an FFRT task. FFRT invokesthis function when the task is scheduled for execution, passing the userdata pointer through the single `void*` argument. |
| [typedef void (\*ffrt_poller_cb)(void* data, uint32_t event)](#ffrt_poller_cb) | ffrt_poller_cb | Defines the poller callback function type.The callback is invoked when the poller detects a registered event. The datapointer carries user data passed in at registration time, and the event valueidentifies the triggered event type. |
| [typedef void (\*ffrt_timer_cb)(void* data)](#ffrt_timer_cb) | ffrt_timer_cb | Defines the timer callback function type.The callback is invoked when the timer expires. The data pointer carriesuser data passed in at timer registration. |

### Variable

| Name | Description |
| -- | -- |
| [ffrt_storage_size_t](capi-type-def-h.md#ffrt_storage_size_t)  | Fiber storage size, in bytes.This constant defines the fiber storage size.The actual value depends on the target architecture:- __aarch64__: 22- __arm__: 64- __x86_64__: 8<br>**Since**: 20 |
| using qos = int | Defines the QoS type.<br>**Since**: 10 |

## Enum type description

### ffrt_queue_priority_t

```c
enum ffrt_queue_priority_t
```

**Description**

Enumerates the task priority types used by concurrent queues to order task dispatch.

**Since**: 12

| Enum item | Description |
| -- | -- |
| ffrt_queue_priority_immediate = 0 | Highest priority. Dispatched as soon as possible (handle time equals submission time); scheduled before high. |
| ffrt_queue_priority_high | High priority. Sorted by handle time; scheduled before low. |
| ffrt_queue_priority_low | Low priority. Sorted by handle time; scheduled before idle. |
| ffrt_queue_priority_idle | Lowest priority. Sorted by handle time; dispatched only when no other priority is present in the queue. |

### ffrt_qos_default_t

```c
enum ffrt_qos_default_t
```

**Description**

Enumerates the task QoS types.

**Since**: 10

| Enum item | Description |
| -- | -- |
| ffrt_qos_inherit = -1 | Inheritance.Inherits the QoS of the calling thread. Used when a task should adopt the priority of its creator. |
| ffrt_qos_background | Background task.Lowest priority. Used for work the user is not aware of, such as background data sync or log flushing. |
| ffrt_qos_utility | Utility-level task.Used for long-running tasks the user is aware of but does not actively wait on,such as data loading or content indexing. |
| ffrt_qos_default | Default type.Default QoS used when no specific priority is required; suitable for most general tasks. |
| ffrt_qos_user_initiated | User initiated.Used for tasks initiated by the user that need a quick response but do not block the UI,such as opening a document or running a search. |
| ffrt_qos_deadline_request | Deadline request.Used for tasks with explicit deadlines. The system prioritizes scheduling resources for such tasks.<br>**Since**: 23 |
| ffrt_qos_user_interactive | User interactive.Used for tasks that interact with the user, such as UI response.<br>**Since**: 23 |
| ffrt_qos_max = ffrt_qos_user_interactive | Maximum QoS.Equivalent to ffrt_qos_user_interactive.<br>**Since**: 23 |

### ffrt_storage_size_t

```c
enum ffrt_storage_size_t
```

**Description**

Defines the storage size of multiple types of structs, in bytes.

**Since**: 10

| Enum item | Description |
| -- | -- |
| ffrt_task_attr_storage_size = 128 | Task attribute storage size, in bytes. |
| ffrt_auto_managed_function_storage_size = 64 + sizeof(ffrt_function_header_t) | Task executor storage size, in bytes. |
| ffrt_mutex_storage_size = 64 | Mutex storage size, in bytes. |
| ffrt_cond_storage_size = 64 | Condition variable storage size, in bytes. |
| ffrt_queue_attr_storage_size = 128 | Queue storage size, in bytes. |
| ffrt_rwlock_storage_size = 64 | Rwlock storage size, in bytes.<br>**Since**: 18 |
| #if defined(__aarch64__) | Fiber storage size, in bytes.This constant defines the fiber storage size.The actual value depends on the target architecture:- __aarch64__: 22- __arm__: 64- __x86_64__: 8<br>**Since**: 20 |

### ffrt_function_kind_t

```c
enum ffrt_function_kind_t
```

**Description**

Enumerates the task types, distinguishing general concurrent tasks from queue-scheduled tasks.

**Since**: 10

| Enum item | Description |
| -- | -- |
| ffrt_function_kind_general | General task. The task can be submitted to the FFRT scheduler and executed concurrently. |
| ffrt_function_kind_queue | Queue task. The task is executed sequentially through a queue in submission order. |

### ffrt_dependence_type_t

```c
enum ffrt_dependence_type_t
```

**Description**

Enumerates the dependency types.Specifies how tasks depend on each other (data readiness or task completion).

**Since**: 10

| Enum item | Description |
| -- | -- |
| ffrt_dependence_data | Data dependency type. The task is scheduled only after the referenced data is ready. |
| ffrt_dependence_task | Task dependency type. The task is scheduled only after the referenced task has completed. |

### ffrt_error_t

```c
enum ffrt_error_t
```

**Description**

Enumerates the error codes returned by FFRT APIs.

**Since**: 10

| Enum item | Description |
| -- | -- |
| ffrt_error = -1 | A generic error. |
| ffrt_success = 0 | Success. |
| ffrt_error_nomem = ENOMEM | An out of memory error. |
| ffrt_error_timedout = ETIMEDOUT | A timeout error. |
| ffrt_error_busy = EBUSY | A busy error. The resource is busy, please retry later. |
| ffrt_error_inval = EINVAL | An invalid value error. |

### ffrt_mutex_type

```c
enum ffrt_mutex_type
```

**Description**

Enumerates the mutex types.

**Since**: 12

| Enum item | Description |
| -- | -- |
| ffrt_mutex_normal = 0 | Normal mutex type. |
| ffrt_mutex_recursive = 2 | Recursive mutex type, which allows the same thread to lock the mutex multiple times. |
| ffrt_mutex_default = ffrt_mutex_normal | Default mutex type, equivalent to ffrt_mutex_normal. |

### qos_default

```c
enum qos_default
```

**Description**

Enumerates the task QoS types.Each enumerator mirrors the corresponding enumerator in [ffrt_qos_default_t](capi-type-def-h.md#ffrt_qos_default_t).

**Since**: 10

| Enum item | Description |
| -- | -- |
| qos_inherit = ffrt_qos_inherit | Inheritance.Inherits the QoS of the calling thread. Used when a task should adopt the priority of its creator. |
| qos_background = ffrt_qos_background | Background task.Lowest priority. Used for work the user is not aware of, such as background data sync or log flushing. |
| qos_utility = ffrt_qos_utility | Utility-level task.Used for long-running tasks the user is aware of but does not actively wait on,such as data loading or content indexing. |
| qos_default = ffrt_qos_default | Default type.Default QoS used when no specific priority is required; suitable for most general tasks. |
| qos_user_initiated = ffrt_qos_user_initiated | User initiated.Used for tasks initiated by the user that need a quick response but do not block the UI,such as opening a document or running a search. |
| qos_deadline_request = ffrt_qos_deadline_request | Deadline request.Used for tasks with explicit deadlines. The system prioritizes scheduling resources for such tasks.<br>**Since**: 23 |
| qos_user_interactive = ffrt_qos_user_interactive | User interactive.Used for tasks that interact with the user, such as UI response.<br>**Since**: 23 |
| qos_max = ffrt_qos_user_interactive | Maximum QoS.Equivalent to ffrt_qos_user_interactive.<br>**Since**: 23 |


## Function description

### ffrt_function_t()

```c
typedef void (*ffrt_function_t)(void*)
```

**Description**

Defines the task function pointer type.The function pointer defines the entry point of an FFRT task. FFRT invokesthis function when the task is scheduled for execution, passing the userdata pointer through the single `void*` argument.

**Since**: 10

### ffrt_poller_cb()

```c
typedef void (*ffrt_poller_cb)(void* data, uint32_t event)
```

**Description**

Defines the poller callback function type.The callback is invoked when the poller detects a registered event. The datapointer carries user data passed in at registration time, and the event valueidentifies the triggered event type.

**Since**: 12

**Parameters**:

| Parameter | Description |
| -- | -- |
| void\* data | Indicates the user data pointer passed in at poller registration. |
| uint32_t event | Indicates the event type that triggered the callback. |

### ffrt_timer_cb()

```c
typedef void (*ffrt_timer_cb)(void* data)
```

**Description**

Defines the timer callback function type.The callback is invoked when the timer expires. The data pointer carriesuser data passed in at timer registration.

**Since**: 12

**Parameters**:

| Parameter | Description |
| -- | -- |
| void\* data | Indicates the user data pointer passed in at timer registration. |


