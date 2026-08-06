# Watcher

Defines parameters for a **Watcher** object. This API is used to configure and manage event watchers to subscribe to and process specified events.
    **NOTE**  
    
    You are not advised to call [removeWatcher]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ in the callback. Once a watcher is  
    removed, the subscription callback of the watcher becomes invalid, and the callback may not be triggered when an  
    event occurs.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface Watcher--><!--Device-hiAppEvent-interface Watcher-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## onReceive

```TypeScript
onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void
```

Real-time subscription callback. Only this callback function is triggered if it is passed together with  
**onTrigger**. The input arguments are described as follows:

domain: domain name.

appEventGroups: event group.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void--><!--Device-Watcher-onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domain | string | Yes |  |
| appEventGroups | Array&lt;AppEventGroup&gt; | Yes |  |

## onTrigger

ArkTS-Dyn:
```TypeScript
onTrigger?: (curRow: number, curSize: number, holder: AppEventPackageHolder) => void
```

ArkTS-Sta:
```TypeScript
onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void
```

Subscription callback. This parameter takes effect only when it is passed together with **triggerCondition**. The input arguments are described as follows:

**curRow**: total number of subscription events when the callback is triggered.

**curSize**: total size of subscribed events when the callback is triggered, in bytes.

**holder**: subscription data holder, which can be used to process subscribed events.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void--><!--Device-Watcher-onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curRow | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes |  |
| curSize | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes |  |
| holder | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## appEventFilters

```TypeScript
appEventFilters?: AppEventFilter[]
```

Subscription filtering condition. This parameter is passed only when subscription events need to be filtered. If this parameter is not set, events are not filtered by default.

**Type:** AppEventFilter[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-appEventFilters?: AppEventFilter[]--><!--Device-Watcher-appEventFilters?: AppEventFilter[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## name

```TypeScript
name: string
```

Unique name of a watcher. The value contains a maximum of 32 characters, including digits (0 to 9), letters (a to z)(A to Z), and underscore (\_). It must start with a letter and end with a digit or letter. For example,  
**testName1** and **crash\_Watcher**.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-name: string--><!--Device-Watcher-name: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## triggerCondition

```TypeScript
triggerCondition?: TriggerCondition
```

Subscription callback triggering condition. This parameter takes effect only when it is passed together with  
**onTrigger**. If this parameter is not set, the **onTrigger** callback is not triggered by default.

**Type:** TriggerCondition

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-triggerCondition?: TriggerCondition--><!--Device-Watcher-triggerCondition?: TriggerCondition-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

