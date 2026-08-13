# ComponentObserver

The ComponentObserver is used to listen for layout, draw and drawChildren events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-inspector-interface ComponentObserver--><!--Device-inspector-interface ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offDraw

```TypeScript
offDraw(callback?: VoidCallback): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the component draw complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-offDraw(callback?: VoidCallback): void--><!--Device-ComponentObserver-offDraw(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | No | callback of the listened event. |

## offDrawChildren

```TypeScript
offDrawChildren(callback?: VoidCallback): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the child of component draw complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-offDrawChildren(callback?: VoidCallback): void--><!--Device-ComponentObserver-offDrawChildren(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | No | callback of the listened event. |

## offDrawChildren

```TypeScript
offDrawChildren(callback?: Callback<int[]>): void
```

Deregisters a callback with the corresponding query conditiion by using the handle. This callback is not triggered when the child of component draw complete.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-offDrawChildren(callback?: Callback<int[]>): void--><!--Device-ComponentObserver-offDrawChildren(callback?: Callback<int[]>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int[]&gt; | No | callback of the listened event. &lt;br&gt;Default value undefined |

## offLayout

```TypeScript
offLayout(callback?: VoidCallback): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the component layout complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-offLayout(callback?: VoidCallback): void--><!--Device-ComponentObserver-offLayout(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | No | callback of the listened event. |

## offLayoutChildren

```TypeScript
offLayoutChildren(callback?: VoidCallback): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the child of component layout complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-offLayoutChildren(callback?: VoidCallback): void--><!--Device-ComponentObserver-offLayoutChildren(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | No | callback of the listened event. |

## onDraw

```TypeScript
onDraw(callback: VoidCallback): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the component draw complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-onDraw(callback: VoidCallback): void--><!--Device-ComponentObserver-onDraw(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | Yes | callback of the listened event. |

## onDrawChildren

```TypeScript
onDrawChildren(callback: VoidCallback): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the child of component draw complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-onDrawChildren(callback: VoidCallback): void--><!--Device-ComponentObserver-onDrawChildren(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | Yes | callback of the listened event. |

## onDrawChildren

```TypeScript
onDrawChildren(callback: Callback<int[]>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the child of component draw complete.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-onDrawChildren(callback: Callback<int[]>): void--><!--Device-ComponentObserver-onDrawChildren(callback: Callback<int[]>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int[]&gt; | Yes | callback of the listened event. |

## onLayout

```TypeScript
onLayout(callback: VoidCallback): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the component layout complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-onLayout(callback: VoidCallback): void--><!--Device-ComponentObserver-onLayout(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | Yes | callback of the listened event. |

## onLayoutChildren

```TypeScript
onLayoutChildren(callback: VoidCallback): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the child of component layout complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentObserver-onLayoutChildren(callback: VoidCallback): void--><!--Device-ComponentObserver-onLayoutChildren(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | Yes | callback of the listened event. |

