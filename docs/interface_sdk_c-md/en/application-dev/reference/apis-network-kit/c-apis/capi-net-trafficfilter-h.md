# net_trafficfilter.h

## Overview

Defines the APIs for traffic filtering.

**Library**: libnet_trafficfilter.so

**System capability**: SystemCapability.Communication.NetManager.NetFirewall

**Since**: 26.0.0

**Related module**: [TrafficFilter](capi-trafficfilter.md)

## Summary

### Function

| Name | Description |
| -- | -- |
| [int32_t OH_TrafficFilter_CreateRedirector(uint32_t group_id, uint32_t priority, OH_TrafficFilter_Redirector** redirector
)](#oh_trafficfilter_createredirector) | Creates a traffic redirection instanceCreates a traffic redirection instance for transparent TCP traffic redirection to proxy serverResource Management: You must call [OH_TrafficFilter_DestroyRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector) to release resources.If this function fails, no valid redirector is returned. |
| [int32_t OH_TrafficFilter_DestroyRedirector(OH_TrafficFilter_Redirector* redirector)](#oh_trafficfilter_destroyredirector) | Destroys a traffic redirection instance.Destroys the redirection instance and releases related resources, including rules.The handle becomes invalid after this call. |
| [int32_t OH_TrafficFilter_AddRedirectRule(OH_TrafficFilter_Redirector* redirector, const OH_TrafficFilter_RedirectRule* rule
)](#oh_trafficfilter_addredirectrule) | Adds a redirection ruleAdds a TCP traffic redirection rule to redirect matched traffic to specified proxy serverTo clear redirect rules, you need to call [OH_TrafficFilter_ClearRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule). |
| [int32_t OH_TrafficFilter_ClearRedirectRule(OH_TrafficFilter_Redirector* redirector)](#oh_trafficfilter_clearredirectrule) | Clear all redirection rule |
| [int32_t OH_TrafficFilter_QueryProcess(const OH_TrafficFilter_ConnectionInfo* connection_info, OH_TrafficFilter_ProcessInfo* process_info
)](#oh_trafficfilter_queryprocess) | Queries corresponding process information based on connection informationQueries corresponding process information based on five-tuple information |
| [int32_t OH_TrafficFilter_AddPacketRule(OH_TrafficFilter_PacketController* controller, const OH_TrafficFilter_FilterRule* rule
)](#oh_trafficfilter_addpacketrule) | Set packet filter ruleAdd a packet filter rule to controller chain.only packets matching the rule will be intercepted and sent to callback function. |
| [int32_t OH_TrafficFilter_ClearPacketRule(OH_TrafficFilter_PacketController* controller)](#oh_trafficfilter_clearpacketrule) | Clear packet filter ruleClear all packet filter rules in controller. |
| [int32_t OH_TrafficFilter_CreatePacketController(uint32_t groupId, uint32_t priority, const OH_TrafficFilter_Config* config, OH_TrafficFilter_PacketController** controller
)](#oh_trafficfilter_createpacketcontroller) | Creates a packet controller instance.Creates a packet controller for intercepting and filtering network packetsResource Management: This instance occupies system resources.You must call [OH_TrafficFilter_DestroyPacketController](capi-net-trafficfilter-h.md#oh_trafficfilter_destroypacketcontroller) to release resources.If this function fails, no valid controller is returned. |
| [int32_t OH_TrafficFilter_DestroyPacketController(OH_TrafficFilter_PacketController* controller)](#oh_trafficfilter_destroypacketcontroller) | Destroys a packet controller instance.Destroys the controller and releases related resources, including rules and callbacks.After calling this function, the handle is invalid. Do not use it again. |
| [int32_t OH_TrafficFilter_RegisterPacketCallback(OH_TrafficFilter_PacketController* controller, OH_TrafficFilter_PacketCallback callback, void* userData
)](#oh_trafficfilter_registerpacketcallback) | Register a packet callback function.Register a callback function to handle intercepted packets.The callback will be triggered when packets match the filter rule. |
| [int32_t OH_TrafficFilter_UnregisterPacketCallback(OH_TrafficFilter_PacketController* controller)](#oh_trafficfilter_unregisterpacketcallback) | Unregister a packet callback function.Unregister the current packet callback function.After calling this, no more packets will be delivered to the callback. |

## Function description

### OH_TrafficFilter_CreateRedirector()

```c
int32_t OH_TrafficFilter_CreateRedirector(uint32_t group_id, uint32_t priority, OH_TrafficFilter_Redirector** redirector
)
```

**Description**

Creates a traffic redirection instanceCreates a traffic redirection instance for transparent TCP traffic redirection to proxy serverResource Management: You must call [OH_TrafficFilter_DestroyRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_destroyredirector) to release resources.If this function fails, no valid redirector is returned.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| uint32_t group_id | Redirection chain identifier.This is the logical grouping ID within the application.Multiple redirectors within the same application can use different group_id.The same group_id from different applications will be automatically isolated.The valid range is [{@link OH_TRAFFICFILTER_MIN_GROUP_ID}, {@link OH_TRAFFICFILTER_MAX_GROUP_ID}],including both boundaries. If group_id is outside this range, this function returns[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode). |
| uint32_t priority | Priority.Determines execution order between different group_id chains. A smaller number executes first.Note: Redirector priority is higher than packet filter priority.The valid range is [{@link OH_TRAFFICFILTER_MIN_PRIORITY}, {@link OH_TRAFFICFILTER_MAX_PRIORITY}],including both boundaries. If priority is outside this range, this function returns[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode). |
| redirector | Output parameter, the redirection handle on success. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_GROUP_ID_IN_USE](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) when group_id already exists.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if priority is invalid.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_NFQUEUE_ERROR](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if NFQueue initialization fails.</li></ul> |

### OH_TrafficFilter_DestroyRedirector()

```c
int32_t OH_TrafficFilter_DestroyRedirector(OH_TrafficFilter_Redirector* redirector)
```

**Description**

Destroys a traffic redirection instance.Destroys the redirection instance and releases related resources, including rules.The handle becomes invalid after this call.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)* redirector | OH_TrafficFilter_Redirector handle |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if redirector is NULL.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_NOT_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if the specified redirector handle is not found.</li></ul> |

### OH_TrafficFilter_AddRedirectRule()

```c
int32_t OH_TrafficFilter_AddRedirectRule(OH_TrafficFilter_Redirector* redirector, const OH_TrafficFilter_RedirectRule* rule
)
```

**Description**

Adds a redirection ruleAdds a TCP traffic redirection rule to redirect matched traffic to specified proxy serverTo clear redirect rules, you need to call [OH_TrafficFilter_ClearRedirectRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearredirectrule).

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)* redirector | OH_TrafficFilter_Redirector handle |
| rule | Redirection rule. Cannot be NULL. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if redirector or rule is NULL.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_TOO_MANY_RULES](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if too many rules added.</li></ul> |

### OH_TrafficFilter_ClearRedirectRule()

```c
int32_t OH_TrafficFilter_ClearRedirectRule(OH_TrafficFilter_Redirector* redirector)
```

**Description**

Clear all redirection rule

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_Redirector](capi-trafficfilter-oh-trafficfilter-redirector.md)* redirector | OH_TrafficFilter_Redirector handle |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if redirector is NULL.</li></ul> |

### OH_TrafficFilter_QueryProcess()

```c
int32_t OH_TrafficFilter_QueryProcess(const OH_TrafficFilter_ConnectionInfo* connection_info, OH_TrafficFilter_ProcessInfo* process_info
)
```

**Description**

Queries corresponding process information based on connection informationQueries corresponding process information based on five-tuple information

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_TrafficFilter_ConnectionInfo](capi-trafficfilter-oh-trafficfilter-connectioninfo.md)* connection_info | Input connection information |
| process_info | Output process information |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if input parameters are invalid.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_NOT_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if process not found.</li></ul> |

### OH_TrafficFilter_AddPacketRule()

```c
int32_t OH_TrafficFilter_AddPacketRule(OH_TrafficFilter_PacketController* controller, const OH_TrafficFilter_FilterRule* rule
)
```

**Description**

Set packet filter ruleAdd a packet filter rule to controller chain.only packets matching the rule will be intercepted and sent to callback function.

>**Note**: 
>Logical relationship:
 *     - Conditions within a single OH_TrafficFilter_FilterRule structure are combined with logical AND.
 *     - Multiple rules added to the same OH_TrafficFilter_PacketController are combined with logical OR.
 *     To clear filter rules, you need to call [OH_TrafficFilter_ClearPacketRule](capi-net-trafficfilter-h.md#oh_trafficfilter_clearpacketrule).

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)* controller | [in] OH_TrafficFilter_PacketController handle |
| rule | [in] Filter rule. Cannot be NULL. |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if controller or rule is NULL.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_TOO_MANY_RULES](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if too many rules added.</li></ul> |

### OH_TrafficFilter_ClearPacketRule()

```c
int32_t OH_TrafficFilter_ClearPacketRule(OH_TrafficFilter_PacketController* controller)
```

**Description**

Clear packet filter ruleClear all packet filter rules in controller.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)* controller | [in] OH_TrafficFilter_PacketController handle |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if controller is NULL.</li></ul> |

### OH_TrafficFilter_CreatePacketController()

```c
int32_t OH_TrafficFilter_CreatePacketController(uint32_t groupId, uint32_t priority, const OH_TrafficFilter_Config* config, OH_TrafficFilter_PacketController** controller
)
```

**Description**

Creates a packet controller instance.Creates a packet controller for intercepting and filtering network packetsResource Management: This instance occupies system resources.You must call [OH_TrafficFilter_DestroyPacketController](capi-net-trafficfilter-h.md#oh_trafficfilter_destroypacketcontroller) to release resources.If this function fails, no valid controller is returned.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| uint32_t groupId | [in] Filter chain identifier.This is the logical grouping ID within the application.Multiple controllers within the same application can use different group_id.The same group_id from different applications will be automatically isolated. |
| uint32_t priority | [in] Priority (determines execution order between different group_id chain,smaller number executes first) |
| [const OH_TrafficFilter_Config](capi-trafficfilter-oh-trafficfilter-config.md)* config | [in] Configuration parameters (can be NULL to use default configuration) |
| controller | [out] Output parameter, <ul><li>the packet controller handle on success.</li></ul> |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_GROUP_ID_IN_USE](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) when group_id already exists.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if priority is invalid.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_NFQUEUE_ERROR](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if NFQueue initialization fails.</li></ul> |

### OH_TrafficFilter_DestroyPacketController()

```c
int32_t OH_TrafficFilter_DestroyPacketController(OH_TrafficFilter_PacketController* controller)
```

**Description**

Destroys a packet controller instance.Destroys the controller and releases related resources, including rules and callbacks.After calling this function, the handle is invalid. Do not use it again.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)* controller | [in] OH_TrafficFilter_PacketController handle |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if controller is NULL.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_NOT_FOUND](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if the specified controller handle is not found.</li></ul> |

### OH_TrafficFilter_RegisterPacketCallback()

```c
int32_t OH_TrafficFilter_RegisterPacketCallback(OH_TrafficFilter_PacketController* controller, OH_TrafficFilter_PacketCallback callback, void* userData
)
```

**Description**

Register a packet callback function.Register a callback function to handle intercepted packets.The callback will be triggered when packets match the filter rule.

>**Note**: 
><strong>Callback Model:</strong>
 *     <ul>
 *     <li><strong>Single Slot Model:</strong> A single <code>controller</code> instance supports only one active
 *         callback at a time.</li>
 *     <li><strong>Repeated Registration:</strong> If called again with a non-NULL callback, the new callback
 *         <strong>replaces</strong> the previously registered one. The previous callback is immediately unregistered.
 *         No error is returned for repeated registration.</li>
 *     <li><strong>Unregister/Destroy Semantics:</strong>
 *       <ul>
 *         <li>Calling [OH_TrafficFilter_UnregisterPacketCallback](capi-net-trafficfilter-h.md#oh_trafficfilter_unregisterpacketcallback) or destroying the <code>controller</code>
 *             immediately stops delivery of new packets to the callback.</li>
 *         <li><strong>No In-Flight Callbacks:</strong> Once unregistered or destroyed, the framework guarantees that
 *             no further callback invocations will occur for that registration, even if packet processing is in
 *             progress at the moment of unregistration.</li>
 *       </ul>
 *     </li>
 *     <li><strong>Callback Execution Constraints:</strong>
 *       <ul>
 *         <li><strong>User Data Lifetime:</strong> The <code>user_data</code> must remain valid from registration until
 *             after the callback is unregistered and all ongoing callback invocations have returned.</li>
 *         <li><strong>Thread Context:</strong> The callback may be invoked on any thread. Callers must ensure thread
 *             safety for shared resources.</li>
 *         <li><strong>Ordering and Concurrency:</strong> Callbacks are not guaranteed to be serialized or preserve
 *             packet order. Multiple callbacks may be invoked concurrently.</li>
 *         <li><strong>Reentrancy:</strong> The callback must not call any <code>OH_TrafficFilter_*</code> registration,
 *             unregistration, or controller destruction functions, as this may cause deadlock or undefined
 *             behavior.</li>
 *     </ul>
 *     </li>
 *     </ul>

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)* controller | [in] OH_TrafficFilter_PacketController handle. Must not be NULL. |
| [OH_TrafficFilter_PacketCallback](capi-net-trafficfilter-type-h.md#oh_trafficfilter_packetcallback) callback | [in] Callback function pointer. Cannot be NULL. |
| userData | [in] User data (will be passed back in callback). |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if controller or callback is NULL.</li></ul> |

### OH_TrafficFilter_UnregisterPacketCallback()

```c
int32_t OH_TrafficFilter_UnregisterPacketCallback(OH_TrafficFilter_PacketController* controller)
```

**Description**

Unregister a packet callback function.Unregister the current packet callback function.After calling this, no more packets will be delivered to the callback.

**Required permission**: ohos.permission.kernel.TRAFFIC_FILTER

**Since**: 26.1.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_TrafficFilter_PacketController](capi-trafficfilter-oh-trafficfilter-packetcontroller.md)* controller | [in] OH_TrafficFilter_PacketController handle |

**Returns**:

| Type | Description |
| -- | -- |
| int32_t | <ul><li>[OH_TRAFFICFILTER_OK](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) on success.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_PERMISSION_DENIED](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if permission is denied.</li><br>     <li>[OH_TRAFFICFILTER_ERROR_INVALID_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode) if controller is NULL.</li></ul> |


