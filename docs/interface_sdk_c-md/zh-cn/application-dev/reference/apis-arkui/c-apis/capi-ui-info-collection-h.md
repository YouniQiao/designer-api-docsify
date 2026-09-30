# ui_info_collection.h

## 概述

Declares the APIs used by in-app intelligent agents and UI automation to observe UI interaction events and hit nodes.

**引用文件：** <arkui/ui_info_collection.h>

**库：** libace_ndk.z.so

**起始版本：** 26.2.0

**相关模块：** [ArkUI_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) | OH_ArkUI_NativeModule_UIAgentTreeRequest | 声明一个UI树采集请求结构体。 |
| [OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md) | OH_ArkUI_NativeModule_UIContentChangeEvent | 声明ArkUI内容变更事件结构体。 |
| [OH_ArkUI_NativeModule_ImageCollection](capi-arkui-nativemodule-oh-arkui-nativemodule-imagecollection.md) | OH_ArkUI_NativeModule_ImageCollection | ArkUI图像采集结果结构体声明 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIInfoCollection_InteractionEventType](#oh_arkui_nativemodule_uiinfocollection_interactioneventtype) | OH_ArkUI_NativeModule_UIInfoCollection_InteractionEventType | 枚举可观察的UI交互事件类型。<br> 这些值是位标志。它们用于构建传递给的eventMask [OH_ArkUI_NativeModule_UIInfoCollectionRegisterInteractionObserver](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectionregisterinteractionobserver)。 |
| [OH_ArkUI_NativeModule_UIAgentTreeType](#oh_arkui_nativemodule_uiagenttreetype) | OH_ArkUI_NativeModule_UIAgentTreeType | UI树采集类型的枚举。 |
| [OH_ArkUI_NativeModule_UIContentChangeEventCategory](#oh_arkui_nativemodule_uicontentchangeeventcategory) | OH_ArkUI_NativeModule_UIContentChangeEventCategory | UI内容变化事件类别枚举 |
| [OH_ArkUI_NativeModule_UIContentChangeIgnoreType](#oh_arkui_nativemodule_uicontentchangeignoretype) | OH_ArkUI_NativeModule_UIContentChangeIgnoreType | UI内容更改事件忽略枚举 |
| [OH_ArkUI_NativeModule_UIContentChangeEventType](#oh_arkui_nativemodule_uicontentchangeeventtype) | OH_ArkUI_NativeModule_UIContentChangeEventType | ArkUI内容变化事件枚举类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| -- | -- | -- |
| [typedef void (\*OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback)(const OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData)](#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback) | OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback | 接收感知到的交互事件的回调类型。<br> 该回调携带一个借用的[OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)对象，该对象持有 事件负载。对象仅在回调调用内有效；回调不能 保留或销毁它。有效载荷中的所有位置坐标都是相对于屏幕的 （显示），以物理像素（px）为单位。负载的顶层结构是：<br> { "schemaVersion": 1, "type": "<事件类型>",...}<br> 事件相关字段如下： -点击或点击：id，点，计数，手指。 -长按：id、point、realDuration（毫秒）、action（结束）。 -平移：id，点，方向，动作（"开始"\|"结束"\|"取消"）。 - Pinch: id, point（【x,y】的数组）,point,action("start"\|"end"\|"cancel");scale是 仅在“结束”时出现。 -旋转：id，点（【x,y】的数组），手指，动作（"开始"\|"结束"\|"取消"）；角度 （度）只出现在“端”上。 - Swipe: id、downPoint（【x,y】的数组）、upPoint（【x,y】的数组）、方向、速度、 实际速度。 -拖动：action ("start" \| "end"); "start"携带id、point、hostName、realDuration;"end" 携带点，dropResult（"成功"\|"失败"）,id（目标，仅在成功时出现）,hostName。 - Touch: action（“向下”\|“向上”）,findId,point；“向下”还携带id（命中节点ID）。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIInfoCollectionRegisterInteractionObserver(ArkUI_ContextHandle uiContext, uint32_t eventMask, uint32_t *registerID, OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback callback, void *userData)](#oh_arkui_nativemodule_uiinfocollectionregisterinteractionobserver) | - | 注册UI交互事件的观察者。<br> 观察者只接收eventMask中包含的事件类型的回调。 可以为同一个UI实例注册多个观察者。注册相同的回调和userData pair再次创建一个具有新注册ID的额外独立观察者。<br> 记得注销回调[OH_ArkUI_NativeModule_UIInfoCollectionUnregisterInteractionObserver](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectionunregisterinteractionobserver) 当它不再使用时。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIInfoCollectionUnregisterInteractionObserver(uint32_t registerID)](#oh_arkui_nativemodule_uiinfocollectionunregisterinteractionobserver) | - | 注销交互观察者。<br> 此调用完成后，关联的回调不再被调用。<br> 这个函数是线程安全的，可以从任何线程调用，不会阻塞调用者，并且是 而不是async-signal-safe。 |
| [typedef void (\*OH_ArkUI_NativeModule_UIAgentJsonCallback)(ArkUI_ContextHandle context, uint64_t requestId, ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData)](#oh_arkui_nativemodule_uiagentjsoncallback) | OH_ArkUI_NativeModule_UIAgentJsonCallback | 声明异步JSON树请求完成后调用的回调。<br> 对于每个接受的请求，在UI线程上只调用一次回调。回调接收控件树json的所有权 只有errorCode为ARKUI_ERROR_CODE_NO_ERROR时，才为非空的JSON对象。调用者使用完后必须调用OH_ArkUI_NativeModule_UIJsonWrapperDestroy释放对象避免内存泄漏。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestCreate(OH_ArkUI_NativeModule_UIAgentTreeType treeType, OH_ArkUI_NativeModule_UIAgentTreeRequest **request)](#oh_arkui_nativemodule_uiagenttreerequestcreate) | - | 创建UI树收集请求。 |
| [void OH_ArkUI_NativeModule_UIAgentTreeRequestDestroy(OH_ArkUI_NativeModule_UIAgentTreeRequest *request)](#oh_arkui_nativemodule_uiagenttreerequestdestroy) | - | 销毁UI树收集请求对象。<br> 传递NULL没有任何效果。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterPureLayoutNodes(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetfilterpurelayoutnodes) | - | 设置是否从返回的树中过滤纯布局节点。<br> 默认情况下，过滤是禁用的。启用时，已筛选节点的保留后代将附加到 最近的保留祖先，同时保持它们的相对顺序。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterOccludedNodes(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetfilteroccludednodes) | - | 设置是否从返回的树中过滤完全遮挡的节点。<br> 默认情况下，过滤是禁用的，只能为可见树启用 请求。禁用此选项不会禁用可见性、剪切、 屏幕外，或完全透明的节点过滤。<br> 遮挡器不透明度阈值可通过以下方式单独配置： [OH_ArkUI_NativeModule_UIAgentTreeRequestSetOcclusionOpacityThreshold](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagenttreerequestsetocclusionopacitythreshold)。 更改此选项不会更改该阈值。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetOcclusionOpacityThreshold(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, float threshold)](#oh_arkui_nativemodule_uiagenttreerequestsetocclusionopacitythreshold) | - | 设置节点作为遮挡物参与的最小最终不透明度。<br> 默认值为1.0。仅可见树请求支持该选项。仅删除目标节点 当合格封堵器区域的结合完全覆盖其有效可见区域时。<br> 如果过滤器选项未启用，则此阈值将不起作用 [OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterOccludedNodes](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagenttreerequestsetfilteroccludednodes)。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetInteractionInfo(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetinteractioninfo) | - | 设置是否收集附加交互信息。<br> 默认情况下，是关闭收集的。启用时，结果包括 支持的交互信息，如节点是否可点击。 可聚焦，或可编辑。此选项不注册事件观察者 或者改变任意节点的交互行为。<br> 禁用此选项不会删除默认选项中包含的字段 简化的结果。高级属性集合不会隐式地 启用此选项或收集为此选项保留的字段。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetAccessibilityInfo(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetaccessibilityinfo) | - | 设置是否收集其他辅助功能信息。<br> 默认情况下，是关闭收集的。启用时，结果包括 支持的辅助功能信息，例如辅助功能内容。 此选项不会启用辅助功能服务或更改节点行为。<br> 禁用此选项不会删除默认选项中包含的字段 简化的结果。高级属性集合不会隐式地 启用此选项或收集为此选项保留的字段。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectVisualProperties(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetcollectvisualproperties) | - | 设置是否收集高级视觉属性。<br> 默认情况下，是关闭收集的。启用后，结果会额外 包括描述可直接感知外观的支持属性， 例如视觉样式和显示的状态。<br> 已包含在默认简化结果中的属性不 重复。为交互或可访问性集合保留的字段 都被排除在此属性组中，无论这些选项是什么。 从不包含内部诊断属性。<br> 此选项独立于高级函数属性集合 并且不会改变树中保留的节点。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectFunctionalProperties(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)](#oh_arkui_nativemodule_uiagenttreerequestsetcollectfunctionalproperties) | - | 设置是否收集高级功能属性。<br> 默认情况下，是关闭收集的。启用后，结果会额外 包括描述开发人员配置的组件的支持属性 行为和功能能力。<br> 已包含在默认简化结果中的属性不 重复。为交互或可访问性集合保留的字段 都被排除在此属性组中，无论这些选项是什么。 从不包含内部诊断属性。<br> 此选项独立于高级视觉特性集合 并且不会改变树中保留的节点。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetTreeJson(ArkUI_ContextHandle context, const OH_ArkUI_NativeModule_UIAgentTreeRequest *request, OH_ArkUI_NativeModule_UIJsonFormat format, OH_ArkUI_NativeModule_UIJsonWrapper **json)](#oh_arkui_nativemodule_uiagentgettreejson) | - | 同步收集UI树并以JSON形式返回。<br> 此函数必须在UI线程上调用。最多包含5000个节点，且不能超过5MiB。 大小限制是使用规范的紧凑型JSON来测量的。如果输出本身超过5 MiB，请求也 失败，没有返回部分JSON。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetTreeJsonAsync(ArkUI_ContextHandle context, const OH_ArkUI_NativeModule_UIAgentTreeRequest *request, OH_ArkUI_NativeModule_UIJsonFormat format, OH_ArkUI_NativeModule_UIAgentJsonCallback callback, void *userData, uint64_t *requestId)](#oh_arkui_nativemodule_uiagentgettreejsonasync) | - | 发起异步UI树收集请求。通过异步回调接收集合。 此函数必须在UI线程上调用。函数在返回之前复制请求和格式，因此 调用方可以在调用后立即销毁或重用请求。每个接受的请求仅完成一次 在UI线程上。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetPageText(ArkUI_ContextHandle uiContext, OH_ArkUI_NativeModule_UIJsonWrapper** pageText)](#oh_arkui_nativemodule_uiagentgetpagetext) | - | 同步采集当前ArkUI页面的文本，并将文本以JSON格式输出。每个JSON项 包含一个整数“id”。 识别控件、相对于目标窗口的矩形“rect”和文本内容 字符串“content”。使用完后，使用OH_ArkUI_NativeModule_UIJsonWrapperDestroy来释放结果 记忆。 函数必须在UI线程上调用。输出格式如下： |
| [typedef void (\*OH_ArkUI_NativeModule_UIContentChangeEventCallback)(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, void* userData)](#oh_arkui_nativemodule_uicontentchangeeventcallback) | OH_ArkUI_NativeModule_UIContentChangeEventCallback | 声明注册的ArkUI内容变化事件的回调。<br> 回调在与注册的上下文关联的用户界面线程上运行。事件快照为 不可变且仅在此回调返回前有效。ArkUI借用但不访问或释放userData。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_RegisterUIContentChangeEvent(ArkUI_ContextHandle uiContext, bool withStart, uint32_t eventMask, uint32_t ignoreMask, void* userData, OH_ArkUI_NativeModule_UIContentChangeEventCallback callback, uint64_t* subscriptionId)](#oh_arkui_nativemodule_registeruicontentchangeevent) | - | 注册指定UI实例内容变化事件监听<br> 每次成功调用都会创建一个独立的订阅。返回的ID非零且在 上下文。在上下文的用户界面线程上同步调用回调。ArkUI借用uiContext 和userData，并且不释放这两个值。如果操作失败，则不修改subscribeId。 此函数必须在UI线程上调用；从非UI线程调用它将中止进程。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UnRegisterUIContentChangeEvent(ArkUI_ContextHandle uiContext, uint64_t subscriptionId)](#oh_arkui_nativemodule_unregisteruicontentchangeevent) | - | 从用户界面上下文中取消注册活动的ArkUI状态更改事件订阅。<br> 此函数成功返回后，后续事件将不再调用已移除的订阅。然后，调用者可以 释放其userData。取消订阅回调不会更改当前正在调度的回调批次。 此函数必须在UI线程上调用；从非UI线程调用它将中止进程。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetType(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, OH_ArkUI_NativeModule_UIContentChangeEventType* type)](#oh_arkui_nativemodule_uicontentchangeeventgettype) | - | 从ArkUI状态变化事件快照中获取事件类型。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetTimestamp(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, uint64_t* nanoTimestamp)](#oh_arkui_nativemodule_uicontentchangeeventgettimestamp) | - | 获取ArkUI状态变化事件快照的单调时间戳。<br> 时间戳在事件完成点捕获，以纳秒表示，不是挂钟时间。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetContext(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, ArkUI_ContextHandle* uiContext)](#oh_arkui_nativemodule_uicontentchangeeventgetcontext) | - | 获取ArkUI状态变化事件快照关联的用户界面上下文。<br> 返回的句柄是借用的，在回调返回后，调用者不得释放或使用它。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetContentChangeEventJson(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, const OH_ArkUI_NativeModule_UIJsonWrapper** json)](#oh_arkui_nativemodule_uicontentchangeeventgetcontentchangeeventjson) | - | 从ArkUI状态变更事件快照中获取内容变更事件详情，作为JSON包装器。<br> JSON输出包括内容变化类型、触发节点、目标节点、覆盖类型和可选的 子树转储取决于事件类别：<br> 页面事件标识目标页面。滚动事件标识滚动节点。重叠事件标识 覆盖节点，并提供覆盖类型（例如“对话框”）。触发节点是启动 内容更改；它适用于覆盖事件和一般开始/结束场景，对于页面和 当没有触发器节点可以暴露时，滚动事件。操作成功并写入一个空的JSON包装器，当 不能暴露任何目标节点。JSON包装器中引用的句柄是借用的，不能被释放 或在回调返回后使用。 |
| [typedef void (\*OH_ArkUI_NativeModule_ImageCollectionCallback)(ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_ImageCollection* collection, void* userData)](#oh_arkui_nativemodule_imagecollectioncallback) | OH_ArkUI_NativeModule_ImageCollectionCallback | 定义ArkUI节点图片采集结果返回的回调。<br> 对于每个接受的请求，框架在UI线程上调用此回调仅一次。 当<b>errorCode</b>为ARKUI_ERROR_CODE_NO_ERROR时，框架将转移non-<b>null</b>的所有权 向主叫方发送<b>collection</b>。当<b>errorCode</b>为ARKUI_ERROR_CODE_INTERNAL_ERROR或 ARKUI_ERROR_CODE_UI_CONTEXT_INVALID,<b>collection</b>为<b>null</b>。<br> 框架在不取消引用的情况下返回不变的<b>userData</b>， 复制，或者释放它所指向的对象。打电话的人一定要留着 对象在回调结束使用之前有效。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_GetImagesByNodeIdAsync(ArkUI_ContextHandle context, const int32_t* nodeIds, uint32_t count, OH_ArkUI_NativeModule_ImageCollectionCallback callback, void* userData)](#oh_arkui_nativemodule_getimagesbynodeidasync) | - | 异步采集指定ArkUI节点ID的镜像。<br> 该框架接受从<b>0</b>到<b>20</b>的唯一节点ID 在此函数返回之前，请求并复制<b>nodeIds</b>数组。 框架接受<b>count</b>等于<b>0</b>的请求， 通过回调返回一个non-<b>null</b>空集合。<br> 每个接受的节点ID在集合中都有一个结果，包括一个结果 对于找不到或无法抓取图像的节点ID。 <b>Image</b>节点在可用时返回其完整的源<b>PixelMap</b> 否则返回到捕获节点内的呈现内容 边界。non-<b>Image</b>节点使用相同的节点边界捕获行为。 节点不需要是可见的。<br> 如果找不到请求的节点ID对应的ArkUI节点，则 对应的收集项报表 <b>ARKUI_ERROR_CODE_PARAM_INVALID</b>；调用方应检查节点ID。 A捕获超时报告 <b>ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_TIMEOUT</b>；调用方可以重试 请求。另一个内部捕获失败报告 该项目的<b>ARKUI_ERROR_CODE_INTERNAL_ERROR</b>；调用方可以重试 处理失败后的请求。项目失败不会改变 请求的整体成功结果。<br> 调用者可以从任何线程调用此函数。对于每一个接受 请求时，框架将在UI线程上调用<b>callback</b>一次 与<b>context</b>关联。并发请求是独立的，而 框架不保证它们的回调顺序。 |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_ImageCollectionTakeItemByNodeId(OH_ArkUI_NativeModule_ImageCollection* collection, int32_t nodeId, OH_PixelmapNative** outPixelmap, ArkUI_ErrorCode* outItemError)](#oh_arkui_nativemodule_imagecollectiontakeitembynodeid) | - | 消费指定节点ID的结果。<br> 对于成功的图像结果，此函数将 向主叫方发送<b>PixelMap</b>。调用者必须通过调用来释放它 <b>OH_PixelmapNative_Destroy</b>。此函数也会消耗失败的映像 在这种情况下，它将<b>*outPixelmap</b>设置为<b>null</b>并写入 项错误到<b>*outItemError</b>。集合中的每个节点ID可以为 只消费一次。<br> 销毁集合仅释放<b>PixelMap</b>实例 调用方未使用且未使转移的<b>PixelMap</b>无效。<br> 调用者不能与另一个集合同时调用此函数 同一个集合的api。 |
| [void OH_ArkUI_NativeModule_ImageCollectionDestroy(OH_ArkUI_NativeModule_ImageCollection* collection)](#oh_arkui_nativemodule_imagecollectiondestroy) | - | 销毁镜像集合，释放未消费的<b>PixelMap</b>实例。<br> 调用方必须销毁回调的每个non-<b>null</b>集合 返回，包括一个空集合或一个在调用者有 消耗了它所有的物品。此功能不会释放或失效 调用方通过获取的<b>PixelMap</b>实例 <b>OH_ArkUI_NativeModule_ImageCollection_TakeItemByNodeId</b>.<br> 调用者不能与另一个集合同时调用此函数 同一个集合的api。 |

### 变量

| 名称 | 描述 |
| -- | -- |
| void (*OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback)( const OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData) | 接收感知到的交互事件的回调类型。<br> 该回调携带一个借用的[OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)对象，该对象持有 事件负载。对象仅在回调调用内有效；回调不能 保留或销毁它。有效载荷中的所有位置坐标都是相对于屏幕的 （显示），以物理像素（px）为单位。负载的顶层结构是：<br> { "schemaVersion": 1, "type": "<事件类型>",...}<br> 事件相关字段如下： -点击或点击：id，点，计数，手指。 -长按：id、point、realDuration（毫秒）、action（结束）。 -平移：id，点，方向，动作（"开始"\|"结束"\|"取消"）。 - Pinch: id, point（【x,y】的数组）,point,action("start"\|"end"\|"cancel");scale是 仅在“结束”时出现。 -旋转：id，点（【x,y】的数组），手指，动作（"开始"\|"结束"\|"取消"）；角度 （度）只出现在“端”上。 - Swipe: id、downPoint（【x,y】的数组）、upPoint（【x,y】的数组）、方向、速度、 实际速度。 -拖动：action ("start" \| "end"); "start"携带id、point、hostName、realDuration;"end" 携带点，dropResult（"成功"\|"失败"）,id（目标，仅在成功时出现）,hostName。 - Touch: action（“向下”\|“向上”）,findId,point；“向下”还携带id（命中节点ID）。<br>**起始版本：** 26.2.0<br>**系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| void (*OH_ArkUI_NativeModule_UIAgentJsonCallback)(ArkUI_ContextHandle context, uint64_t requestId, ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData) | 声明异步JSON树请求完成后调用的回调。<br> 对于每个接受的请求，在UI线程上只调用一次回调。回调接收控件树json的所有权 只有errorCode为ARKUI_ERROR_CODE_NO_ERROR时，才为非空的JSON对象。调用者使用完后必须调用OH_ArkUI_NativeModule_UIJsonWrapperDestroy释放对象避免内存泄漏。<br>**起始版本：** 26.2.0<br>**系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| void (*OH_ArkUI_NativeModule_UIContentChangeEventCallback)( const OH_ArkUI_NativeModule_UIContentChangeEvent* event, void* userData) | 声明注册的ArkUI内容变化事件的回调。<br> 回调在与注册的上下文关联的用户界面线程上运行。事件快照为 不可变且仅在此回调返回前有效。ArkUI借用但不访问或释放userData。<br>**起始版本：** 26.2.0<br>**系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| void (*OH_ArkUI_NativeModule_ImageCollectionCallback)(ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_ImageCollection* collection, void* userData) | 定义ArkUI节点图片采集结果返回的回调。<br> 对于每个接受的请求，框架在UI线程上调用此回调仅一次。 当<b>errorCode</b>为ARKUI_ERROR_CODE_NO_ERROR时，框架将转移non-<b>null</b>的所有权 向主叫方发送<b>collection</b>。当<b>errorCode</b>为ARKUI_ERROR_CODE_INTERNAL_ERROR或 ARKUI_ERROR_CODE_UI_CONTEXT_INVALID,<b>collection</b>为<b>null</b>。<br> 框架在不取消引用的情况下返回不变的<b>userData</b>， 复制，或者释放它所指向的对象。打电话的人一定要留着 对象在回调结束使用之前有效。<br>**起始版本：** 26.2.0<br>**系统能力：** SystemCapability.ArkUI.ArkUI.Full |

## 枚举类型说明

### OH_ArkUI_NativeModule_UIInfoCollection_InteractionEventType

```c
enum OH_ArkUI_NativeModule_UIInfoCollection_InteractionEventType
```

**描述：**

枚举可观察的UI交互事件类型。<br> 这些值是位标志。它们用于构建传递给的eventMask [OH_ArkUI_NativeModule_UIInfoCollectionRegisterInteractionObserver](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectionregisterinteractionobserver)。

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_NONE = 0 | 无事件。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_TAP = 1 << 0 | 点击手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_CLICK = 1 << 1 | 单击。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_LONG_PRESS = 1 << 2 | 长按手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_PAN = 1 << 3 | 平移手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_PINCH = 1 << 4 | 捏合手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_ROTATION = 1 << 5 | 旋转手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_SWIPE = 1 << 6 | 滑动手势。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_DRAG = 1 << 7 | 统一拖放。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_TOUCH = 1 << 8 | 原始触地或向上触地。<br>**起始版本：** 26.2.0 |

### OH_ArkUI_NativeModule_UIAgentTreeType

```c
enum OH_ArkUI_NativeModule_UIAgentTreeType
```

**描述：**

UI树采集类型的枚举。

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVE_MODULE_UI_AGENT_TREE_FULL = 0 | 收集全量UI树，包括不可见节点、透明节点、离屏节点、阻塞节点。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVE_MODULE_UI_AGENT_TREE_VISIBLE = 1 | 采集可视、裁剪、离屏、遮挡过滤后的可见树。<br>**起始版本：** 26.2.0 |

### OH_ArkUI_NativeModule_UIContentChangeEventCategory

```c
enum OH_ArkUI_NativeModule_UIContentChangeEventCategory
```

**描述：**

UI内容变化事件类别枚举

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVEMODULE_EVENT_CATEGORY_PAGE = 1U << 0 | 页面切换事件，包括导航、路由、滑动、Tabs切换事件。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_CATEGORY_SCROLL = 1U << 1 | 滚动事件。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_CATEGORY_OVERLAY = 1U << 2 | 叠加事件。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_CATEGORY_ALL = ~0U | 所有支持的事件类别。<br>**起始版本：** 26.2.0 |

### OH_ArkUI_NativeModule_UIContentChangeIgnoreType

```c
enum OH_ArkUI_NativeModule_UIContentChangeIgnoreType
```

**描述：**

UI内容更改事件忽略枚举

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVEMODULE_CONTENTCHANGE_IGNORE_SCROLLBY = 1U << 0 | 按事件滚动。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_CONTENTCHANGE_IGNORE_SCROLLTO = 1U << 1 | 滚动到事件。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_CONTENTCHANGE_IGNORE_TOAST = 1U << 2 | Toast事件。<br>**起始版本：** 26.2.0 |

### OH_ArkUI_NativeModule_UIContentChangeEventType

```c
enum OH_ArkUI_NativeModule_UIContentChangeEventType
```

**描述：**

ArkUI内容变化事件枚举类型。

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVEMODULE_EVENT_PAGE_CHANGE_START = 0 | 页面更改的开始。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_PAGE_CHANGE_END = 1 | 换页结束<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_SCROLL_START = 2 | 滚动事件开始<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_SCROLL_END = 3 | 一个滚动交互和任何后续的惯性滚动都已经结束。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_OVERLAY_SHOW = 4 | 覆盖层已完成显示。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_OVERLAY_HIDE = 5 | 覆盖层已完成消失。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_SWIPER_START = 6 | 一个滑动器交互已经开始。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_SWIPER_END = 7 | 滑动器交互已经完成，包括其过渡动画（如果存在）。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_SWIPER_CANCEL = 8 | Swiper切换事件返回起始索引。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_TABS_START = 9 | 选项卡开始事件<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_TABS_END = 10 | 选项卡结束事件<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVEMODULE_EVENT_TABS_CANCEL = 11 | Tabs开关启动后，取消事件。指数启动后反弹<br>**起始版本：** 26.2.0 |


## 函数说明

### OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback()

```c
typedef void (*OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback)(const OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData)
```

**描述：**

接收感知到的交互事件的回调类型。<br> 该回调携带一个借用的[OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)对象，该对象持有 事件负载。对象仅在回调调用内有效；回调不能 保留或销毁它。有效载荷中的所有位置坐标都是相对于屏幕的 （显示），以物理像素（px）为单位。负载的顶层结构是：<br> { "schemaVersion": 1, "type": "<事件类型>",...}<br> 事件相关字段如下： -点击或点击：id，点，计数，手指。 -长按：id、point、realDuration（毫秒）、action（结束）。 -平移：id，点，方向，动作（"开始"\|"结束"\|"取消"）。 - Pinch: id, point（【x,y】的数组）,point,action("start"\|"end"\|"cancel");scale是 仅在“结束”时出现。 -旋转：id，点（【x,y】的数组），手指，动作（"开始"\|"结束"\|"取消"）；角度 （度）只出现在“端”上。 - Swipe: id、downPoint（【x,y】的数组）、upPoint（【x,y】的数组）、方向、速度、 实际速度。 -拖动：action ("start" \| "end"); "start"携带id、point、hostName、realDuration;"end" 携带点，dropResult（"成功"\|"失败"）,id（目标，仅在成功时出现）,hostName。 - Touch: action（“向下”\|“向上”）,findId,point；“向下”还携带id（命中节点ID）。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] 借用的JSON对象。仅在回调调用时有效。 |
| void *userData | [in] 注册时传递的自定义用户数据。可以为空。框架 不拥有、取消引用或释放它。 |

### OH_ArkUI_NativeModule_UIInfoCollectionRegisterInteractionObserver()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIInfoCollectionRegisterInteractionObserver(ArkUI_ContextHandle uiContext, uint32_t eventMask, uint32_t *registerID, OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback callback, void *userData)
```

**描述：**

注册UI交互事件的观察者。<br> 观察者只接收eventMask中包含的事件类型的回调。 可以为同一个UI实例注册多个观察者。注册相同的回调和userData pair再次创建一个具有新注册ID的额外独立观察者。<br> 记得注销回调[OH_ArkUI_NativeModule_UIInfoCollectionUnregisterInteractionObserver](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectionunregisterinteractionobserver) 当它不再使用时。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) uiContext | [in] 指向UI实例的指针。不能为空。 |
| uint32_t eventMask | [in] [OH_ArkUI_NativeModule_UIInfoCollection_InteractionEventType](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollection_interactioneventtype)的位掩码 要观察的值，与按位OR运算符结合使用。支持的位数为 OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_TAP至 OH_ARKUI_NATIVEMODULE_UIINFOCOLLECTION_INTERACTION_EVENT_TOUCH。此范围之外的位 忽略。如果没有设置支持的位，则返回ARKUI_ERROR_CODE_PARAM_INVALID。 |
| uint32_t *registerID | [out] 成功时接收观察者注册ID。不能为空。 不需要初始化，失败时设置为0。 |
| [OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback) callback | [in] 匹配事件发生时调用的回调。不能为空。 |
| void *userData | [in] 传递给回调的自定义用户数据。可以为空。框架做了 而不是取得它的所有权；调用者必须保持它有效，直到观察者未注册为止。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果需要的指针为空或事件掩码不包含任何支持的位。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果UI上下文无效。</li> </ul> |

### OH_ArkUI_NativeModule_UIInfoCollectionUnregisterInteractionObserver()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIInfoCollectionUnregisterInteractionObserver(uint32_t registerID)
```

**描述：**

注销交互观察者。<br> 此调用完成后，关联的回调不再被调用。<br> 这个函数是线程安全的，可以从任何线程调用，不会阻塞调用者，并且是 而不是async-signal-safe。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| uint32_t registerID | [in] 注册成功返回的注册ID。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果注册ID无效。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentJsonCallback()

```c
typedef void (*OH_ArkUI_NativeModule_UIAgentJsonCallback)(ArkUI_ContextHandle context, uint64_t requestId, ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_UIJsonWrapper *json, void *userData)
```

**描述：**

声明异步JSON树请求完成后调用的回调。<br> 对于每个接受的请求，在UI线程上只调用一次回调。回调接收控件树json的所有权 只有errorCode为ARKUI_ERROR_CODE_NO_ERROR时，才为非空的JSON对象。调用者使用完后必须调用OH_ArkUI_NativeModule_UIJsonWrapperDestroy释放对象避免内存泄漏。

**起始版本：** 26.2.0

**资源释放：** ui_json_wrapper/OH_ArkUI_NativeModule_UIJsonWrapperDestroy {json}.

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) context | [in] 用于指定本次采集结果对应的UI上下文。 |
| uint64_t requestId | [in] 分配给被接受的请求的标识符。 |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) errorCode | [in] 采集请求的结果。 |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] 不可变的JSON结果，如果请求失败，则为NULL。否则为Json结构的控件树。这个对象在使用完毕后需要开发者显示释放。 |
| void *userData | [in] 传递给OH_ArkUI_NativeModule_UIAgent_GetTreeJsonAsync的调用方提供的数据。 |

### OH_ArkUI_NativeModule_UIAgentTreeRequestCreate()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestCreate(OH_ArkUI_NativeModule_UIAgentTreeType treeType, OH_ArkUI_NativeModule_UIAgentTreeRequest **request)
```

**描述：**

创建UI树收集请求。

**起始版本：** 26.2.0

**资源释放：** OH_ArkUI_NativeModule_UIAgentTreeRequestDestroy {request}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeType](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagenttreetype) treeType | [in] 树型。该值必须是OH_ArkUI_NativeModule_UIAgentTreeType的成员。 |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) **request | [out] 输出请求对象。调用者必须通过调用来释放它 OH_ArkUI_NativeModule_UIAgentTreeRequest_Destroy. |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果请求创建成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果输入或输出参数无效。</li> <li>ARKUI_ERROR_CODE_RESOURCE_EXHAUSTED 如果分配失败。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestDestroy()

```c
void OH_ArkUI_NativeModule_UIAgentTreeRequestDestroy(OH_ArkUI_NativeModule_UIAgentTreeRequest *request)
```

**描述：**

销毁UI树收集请求对象。<br> 传递NULL没有任何效果。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 销毁的请求。 |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterPureLayoutNodes()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterPureLayoutNodes(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否从返回的树中过滤纯布局节点。<br> 默认情况下，过滤是禁用的。启用时，已筛选节点的保留后代将附加到 最近的保留祖先，同时保持它们的相对顺序。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。 |
| bool enabled | [in] 是否过滤纯布局节点。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li> ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。</li> <li> ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为空。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterOccludedNodes()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterOccludedNodes(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否从返回的树中过滤完全遮挡的节点。<br> 默认情况下，过滤是禁用的，只能为可见树启用 请求。禁用此选项不会禁用可见性、剪切、 屏幕外，或完全透明的节点过滤。<br> 遮挡器不透明度阈值可通过以下方式单独配置： [OH_ArkUI_NativeModule_UIAgentTreeRequestSetOcclusionOpacityThreshold](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagenttreerequestsetocclusionopacitythreshold)。 更改此选项不会更改该阈值。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。它不能为NULL。 |
| bool enabled | [in] true表示启用遮挡过滤；false表示禁用遮挡过滤。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。为全树请求设置false也会成功</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为NULL。</li> <li>ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED （如果启用）对于全树请求为true。请求保持不变。使用可见树请求来启用此选项。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetOcclusionOpacityThreshold()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetOcclusionOpacityThreshold(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, float threshold)
```

**描述：**

设置节点作为遮挡物参与的最小最终不透明度。<br> 默认值为1.0。仅可见树请求支持该选项。仅删除目标节点 当合格封堵器区域的结合完全覆盖其有效可见区域时。<br> 如果过滤器选项未启用，则此阈值将不起作用 [OH_ArkUI_NativeModule_UIAgentTreeRequestSetFilterOccludedNodes](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagenttreerequestsetfilteroccludednodes)。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] UI树收集请求。 |
| float threshold | [in] 范围【0.0,1.0】内的不透明度阈值。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果设置成功</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为空。</li> <li>ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE 如果阈值超出有效范围</li> <li>ARKUI_ERROR_CODE_ATTRIBUTE_OR_EVENT_NOT_SUPPORTED 如果请求的是完整的树。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetInteractionInfo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetInteractionInfo(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否收集附加交互信息。<br> 默认情况下，是关闭收集的。启用时，结果包括 支持的交互信息，如节点是否可点击。 可聚焦，或可编辑。此选项不注册事件观察者 或者改变任意节点的交互行为。<br> 禁用此选项不会删除默认选项中包含的字段 简化的结果。高级属性集合不会隐式地 启用此选项或收集为此选项保留的字段。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。它不能为NULL。 |
| bool enabled | [in] 表示收集交互信息为true，否则为false。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为NULL。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetAccessibilityInfo()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetAccessibilityInfo(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否收集其他辅助功能信息。<br> 默认情况下，是关闭收集的。启用时，结果包括 支持的辅助功能信息，例如辅助功能内容。 此选项不会启用辅助功能服务或更改节点行为。<br> 禁用此选项不会删除默认选项中包含的字段 简化的结果。高级属性集合不会隐式地 启用此选项或收集为此选项保留的字段。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。它不能为NULL。 |
| bool enabled | [in] 为true则收集可访问性信息；否则为false。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为NULL。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectVisualProperties()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectVisualProperties(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否收集高级视觉属性。<br> 默认情况下，是关闭收集的。启用后，结果会额外 包括描述可直接感知外观的支持属性， 例如视觉样式和显示的状态。<br> 已包含在默认简化结果中的属性不 重复。为交互或可访问性集合保留的字段 都被排除在此属性组中，无论这些选项是什么。 从不包含内部诊断属性。<br> 此选项独立于高级函数属性集合 并且不会改变树中保留的节点。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。它不能为NULL。 |
| bool enabled | [in] true表示收集高级视觉属性，否则为false。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为NULL。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectFunctionalProperties()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentTreeRequestSetCollectFunctionalProperties(OH_ArkUI_NativeModule_UIAgentTreeRequest *request, bool enabled)
```

**描述：**

设置是否收集高级功能属性。<br> 默认情况下，是关闭收集的。启用后，结果会额外 包括描述开发人员配置的组件的支持属性 行为和功能能力。<br> 已包含在默认简化结果中的属性不 重复。为交互或可访问性集合保留的字段 都被排除在此属性组中，无论这些选项是什么。 从不包含内部诊断属性。<br> 此选项独立于高级视觉特性集合 并且不会改变树中保留的节点。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 配置的请求。它不能为NULL。 |
| bool enabled | [in] true表示收集高级函数属性，否则为false。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果选项设置成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果请求为NULL。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentGetTreeJson()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetTreeJson(ArkUI_ContextHandle context, const OH_ArkUI_NativeModule_UIAgentTreeRequest *request, OH_ArkUI_NativeModule_UIJsonFormat format, OH_ArkUI_NativeModule_UIJsonWrapper **json)
```

**描述：**

同步收集UI树并以JSON形式返回。<br> 此函数必须在UI线程上调用。最多包含5000个节点，且不能超过5MiB。 大小限制是使用规范的紧凑型JSON来测量的。如果输出本身超过5 MiB，请求也 失败，没有返回部分JSON。

**起始版本：** 26.2.0

**资源释放：** ui_json_wrapper/OH_ArkUI_NativeModule_UIJsonWrapperDestroy {json}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) context | [in] 收集其树的UI上下文。 |
| [const OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 催缴请求。 |
| [OH_ArkUI_NativeModule_UIJsonFormat](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonformat) format | [in] JSON输出格式。 |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) **json | [out] 输出不可变的JSON对象。调用者必须通过调用来释放它 OH_ArkUI_NativeModule_UIJsonWrapperDestroy. |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果收集成功</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果参数或格式无效。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果上下文无效。</li> <li>ARKUI_ERROR_CODE_NODE_ON_INVALID_THREAD 如果在UI线程外部调用。</li> <li>ARKUI_ERROR_CODE_RESULT_TOO_LARGE 如果超过结果限制。</li> <li>ARKUI_ERROR_CODE_RESOURCE_EXHAUSTED 如果分配失败。</li> <li>ARKUI_ERROR_CODE_INTERNAL_ERROR 如果发生其他内部错误。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentGetTreeJsonAsync()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetTreeJsonAsync(ArkUI_ContextHandle context, const OH_ArkUI_NativeModule_UIAgentTreeRequest *request, OH_ArkUI_NativeModule_UIJsonFormat format, OH_ArkUI_NativeModule_UIAgentJsonCallback callback, void *userData, uint64_t *requestId)
```

**描述：**

发起异步UI树收集请求。通过异步回调接收集合。 此函数必须在UI线程上调用。函数在返回之前复制请求和格式，因此 调用方可以在调用后立即销毁或重用请求。每个接受的请求仅完成一次 在UI线程上。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) context | [in] 收集其树的UI上下文。 |
| [const OH_ArkUI_NativeModule_UIAgentTreeRequest](capi-arkui-nativemodule-oh-arkui-nativemodule-uiagenttreerequest.md) *request | [in] 催缴请求。 |
| [OH_ArkUI_NativeModule_UIJsonFormat](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonformat) format | [in] JSON输出格式。 |
| [OH_ArkUI_NativeModule_UIAgentJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiagentjsoncallback) callback | [in] 完成回调。成功后，回调将接收JSON对象的所有权，并且必须 通过调用OH_ArkUI_NativeModule_UIJsonWrapperDestroy来释放它。 |
| void *userData | [in] 传递给回调的调用方提供的数据。 |
| uint64_t *requestId | [out] 接受的请求的输出标识符。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果请求被接受。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果参数或格式无效。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果上下文无效。</li> <li>ARKUI_ERROR_CODE_NODE_ON_INVALID_THREAD 如果在UI线程外部调用。</li> <li>ARKUI_ERROR_CODE_COMMAND_UNFINISHED 如果最后一个请求未完成。</li> </ul> |

### OH_ArkUI_NativeModule_UIAgentGetPageText()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIAgentGetPageText(ArkUI_ContextHandle uiContext, OH_ArkUI_NativeModule_UIJsonWrapper** pageText)
```

**描述：**

同步采集当前ArkUI页面的文本，并将文本以JSON格式输出。每个JSON项 包含一个整数“id”。 识别控件、相对于目标窗口的矩形“rect”和文本内容 字符串“content”。使用完后，使用OH_ArkUI_NativeModule_UIJsonWrapperDestroy来释放结果 记忆。 函数必须在UI线程上调用。输出格式如下：

**起始版本：** 26.2.0

**资源释放：** ui_json_wrapper/OH_ArkUI_NativeModule_UIJsonWrapperDestroy {pageText}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) uiContext | [in] 文本收集的目标UI实例的上下文 |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)** pageText | [out] 输出槽，由调用者初始化为NULL。 失败时将有效槽设置为NULL；空页仍然返回 包装纸。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果pageText为NULL。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果uiContext为NULL或不再有效。</li> <li>ARKUI_ERROR_CODE_CAPI_INIT_ERROR 如果本机实现不可用。</li> <li>ARKUI_ERROR_CODE_INTERNAL_ERROR 如果当前页面不存在、JSON负载大小无法用uint32_t表示，或收集/序列化失败。</li> </ul> |

### OH_ArkUI_NativeModule_UIContentChangeEventCallback()

```c
typedef void (*OH_ArkUI_NativeModule_UIContentChangeEventCallback)(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, void* userData)
```

**描述：**

声明注册的ArkUI内容变化事件的回调。<br> 回调在与注册的上下文关联的用户界面线程上运行。事件快照为 不可变且仅在此回调返回前有效。ArkUI借用但不访问或释放userData。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md)* event | [in] 指向不可变事件对象的指针。 |
| void* userData | [in] 注册回调时提供的指针。指针可以为NULL。 |

### OH_ArkUI_NativeModule_RegisterUIContentChangeEvent()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_RegisterUIContentChangeEvent(ArkUI_ContextHandle uiContext, bool withStart, uint32_t eventMask, uint32_t ignoreMask, void* userData, OH_ArkUI_NativeModule_UIContentChangeEventCallback callback, uint64_t* subscriptionId)
```

**描述：**

注册指定UI实例内容变化事件监听<br> 每次成功调用都会创建一个独立的订阅。返回的ID非零且在 上下文。在上下文的用户界面线程上同步调用回调。ArkUI借用uiContext 和userData，并且不释放这两个值。如果操作失败，则不修改subscribeId。 此函数必须在UI线程上调用；从非UI线程调用它将中止进程。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) uiContext | [in] 要观察的用户界面上下文。句柄必须对订阅保持有效。 |
| bool withStart | [in] 是否上报开始事件。设置为true时，启动事件(如页面更改开始和 如果设置为false，则只报告结束事件。 |
| uint32_t eventMask | [in] [OH_ArkUI_NativeModule_UIContentChangeEventCategory](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeeventcategory)值的按位或组合。 不能为零。[OH_ARKUI_NATIVEMODULE_EVENT_CATEGORY_SCROLL](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeeventcategory)类别可以执行以下操作： 不区分滚动子类型。设置对应的 [OH_ARKUI_NATIVEMODULE_CONTENTCHANGE_IGNORE_SCROLLTO](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeignoretype)或 忽略掩码中的[OH_ARKUI_NATIVEMODULE_CONTENTCHANGE_IGNORE_SCROLLBY](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeignoretype)位以忽略这些事件。 |
| uint32_t ignoreMask | [in] [OH_ArkUI_NativeModule_UIContentChangeIgnoreType](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeignoretype)值的按位或组合。 |
| void* userData | [in] 传递给回调的用户定义数据。指针可以是NULL，并且由调用者拥有。 |
| [OH_ArkUI_NativeModule_UIContentChangeEventCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeeventcallback) callback | [in] 匹配事件调用的回调。回调不能为NULL。 |
| uint64_t* subscriptionId | [out] 操作成功时写入的非零订阅ID指针。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果uiContext为NULL或不再活动。</li> <li>ARKUI_ERROR_CODE_CALLBACK_INVALID 如果回调为NULL。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果eventMask或subscriptionId无效。</li> <li>ARKUI_ERROR_CODE_CAPI_INIT_ERROR 如果本机C API未初始化。</li></ul> |

### OH_ArkUI_NativeModule_UnRegisterUIContentChangeEvent()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UnRegisterUIContentChangeEvent(ArkUI_ContextHandle uiContext, uint64_t subscriptionId)
```

**描述：**

从用户界面上下文中取消注册活动的ArkUI状态更改事件订阅。<br> 此函数成功返回后，后续事件将不再调用已移除的订阅。然后，调用者可以 释放其userData。取消订阅回调不会更改当前正在调度的回调批次。 此函数必须在UI线程上调用；从非UI线程调用它将中止进程。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) uiContext | [in] 拥有订阅的用户界面上下文。 |
| uint64_t subscriptionId | [in] uiContext拥有的活动订阅的非零ID。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID 如果uiContext为NULL或不再活动。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果subscriptionId为零、未知或已被移除。</li> <li>ARKUI_ERROR_CODE_CAPI_INIT_ERROR 如果原生C API未初始化。</li> </ul> |

### OH_ArkUI_NativeModule_UIContentChangeEventGetType()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetType(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, OH_ArkUI_NativeModule_UIContentChangeEventType* type)
```

**描述：**

从ArkUI状态变化事件快照中获取事件类型。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md)* event | [in] 事件快照指针。该指针仅在回调运行时有效。 |
| [OH_ArkUI_NativeModule_UIContentChangeEventType](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uicontentchangeeventtype)* type | [out] 操作成功时写入的事件类型指针。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果事件或类型为NULL。</li></ul> |

### OH_ArkUI_NativeModule_UIContentChangeEventGetTimestamp()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetTimestamp(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, uint64_t* nanoTimestamp)
```

**描述：**

获取ArkUI状态变化事件快照的单调时间戳。<br> 时间戳在事件完成点捕获，以纳秒表示，不是挂钟时间。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md)* event | [in] 事件快照指针。该指针仅在回调运行时有效。 |
| uint64_t* nanoTimestamp | [out] 操作成功时写入的以纳秒为单位的单调时间戳指针。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果事件或nano时间戳为NULL。</li></ul> |

### OH_ArkUI_NativeModule_UIContentChangeEventGetContext()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetContext(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, ArkUI_ContextHandle* uiContext)
```

**描述：**

获取ArkUI状态变化事件快照关联的用户界面上下文。<br> 返回的句柄是借用的，在回调返回后，调用者不得释放或使用它。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md)* event | [in] 事件快照指针。该指针仅在回调运行时有效。 |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md)* uiContext | [out] 操作成功时写入的用户界面上下文句柄指针。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果事件或uiContext为NULL。</li></ul> |

### OH_ArkUI_NativeModule_UIContentChangeEventGetContentChangeEventJson()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIContentChangeEventGetContentChangeEventJson(const OH_ArkUI_NativeModule_UIContentChangeEvent* event, const OH_ArkUI_NativeModule_UIJsonWrapper** json)
```

**描述：**

从ArkUI状态变更事件快照中获取内容变更事件详情，作为JSON包装器。<br> JSON输出包括内容变化类型、触发节点、目标节点、覆盖类型和可选的 子树转储取决于事件类别：<br> 页面事件标识目标页面。滚动事件标识滚动节点。重叠事件标识 覆盖节点，并提供覆盖类型（例如“对话框”）。触发节点是启动 内容更改；它适用于覆盖事件和一般开始/结束场景，对于页面和 当没有触发器节点可以暴露时，滚动事件。操作成功并写入一个空的JSON包装器，当 不能暴露任何目标节点。JSON包装器中引用的句柄是借用的，不能被释放 或在回调返回后使用。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIContentChangeEvent](capi-arkui-nativemodule-oh-arkui-nativemodule-uicontentchangeevent.md)* event | [in] 事件快照指针。该指针仅在回调运行时有效。 |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)** json | [out] 接收到内容变更事件的[OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md)指针 .在回调返回后，调用者不得释放包装器或使用它。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果事件或json为NULL。</li></ul> |

### OH_ArkUI_NativeModule_ImageCollectionCallback()

```c
typedef void (*OH_ArkUI_NativeModule_ImageCollectionCallback)(ArkUI_ErrorCode errorCode, OH_ArkUI_NativeModule_ImageCollection* collection, void* userData)
```

**描述：**

定义ArkUI节点图片采集结果返回的回调。<br> 对于每个接受的请求，框架在UI线程上调用此回调仅一次。 当<b>errorCode</b>为ARKUI_ERROR_CODE_NO_ERROR时，框架将转移non-<b>null</b>的所有权 向主叫方发送<b>collection</b>。当<b>errorCode</b>为ARKUI_ERROR_CODE_INTERNAL_ERROR或 ARKUI_ERROR_CODE_UI_CONTEXT_INVALID,<b>collection</b>为<b>null</b>。<br> 框架在不取消引用的情况下返回不变的<b>userData</b>， 复制，或者释放它所指向的对象。打电话的人一定要留着 对象在回调结束使用之前有效。

**起始版本：** 26.2.0

**资源释放：** OH_ArkUI_NativeModule_ImageCollectionDestroy {collection}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) errorCode | [in] 表示请求的整体结果。 <ul<li>>ARKUI_ERROR_CODE_NO_ERROR表示采集成功。</li> <li>ARKUI_ERROR_CODE_INTERNAL_ERROR表示内部采集失败。</li> <li>ARKUI_ERROR_CODE_UI_CONTEXT_INVALID上下文在请求被接受后变得无效。</li></ul> |
| [OH_ArkUI_NativeModule_ImageCollection](capi-arkui-nativemodule-oh-arkui-nativemodule-imagecollection.md)* collection | [in] 表示结果集合。该值为non-<b>null</b>表示总体成功， <b>null</b>表示总体误差。 |
| void* userData | [in] 表示调用者定义的上下文指针。取值范围：<b>null</b>。 |

