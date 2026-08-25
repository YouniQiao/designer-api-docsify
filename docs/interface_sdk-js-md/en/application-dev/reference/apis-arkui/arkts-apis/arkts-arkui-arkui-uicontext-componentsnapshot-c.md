# ComponentSnapshot

Provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet.

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 12.&gt;
> - In the following API examples, you must first use [getComponentSnapshot()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> in **UIContext** to obtain a **ComponentSnapshot** instance, and then call the APIs using the obtained instance.&gt;
> - Transformation properties such as scaling, translation, and rotation only apply to the child components of the
> target component. Applying these transformation properties directly to the target component itself has no effect;
> the snapshot will still display the component as it appears before any transformations are applied.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from 'kits/@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from 'kits/@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from 'kits/@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from 'kits/@kit.ArkUI';
```

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void
```

Captures a snapshot of an offscreen-rendered component created from a [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md). This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - Due to the need to wait for the component to be built and rendered, there is a delay of not more than 500 ms in
> the callback for off-screen snapshot capturing. Therefore, this API is not recommended for performance-sensitive
> scenarios.&gt;
> - If a component is on a time-consuming task, for example, an Image or Web component
> that is loading online images, its loading may be still in progress when this API is called. In this case, the
> output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | componentSnapshot.SnapshotOptions | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
| [160004](../errorcode-snapshot.md#160004-unsupported-isauto-setting-of-the-color-space-or-dynamic-range-mode-for-offscreen-node-snapshot) |

## createFromBuilder

```TypeScript
createFromBuilder(builder: CustomBuilder, delay?: number,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

Captures a snapshot of an offscreen-rendered component created from a [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md). This API uses a promise to return the result.

> **NOTE：**&gt;
> - Due to the need to wait for the component to be built and rendered, there is a delay of not more than 500 ms in
> the callback for off-screen snapshot capturing. Therefore, this API is not recommended for performance-sensitive
> scenarios.&gt;
> - If a component is on a time-consuming task, for example, an Image or Web component
> that is loading online images, its loading may be still in progress when this API is called. In this case, the
> output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
| [160004](../errorcode-snapshot.md#160004-unsupported-isauto-setting-of-the-color-space-or-dynamic-range-mode-for-offscreen-node-snapshot) |

## createFromComponent

```TypeScript
createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: number,
    checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

Captures a snapshot of the provided component content. This API uses a promise to return the result.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | ComponentContent & lt;T & gt; | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
| [160004](../errorcode-snapshot.md#160004-unsupported-isauto-setting-of-the-color-space-or-dynamic-range-mode-for-offscreen-node-snapshot) |

## get

```TypeScript
get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |

## get

```TypeScript
get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |

## getSizeLimitation

```TypeScript
getSizeLimitation(): componentSnapshot.SnapshotSizeLimitation
```

Obtains the size limit of a component screenshot.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| componentSnapshot.SnapshotSizeLimitation |

## getSync

```TypeScript
getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap
```

Obtains the snapshot of a component that has been loaded based on the provided component ID. This API synchronously returns a [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) after completing the capture. Note that this API blocks the main thread and has a 3-second timeout. If the operation exceeds this limit, it throws an exception. Use with caution in performance-critical scenarios.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160002](../errorcode-snapshot.md#160002-snapshot-timeout) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |

## getSyncWithUniqueId

```TypeScript
getSyncWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): image.PixelMap
```

Obtains the snapshot of a component that has been loaded based on the provided **uniqueId**. This API synchronously waits for the snapshot to complete and returns a [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) object.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uniqueId | number | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160002](../errorcode-snapshot.md#160002-snapshot-timeout) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |

## getWithUniqueId

```TypeScript
getWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

Obtains the snapshot of a component that has been loaded based on the provided **uniqueId**. This API uses a promise to return the result.

> **NOTE：**&gt;
> The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
> update, the re-rendered content will not be included in the obtained snapshot.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uniqueId | number | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
