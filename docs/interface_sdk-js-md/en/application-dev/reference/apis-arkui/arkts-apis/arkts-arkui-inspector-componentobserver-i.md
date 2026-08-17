# ComponentObserver

The ComponentObserver is used to listen for layout, draw and drawChildren events.

**Since:** 10

<!--Device-inspector-interface ComponentObserver--><!--Device-inspector-interface ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { inspector } from 'inspector';
```

## offDrawChildren

```TypeScript
offDrawChildren(callback?: Callback<int[]>): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the child of component draw complete.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ComponentObserver-offDrawChildren(callback?: Callback<int[]>): void--><!--Device-ComponentObserver-offDrawChildren(callback?: Callback<int[]>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int[]&gt; | No | callback of the listened event. |

## offLayoutChildren

```TypeScript
offLayoutChildren(callback?: Callback<void>): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback will not be triggered when the child of component layout is complete.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ComponentObserver-offLayoutChildren(callback?: Callback<void>): void--><!--Device-ComponentObserver-offLayoutChildren(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | callback of the listened event. |

## off_draw

```TypeScript
off(type: 'draw', callback?: () => void): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the component draw complete.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ComponentObserver-off(type: 'draw', callback?: () => void): void--><!--Device-ComponentObserver-off(type: 'draw', callback?: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'draw' | Yes | type of the listened event.<br>**Since:** 12 |
| callback | () =&gt; void | No | callback of the listened event.<br>**Since:** 12 |

## off_drawChildren

```TypeScript
off(type: 'drawChildren', callback?: Callback<void>): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the child of component draw complete.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ComponentObserver-off(type: 'drawChildren', callback?: Callback<void>): void--><!--Device-ComponentObserver-off(type: 'drawChildren', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'drawChildren' | Yes | type of the listened event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | callback of the listened event. |

## off_layout

```TypeScript
off(type: 'layout', callback?: () => void): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the component layout complete.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ComponentObserver-off(type: 'layout', callback?: () => void): void--><!--Device-ComponentObserver-off(type: 'layout', callback?: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'layout' | Yes | type of the listened event.<br>**Since:** 12 |
| callback | () =&gt; void | No | callback of the listened event.<br>**Since:** 12 |

## onDrawChildren

```TypeScript
onDrawChildren(callback: Callback<int[]>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the child of component draw complete.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ComponentObserver-onDrawChildren(callback: Callback<int[]>): void--><!--Device-ComponentObserver-onDrawChildren(callback: Callback<int[]>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int[]&gt; | Yes | callback of the listened event. |

## onLayoutChildren

```TypeScript
onLayoutChildren(callback: Callback<void>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback will be triggered when the child of component layout is complete.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ComponentObserver-onLayoutChildren(callback: Callback<void>): void--><!--Device-ComponentObserver-onLayoutChildren(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | callback of the listened event. |

## on_draw

```TypeScript
on(type: 'draw', callback: () => void): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the component draw complete.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ComponentObserver-on(type: 'draw', callback: () => void): void--><!--Device-ComponentObserver-on(type: 'draw', callback: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'draw' | Yes | type of the listened event.<br>**Since:** 12 |
| callback | () =&gt; void | Yes | callback of the listened event.<br>**Since:** 12 |

## on_drawChildren

```TypeScript
on(type: 'drawChildren', callback: Callback<void>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the child of component draw complete.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ComponentObserver-on(type: 'drawChildren', callback: Callback<void>): void--><!--Device-ComponentObserver-on(type: 'drawChildren', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'drawChildren' | Yes | type of the listened event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | callback of the listened event. |

## on_layout

```TypeScript
on(type: 'layout', callback: () => void): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the component layout complete.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ComponentObserver-on(type: 'layout', callback: () => void): void--><!--Device-ComponentObserver-on(type: 'layout', callback: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'layout' | Yes | type of the listened event.<br>**Since:** 12 |
| callback | () =&gt; void | Yes | callback of the listened event.<br>**Since:** 12 |