### OH_ArkUI_NativeModule_GetImagesByNodeIdAsync()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_GetImagesByNodeIdAsync(ArkUI_ContextHandle context, const int32_t* nodeIds, uint32_t count, OH_ArkUI_NativeModule_ImageCollectionCallback callback, void* userData)
```

**描述：**

异步采集指定ArkUI节点ID的镜像。<br> 该框架接受从<b>0</b>到<b>20</b>的唯一节点ID 在此函数返回之前，请求并复制<b>nodeIds</b>数组。 框架接受<b>count</b>等于<b>0</b>的请求， 通过回调返回一个non-<b>null</b>空集合。<br> 每个接受的节点ID在集合中都有一个结果，包括一个结果 对于找不到或无法抓取图像的节点ID。 <b>Image</b>节点在可用时返回其完整的源<b>PixelMap</b> 否则返回到捕获节点内的呈现内容 边界。non-<b>Image</b>节点使用相同的节点边界捕获行为。 节点不需要是可见的。<br> 如果找不到请求的节点ID对应的ArkUI节点，则 对应的收集项报表 <b>ARKUI_ERROR_CODE_PARAM_INVALID</b>；调用方应检查节点ID。 A捕获超时报告 <b>ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_TIMEOUT</b>；调用方可以重试 请求。另一个内部捕获失败报告 该项目的<b>ARKUI_ERROR_CODE_INTERNAL_ERROR</b>；调用方可以重试 处理失败后的请求。项目失败不会改变 请求的整体成功结果。<br> 调用者可以从任何线程调用此函数。对于每一个接受 请求时，框架将在UI线程上调用<b>callback</b>一次 与<b>context</b>关联。并发请求是独立的，而 框架不保证它们的回调顺序。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [ArkUI_ContextHandle](capi-arkui-nativemodule-arkui-contexthandle.md) context | [in] 表示用于处理请求的ArkUI上下文。 参数不能为<b>null</b>。 |
| const int32_t* nodeIds | [in] 表示数组的第一个元素，包含 <b>count</b>唯一的ArkUI节点ID。参数不能为NULL。 |
| uint32_t count | [in] 表示节点ID的个数。有效范围为(0, 20] |
| [OH_ArkUI_NativeModule_ImageCollectionCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_imagecollectioncallback) callback | [in] 表示用于接收结果的回调。 参数不能为<b>null</b>。 |
| void* userData | [in] 表示传递的调用者定义的上下文指针 与回调保持一致。取值范围：<b>null</b>。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果框架接受请求。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果上下文或回调为空。</li> <li>ARKUI_ERROR_CODE_PARAM_OUT_OF_RANGE 计数超出范围(0, 20]。</li> <li>ARKUI_ERROR_CODE_COMMAND_UNFINISHED 如果最后一个请求未完成。</li></ul> |

### OH_ArkUI_NativeModule_ImageCollectionTakeItemByNodeId()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImageCollectionTakeItemByNodeId(OH_ArkUI_NativeModule_ImageCollection* collection, int32_t nodeId, OH_PixelmapNative** outPixelmap, ArkUI_ErrorCode* outItemError)
```

