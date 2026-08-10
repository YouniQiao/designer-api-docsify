# FocusMoveResultCode (System API)

表示查询无障碍节点返回结果类型的枚举。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export enum FocusMoveResultCode--><!--Device-unnamed-export enum FocusMoveResultCode-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## NOT_SUPPORTED

```TypeScript
NOT_SUPPORTED = -1
```

当前节点不支持查询操作。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-NOT_SUPPORTED = -1--><!--Device-FocusMoveResultCode-NOT_SUPPORTED = -1-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_SUCCESS

```TypeScript
SEARCH_SUCCESS = 0
```

节点查询成功。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_SUCCESS = 0--><!--Device-FocusMoveResultCode-SEARCH_SUCCESS = 0-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_SUCCESS_NEXT_BYPASS_DESCENDANTS

```TypeScript
SEARCH_SUCCESS_NEXT_BYPASS_DESCENDANTS = 1
```

节点查询成功，建议下一次查询使用参数bypassSelfDescendants可更快获取结果。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_SUCCESS_NEXT_BYPASS_DESCENDANTS = 1--><!--Device-FocusMoveResultCode-SEARCH_SUCCESS_NEXT_BYPASS_DESCENDANTS = 1-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_FAILURE

```TypeScript
SEARCH_FAILURE = 2
```

节点查询失败，当前节点所在页面内无可聚焦节点。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_FAILURE = 2--><!--Device-FocusMoveResultCode-SEARCH_FAILURE = 2-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_FAILURE_IN_CHILD_TREE

```TypeScript
SEARCH_FAILURE_IN_CHILD_TREE = 3
```

节点查询失败，当前节点所在容器内无可聚焦节点。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_FAILURE_IN_CHILD_TREE = 3--><!--Device-FocusMoveResultCode-SEARCH_FAILURE_IN_CHILD_TREE = 3-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_FAILURE_LOST_NODE

```TypeScript
SEARCH_FAILURE_LOST_NODE = 4
```

节点查询失败，未找到起始节点。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_FAILURE_LOST_NODE = 4--><!--Device-FocusMoveResultCode-SEARCH_FAILURE_LOST_NODE = 4-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_NEXT

```TypeScript
SEARCH_NEXT = 5
```

返回节点不具备可聚焦属性，继续使用返回节点查询。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_NEXT = 5--><!--Device-FocusMoveResultCode-SEARCH_NEXT = 5-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## DOUBLE_CHECK_CHILD_PROPERTY

```TypeScript
DOUBLE_CHECK_CHILD_PROPERTY = 6
```

返回节点不具备可聚焦属性，需要使用返回节点的所有子节点继续查询。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-DOUBLE_CHECK_CHILD_PROPERTY = 6--><!--Device-FocusMoveResultCode-DOUBLE_CHECK_CHILD_PROPERTY = 6-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## DOUBLE_CHECK_CHILD_PROPERTY_AND_GET_LAST

```TypeScript
DOUBLE_CHECK_CHILD_PROPERTY_AND_GET_LAST = 7
```

返回节点不具备可聚焦属性，需要使用返回节点的子节点列表中的最后一个节点继续查询。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-DOUBLE_CHECK_CHILD_PROPERTY_AND_GET_LAST = 7--><!--Device-FocusMoveResultCode-DOUBLE_CHECK_CHILD_PROPERTY_AND_GET_LAST = 7-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## SEARCH_FAILURE_IN_SCROLL

```TypeScript
SEARCH_FAILURE_IN_SCROLL = 8
```

节点在滚动组件内查询失败。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-FocusMoveResultCode-SEARCH_FAILURE_IN_SCROLL = 8--><!--Device-FocusMoveResultCode-SEARCH_FAILURE_IN_SCROLL = 8-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