**描述：**

消费指定节点ID的结果。<br> 对于成功的图像结果，此函数将 向主叫方发送<b>PixelMap</b>。调用者必须通过调用来释放它 <b>OH_PixelmapNative_Destroy</b>。此函数也会消耗失败的映像 在这种情况下，它将<b>*outPixelmap</b>设置为<b>null</b>并写入 项错误到<b>*outItemError</b>。集合中的每个节点ID可以为 只消费一次。<br> 销毁集合仅释放<b>PixelMap</b>实例 调用方未使用且未使转移的<b>PixelMap</b>无效。<br> 调用者不能与另一个集合同时调用此函数 同一个集合的api。

**起始版本：** 26.2.0

**资源释放：** multimedia/image_framework/image/OH_PixelmapNative_Destroy {outPixelmap}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_ImageCollection](capi-arkui-nativemodule-oh-arkui-nativemodule-imagecollection.md)* collection | [in] 表示被消费的图片集合。参数不能为空。 |
| int32_t nodeId | [in] 表示要消费的item的ArkUI节点ID。 |
| [OH_PixelmapNative](../../apis-image-kit/c-apis/capi-image-nativemodule-oh-pixelmapnative.md)** outPixelmap | [out] 接收传入的PixelMap的输出指针。参数不能 为null。对于失败的项目，该函数将outPixelmap设置为null。 |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode)* outItemError | [out] 表示指向该项目的结果代码的输出指针。参数不能为 null。函数为成功的项写入ARKUI_ERROR_CODE_NO_ERROR。 ARKUI_ERROR_CODE_NODE_NOT_FOUND如果请求的节点ID对应的ArkUI节点不能 在收集其图像时发现，ARKUI_ERROR_CODE_COMPONENT_SNAPSHOT_TIMEOUT捕获超时，或 ARKUI_ERROR_CODE_INTERNAL_ERROR如果再次捕获失败，调用者可以重试请求。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果此函数消耗项目，包括失败的图像结果。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果所需指针为NULL、nodeId不对应集合中的任何项，或者调用者已经消费了该项。要解决此错误，请提供所有必需的指针并使用nodeId来标识集合中的未消费项。</li></ul> |

### OH_ArkUI_NativeModule_ImageCollectionDestroy()

```c
void OH_ArkUI_NativeModule_ImageCollectionDestroy(OH_ArkUI_NativeModule_ImageCollection* collection)
```

**描述：**

销毁镜像集合，释放未消费的<b>PixelMap</b>实例。<br> 调用方必须销毁回调的每个non-<b>null</b>集合 返回，包括一个空集合或一个在调用者有 消耗了它所有的物品。此功能不会释放或失效 调用方通过获取的<b>PixelMap</b>实例 <b>OH_ArkUI_NativeModule_ImageCollection_TakeItemByNodeId</b>.<br> 调用者不能与另一个集合同时调用此函数 同一个集合的api。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_ImageCollection](capi-arkui-nativemodule-oh-arkui-nativemodule-imagecollection.md)* collection | [in] 表示要销毁的图像集合。 参数可以是<b>null</b>。如果<b>collection</b>为<b>null</b>，则此 函数什么也不做。 |


